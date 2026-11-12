#!/usr/bin/env python3
"""Build the public reasoning-log release from the gpt-5.6-high epitope runs.

Copies the hypothesis-launcher sessions (casp16/casp17 r1-r3, E1 arm) and the
post_refactor gather/refine sessions (canonical lineage only) into a staging
tree, redacting account identifiers, local paths, hostnames and secrets, and
dropping agent runtime state (agent_home/), encrypted reasoning blobs and
third-party full-text documents (which are replaced by a listing).

Usage:
  build_reasoning_release.py --out DIR [--targets H1346_agCD ...] [--dry-run]
  build_reasoning_release.py --scan DIR         # secret/PII scan of a built tree
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

SRC = Path("/<lab-storage>/ape/preprint_v1/epitope/gpt-5.6-high")
RELEASE_NAME = "apar_epitope_reasoning_logs_v1"

# (source dir relative to SRC, destination cohort name, rounds)
LAUNCHER_SETS = [("casp16", "casp16", ["r1", "r2", "r3"]),
                 ("casp17", "casp17", ["r1", "r2", "r3"]),
                 ("nocut/casp17", "casp17_nocut", ["r1", "r2", "r3"])]
GATHER_COHORTS = {
    "released_structure_20261030": {"lineage": "canonical_lineage.json", "policy_dirs": None},
    "unreleased_20261029": {"lineage": "canonical_lineage.json", "policy_dirs": {"gated": "gated", "no-cutoff": "nocut"}},
}
COHORT_FILES = [
    "CANONICAL_LINEAGE.md", "canonical_lineage.json", "controller.log", "controller_state.json",
    "judge_rerun.log", "judge_rerun_state.json",
]

# ---------------------------------------------------------------- redaction
USER = "<operator-username>"
EMAIL = "<operator-email>"
STR_REPLACEMENTS = [
    (str(SRC), "/data/release"),
    ("/<lab-storage>/ape/preprint_v1/epitope", "/data/epitope"),
    ("/<lab-storage>/ape", "/data/ape"),
    ("/<lab-storage>/<collaborator-username>", "/data/collaborator"),
    ("/home/<collaborator-username>", "/home/COLLABORATOR"),
    (f"/home/{USER}", "/home/USER"),
    (f"/tmp/pixi-cache-{USER}", "/tmp/pixi-cache-USER"),
    (EMAIL, "[email-redacted]"),
    ("<login-hostname>", "login-host"),
]
REGEX_REPLACEMENTS = [
    (re.compile(rf"\b{USER}\b"), "USER"),
    (re.compile(r"/home/(?!USER\b|COLLABORATOR\b|software\b|OTHERUSER\b)[a-z][a-z0-9_.-]*"), "/home/OTHERUSER"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}"), "[email-redacted]"),
    (re.compile(r"\bnode0[0-9]\b"), "compute-node"),
    (re.compile(r"\buser-[A-Za-z0-9]{20,}"), "user-REDACTED"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"), "sk-REDACTED"),
    (re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}"), "Bearer REDACTED"),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AKIAREDACTED"),
    (re.compile(r"(?i)\b(api[_-]?key|x-api-key|authorization|access[_-]?token|auth[_-]?token|secret[_-]?key|password)(\s*[=:]\s*[\"']?)[A-Za-z0-9._\-]{16,}"), r"\1\2REDACTED"),
]
# Account ids found in rollout session_meta are added to this set at build time
DYNAMIC_SECRETS: set[str] = set()

TEXT_EXT = {".json", ".jsonl", ".md", ".txt", ".log", ".py", ".out", ".err", ".sh", ".sbatch",
            ".tsv", ".csv", ".fasta", ".yaml", ".yml", ".stdout", ".cfg", ".toml", ""}
BINARY_OK_EXT = {".pdb", ".cif", ".pdf", ".pyc", ".npz", ".npy", ".gz", ".png", ".jpg", ".jpeg"}

# per-session exclusions
SESSION_DROP_TOP = {"agent_home", "gate.port", "proxy.err", "stderr.log", "staged.err",
                    "cutoff_audit.json"}  # cutoff_audit.json = post-run network audit result, not released
WORKDIR_DROP_DIRS = {"__pycache__", ".git", ".codex", ".aws", ".agents", ".tmp_anarci", "runs"}
THIRD_PARTY_DIRS = {"fetched", "papers", "patents"}
# loose downloaded documents saved directly in the workdir (no-cutoff runs had no helper CLIs)
THIRD_PARTY_EXT = {".pdf", ".html", ".htm", ".xml", ".jpg", ".jpeg", ".epub", ".docx", ".doc", ".gz", ".zip"}
THIRD_PARTY_NAME = re.compile(r"(?i)(patent|^figure\d*\.png$|\bPMC\d{5,9}\b|^(US|EP|WO|CN|JP|KR|AU)\d{6,13}[AB]?\d?\b)")


def is_third_party_file(fn: str) -> bool:
    ext = os.path.splitext(fn)[1].lower()
    if ext in THIRD_PARTY_EXT:
        return True
    if ext in (".txt", ".png") and THIRD_PARTY_NAME.search(fn):
        return True
    return False


def redact_text(s: str) -> tuple[str, Counter]:
    hits: Counter = Counter()
    for old, new in STR_REPLACEMENTS:
        if old in s:
            hits[old] += s.count(old)
            s = s.replace(old, new)
    for sec in DYNAMIC_SECRETS:
        if sec in s:
            hits["<dynamic-id>"] += s.count(sec)
            s = s.replace(sec, "REDACTED")
    for rx, new in REGEX_REPLACEMENTS:
        s, n = rx.subn(new, s)
        if n:
            hits[rx.pattern[:30]] += n
    return s, hits


def redact_rollout_line(line: str) -> tuple[str, Counter]:
    """JSON-aware pass for codex rollout.jsonl records."""
    hits: Counter = Counter()
    try:
        d = json.loads(line)
    except json.JSONDecodeError:
        return redact_text(line)
    p = d.get("payload")
    if d.get("type") == "session_meta" and isinstance(p, dict):
        for k in ("creator_user_id", "creator_account_id"):
            v = p.get(k)
            if isinstance(v, str) and v:
                DYNAMIC_SECRETS.add(v)
                p[k] = "REDACTED"
                hits[k] += 1
    def strip_enc(o):
        if isinstance(o, dict):
            if isinstance(o.get("encrypted_content"), str):
                o["encrypted_content_removed_chars"] = len(o["encrypted_content"])
                o["encrypted_content"] = None
                hits["encrypted_content"] += 1
            for v in o.values():
                strip_enc(v)
        elif isinstance(o, list):
            for v in o:
                strip_enc(v)
    strip_enc(d)
    out = json.dumps(d, ensure_ascii=False)
    out, h2 = redact_text(out)
    hits.update(h2)
    return out + "\n", hits


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


ID_PATTERNS = [
    ("PMC", re.compile(r"\b(PMC\d{5,9})\b")),
    ("DOI", re.compile(r"(10\.\d{4,9}/[^\s/_]+(?:_[^\s/_]+)*)")),
    ("patent", re.compile(r"\b((?:US|EP|WO|CN|JP|KR)\d{6,13}[AB]?\d?)\b")),
    ("PDB", re.compile(r"^([1-9][A-Za-z0-9]{3})\.(?:cif|pdb)$")),
    ("PMID", re.compile(r"^(\d{7,8})\.(?:txt|pdf)$")),
]


def guess_id(name: str) -> str:
    for kind, rx in ID_PATTERNS:
        m = rx.search(name)
        if m:
            return f"{kind}:{m.group(1)}"
    return ""


class Builder:
    def __init__(self, out: Path, targets: set[str] | None, dry: bool):
        self.out = out
        self.targets = targets
        self.dry = dry
        self.hits: Counter = Counter()
        self.third_party: list[dict] = []
        self.launcher_rows: list[dict] = []
        self.gather_rows: list[dict] = []
        self.launcher_index: dict[str, list[tuple[Path, str]]] = defaultdict(list)  # case id -> [(workdir, dest)]
        self.n_files = 0
        self.n_bytes = 0

    # -------------------------------------------------------------- copying
    def copy_file(self, src: Path, dst: Path, mode: str = "text"):
        if self.dry:
            self.n_files += 1
            self.n_bytes += src.stat().st_size
            return
        dst.parent.mkdir(parents=True, exist_ok=True)
        if src.is_symlink():
            raise RuntimeError(f"refusing to copy symlink {src}")
        ext = src.suffix.lower()
        if mode == "rollout":
            with open(src, encoding="utf-8", errors="surrogateescape") as f, open(dst, "w", encoding="utf-8") as g:
                for line in f:
                    o, h = redact_rollout_line(line)
                    self.hits.update(h)
                    g.write(o)
        elif ext in TEXT_EXT and ext not in BINARY_OK_EXT:
            try:
                s = src.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                shutil.copyfile(src, dst)
            else:
                o, h = redact_text(s)
                self.hits.update(h)
                dst.write_text(o, encoding="utf-8")
        else:
            shutil.copyfile(src, dst)
        self.n_files += 1
        self.n_bytes += dst.stat().st_size

    def copy_session(self, src: Path, dst: Path, kind: str) -> dict:
        """Copy one codex session directory with the drop/redact rules."""
        info = {"src": str(src), "dst": str(dst.relative_to(self.out)), "third_party_removed": 0}
        third: list[dict] = []
        for root, dirs, files in os.walk(src):
            root_p = Path(root)
            rel = root_p.relative_to(src)
            parts = rel.parts
            # prune
            if not parts:
                dirs[:] = [d for d in dirs if d not in SESSION_DROP_TOP]
            if parts and parts[0] == "workdir":
                sub = parts[1:]
                if not sub:
                    keep = []
                    for d in dirs:
                        if d in WORKDIR_DROP_DIRS or d.startswith("."):
                            continue
                        if d in THIRD_PARTY_DIRS:
                            for r2, _, f2 in os.walk(root_p / d):
                                for fn in f2:
                                    fp = Path(r2) / fn
                                    relp = fp.relative_to(src)
                                    third.append({"session": info["dst"], "path": str(relp),
                                                  "bytes": fp.stat().st_size, "sha256": sha256(fp),
                                                  "id_guess": guess_id(fn) or guess_id(str(relp))})
                            continue
                        keep.append(d)
                    dirs[:] = keep
            if parts and parts[0] == "runs":  # judge packet runs/ are launcher workdir copies
                dirs[:] = []
                continue
            if not parts:
                dirs[:] = [d for d in dirs if d != "runs"]
            dirs.sort()
            for fn in sorted(files):
                fp = root_p / fn
                if fp.is_symlink():
                    self.hits["symlink-skipped"] += 1
                    continue
                if not parts and fn in SESSION_DROP_TOP:
                    continue
                if fp.stat().st_size == 0:
                    continue
                if fn.endswith(".pyc") or fn.endswith(".corrupt"):
                    continue
                if parts and parts[0] == "workdir" and is_third_party_file(fn):
                    third.append({"session": info["dst"], "path": str(rel / fn), "bytes": fp.stat().st_size,
                                  "sha256": sha256(fp), "id_guess": guess_id(fn)})
                    continue
                mode = "rollout" if fn == "rollout.jsonl" else "text"
                self.copy_file(fp, dst / rel / fn, mode)
        if third:
            info["third_party_removed"] = len(third)
            self.third_party.extend(third)
            if not self.dry:
                tp = dst / "workdir" / "THIRD_PARTY_REMOVED.tsv"
                tp.parent.mkdir(parents=True, exist_ok=True)
                with open(tp, "w") as g:
                    g.write("path\tbytes\tsha256\tid_guess\n")
                    for t in third:
                        g.write(f"{t['path']}\t{t['bytes']}\t{t['sha256']}\t{t['id_guess']}\n")
        return info

    # ------------------------------------------------------------- launcher
    def match_packet_run(self, run_dir: Path, case: str) -> str:
        """Find the hypothesis workdir whose files the packet run was copied from."""
        files = [(fn, sha256(run_dir / fn)) for fn in sorted(os.listdir(run_dir)) if (run_dir / fn).is_file()]
        if not files:
            return "EMPTY"
        for wd, dest in self.launcher_index.get(case, []):
            if all((wd / fn).is_file() and sha256(wd / fn) == h for fn, h in files):
                return dest
        return "UNMATCHED"

    def build_launcher(self):
        for src_rel, cohort, rounds in LAUNCHER_SETS:
            for r in rounds:
                for case_dir in sorted((SRC / src_rel / r).glob("case_*_E1_rep*")):
                    st_p = case_dir / "status.json"
                    if not st_p.exists():
                        continue
                    st = json.load(open(st_p))
                    tgt = st["target"]
                    if self.targets and tgt not in self.targets:
                        continue
                    dst = self.out / "hypothesis" / cohort / r / f"{tgt}__{case_dir.name}"
                    info = self.copy_session(case_dir, dst, "launcher")
                    self.launcher_index[st["case"]].append((case_dir / "workdir", info["dst"]))
                    self.launcher_rows.append({
                        "cohort": cohort, "round": r, "target": tgt, "case": st["case"], "arm": st["arm"],
                        "no_cutoff": st.get("no_cutoff", False),
                        "rep": st["rep"], "status": st["status"], "started": st["started"], "finished": st["finished"],
                        "session_id": st.get("session_id", ""), "evidence_cutoff": st.get("cutoff", ""),
                        "model": st.get("model", ""), "searcher_model": st.get("searcher_model", ""),
                        "path": info["dst"], "third_party_removed": info["third_party_removed"],
                    })
                    print(f"[launcher] {cohort}/{r} {tgt} -> {info['dst']}  (3rd-party removed: {info['third_party_removed']})")

    # --------------------------------------------------------------- gather
    def build_gather(self):
        for cohort, spec in GATHER_COHORTS.items():
            croot = SRC / "gather_refine" / "post_refactor" / cohort
            lin = json.load(open(croot / spec["lineage"]))
            dst_c = self.out / "gather_refine" / cohort
            for fn in COHORT_FILES:
                if (croot / fn).exists():
                    self.copy_file(croot / fn, dst_c / fn)
            # per-policy controller logs (unreleased cohort keeps them under gated/ and nocut/)
            for pol in ("gated", "nocut"):
                for fn in ("controller.log", "controller_state.json"):
                    if (croot / pol / fn).exists():
                        self.copy_file(croot / pol / fn, dst_c / pol / fn)
            # published results (small, keeps the archive self-contained)
            res = croot / "results"
            if res.exists():
                for root, dirs, files in os.walk(res):
                    dirs.sort()
                    for fn in sorted(files):
                        fp = Path(root) / fn
                        self.copy_file(fp, dst_c / "results" / fp.relative_to(res))
            for t in lin["targets"]:
                tgt = t["target"]
                if self.targets and tgt not in self.targets:
                    continue
                pol = t.get("retrieval_policy", "gated")
                for stage in ("refine", "judge", "judge_packet", "assembled"):
                    sp = Path(t[stage])
                    rel = sp.relative_to(croot)  # e.g. casp17/H1346_agCD/case_fed304_GR_rep1
                    dst = dst_c / rel
                    info = self.copy_session(sp, dst, stage)
                    row = {"cohort": cohort, "policy": pol, "target": tgt, "stage": stage, "case_dir": sp.name,
                           "path": info["dst"], "third_party_removed": info["third_party_removed"],
                           "packet_runs_a": "", "packet_runs_b": "", "packet_runs_c": ""}
                    st_p = sp / "status.json"
                    if st_p.exists():
                        st = json.load(open(st_p))
                        row.update({"status": st.get("status", ""), "started": st.get("started", ""),
                                    "finished": st.get("finished", ""), "session_id": st.get("session_id", ""),
                                    "model": st.get("model", "")})
                    if stage == "judge_packet":
                        case_id = "_".join(sp.name.split("_")[:2])
                        for s in "abc":
                            rd = sp / "runs" / s
                            if rd.is_dir():
                                row[f"packet_runs_{s}"] = self.match_packet_run(rd, case_id)
                    gm = sp.parent / "gather_mode.json"
                    if gm.exists():
                        self.copy_file(gm, dst.parent / "gather_mode.json")
                    self.gather_rows.append(row)
                    print(f"[gather] {cohort}/{pol} {tgt} {stage} -> {info['dst']}  (3rd-party removed: {info['third_party_removed']})"
                          + (f"  runs a/b/c -> {row['packet_runs_a']} | {row['packet_runs_b']} | {row['packet_runs_c']}" if stage == "judge_packet" else ""))
        # steering inputs and DockQ summaries (raw Protenix outputs are NOT included)
        si = SRC / "gather_refine" / "post_refactor" / "steerable_inputs"
        for root, dirs, files in os.walk(si):
            dirs.sort()
            for fn in sorted(files):
                fp = Path(root) / fn
                self.copy_file(fp, self.out / "steerable" / "inputs" / fp.relative_to(si))
        for cohort in GATHER_COHORTS:
            sd = SRC / "gather_refine" / "post_refactor" / cohort / "steerable_dockq"
            if sd.exists():
                for fp in sorted(sd.iterdir()):
                    if fp.is_file():
                        self.copy_file(fp, self.out / "steerable" / "dockq" / cohort / fp.name)

    # -------------------------------------------------------------- outputs
    def write_tables(self):
        if self.dry:
            return
        ld = self.out / "lineage"
        ld.mkdir(parents=True, exist_ok=True)
        if self.launcher_rows:
            cols = list(self.launcher_rows[0].keys())
            with open(ld / "hypothesis_sessions.tsv", "w") as g:
                g.write("\t".join(cols) + "\n")
                for r in self.launcher_rows:
                    g.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")
        if self.gather_rows:
            cols = ["cohort", "policy", "target", "stage", "case_dir", "path", "status", "started", "finished",
                    "session_id", "model", "third_party_removed", "packet_runs_a", "packet_runs_b", "packet_runs_c"]
            with open(ld / "gather_sessions.tsv", "w") as g:
                g.write("\t".join(cols) + "\n")
                for r in self.gather_rows:
                    g.write("\t".join(str(r.get(c, "")) for c in cols) + "\n")
        with open(ld / "third_party_removed.tsv", "w") as g:
            g.write("session\tpath\tbytes\tsha256\tid_guess\n")
            for t in self.third_party:
                g.write(f"{t['session']}\t{t['path']}\t{t['bytes']}\t{t['sha256']}\t{t['id_guess']}\n")

    def write_manifest(self):
        if self.dry:
            return
        rows = []
        for root, dirs, files in os.walk(self.out):
            dirs.sort()
            for fn in sorted(files):
                fp = Path(root) / fn
                rel = fp.relative_to(self.out)
                if str(rel) == "MANIFEST.tsv":
                    continue
                rows.append((str(rel), fp.stat().st_size, sha256(fp)))
        with open(self.out / "MANIFEST.tsv", "w") as g:
            g.write("path\tbytes\tsha256\n")
            for r in rows:
                g.write(f"{r[0]}\t{r[1]}\t{r[2]}\n")
        print(f"[manifest] {len(rows)} files, {sum(r[1] for r in rows)/1e6:.1f} MB")


# -------------------------------------------------------------------- scan
SCAN_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}"),
    "sk-key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}"),
    "bearer": re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{20,}"),
    "keyval": re.compile(r"(?i)\b(api[_-]?key|x-api-key|authorization|access[_-]?token|secret[_-]?key|password)\s*[=:]\s*[\"']?[A-Za-z0-9._\-]{16,}"),
    "openai-user": re.compile(r"\buser-[A-Za-z0-9]{20,}"),
    "username": re.compile(rf"\b{USER}\b"),
    "home": re.compile(r"/home/(?!USER\b|COLLABORATOR\b|OTHERUSER\b|software\b)[A-Za-z0-9_.-]+"),
    "public_data02": re.compile(r"/<lab-storage>/[A-Za-z0-9_.-]+"),
    "hostname": re.compile(r"\b(<login-hostname>|node0[0-9])\b"),
    "encrypted": re.compile(r"\"encrypted_content\":\s*\"[A-Za-z0-9]"),
    "uuid-account": re.compile(r"\"(creator_user_id|creator_account_id)\":\s*\"(?!REDACTED)"),
    "ssh/aws": re.compile(r"(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|AKIA[0-9A-Z]{16})"),
}


def scan(root: Path):
    hits: dict[str, Counter] = defaultdict(Counter)
    examples: dict[str, set] = defaultdict(set)
    n = 0
    for r, dirs, files in os.walk(root):
        dirs.sort()
        for fn in sorted(files):
            fp = Path(r) / fn
            if fp.suffix.lower() in BINARY_OK_EXT:
                continue
            try:
                s = fp.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            n += 1
            for k, rx in SCAN_PATTERNS.items():
                for m in rx.finditer(s):
                    hits[k][str(fp.relative_to(root))] += 1
                    v = m.group(0)
                    examples[k].add(v if k in ("email", "home", "public_data02", "hostname", "username") else v[:10] + "***")
    print(f"scanned {n} text files")
    for k in SCAN_PATTERNS:
        tot = sum(hits[k].values())
        print(f"== {k}: {tot} hits in {len(hits[k])} files")
        for ex in sorted(examples[k])[:25]:
            print("   ", ex)
        for f, c in hits[k].most_common(5):
            print(f"      {c:5d} {f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path)
    ap.add_argument("--targets", nargs="*")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--scan", type=Path)
    ap.add_argument("--manifest", type=Path, help="(re)write MANIFEST.tsv for an existing tree")
    a = ap.parse_args()
    if a.scan:
        scan(a.scan)
        return
    if a.manifest:
        b = Builder(a.manifest, None, False)
        b.write_manifest()
        return
    out = a.out / RELEASE_NAME
    if out.exists() and not a.dry_run:
        print(f"refusing to overwrite existing {out}", file=sys.stderr)
        sys.exit(1)
    b = Builder(out, set(a.targets) if a.targets else None, a.dry_run)
    b.build_launcher()
    b.build_gather()
    b.write_tables()
    b.write_manifest()
    print(f"files: {b.n_files}  bytes: {b.n_bytes/1e6:.1f} MB  third-party removed: {len(b.third_party)}")
    print("redaction hits:", dict(b.hits.most_common()))


if __name__ == "__main__":
    main()
