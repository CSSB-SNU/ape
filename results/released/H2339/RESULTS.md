# H2339 — gather batched answer

Case `case_5886c7` · set `casp17` · retrieval cutoff **2026-05-15**

Antibody: `antibody.pdb` (A:unknown, B:unknown) · antigen chains C, D

Truth: **22 residues** over D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C4** at confidence 0.44 — precision **0.294**, recall **0.227**, **F1 0.256** (5 of 17 predicted residues are in the 22-residue truth). The best pocket the answer contains is **C4**, precision **0.294**, F1 **0.256**, sitting at judge rank 1.

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
| **C4** | 1 | 0.44 | 0.55 | 17 | 0.294 | 0.227 | 0.256 | `side` | The broad active-cleft face of the f |
| **C7** | 2 | 0.25 | 0.32 | 19 | 0.000 | 0.000 | 0.000 | `side` | The allosteric 37/60/140-loop face o |
| **C5** | 3 | 0.22 | 0.3 | 14 | 0.000 | 0.000 | 0.000 | `side` | The glycan-bearing 60-loop/99-loop s |
| **C6** | 4 | 0.05 | 0.08 | 16 | 0.000 | 0.000 | 0.000 | `side` | The factor-XI activation-cleavage ju |
| **C2** | 5 | 0.02 | 0.03 | 11 | 0.000 | 0.000 | 0.000 | `side` | The solvent-exposed rim of the inter |
| **C1** | 6 | 0.01 | 0.015 | 23 | 0.000 | 0.000 | 0.000 | `side` | The high-molecular-weight-kininogen  |
| **C3** | 7 | 0.01 | 0.015 | 21 | 0.000 | 0.000 | 0.000 | `side` | The contact-defined core of the high |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> Tier A identified REGN7508 and localized it only to the factor-XI catalytic domain; no evidence about this binder separated C4, C5, and C7 at face level. Among those, the ordering is a deliberately broad Tier B prior: same-antigen antibody precedent and state recognition, independently recomputed paratope reach/charge, native glycan/accessibility, species side-chain clashes, and agreement with REGN7508's activation-biased functional phenotype. C1/C3 were the same Apple-2 face drawn twice and split only residual model-error mass.

## Which antibody binds which antigen residues

### C4 — confidence 0.44 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | D | 17 | 0.294 | 0.7571 | 0.95 | 44:0.72, 47:0.94, 48:0.77, 85:0.55, 86:0.88, 87:0.8, 89:0.68, 134:0.7, 135:0.91, 136:0.9, 137:0.95, 138:0.95, 139:0.74, 188:0.7, 208:0.4, 209:0.56, 210:0.72 |
| B (unknown) | D | 17 | 0.294 | 0.7571 | 0.95 | 44:0.72, 47:0.94, 48:0.77, 85:0.55, 86:0.88, 87:0.8, 89:0.68, 134:0.7, 135:0.91, 136:0.9, 137:0.95, 138:0.95, 139:0.74, 188:0.7, 208:0.4, 209:0.56, 210:0.72 |

> Heavy supplies about 65-70%, crossing D:44/D:47, D:89, D:134-D:139, D:188 and D:208-D:210. Light supplies about 30-35% over D:48/D:85-D:87 and the near half of the central ridge. Both chains converge at D:47/D:87 and D:134-D:139.

### C7 — confidence 0.25 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 19 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | D | 19 | 0.000 | 0.7416 | 0.95 | 23:0.74, 24:0.82, 25:0.86, 26:0.82, 27:0.15, 63:0.38, 64:0.9, 65:0.94, 67:0.48, 68:0.86, 135:0.82, 136:0.85, 137:0.94, 138:0.95, 139:0.73, 140:0.9, 141:0.75, 142:0.42, 143:0.78 |
| B (unknown) | D | 19 | 0.000 | 0.7416 | 0.95 | 23:0.74, 24:0.82, 25:0.86, 26:0.82, 27:0.15, 63:0.38, 64:0.9, 65:0.94, 67:0.48, 68:0.86, 135:0.82, 136:0.85, 137:0.94, 138:0.95, 139:0.73, 140:0.9, 141:0.75, 142:0.42, 143:0.78 |

> Heavy supplies about 65%, placing H3/H2 over D:63-D:68 and D:139-D:143. Light supplies about 35% over D:23-D:27 and D:135-D:136. Both chains converge at D:26/D:65/D:68 and D:137-D:138/D:142-D:143.

### C5 — confidence 0.22 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | D | 14 | 0.000 | 0.6964 | 0.89 | 53:0.86, 54:0.46, 56:0.71, 63:0.32, 64:0.78, 65:0.89, 66:0.58, 68:0.87, 69:0.8, 70:0.72, 72:0.77, 73:0.88, 74:0.48, 100:0.63 |
| B (unknown) | D | 14 | 0.000 | 0.6964 | 0.89 | 53:0.86, 54:0.46, 56:0.71, 63:0.32, 64:0.78, 65:0.89, 66:0.58, 68:0.87, 69:0.8, 70:0.72, 72:0.77, 73:0.88, 74:0.48, 100:0.63 |

> Heavy supplies about 60-65% over D:53-D:68 and D:73-D:74, with H3 central on D:64-D:65. Light supplies about 35-40% on D:63/D:66/D:69-D:72/D:100. Both chains converge at D:56 and D:64-D:65/D:100.

### C6 — confidence 0.05 (judge rank 4)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 6 | 0.000 | 0.7967 | 0.91 | 364:0.55, 365:0.88, 366:0.68, 367:0.91, 368:0.86, 369:0.9 |
| A (unknown) | D | 10 | 0.000 | 0.556 | 0.82 | 8:0.7, 9:0.82, 11:0.45, 104:0.55, 105:0.7, 106:0.62, 107:0.44, 108:0.5, 109:0.38, 110:0.4 |
| B (unknown) | C | 6 | 0.000 | 0.7967 | 0.91 | 364:0.55, 365:0.88, 366:0.68, 367:0.91, 368:0.86, 369:0.9 |
| B (unknown) | D | 10 | 0.000 | 0.556 | 0.82 | 8:0.7, 9:0.82, 11:0.45, 104:0.55, 105:0.7, 106:0.62, 107:0.44, 108:0.5, 109:0.38, 110:0.4 |

> Heavy contributes about 65%, centring H3 on C:365-C:369/D:8-D:9/D:105. Light contributes about 35% over C:364 and D:11/D:104/D:106-D:109. Both chains meet at C:367/C:369 and D:9/D:107/D:110.

### C2 — confidence 0.02 (judge rank 5)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 5 | 0.000 | 0.57 | 0.78 | 88:0.78, 90:0.74, 92:0.41, 94:0.42, 95:0.5 |
| A (unknown) | D | 6 | 0.000 | 0.5733 | 0.83 | 105:0.68, 229:0.55, 232:0.16, 233:0.83, 236:0.47, 238:0.75 |
| B (unknown) | C | 5 | 0.000 | 0.57 | 0.78 | 88:0.78, 90:0.74, 92:0.41, 94:0.42, 95:0.5 |
| B (unknown) | D | 6 | 0.000 | 0.5733 | 0.83 | 105:0.68, 229:0.55, 232:0.16, 233:0.83, 236:0.47, 238:0.75 |

> Heavy contributes about 60%, anchoring C:88/C:94 and D:105/D:238. Light contributes about 40% on C:90-C:95 and D:229-D:236. Both chains meet over C:90/C:94 and D:236; buried D:232 is only a low-confidence floor contact.

### C1 — confidence 0.01 (judge rank 6)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 23 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 23 | 0.000 | 0.7348 | 0.94 | 103:0.82, 105:0.58, 106:0.88, 107:0.94, 108:0.48, 109:0.78, 136:0.91, 137:0.82, 138:0.64, 139:0.72, 140:0.65, 141:0.7, 142:0.76, 143:0.93, 144:0.72, 145:0.45, 146:0.81, 148:0.84, 159:0.38, 162:0.66, 163:0.88, 164:0.79, 165:0.76 |
| B (unknown) | C | 23 | 0.000 | 0.7348 | 0.94 | 103:0.82, 105:0.58, 106:0.88, 107:0.94, 108:0.48, 109:0.78, 136:0.91, 137:0.82, 138:0.64, 139:0.72, 140:0.65, 141:0.7, 142:0.76, 143:0.93, 144:0.72, 145:0.45, 146:0.81, 148:0.84, 159:0.38, 162:0.66, 163:0.88, 164:0.79, 165:0.76 |

> Heavy supplies about 60-65%: H3/H2 cover C:103-C:140 and the C:159/C:162 anchors. Light supplies about 35-40% over C:108-C:109 and C:141-C:165. Both chains converge on C:106-C:107, C:136-C:137, C:143/C:146/C:148 and C:163.

### C3 — confidence 0.01 (judge rank 7)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:unknown, B:unknown, 21 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (unknown) | C | 21 | 0.000 | 0.6157 | 0.95 | 101:0.2, 103:0.88, 104:0.4, 105:0.7, 106:0.92, 107:0.94, 108:0.45, 109:0.82, 127:0.3, 132:0.22, 134:0.24, 136:0.79, 137:0.72, 138:0.66, 140:0.64, 143:0.95, 146:0.82, 148:0.87, 151:0.4, 163:0.86, 166:0.15 |
| B (unknown) | C | 21 | 0.000 | 0.6157 | 0.95 | 101:0.2, 103:0.88, 104:0.4, 105:0.7, 106:0.92, 107:0.94, 108:0.45, 109:0.82, 127:0.3, 132:0.22, 134:0.24, 136:0.79, 137:0.72, 138:0.66, 140:0.64, 143:0.95, 146:0.82, 148:0.87, 151:0.4, 163:0.86, 166:0.15 |

> Heavy supplies about 65% over C:101-C:140 and the hydrophobic pocket floor. Light supplies about 35% over C:108-C:109/C:127/C:151 and the C:163/C:166 edge. Both chains meet on C:106-C:107, C:136-C:137, C:140/C:143/C:146/C:148 and C:163.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| judge | `case_5886c7_GJ_rep3` | 9 | 1 | 15 |
| advocate C4 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C7 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C5 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C6 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C2 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C1 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |
| advocate C3 | `case_5886c7_GR_rep1` | 3 | 0 | 4 |

