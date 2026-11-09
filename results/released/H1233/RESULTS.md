# H1233 — gather batched answer

Case `case_a49017` · set `casp16` · retrieval cutoff **2024-06-16**

Antibody: `antibody.1.pdb` (C:unknown, F:unknown), `antibody.2.pdb` (D:unknown, E:unknown) · antigen chains A, B

Truth: **44 residues** over A, B (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C5** at confidence 0.42 — precision **0.571**, recall **0.364**, **F1 0.444** (16 of 28 predicted residues are in the 44-residue truth). The best pocket the answer contains is **C3**, precision **0.455**, F1 **0.455**, sitting at judge rank 2.

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
| **C5** | 1 | 0.42 | 0.52 | 28 | 0.571 | 0.364 | 0.444 | `per_antibody` | A compact version of the inferior/la |
| **C3** | 2 | 0.265 | 0.4 | 44 | 0.455 | 0.455 | 0.455 | `per_antibody` | The inferior/lateral loop-2 face of  |
| **C8** | 3 | 0.265 | 0.4 | 44 | 0.455 | 0.455 | 0.455 | `per_antibody` | The inferior/lateral loop-2 face of  |
| **C4** | 4 | 0.02 | 0.08 | 34 | 0.000 | 0.000 | 0.000 | `per_antibody` | A compact single-protomer conformati |
| **C2** | 5 | 0.01 | 0.04 | 30 | 0.000 | 0.000 | 0.000 | `per_antibody` | The crown of the dimeric capsid spik |
| **C7** | 6 | 0.008 | 0.03 | 32 | 0.000 | 0.000 | 0.000 | `per_antibody` | The broad top long-loop/dimer-rim fa |
| **C1** | 7 | 0.006 | 0.02 | 34 | 0.000 | 0.000 | 0.000 | `per_antibody` | A quaternary capsid-spike epitope th |
| **C6** | 8 | 0.006 | 0.015 | 26 | 0.000 | 0.000 | 0.000 | `per_antibody` | A PL-2-like composite attachment fac |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> Exact clone identification plus clone-specific K504E escape is the only Tier A localization and assigns 0.95 total probability to the K75 group. Within that group Tier A does not define a boundary: C5 gets a modest compactness/chemistry prior, while C3 and C8 are exact duplicate advocacy footprints and therefore split the broad-boundary mass equally. The remaining candidates are a low-probability allosteric or identity-failure tail supported only by other-antibody precedent.

## Which antibody binds which antigen residues

### C5 — confidence 0.42 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `single-chain`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 14 | 0.571 | 0.7357 | 0.99 | 41:0.67, 43:0.66, 45:0.72, 46:0.8, 72:0.59, 73:0.76, 74:0.4, 75:0.99, 76:0.9, 78:0.84, 82:0.7, 83:0.91, 85:0.78, 90:0.58 |
| F (unknown) | A | 14 | 0.571 | 0.7357 | 0.99 | 41:0.67, 43:0.66, 45:0.72, 46:0.8, 72:0.59, 73:0.76, 74:0.4, 75:0.99, 76:0.9, 78:0.84, 82:0.7, 83:0.91, 85:0.78, 90:0.58 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `single-chain`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | B | 14 | 0.571 | 0.7357 | 0.99 | 41:0.67, 43:0.66, 45:0.72, 46:0.8, 72:0.59, 73:0.76, 74:0.4, 75:0.99, 76:0.9, 78:0.84, 82:0.7, 83:0.91, 85:0.78, 90:0.58 |
| E (unknown) | B | 14 | 0.571 | 0.7357 | 0.99 | 41:0.67, 43:0.66, 45:0.72, 46:0.8, 72:0.59, 73:0.76, 74:0.4, 75:0.99, 76:0.9, 78:0.84, 82:0.7, 83:0.91, 85:0.78, 90:0.58 |

> Heavy supplies about two-thirds over 41–78; light L1/L3 covers 82–90. The 73–76 crest is shared by both halves.

### C3 — confidence 0.265 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `single-chain`, 22 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |
| F (unknown) | A | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `single-chain`, 22 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | B | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |
| E (unknown) | B | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |

> Heavy contributes about two-thirds: H3/H2 cover 41–46 and 72–80; light L1/L3 covers 82–90 and 212–216. Residues 73–76 sit at the shared centre.

### C8 — confidence 0.265 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `single-chain`, 22 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |
| F (unknown) | A | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `single-chain`, 22 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | B | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |
| E (unknown) | B | 22 | 0.455 | 0.6118 | 0.99 | 41:0.62, 42:0.52, 43:0.59, 45:0.67, 46:0.74, 72:0.64, 73:0.79, 74:0.43, 75:0.99, 76:0.9, 78:0.82, 80:0.31, 82:0.5, 83:0.73, 85:0.57, 88:0.43, 90:0.61, 212:0.28, 213:0.49, 214:0.68, 215:0.52, 216:0.63 |

> Heavy contributes about two-thirds over 41–80; light L1/L3 covers 82–90 and 212–216. Residues 73–76 lie at the shared centre.

### C4 — confidence 0.02 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `single-chain`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 17 | 0.000 | 0.5906 | 0.94 | 30:0.28, 31:0.2, 32:0.84, 33:0.72, 34:0.8, 35:0.92, 38:0.61, 81:0.3, 82:0.76, 83:0.94, 84:0.68, 86:0.46, 119:0.87, 120:0.12, 121:0.48, 148:0.71, 150:0.35 |
| F (unknown) | A | 17 | 0.000 | 0.5906 | 0.94 | 30:0.28, 31:0.2, 32:0.84, 33:0.72, 34:0.8, 35:0.92, 38:0.61, 81:0.3, 82:0.76, 83:0.94, 84:0.68, 86:0.46, 119:0.87, 120:0.12, 121:0.48, 148:0.71, 150:0.35 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `single-chain`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | B | 17 | 0.000 | 0.5906 | 0.94 | 30:0.28, 31:0.2, 32:0.84, 33:0.72, 34:0.8, 35:0.92, 38:0.61, 81:0.3, 82:0.76, 83:0.94, 84:0.68, 86:0.46, 119:0.87, 120:0.12, 121:0.48, 148:0.71, 150:0.35 |
| E (unknown) | B | 17 | 0.000 | 0.5906 | 0.94 | 30:0.28, 31:0.2, 32:0.84, 33:0.72, 34:0.8, 35:0.92, 38:0.61, 81:0.3, 82:0.76, 83:0.94, 84:0.68, 86:0.46, 119:0.87, 120:0.12, 121:0.48, 148:0.71, 150:0.35 |

> Heavy supplies about 65%: H1/H2/H3 cover loop 1 and beta5–beta6; light L1/L3 covers beta8/beta9. Residues 32/33/35 and 119 can be reached from both halves.

### C2 — confidence 0.01 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 9 | 0.000 | 0.6244 | 0.95 | 128:0.38, 130:0.56, 131:0.95, 132:0.5, 133:0.89, 134:0.33, 135:0.83, 136:0.48, 137:0.7 |
| C (unknown) | B | 6 | 0.000 | 0.5467 | 0.81 | 144:0.4, 145:0.64, 146:0.7, 147:0.81, 148:0.46, 185:0.27 |
| F (unknown) | A | 9 | 0.000 | 0.6244 | 0.95 | 128:0.38, 130:0.56, 131:0.95, 132:0.5, 133:0.89, 134:0.33, 135:0.83, 136:0.48, 137:0.7 |
| F (unknown) | B | 6 | 0.000 | 0.5467 | 0.81 | 144:0.4, 145:0.64, 146:0.7, 147:0.81, 148:0.46, 185:0.27 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | A | 6 | 0.000 | 0.5467 | 0.81 | 144:0.4, 145:0.64, 146:0.7, 147:0.81, 148:0.46, 185:0.27 |
| D (unknown) | B | 9 | 0.000 | 0.6244 | 0.95 | 128:0.38, 130:0.56, 131:0.95, 132:0.5, 133:0.89, 134:0.33, 135:0.83, 136:0.48, 137:0.7 |
| E (unknown) | A | 6 | 0.000 | 0.5467 | 0.81 | 144:0.4, 145:0.64, 146:0.7, 147:0.81, 148:0.46, 185:0.27 |
| E (unknown) | B | 9 | 0.000 | 0.6244 | 0.95 | 128:0.38, 130:0.56, 131:0.95, 132:0.5, 133:0.89, 134:0.33, 135:0.83, 136:0.48, 137:0.7 |

> Heavy supplies about 65–70% of the contact surface over 128–137; light L1/L3 covers partner 144–148 and the weak 185 rim. S131 and Y147 are assigned to both at the paratope seam.

### C7 — confidence 0.008 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 11 | 0.000 | 0.5673 | 0.95 | 128:0.36, 130:0.55, 131:0.95, 132:0.48, 133:0.9, 134:0.31, 135:0.84, 136:0.5, 137:0.71, 138:0.2, 139:0.44 |
| C (unknown) | B | 5 | 0.000 | 0.636 | 0.83 | 144:0.42, 145:0.66, 146:0.72, 147:0.83, 148:0.55 |
| F (unknown) | A | 11 | 0.000 | 0.5673 | 0.95 | 128:0.36, 130:0.55, 131:0.95, 132:0.48, 133:0.9, 134:0.31, 135:0.84, 136:0.5, 137:0.71, 138:0.2, 139:0.44 |
| F (unknown) | B | 5 | 0.000 | 0.636 | 0.83 | 144:0.42, 145:0.66, 146:0.72, 147:0.83, 148:0.55 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | A | 5 | 0.000 | 0.636 | 0.83 | 144:0.42, 145:0.66, 146:0.72, 147:0.83, 148:0.55 |
| D (unknown) | B | 11 | 0.000 | 0.5673 | 0.95 | 128:0.36, 130:0.55, 131:0.95, 132:0.48, 133:0.9, 134:0.31, 135:0.84, 136:0.5, 137:0.71, 138:0.2, 139:0.44 |
| E (unknown) | A | 5 | 0.000 | 0.636 | 0.83 | 144:0.42, 145:0.66, 146:0.72, 147:0.83, 148:0.55 |
| E (unknown) | B | 11 | 0.000 | 0.5673 | 0.95 | 128:0.36, 130:0.55, 131:0.95, 132:0.48, 133:0.9, 134:0.31, 135:0.84, 136:0.5, 137:0.71, 138:0.2, 139:0.44 |

> Heavy contributes about 70% over 128–139; light L1/L3 covers the partner 144–148 ledge. S131/Y147 form the shared central seam.

### C1 — confidence 0.006 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `straddling`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 15 | 0.000 | 0.6707 | 0.91 | 99:0.58, 100:0.78, 101:0.91, 102:0.86, 103:0.8, 135:0.73, 136:0.36, 137:0.68, 139:0.43, 168:0.88, 169:0.56, 170:0.74, 185:0.89, 186:0.47, 187:0.39 |
| C (unknown) | B | 2 | 0.000 | 0.52 | 0.62 | 17:0.42, 19:0.62 |
| F (unknown) | A | 15 | 0.000 | 0.6707 | 0.91 | 99:0.58, 100:0.78, 101:0.91, 102:0.86, 103:0.8, 135:0.73, 136:0.36, 137:0.68, 139:0.43, 168:0.88, 169:0.56, 170:0.74, 185:0.89, 186:0.47, 187:0.39 |
| F (unknown) | B | 2 | 0.000 | 0.52 | 0.62 | 17:0.42, 19:0.62 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `straddling`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | A | 2 | 0.000 | 0.52 | 0.62 | 17:0.42, 19:0.62 |
| D (unknown) | B | 15 | 0.000 | 0.6707 | 0.91 | 99:0.58, 100:0.78, 101:0.91, 102:0.86, 103:0.8, 135:0.73, 136:0.36, 137:0.68, 139:0.43, 168:0.88, 169:0.56, 170:0.74, 185:0.89, 186:0.47, 187:0.39 |
| E (unknown) | A | 2 | 0.000 | 0.52 | 0.62 | 17:0.42, 19:0.62 |
| E (unknown) | B | 15 | 0.000 | 0.6707 | 0.91 | 99:0.58, 100:0.78, 101:0.91, 102:0.86, 103:0.8, 135:0.73, 136:0.36, 137:0.68, 139:0.43, 168:0.88, 169:0.56, 170:0.74, 185:0.89, 186:0.47, 187:0.39 |

> Heavy contributes roughly two-thirds of the buried area: H3/H2 cover 99–103 and 168–187; light L1/L3 covers 135–139 and reaches the partner-chain 17/19 edge. Residues 100, 101 and 185 lie at the shared seam.

### C6 — confidence 0.006 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:unknown, F:unknown, binding mode `straddling`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (unknown) | A | 12 | 0.000 | 0.6542 | 0.94 | 32:0.84, 33:0.78, 34:0.75, 35:0.88, 82:0.82, 83:0.94, 100:0.66, 121:0.57, 123:0.8, 126:0.03, 146:0.64, 149:0.14 |
| C (unknown) | B | 1 | 0.000 | 0.72 | 0.72 | 135:0.72 |
| F (unknown) | A | 12 | 0.000 | 0.6542 | 0.94 | 32:0.84, 33:0.78, 34:0.75, 35:0.88, 82:0.82, 83:0.94, 100:0.66, 121:0.57, 123:0.8, 126:0.03, 146:0.64, 149:0.14 |
| F (unknown) | B | 1 | 0.000 | 0.72 | 0.72 | 135:0.72 |

**`antibody.2.pdb`** — chains D:unknown, E:unknown, binding mode `straddling`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (unknown) | A | 1 | 0.000 | 0.72 | 0.72 | 135:0.72 |
| D (unknown) | B | 12 | 0.000 | 0.6542 | 0.94 | 32:0.84, 33:0.78, 34:0.75, 35:0.88, 82:0.82, 83:0.94, 100:0.66, 121:0.57, 123:0.8, 126:0.03, 146:0.64, 149:0.14 |
| E (unknown) | A | 1 | 0.000 | 0.72 | 0.72 | 135:0.72 |
| E (unknown) | B | 12 | 0.000 | 0.6542 | 0.94 | 32:0.84, 33:0.78, 34:0.75, 35:0.88, 82:0.82, 83:0.94, 100:0.66, 121:0.57, 123:0.8, 126:0.03, 146:0.64, 149:0.14 |

> Heavy contributes roughly 70% across 32–123; light spans the distal 126/146/149 edge and reaches partner D135. Residue 32 is at the shared seam. All six CDRs would need to participate.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| judge | `case_a49017_GJ_rep2` | 5 | 0 | 2 |
| advocate C5 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C3 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C8 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C4 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C2 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C7 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C1 | `case_a49017_GR_rep1` | 1 | 0 | 6 |
| advocate C6 | `case_a49017_GR_rep1` | 1 | 0 | 6 |

