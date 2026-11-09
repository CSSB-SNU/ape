# H2321 — gather batched answer

Case `case_6e4153` · set `casp17` · retrieval cutoff **2026-05-20**

Antibody: `antibody.1.pdb` (B:unknown, F:unknown), `antibody.2.pdb` (C:unknown, E:unknown) · antigen chains A, D

Truth: **70 residues** over A, D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C3** at confidence 0.47 — precision **0.571**, recall **0.114**, **F1 0.191** (8 of 14 predicted residues are in the 70-residue truth). The best pocket the answer contains is **C1**, precision **0.667**, F1 **0.195**, sitting at judge rank 3.

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
| **C3** | 1 | 0.47 | 0.72 | 14 | 0.571 | 0.114 | 0.191 | `per_antibody` | The 2A2 escape-centred lateral ridge |
| **C5** | 2 | 0.35 | 0.65 | 12 | 0.500 | 0.086 | 0.146 | `per_antibody` | The compact S205/R209 loop-and-shoul |
| **C1** | 3 | 0.13 | 0.4 | 12 | 0.667 | 0.114 | 0.195 | `per_antibody` | The lower lateral face of the dimeri |
| **C4** | 4 | 0.02 | 0.08 | 14 | 0.286 | 0.057 | 0.095 | `per_antibody` | A compact, single-protomer acidic mi |
| **C2** | 5 | 0.01 | 0.04 | 12 | 0.167 | 0.029 | 0.049 | `per_antibody` | A glycan-free upper-lateral single-p |
| **C6** | 6 | 0.007 | 0.02 | 10 | 0.000 | 0.000 | 0.000 | `per_antibody` | A compact, single-protomer protrudin |
| **C7** | 7 | 0.007 | 0.02 | 12 | 0.000 | 0.000 | 0.000 | `per_antibody` | The discrete 133–140 protruding top- |
| **C8** | 8 | 0.006 | 0.02 | 20 | 0.000 | 0.000 | 0.000 | `per_antibody` | One of two symmetry-related quaterna |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> A Tier A line exists: exact patent sequences identify supplied 2A2, and its dated escape pair maps to S205/R209, separating C1/C3/C5 from the other five. Geometry demotes C1's lower extension but cannot decisively separate overlapping C3 and C5, so most mass remains split between them.

## Which antibody binds which antigen residues

### C3 — confidence 0.47 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `straddling`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 6 | 0.500 | 0.8733 | 0.99 | 154:0.68, 204:0.82, 205:0.99, 207:0.86, 209:0.99, 210:0.9 |
| B (unknown) | D | 1 | 1.000 | 0.56 | 0.56 | 247:0.56 |
| F (unknown) | A | 6 | 0.500 | 0.8733 | 0.99 | 154:0.68, 204:0.82, 205:0.99, 207:0.86, 209:0.99, 210:0.9 |
| F (unknown) | D | 1 | 1.000 | 0.56 | 0.56 | 247:0.56 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `straddling`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 1 | 1.000 | 0.56 | 0.56 | 247:0.56 |
| C (unknown) | D | 6 | 0.500 | 0.8733 | 0.99 | 154:0.68, 204:0.82, 205:0.99, 207:0.86, 209:0.99, 210:0.9 |
| E (unknown) | A | 1 | 1.000 | 0.56 | 0.56 | 247:0.56 |
| E (unknown) | D | 6 | 0.500 | 0.8733 | 0.99 | 154:0.68, 204:0.82, 205:0.99, 207:0.86, 209:0.99, 210:0.9 |

> Heavy-dominant 203–211 ridge; the light chain covers the 152–159 shoulder and opposite-protomer 245/247 rim, with both chains converging at Y204/S205/L154.

### C5 — confidence 0.35 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `straddling`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 5 | 0.400 | 0.92 | 0.99 | 204:0.84, 205:0.99, 207:0.87, 209:0.99, 210:0.91 |
| B (unknown) | D | 1 | 1.000 | 0.54 | 0.54 | 247:0.54 |
| F (unknown) | A | 5 | 0.400 | 0.92 | 0.99 | 204:0.84, 205:0.99, 207:0.87, 209:0.99, 210:0.91 |
| F (unknown) | D | 1 | 1.000 | 0.54 | 0.54 | 247:0.54 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `straddling`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 1 | 1.000 | 0.54 | 0.54 | 247:0.54 |
| C (unknown) | D | 5 | 0.400 | 0.92 | 0.99 | 204:0.84, 205:0.99, 207:0.87, 209:0.99, 210:0.91 |
| E (unknown) | A | 1 | 1.000 | 0.54 | 0.54 | 247:0.54 |
| E (unknown) | D | 5 | 0.400 | 0.92 | 0.99 | 204:0.84, 205:0.99, 207:0.87, 209:0.99, 210:0.91 |

> Heavy-dominant 203–211 core; light-chain shoulder and opposite-protomer rim, with both chains converging at 154/204/205.

### C1 — confidence 0.13 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `straddling`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 5 | 0.600 | 0.878 | 0.99 | 154:0.68, 205:0.99, 207:0.84, 209:0.99, 210:0.89 |
| B (unknown) | D | 1 | 1.000 | 0.5 | 0.5 | 247:0.5 |
| F (unknown) | A | 5 | 0.600 | 0.878 | 0.99 | 154:0.68, 205:0.99, 207:0.84, 209:0.99, 210:0.89 |
| F (unknown) | D | 1 | 1.000 | 0.5 | 0.5 | 247:0.5 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `straddling`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 1 | 1.000 | 0.5 | 0.5 | 247:0.5 |
| C (unknown) | D | 5 | 0.600 | 0.878 | 0.99 | 154:0.68, 205:0.99, 207:0.84, 209:0.99, 210:0.89 |
| E (unknown) | A | 1 | 1.000 | 0.5 | 0.5 | 247:0.5 |
| E (unknown) | D | 5 | 0.600 | 0.878 | 0.99 | 154:0.68, 205:0.99, 207:0.84, 209:0.99, 210:0.89 |

> Heavy-dominant core over S205/T207/R209/Q210; the light chain covers the 150–156 shoulder and the opposite-protomer 247/249 rim.

### C4 — confidence 0.02 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `single-chain`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 7 | 0.286 | 0.7814 | 0.96 | 112:0.74, 113:0.82, 114:0.7, 156:0.78, 158:0.96, 159:0.8, 161:0.67 |
| F (unknown) | A | 7 | 0.286 | 0.7814 | 0.96 | 112:0.74, 113:0.82, 114:0.7, 156:0.78, 158:0.96, 159:0.8, 161:0.67 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `single-chain`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | D | 7 | 0.286 | 0.7814 | 0.96 | 112:0.74, 113:0.82, 114:0.7, 156:0.78, 158:0.96, 159:0.8, 161:0.67 |
| E (unknown) | D | 7 | 0.286 | 0.7814 | 0.96 | 112:0.74, 113:0.82, 114:0.7, 156:0.78, 158:0.96, 159:0.8, 161:0.67 |

> Heavy chain dominates the 112–159 acidic centre; the light chain supports the outer acidic and hydrophobic edges.

### C2 — confidence 0.01 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `single-chain`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 6 | 0.167 | 0.735 | 0.86 | 44:0.63, 112:0.72, 113:0.78, 114:0.7, 158:0.86, 159:0.72 |
| F (unknown) | A | 6 | 0.167 | 0.735 | 0.86 | 44:0.63, 112:0.72, 113:0.78, 114:0.7, 158:0.86, 159:0.72 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `single-chain`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | D | 6 | 0.167 | 0.735 | 0.86 | 44:0.63, 112:0.72, 113:0.78, 114:0.7, 158:0.86, 159:0.72 |
| E (unknown) | D | 6 | 0.167 | 0.735 | 0.86 | 44:0.63, 112:0.72, 113:0.78, 114:0.7, 158:0.86, 159:0.72 |

> Heavy chain over the 112–163 acidic/polar centre; light chain over the 43–50 lip and outer rim.

### C6 — confidence 0.007 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `single-chain`, 5 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 5 | 0.000 | 0.82 | 0.98 | 133:0.6, 136:0.88, 137:0.98, 138:0.94, 139:0.7 |
| F (unknown) | A | 5 | 0.000 | 0.82 | 0.98 | 133:0.6, 136:0.88, 137:0.98, 138:0.94, 139:0.7 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `single-chain`, 5 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | D | 5 | 0.000 | 0.82 | 0.98 | 133:0.6, 136:0.88, 137:0.98, 138:0.94, 139:0.7 |
| E (unknown) | D | 5 | 0.000 | 0.82 | 0.98 | 133:0.6, 136:0.88, 137:0.98, 138:0.94, 139:0.7 |

> H3-dominant cap over Q136/P137/H138/Q139; light loops support the 131–134/N223 side.

### C7 — confidence 0.007 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `single-chain`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 6 | 0.000 | 0.8033 | 0.98 | 133:0.62, 135:0.65, 136:0.9, 137:0.98, 138:0.95, 139:0.72 |
| F (unknown) | A | 6 | 0.000 | 0.8033 | 0.98 | 133:0.62, 135:0.65, 136:0.9, 137:0.98, 138:0.95, 139:0.72 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `single-chain`, 6 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | D | 6 | 0.000 | 0.8033 | 0.98 | 133:0.62, 135:0.65, 136:0.9, 137:0.98, 138:0.95, 139:0.72 |
| E (unknown) | D | 6 | 0.000 | 0.8033 | 0.98 | 133:0.62, 135:0.65, 136:0.9, 137:0.98, 138:0.95, 139:0.72 |

> H3 dominates P137/H138 and the Q136/Q139 shoulders; light loops support H131/N133/A134/N223.

### C8 — confidence 0.006 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:unknown, F:unknown, binding mode `straddling`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (unknown) | A | 8 | 0.000 | 0.85 | 0.94 | 173:0.72, 174:0.78, 175:0.84, 176:0.82, 177:0.92, 178:0.94, 179:0.88, 180:0.9 |
| B (unknown) | D | 2 | 0.000 | 0.68 | 0.72 | 195:0.72, 197:0.64 |
| F (unknown) | A | 8 | 0.000 | 0.85 | 0.94 | 173:0.72, 174:0.78, 175:0.84, 176:0.82, 177:0.92, 178:0.94, 179:0.88, 180:0.9 |
| F (unknown) | D | 2 | 0.000 | 0.68 | 0.72 | 195:0.72, 197:0.64 |

**`antibody.2.pdb`** — chains C:unknown, E:unknown, binding mode `straddling`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 2 | 0.000 | 0.68 | 0.72 | 195:0.72, 197:0.64 |
| C (unknown) | D | 8 | 0.000 | 0.85 | 0.94 | 173:0.72, 174:0.78, 175:0.84, 176:0.82, 177:0.92, 178:0.94, 179:0.88, 180:0.9 |
| E (unknown) | A | 2 | 0.000 | 0.68 | 0.72 | 195:0.72, 197:0.64 |
| E (unknown) | D | 8 | 0.000 | 0.85 | 0.94 | 173:0.72, 174:0.78, 175:0.84, 176:0.82, 177:0.92, 178:0.94, 179:0.88, 180:0.9 |

> Heavy chain dominates the 172–181 major loop; light chain covers the partner 192–199 turn, with convergence at 177–181/195.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| judge | `case_6e4153_GJ_rep2` | 0 | 0 | 0 |
| advocate C3 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C5 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C1 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C4 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C2 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C6 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C7 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |
| advocate C8 | `case_6e4153_GR_rep1` | 1 | 0 | 0 |

