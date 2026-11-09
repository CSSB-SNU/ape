# H2338 — gather batched answer

Case `case_718c80` · set `casp17` · retrieval cutoff **2026-05-14**

Antibody: `antibody.pdb` (A:unknown, B:unknown) · antigen chains C, D

Truth: **17 residues** over C (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C2** at confidence 0.52 — precision **0.647**, recall **0.647**, **F1 0.647** (11 of 17 predicted residues are in the 17-residue truth). The best pocket the answer contains is **C2**, precision **0.647**, F1 **0.647**, sitting at judge rank 1.

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
| **C2** | 1 | 0.52 | 0.62 | 17 | 0.647 | 0.647 | 0.647 | `side` | The exposed loop-and-ridge face at a |
| **C3** | 2 | 0.3 | 0.38 | 19 | 0.316 | 0.353 | 0.333 | `side` | The A2 beta-sheet peptide pocket and |
| **C1** | 3 | 0.18 | 0.24 | 15 | 0.133 | 0.118 | 0.125 | `side` | The solvent-exposed outer polar/late |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate has face-level Tier A evidence: REGN9933-specific evidence stops at A2, species binding, function, and competition with an unmapped A2 antibody. C2 separated itself through independent Tier-B agreement between exact-antigen other-antibody HDX and the best computed geometry/chemistry. C3's functional-pocket evidence concerns another ligand, while C1's homolog precedent lost discriminatory value after measuring only 50% identity over a broad interval.

## Which antibody binds which antigen residues

### C2 — confidence 0.52 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 17 | 0.647 | 0.7441 | 0.94 | 136:0.78, 137:0.72, 138:0.34, 139:0.84, 140:0.62, 141:0.89, 142:0.93, 143:0.94, 144:0.91, 145:0.61, 146:0.38, 148:0.5, 161:0.55, 162:0.92, 163:0.88, 164:0.93, 165:0.91 |
| B (unknown) | C | 17 | 0.647 | 0.7441 | 0.94 | 136:0.78, 137:0.72, 138:0.34, 139:0.84, 140:0.62, 141:0.89, 142:0.93, 143:0.94, 144:0.91, 145:0.61, 146:0.38, 148:0.5, 161:0.55, 162:0.92, 163:0.88, 164:0.93, 165:0.91 |

> Strongly heavy-dominant: H3/H2 cover C:141-C:144 and C:162-C:165; both chains converge on C:139/C:142/C:143/C:145/C:163; light loops cover the outer rim.

Pooled from 3 phase-1 patches, which drew different residues — 10 shared and 22 disputed at pooling. What the advocate then kept of each:

- `P2` (21 res) — 17 kept, 4 dropped · A2 antibody-hotspot face around residues 133-148 and
- `P5` (12 res) — 12 kept, 0 dropped · A2 C-terminal loop face
- `P8` (27 res) — 15 kept, 12 dropped · A2 DFP-ligand groove and basic mouth

### C3 — confidence 0.3 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 19 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 19 | 0.316 | 0.6474 | 0.92 | 103:0.91, 105:0.76, 106:0.92, 107:0.74, 108:0.24, 109:0.7, 110:0.34, 132:0.42, 134:0.44, 143:0.86, 146:0.56, 148:0.82, 151:0.52, 153:0.82, 154:0.68, 158:0.67, 159:0.72, 161:0.42, 163:0.76 |
| B (unknown) | C | 19 | 0.316 | 0.6474 | 0.92 | 103:0.91, 105:0.76, 106:0.92, 107:0.74, 108:0.24, 109:0.7, 110:0.34, 132:0.42, 134:0.44, 143:0.86, 146:0.56, 148:0.82, 151:0.52, 153:0.82, 154:0.68, 158:0.67, 159:0.72, 161:0.42, 163:0.76 |

> Heavy-dominant pocket engagement: H3 occupies C:103/C:105/C:106/C:132/C:134/C:143/C:146, both chains meet across C:107/C:109/C:148/C:151/C:163, and L1/L3 cover C:108/C:110/C:153-C:161.

Pooled from 2 phase-1 patches, which drew different residues — 7 shared and 20 disputed at pooling. What the advocate then kept of each:

- `P4` (21 res) — 15 kept, 6 dropped · A2 DFP-peptide groove and distal 151-159 lobe
- `P7` (13 res) — 11 kept, 2 dropped · A2 beta-sheet ligand pocket and rim

### C1 — confidence 0.18 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 15 | 0.133 | 0.6067 | 0.94 | 95:0.52, 96:0.55, 98:0.68, 99:0.4, 110:0.42, 111:0.72, 113:0.94, 114:0.68, 115:0.38, 116:0.88, 117:0.67, 120:0.82, 121:0.74, 124:0.48, 174:0.22 |
| B (unknown) | C | 15 | 0.133 | 0.6067 | 0.94 | 95:0.52, 96:0.55, 98:0.68, 99:0.4, 110:0.42, 111:0.72, 113:0.94, 114:0.68, 115:0.38, 116:0.88, 117:0.67, 120:0.82, 121:0.74, 124:0.48, 174:0.22 |

> Heavy-dominant: H3 centres on C:111/C:113/C:116/C:121, H2 supports the 117/120/124 acidic ridge, and light loops cover the 95-99/174 rim.

Pooled from 3 phase-1 patches, which drew different residues — 6 shared and 15 disputed at pooling. What the advocate then kept of each:

- `P1` (11 res) — 10 kept, 1 dropped · A2 outer polar face
- `P3` (16 res) — 14 kept, 2 dropped · A2 N-terminal/polar face near the A1 and protease-fa
- `P6` (11 res) — 7 kept, 4 dropped · A2 charged lateral ridge

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_718c80_GR_rep1` | 4 | 0 | 0 |
| judge | `case_718c80_GJ_rep2` | 5 | 1 | 9 |
| advocate C2 | `case_718c80_GR_rep1` | 4 | 0 | 0 |
| advocate C3 | `case_718c80_GR_rep1` | 4 | 0 | 0 |
| advocate C1 | `case_718c80_GR_rep1` | 4 | 0 | 0 |

