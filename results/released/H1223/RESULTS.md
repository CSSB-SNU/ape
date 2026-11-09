# H1223 — gather batched answer

Case `case_c794c2` · set `casp16` · retrieval cutoff **2024-06-05**

Antibody: `antibody.pdb` (B:heavy, C:light) · antigen chains A

Truth: **18 residues** over A (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C3** at confidence 0.75 — precision **0.769**, recall **0.556**, **F1 0.645** (10 of 13 predicted residues are in the 18-residue truth). The best pocket the answer contains is **C2**, precision **0.818**, F1 **0.900**, sitting at judge rank 2.

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
| **C3** | 1 | 0.75 | 0.92 | 13 | 0.769 | 0.556 | 0.645 | `side` | The compact aromatic N-terminal flan |
| **C2** | 2 | 0.22 | 0.35 | 22 | 0.818 | 1.000 | 0.900 | `side` | The broad conformational face of the |
| **C1** | 3 | 0.03 | 0.08 | 16 | 0.375 | 0.333 | 0.353 | `side` | The outward face of the disulfide-st |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> Tier A evidence exists here: the pre-cutoff patent maps this binder to A:5–A:14. Because both C2 and C3 contain that core, the remaining separator was how much unsupported footprint each adds: C3 is the tighter, contiguous structural extension, whereas C2 imports distant satellites from 3G12. C1's functional and antibody-precedent lines are Tier B and conflict with the mapped center. Uniform exposure, coverability, and broad chemistry did not by themselves separate C2 from C3.

## Which antibody binds which antigen residues

### C3 — confidence 0.75 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 10 | 0.900 | 0.83 | 0.98 | 7:0.97, 8:0.91, 9:0.96, 10:0.95, 11:0.93, 12:0.98, 13:0.92, 14:0.96, 15:0.46, 16:0.26 |
| C (light) | A | 7 | 0.571 | 0.8414 | 0.97 | 4:0.36, 5:0.84, 6:0.9, 7:0.97, 8:0.91, 9:0.96, 10:0.95 |

> Heavy-dominant with a substantial light shoulder: A:4–A:6 are light, A:7–A:10 both, and A:11–A:16 heavy. The heavy side owns the later hydrophobic half and central H3, while L1/L3 provide the charged/aromatic N-terminal edge.

Pooled from 3 phase-1 patches, which drew different residues — 10 shared and 8 disputed at pooling. What the advocate then kept of each:

- `P3` (18 res) — 13 kept, 5 dropped · Broader conformational N-flank footprint around the 
- `P7` (13 res) — 13 kept, 0 dropped · Published 1G8 linear gamma1 epitope and immediate st
- `P9` (10 res) — 10 kept, 0 dropped · Patent-mapped 1G8 aromatic N-flank epitope

### C2 — confidence 0.22 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 22 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 18 | 0.889 | 0.6867 | 0.96 | 7:0.91, 9:0.89, 10:0.91, 11:0.9, 12:0.96, 13:0.87, 14:0.91, 15:0.5, 16:0.43, 17:0.27, 18:0.82, 19:0.88, 20:0.22, 21:0.78, 22:0.82, 23:0.6, 26:0.3, 33:0.39 |
| C (light) | A | 7 | 0.571 | 0.7543 | 0.91 | 4:0.42, 5:0.66, 6:0.7, 7:0.91, 8:0.79, 9:0.89, 10:0.91 |

> Heavy-dominant, roughly three-quarters by conceptual contact area: L1/L3 cover A:4–A:9, both chains meet over A:7–A:10, and H1/H2/H3 cover A:11–A:23 plus A:26/A:33.

### C1 — confidence 0.03 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 12 | 0.417 | 0.7108 | 0.94 | 20:0.16, 21:0.55, 22:0.76, 23:0.68, 24:0.82, 25:0.8, 26:0.24, 27:0.94, 28:0.86, 29:0.92, 31:0.86, 32:0.94 |
| C (light) | A | 9 | 0.111 | 0.76 | 0.94 | 27:0.94, 28:0.86, 29:0.92, 30:0.22, 31:0.86, 32:0.94, 33:0.82, 34:0.76, 35:0.52 |

> Heavy-dominant, approximately two-thirds of the conditional footprint: H1/H2/H3 cover A:20–A:29, both chains converge over A:27–A:32, and L3/L1 cover A:30–A:35.

Pooled from 5 phase-1 patches, which drew different residues — 2 shared and 21 disputed at pooling. What the advocate then kept of each:

- `P1` (14 res) — 14 kept, 0 dropped · CX3C receptor/noose face
- `P4` (11 res) — 5 kept, 6 dropped · Downstream basic heparin-binding tail
- `P5` (14 res) — 13 kept, 1 dropped · CX3C cystine-noose gamma2 surface
- `P6` (13 res) — 13 kept, 0 dropped · CX3C/noose outer face approached from the C-terminal
- `P8` (11 res) — 5 kept, 6 dropped · C-terminal basic flank

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_c794c2_GR_rep1` | 2 | 0 | 2 |
| judge | `case_c794c2_GJ_rep2` | 0 | 0 | 0 |
| advocate C3 | `case_c794c2_GR_rep1` | 2 | 0 | 2 |
| advocate C2 | `case_c794c2_GR_rep1` | 2 | 0 | 2 |
| advocate C1 | `case_c794c2_GR_rep1` | 2 | 0 | 2 |

