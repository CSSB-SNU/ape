# Redaction and exclusion rules

This tree was produced from the raw run directories by
`tools/build_reasoning_release.py`. Nothing was edited by hand. The rules
below describe exactly what was removed or rewritten.

## Excluded wholesale

| what | why |
|---|---|
| `agent_home/` in every session (Codex runtime state: auth file link, sqlite state, plugin/model caches, shell snapshots, installation id) | account credentials and runtime caches; no reasoning content. The search agent's sub-sessions that lived there are already captured in `gate.searcher.log`. |
| `steerable_results/` (raw Protenix predictions, ~1 TB) | size; summarised by `steerable/dockq/`. |
| `workdir/{fetched,papers,patents}/`, loose downloaded documents in a workdir (`.pdf`, `.html`, `.xml`, `.jpg`, `.gz`, and `.txt`/`.png` files named after a patent, PMC id or figure), and judge-packet / refine `workdir/runs/` | downloaded third-party full text (papers, patents, PDFs, supplementary files) is not redistributable. Each removed file is listed with its size, sha256 and inferred identifier in `workdir/THIRD_PARTY_REMOVED.tsv` and globally in `lineage/third_party_removed.tsv`. PDB/mmCIF files fetched from RCSB are kept. `runs/a,b,c` were copies of hypothesis-session workdirs and are mapped (by file hash) in `lineage/gather_sessions.tsv`. |
| hypothesis arm stubs (`case_*_E_rep*`: sbatch + Slurm out/err only) and non-canonical gather reps | not sessions / not part of the published lineage. |
| H1347_agCD hypothesis reps 4–8 | an additional-sampling experiment, not part of the published 3-rep protocol. |
| `cutoff_audit.json` in every gather session, and the cohort-level network audit reports | post-run network / evidence-cutoff audit results; not part of this release. |
| `gate.port`, `proxy.err`, zero-byte files, `__pycache__`, hidden sandbox dirs (`.git`, `.codex`, `.aws`, `.agents` — all empty) | noise. |

## Rewritten inside files

Applied to every text file (JSON records are parsed and re-serialised so they
stay valid):

| original | replacement |
|---|---|
| `encrypted_content` strings in `reasoning`, `compaction` and compaction-history records | `null`, plus `encrypted_content_removed_chars` |
| `creator_user_id`, `creator_account_id` in `session_meta` (and the same values anywhere else) | `REDACTED` |
| `/public_data02/ape/preprint_v1/epitope/gpt-5.6-high` (run root) | `/data/release` |
| other `/public_data02/...` project paths | `/data/...` |
| `/home/<operator>` | `/home/USER`; other home directories → `/home/COLLABORATOR` or `/home/OTHERUSER` |
| operator username, login/compute hostnames | `USER`, `login-host`, `compute-node` |
| every e-mail address (including third-party addresses printed from fetched documents) | `[email-redacted]` |
| `sk-…`, `Bearer …`, `api_key=…`-style tokens | `…REDACTED` (no genuine operator secrets were found; the only matches were `?Authorization=…` and `X-Amz-Credential=AKIA…` parameters of third-party pre-signed download URLs returned by web search, which were masked anyway) |
| build script shipped in `tools/` | the operator's username, e-mail, hostnames and project paths that the script needs as literals were replaced by placeholders in the shipped copy |

Not changed: Codex session / turn / call ids (opaque), Slurm job ids, model
names, timestamps, PDB / UniProt / PubMed / patent identifiers, URLs.

## Verification

After the build, `tools/build_reasoning_release.py --scan` was run over the
whole tree with patterns for e-mails, API keys, bearer tokens, key=value
secrets, OpenAI user ids, the operator username, non-rewritten home or
project paths, hostnames, remaining `encrypted_content`, account ids, and
SSH/AWS key material. The report is in `scan_report.txt` next to this archive
and showed zero hits in every category.
