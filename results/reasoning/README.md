# Agent reasoning logs — full sessions behind `results/`

The complete, redacted Codex sessions that produced every epitope prediction
in `results/released/` and `results/unreleased/` (hypothesis, refine, judge
and assembly stages, plus the no-cutoff arm and the SteerABLE steering
inputs / DockQ summaries). 6,760 files, 913 MB unpacked.

## Getting the archive

The archive is too large for a git file (197 MB), so it is attached to a
GitHub Release and mirrored on Zenodo:

| | |
|---|---|
| GitHub Release | https://github.com/CSSB-SNU/ape/releases/download/reasoning-logs-v1/apar_epitope_reasoning_logs_v1.tar.gz |
| Zenodo | (DOI to be added) |
| size | 187,088,522 bytes |
| sha256 | `e73bd1ba1b9fc1920be95bad35964e75d9d8d7ab99285bbb76edbcd182d9f926` (`apar_epitope_reasoning_logs_v1.tar.gz.sha256`) |

```sh
curl -LO https://github.com/CSSB-SNU/ape/releases/download/reasoning-logs-v1/apar_epitope_reasoning_logs_v1.tar.gz
sha256sum -c apar_epitope_reasoning_logs_v1.tar.gz.sha256
tar xzf apar_epitope_reasoning_logs_v1.tar.gz
```

## What is in this directory (without downloading the archive)

| file | what it is |
|---|---|
| `MANIFEST.tsv` | path, bytes, sha256 of every file in the archive |
| `lineage/hypothesis_sessions.tsv` | one row per hypothesis session (target, round, rep, timings, session id) |
| `lineage/gather_sessions.tsv` | one row per refine / judge / assembly stage dir, incl. which hypothesis sessions fed each judge packet; the `GR`/`GJ`/`G` run ids are the ones listed in `results/index.tsv` |
| `lineage/third_party_removed.tsv` | every downloaded third-party document that was removed from the archive, with sha256 and identifier |
| `REDACTION.md` | exactly what was excluded or rewritten, and how the tree was verified |
| `build_reasoning_release.py` | the script that produced the archive from the raw run directories |

## Archive contents

This archive contains the complete, redacted agent sessions behind the epitope
predictions in `results/` and `inputs/` of this repository. It is meant for
people who want to see *how* each prediction was reasoned out: every shell
command the agent ran, every file it wrote, every database / literature /
web query it issued through the search gate, the candidate advocacies, the
judge's verdicts, and the assembled answers.

Model configuration for every session: agent `gpt-5.6` (reasoning effort
`high`) driven through the Codex CLI, with a separate `gpt-5.6` search agent
(3 draws, effort `high`) behind the evidence-cutoff gate.

## What a reader can and cannot see

* **Visible**: assistant messages, tool calls with their full input and
  output, file edits, the agent's own running notes (`workdir/analysis_log.md`),
  the helper scripts the agent wrote, all search-gate traffic (queries, which
  hits were withheld by the evidence cutoff and why), the final structured
  answers, and reasoning *summaries* (one-line section headers emitted by the
  model).
* **Not visible**: the model's chain-of-thought itself. OpenAI returns it only
  as an encrypted blob (`encrypted_content`). Those blobs were removed; the
  field is kept as `null` with `encrypted_content_removed_chars` so the record
  structure is unchanged. `reasoning.md` in each session lists the readable
  summaries in order.
* **Masked**: the text of third-party documents. The agent read papers,
  patents and other downloaded documents, in excerpts or in full, through
  the helper CLIs (`paper`, `patent`, `fetch`). To avoid redistributing
  that material, the downloaded files are not in the archive and every
  tool output longer than 3,000 characters that came from a command reading
  one of them was replaced by a placeholder giving the number of characters
  removed and the files the command read. The command itself is kept, so a
  reader can see which document, and which part of it, the agent looked at,
  and can obtain the document from the identifiers in
  `lineage/third_party_removed.tsv`. Excerpts of up to 3,000 characters per
  command were kept as quotation, as were the search-engine snippets in
  `gate.searcher.log`.

## Layout

```
apar_epitope_reasoning_logs_v1/
  README.md, REDACTION.md, MANIFEST.tsv (path, bytes, sha256 of every file)
  lineage/
    hypothesis_sessions.tsv     one row per hypothesis session (target, round, rep, timings, session id)
    gather_sessions.tsv         one row per gather/refine stage dir, incl. which hypothesis
                                sessions fed each judge packet (runs a/b/c)
    third_party_removed.tsv     every third-party document removed, with sha256 and id
  hypothesis/{casp16,casp17}/r{1,2,3}/<TARGET>__case_<id>_E1_rep<N>/
                                phase-1 hypothesis sessions, 3 independent reps per target,
                                evidence cutoff enforced by the search gate
  hypothesis/casp17_nocut/r{1,2,3}/<TARGET>__case_<id>_E1_rep<N>/
                                the same for the no-cutoff arm of the unreleased targets
                                (direct web access, no gate); these feed gather_refine/unreleased_20261029/nocut
  gather_refine/
    released_structure_20261030/   targets whose complex structure was public at run time
      {casp16,casp17}/<TARGET>/case_<id>_{GR,GJ,GJ_packet,G}_rep<N>/
      results/<TARGET>/            the assembled, published answer
      CANONICAL_LINEAGE.md, canonical_lineage.json, controller*.log/json, judge_rerun*
    unreleased_20261029/           targets with no public complex structure
      {gated,nocut}/casp17/<TARGET>/...   gated = evidence cutoff enforced; nocut = no cutoff
      results/{gated,nocut}/<TARGET>/
  steerable/
    inputs/     Protenix steering inputs derived from the predicted epitopes
    dockq/      per-pose DockQ summaries of the steered predictions
                (the raw Protenix outputs, ~1 TB, are not part of this archive)
  tools/build_reasoning_release.py   the script that produced this tree from the raw runs
```

Stage codes: `GR` = refine (organise + advocate candidates), `GJ` = judge,
`GJ_packet` = the shuffled packet the judge was shown, `G` = assembled final
answer. Only the canonical rep of each stage (the one that produced the
published answer, as recorded in `CANONICAL_LINEAGE.md`) is included.

## Files inside a session directory

| file | what it is |
|---|---|
| `rollout.jsonl` | Codex session transcript: one JSON record per event (`session_meta`, developer/user/assistant messages, `reasoning` summaries, `custom_tool_call` + `custom_tool_call_output`, token counts). The primary source. |
| `run.jsonl` | Codex `exec` event stream of the same session (`command_execution` with `aggregated_output`, `file_change`, `agent_message`). Easier to read than `rollout.jsonl`. |
| `reasoning.md` | the readable reasoning summaries extracted from `rollout.jsonl`, in order |
| `prompt.txt` | the task prompt given to the agent |
| `status.json` | run metadata: target, arm, rep, model, evidence cutoff, timings, exit status |
| `answer_key.json` | the task specification handed to the harness (inputs, cutoff, schema); *not* a ground-truth answer |
| `gate.jsonl` | search-gate log: every RCSB / UniProt / literature / web request, the hit ids, and which hits were withheld by the evidence cutoff |
| `gate.searcher.log` | the search agent's own transcript for each batch of web queries |
| `gate.out`, `proxy.jsonl` | gate / whitelist-proxy startup lines |
| `out/last_message.json` | the agent's final structured answer |
| `workdir/` | the agent's working directory: inputs (`antigen.pdb`, `antibody*.pdb`, `chains.tsv`, `sequences.fasta`, `search_results.json`), the helper CLIs it was given (`research`, `paper`, `patent`, `fetch`, `rcsb`), its notes (`analysis_log.md`), scripts and result JSONs. Downloaded third-party documents were removed; see `workdir/THIRD_PARTY_REMOVED.tsv`. |
| `advocacies/`, `grouping*.json`, `staged.json`, `schema/` | refine-stage artefacts (candidate grouping, per-candidate advocacy, answer schema) |

A masked tool output looks like `[release build: 23891 chars of command
output removed because the command read third-party document files
(papers/PMC5856423.txt); ...]` and the record carries
`third_party_output_removed_chars`. In `rollout.jsonl` it replaces the
`custom_tool_call_output` text; in `run.jsonl` it replaces
`aggregated_output`.

Paths inside the logs were rewritten (see `REDACTION.md`): the original run
root appears as `/data/release/...`, so a path like
`/data/release/casp17/r1/case_fed304_E1_rep1/workdir` corresponds to
`hypothesis/casp17/r1/H1346_agCD__case_fed304_E1_rep1/workdir` here. Judge
packets reference their inputs as `runs/a`, `runs/b`, `runs/c`; those were
copies of the three hypothesis sessions' workdirs and are mapped in
`lineage/gather_sessions.tsv` instead of being duplicated.

## Reading the logs

```python
import json
for line in open("rollout.jsonl"):
    rec = json.loads(line)
    p = rec.get("payload", {})
    if p.get("type") == "custom_tool_call":
        print("CALL", p["input"][:200])
    elif p.get("type") == "custom_tool_call_output":
        print("OUT ", "".join(c.get("text", "") for c in p["output"])[:200])
    elif p.get("type") == "message" and p.get("role") == "assistant":
        print("MSG ", p["content"][0]["text"][:200])
    elif p.get("type") == "reasoning":
        print("SUM ", " ".join(s["text"] for s in p["summary"]))
```
