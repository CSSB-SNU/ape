# H1225 — gather batched answer

Case `case_db141c` · set `casp16` · retrieval cutoff **2024-06-06**

Antibody: `antibody.pdb` (B:unknown, C:unknown) · antigen chains A

Truth: **17 residues** over A (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C3** at confidence 0.76 — precision **0.750**, recall **0.706**, **F1 0.727** (12 of 16 predicted residues are in the 17-residue truth). The best pocket the answer contains is **C1**, precision **1.000**, F1 **0.786**, sitting at judge rank 2.

## The two confidences, and where each comes from

| level | field | source | meaning | sums to |
|---|---|---|---|---|
| **pocket** (global) | `pocket.confidence` | the judge | how sure the judge is that this pocket is the site | about 1 across pockets |
| **residue** | `interfaces[].residue_confidence` | that pocket's advocate | P(residue in the interface \| this pocket is the epitope) | nothing |

The residue level is conditional on the pocket being right, so it is **not** reduced by the judge's doubt about the pocket. To weight a residue across the whole answer, multiply the two. Nothing is thresholded: the whole vector is the answer and where to cut is yours. `mapping.tsv` carries both on every row.

The judge holds no residues at all — by design, it ranks, and the footprint under each rank is that pocket's advocacy verbatim. So every residue number and residue confidence here comes from an advocate, and every pocket confidence from the judge.

## Pockets, and how sure the judge is of each

| pocket | judge rank | confidence | p(rests_on) | n res | precision | recall | F1 | mapping | name |
|---|---|---|---|---|---|---|---|---|---|
| **C3** | 1 | 0.76 | 0.84 | 16 | 0.750 | 0.706 | 0.727 | `side` | The broad N-terminal conserved face  |
| **C1** | 2 | 0.18 | 0.3 | 11 | 1.000 | 0.647 | 0.786 | `side` | The exposed N-terminal hydrophobic r |
| **C2** | 3 | 0.06 | 0.12 | 12 | 0.250 | 0.176 | 0.207 | `side` | The receptor-facing cystine-noose/CX |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> Tier A evidence exists here: the exact binder is 1G1. No single patent statement uniquely selects C3, because the interval also reaches C1 and conformational binding also fits C2. Their conjunction does: C3 contains the interval and supplies a discontinuous folded shoulder, whereas C1 explains only the interval and C2 only the conformational character. All three pass geometry and have other-antibody precedent, so those Tier B lines mainly establish feasibility and do not drive the order.

## Which antibody binds which antigen residues

### C3 — confidence 0.76 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:unknown, C:unknown, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 16 | 0.750 | 0.7731 | 0.94 | 4:0.48, 5:0.62, 6:0.82, 7:0.92, 8:0.84, 9:0.94, 10:0.9, 11:0.93, 12:0.92, 13:0.85, 14:0.86, 18:0.68, 19:0.84, 21:0.58, 22:0.66, 23:0.53 |
| C (unknown) | A | 16 | 0.750 | 0.7731 | 0.94 | 4:0.48, 5:0.62, 6:0.82, 7:0.92, 8:0.84, 9:0.94, 10:0.9, 11:0.93, 12:0.92, 13:0.85, 14:0.86, 18:0.68, 19:0.84, 21:0.58, 22:0.66, 23:0.53 |

> Approximately 70:30 heavy:light. L1/L3 occupy the A:4-A:11 edge; H3/H1/H2 dominate A:6-A:14 and extend to A:18-A:23, with both-chain overlap at A:6-A:8 and A:10-A:11.

Pooled from 2 phase-1 patches, which drew different residues — 20 shared and 2 disputed at pooling. What the advocate then kept of each:

- `P7` (22 res) — 16 kept, 6 dropped · 3G12-like N-terminal conserved face
- `P9` (20 res) — 16 kept, 4 dropped · N-terminal conserved hydrophobic face

### C1 — confidence 0.18 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:unknown, C:unknown, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 11 | 1.000 | 0.7391 | 0.95 | 6:0.72, 7:0.93, 8:0.55, 9:0.95, 10:0.7, 11:0.88, 12:0.94, 13:0.78, 14:0.91, 15:0.42, 16:0.35 |
| C (unknown) | A | 11 | 1.000 | 0.7391 | 0.95 | 6:0.72, 7:0.93, 8:0.55, 9:0.95, 10:0.7, 11:0.88, 12:0.94, 13:0.78, 14:0.91, 15:0.42, 16:0.35 |

> Approximately 75:25 heavy:light. H3/H1/H2 form the aromatic ridge-binding center; L1/L3 supply a smaller polar edge, with overlap around A:6-A:9 and A:12-A:13.

### C2 — confidence 0.06 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:unknown, C:unknown, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 12 | 0.250 | 0.735 | 0.96 | 17:0.4, 21:0.72, 22:0.88, 23:0.76, 24:0.84, 25:0.86, 27:0.96, 28:0.82, 29:0.93, 30:0.25, 31:0.52, 32:0.88 |
| C (unknown) | A | 12 | 0.250 | 0.735 | 0.96 | 17:0.4, 21:0.72, 22:0.88, 23:0.76, 24:0.84, 25:0.86, 27:0.96, 28:0.82, 29:0.93, 30:0.25, 31:0.52, 32:0.88 |

> Approximately 80:20 heavy:light. H3/H2 cover A:17/A:21-A:22/A:24-A:32; L1/L3 form a smaller polar shelf at A:22-A:24 and A:27, with both-chain overlap at A:22/A:24/A:27.

Pooled from 6 phase-1 patches, which drew different residues — 2 shared and 33 disputed at pooling. What the advocate then kept of each:

- `P2` (18 res) — 12 kept, 6 dropped · CX3C cystine-noose/Trp27 face
- `P3` (24 res) — 4 kept, 20 dropped · Bipartite conserved-flank face around the cystine no
- `P4` (18 res) — 12 kept, 6 dropped · CX3C/cystine-noose face
- `P5` (21 res) — 1 kept, 20 dropped · Folded conserved-strand/C-terminal-return face
- `P6` (16 res) — 12 kept, 4 dropped · 2D10-like cystine-noose/CX3C face
- `P8` (22 res) — 2 kept, 20 dropped · CB017.5-like conserved N/C-flank clasp

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_db141c_GR_rep1` | 13 | 0 | 0 |
| judge | `case_db141c_GJ_rep2` | 0 | 0 | 0 |
| advocate C3 | `case_db141c_GR_rep1` | 13 | 0 | 0 |
| advocate C1 | `case_db141c_GR_rep1` | 13 | 0 | 0 |
| advocate C2 | `case_db141c_GR_rep1` | 13 | 0 | 0 |

