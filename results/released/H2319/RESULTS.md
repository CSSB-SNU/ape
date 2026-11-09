# H2319 — gather batched answer

Case `case_5816d5` · set `casp17` · retrieval cutoff **2026-05-19**

Antibody: `antibody.1.pdb` (B:heavy, F:light), `antibody.2.pdb` (C:light, E:heavy) · antigen chains A, D

Truth: **26 residues** over A, D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C5** at confidence 0.5 — precision **0.769**, recall **0.769**, **F1 0.769** (20 of 26 predicted residues are in the 26-residue truth). The best pocket the answer contains is **C5**, precision **0.769**, F1 **0.769**, sitting at judge rank 1.

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
| **C5** | 1 | 0.5 | 0.56 | 26 | 0.769 | 0.769 | 0.769 | `per_antibody` | The 7C8 escape-loop epitope on each  |
| **C7** | 2 | 0.41 | 0.48 | 26 | 0.769 | 0.769 | 0.769 | `per_antibody` | A shallow two-loop lateral face join |
| **C8** | 3 | 0.022 | 0.04 | 22 | 0.000 | 0.000 | 0.000 | `per_antibody` | An acidic lateral site where the 156 |
| **C6** | 4 | 0.018 | 0.035 | 28 | 0.000 | 0.000 | 0.000 | `per_antibody` | A dimer-edge antigenic site centred  |
| **C2** | 5 | 0.013 | 0.03 | 26 | 0.000 | 0.000 | 0.000 | `per_antibody` | An upper lateral single-protomer ter |
| **C9** | 6 | 0.012 | 0.025 | 20 | 0.000 | 0.000 | 0.000 | `per_antibody` | A highly exposed upper lateral terra |
| **C4** | 7 | 0.01 | 0.025 | 20 | 0.000 | 0.000 | 0.000 | `per_antibody` | A basic lower-lateral shoulder combi |
| **C1** | 8 | 0.008 | 0.02 | 28 | 0.000 | 0.000 | 0.000 | `per_antibody` | The distal shoulder of the intertwin |
| **C3** | 9 | 0.007 | 0.018 | 22 | 0.000 | 0.000 | 0.000 | `per_antibody` | The narrow distal quaternary cap mad |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> Tier A exists here: exact sequence identification connects the supplied binder to 7C8, and 7C8 escape localizes it to P137. That concentrates 0.91 on the overlapping C5/C7 neighborhood. Nothing pre-cutoff separates their boundaries, so the modest C5 edge comes only from an independent structural comparison: C5 is tighter around P137 and more exposed on average. Generic exposure, function and antibody precedent did not decide the order among the remaining surfaces.

## Which antibody binds which antigen residues

### C5 — confidence 0.5 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 9 | 0.889 | 0.7889 | 0.99 | 133:0.68, 134:0.76, 135:0.88, 136:0.96, 137:0.99, 138:0.93, 139:0.7, 140:0.55, 235:0.65 |
| F (light) | A | 7 | 0.714 | 0.65 | 0.99 | 136:0.96, 137:0.99, 223:0.42, 235:0.65, 236:0.58, 238:0.45, 239:0.5 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 7 | 0.714 | 0.65 | 0.99 | 136:0.96, 137:0.99, 223:0.42, 235:0.65, 236:0.58, 238:0.45, 239:0.5 |
| E (heavy) | D | 9 | 0.889 | 0.7889 | 0.99 | 133:0.68, 134:0.76, 135:0.88, 136:0.96, 137:0.99, 138:0.93, 139:0.7, 140:0.55, 235:0.65 |

> B/E H1-H3 dominate E135-Q136-P137-H138; F/C L1/L3 cover N223 and E235-S239. Q136, P137 and E235 lie at the junction.

### C7 — confidence 0.41 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 8 | 1.000 | 0.795 | 0.99 | 134:0.72, 135:0.86, 136:0.95, 137:0.99, 138:0.92, 139:0.68, 140:0.52, 235:0.72 |
| F (light) | A | 8 | 0.625 | 0.625 | 0.99 | 136:0.95, 137:0.99, 233:0.22, 235:0.72, 236:0.64, 237:0.44, 238:0.48, 239:0.56 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 8 | 0.625 | 0.625 | 0.99 | 136:0.95, 137:0.99, 233:0.22, 235:0.72, 236:0.64, 237:0.44, 238:0.48, 239:0.56 |
| E (heavy) | D | 8 | 1.000 | 0.795 | 0.99 | 134:0.72, 135:0.86, 136:0.95, 137:0.99, 138:0.92, 139:0.68, 140:0.52, 235:0.72 |

> B/E heavy centres on E135-Q136-P137-H138; F/C light covers P233 and E235-D239. Q136, P137 and E235 are junction residues.

### C8 — confidence 0.022 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 7 | 0.000 | 0.6257 | 0.96 | 114:0.55, 156:0.8, 157:0.25, 158:0.96, 159:0.75, 161:0.65, 201:0.42 |
| F (light) | A | 7 | 0.000 | 0.5443 | 0.96 | 112:0.5, 113:0.65, 114:0.55, 158:0.96, 201:0.42, 204:0.28, 205:0.45 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 7 | 0.000 | 0.5443 | 0.96 | 112:0.5, 113:0.65, 114:0.55, 158:0.96, 201:0.42, 204:0.28, 205:0.45 |
| E (heavy) | D | 7 | 0.000 | 0.6257 | 0.96 | 114:0.55, 156:0.8, 157:0.25, 158:0.96, 159:0.75, 161:0.65, 201:0.42 |

> B/E heavy covers the acidic 156-161 centre; F/C light reaches 112-114 and 201-205. R114, E158 and R201 are junction residues.

### C6 — confidence 0.018 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 9 | 0.000 | 0.6033 | 0.96 | 77:0.3, 78:0.5, 79:0.5, 80:0.42, 153:0.4, 154:0.68, 156:0.72, 205:0.95, 209:0.96 |
| F (light) | A | 8 | 0.000 | 0.6462 | 0.96 | 79:0.5, 80:0.42, 156:0.72, 204:0.25, 205:0.95, 207:0.55, 209:0.96, 210:0.82 |
| F (light) | D | 2 | 0.000 | 0.23 | 0.26 | 245:0.2, 247:0.26 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | A | 2 | 0.000 | 0.23 | 0.26 | 245:0.2, 247:0.26 |
| C (light) | D | 8 | 0.000 | 0.6462 | 0.96 | 79:0.5, 80:0.42, 156:0.72, 204:0.25, 205:0.95, 207:0.55, 209:0.96, 210:0.82 |
| E (heavy) | D | 9 | 0.000 | 0.6033 | 0.96 | 77:0.3, 78:0.5, 79:0.5, 80:0.42, 153:0.4, 154:0.68, 156:0.72, 205:0.95, 209:0.96 |

> B/E heavy covers 77-80 and 153-156 and meets light at S205; F/C L3 covers R209/Q210 and may graze the partner 245/247 rim.

### C2 — confidence 0.013 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 8 | 0.000 | 0.6837 | 0.94 | 43:0.79, 44:0.67, 45:0.94, 46:0.5, 47:0.82, 48:0.9, 49:0.54, 52:0.31 |
| F (light) | A | 8 | 0.000 | 0.5712 | 0.82 | 44:0.67, 47:0.82, 52:0.31, 55:0.51, 112:0.56, 113:0.72, 115:0.4, 117:0.58 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 8 | 0.000 | 0.5712 | 0.82 | 44:0.67, 47:0.82, 52:0.31, 55:0.51, 112:0.56, 113:0.72, 115:0.4, 117:0.58 |
| E (heavy) | D | 8 | 0.000 | 0.6837 | 0.94 | 43:0.79, 44:0.67, 45:0.94, 46:0.5, 47:0.82, 48:0.9, 49:0.54, 52:0.31 |

> B/E heavy covers the 43-49 ridge; F/C light covers 55 and 112-117. D44, E47 and the inter-loop junction are shared.

### C9 — confidence 0.012 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 7 | 0.000 | 0.7457 | 0.94 | 41:0.48, 43:0.8, 44:0.7, 45:0.94, 47:0.84, 48:0.91, 50:0.55 |
| F (light) | A | 5 | 0.000 | 0.676 | 0.84 | 44:0.7, 47:0.84, 112:0.58, 113:0.7, 117:0.56 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 5 | 0.000 | 0.676 | 0.84 | 44:0.7, 47:0.84, 112:0.58, 113:0.7, 117:0.56 |
| E (heavy) | D | 7 | 0.000 | 0.7457 | 0.94 | 41:0.48, 43:0.8, 44:0.7, 45:0.94, 47:0.84, 48:0.91, 50:0.55 |

> B/E H1-H3 covers the 41-50 terrace; F/C L1/L3 covers 112-117. D44 and E47 form the shared junction.

### C4 — confidence 0.01 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 8 | 0.000 | 0.715 | 0.86 | 114:0.86, 115:0.64, 117:0.72, 150:0.58, 153:0.51, 154:0.79, 156:0.78, 209:0.84 |
| F (light) | A | 6 | 0.000 | 0.7067 | 0.86 | 114:0.86, 115:0.64, 156:0.78, 209:0.84, 210:0.77, 211:0.35 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | D | 6 | 0.000 | 0.7067 | 0.86 | 114:0.86, 115:0.64, 156:0.78, 209:0.84, 210:0.77, 211:0.35 |
| E (heavy) | D | 8 | 0.000 | 0.715 | 0.86 | 114:0.86, 115:0.64, 117:0.72, 150:0.58, 153:0.51, 154:0.79, 156:0.78, 209:0.84 |

> B/E heavy covers Y117/K150/V153/L154 and meets light at R114/E156; F/C L3 reaches R209/Q210/G211.

### C1 — confidence 0.008 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 9 | 0.000 | 0.7389 | 0.93 | 172:0.25, 173:0.68, 174:0.88, 175:0.86, 176:0.64, 177:0.89, 178:0.93, 179:0.7, 180:0.82 |
| B (heavy) | D | 1 | 0.000 | 0.74 | 0.74 | 195:0.74 |
| F (light) | A | 3 | 0.000 | 0.5967 | 0.82 | 173:0.68, 180:0.82, 181:0.29 |
| F (light) | D | 4 | 0.000 | 0.395 | 0.74 | 193:0.12, 194:0.32, 195:0.74, 196:0.4 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | A | 4 | 0.000 | 0.395 | 0.74 | 193:0.12, 194:0.32, 195:0.74, 196:0.4 |
| C (light) | D | 3 | 0.000 | 0.5967 | 0.82 | 173:0.68, 180:0.82, 181:0.29 |
| E (heavy) | A | 1 | 0.000 | 0.74 | 0.74 | 195:0.74 |
| E (heavy) | D | 9 | 0.000 | 0.7389 | 0.93 | 172:0.25, 173:0.68, 174:0.88, 175:0.86, 176:0.64, 177:0.89, 178:0.93, 179:0.7, 180:0.82 |

> For antibody.1, B heavy covers A:172-180 and F light closes on D:193-196; antibody.2 uses E heavy on D and C light on A. Residues 173, 180 and 195 can be shared by both paratope chains.

### C3 — confidence 0.007 (judge rank 9)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains B:heavy, F:light, binding mode `straddling`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 8 | 0.000 | 0.805 | 0.94 | 173:0.67, 174:0.87, 175:0.88, 176:0.66, 177:0.9, 178:0.94, 179:0.72, 180:0.8 |
| B (heavy) | D | 1 | 0.000 | 0.78 | 0.78 | 195:0.78 |
| F (light) | A | 2 | 0.000 | 0.735 | 0.8 | 173:0.67, 180:0.8 |
| F (light) | D | 3 | 0.000 | 0.6067 | 0.78 | 195:0.78, 196:0.58, 197:0.46 |

**`antibody.2.pdb`** — chains C:light, E:heavy, binding mode `straddling`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (light) | A | 3 | 0.000 | 0.6067 | 0.78 | 195:0.78, 196:0.58, 197:0.46 |
| C (light) | D | 2 | 0.000 | 0.735 | 0.8 | 173:0.67, 180:0.8 |
| E (heavy) | A | 1 | 0.000 | 0.78 | 0.78 | 195:0.78 |
| E (heavy) | D | 8 | 0.000 | 0.805 | 0.94 | 173:0.67, 174:0.87, 175:0.88, 176:0.66, 177:0.9, 178:0.94, 179:0.72, 180:0.8 |

> B/E heavy occupies the 173-180 crest; F/C L3 occupies the partner 195-197 tip. Residues 173, 180 and 195 form the shared junction.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| judge | `case_5816d5_GJ_rep2` | 2 | 0 | 0 |
| advocate C5 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C7 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C8 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C6 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C2 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C9 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C4 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C1 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |
| advocate C3 | `case_5816d5_GR_rep1` | 2 | 0 | 1 |

