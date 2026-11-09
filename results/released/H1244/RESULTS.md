# H1244 — gather batched answer

Case `case_4a7bba` · set `casp16` · retrieval cutoff **2024-06-23**

Antibody: `antibody.1.pdb` (E:heavy), `antibody.2.pdb` (F:heavy) · antigen chains A, B, C, D

Truth: **38 residues** over A, B, C, D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C7** at confidence 0.27 — precision **0.364**, recall **0.210**, **F1 0.267** (8 of 22 predicted residues are in the 38-residue truth). The best pocket the answer contains is **C2**, precision **0.462**, F1 **0.375**, sitting at judge rank 6.

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
| **C7** | 1 | 0.27 | 0.45 | 22 | 0.364 | 0.210 | 0.267 | `per_antibody` | A continuous single-chain aromatic/b |
| **C1** | 2 | 0.19 | 0.38 | 22 | 0.000 | 0.000 | 0.000 | `per_antibody` | The exposed exit and terminal tail o |
| **C4** | 3 | 0.13 | 0.26 | 24 | 0.250 | 0.158 | 0.194 | `per_antibody` | The assembly-exposed aromatic/basic  |
| **C3** | 4 | 0.11 | 0.3 | 26 | 0.000 | 0.000 | 0.000 | `per_antibody` | The exposed charged C/D helical face |
| **C9** | 5 | 0.1 | 0.2 | 24 | 0.250 | 0.158 | 0.194 | `per_antibody` | A three-chain W87 junction: the A/B  |
| **C2** | 6 | 0.07 | 0.18 | 26 | 0.462 | 0.316 | 0.375 | `per_antibody` | A compact two-chain flank on the ant |
| **C6** | 7 | 0.055 | 0.15 | 32 | 0.062 | 0.053 | 0.057 | `per_antibody` | The mid-shaft A/C or B/D groove cent |
| **C5** | 8 | 0.045 | 0.12 | 28 | 0.000 | 0.000 | 0.000 | `per_antibody` | A distal two-chain charged groove on |
| **C8** | 9 | 0.03 | 0.08 | 24 | 0.000 | 0.000 | 0.000 | `per_antibody` | The charged cap where the resolved A |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate had Tier A evidence about this exact VHH. All passed assembly-exposure and reach filters. The broad order was separated by denaturing-blot continuity, coarse paratope-patch chemistry, required chain count, and C8's missing-segment gap.

## Which antibody binds which antigen residues

### C7 — confidence 0.27 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 11 | 0.364 | 0.6873 | 0.96 | 84:0.34, 86:0.76, 87:0.96, 90:0.48, 91:0.74, 93:0.85, 94:0.93, 95:0.46, 97:0.68, 98:0.6, 100:0.76 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 11 | 0.364 | 0.6873 | 0.96 | 84:0.34, 86:0.76, 87:0.96, 90:0.48, 91:0.74, 93:0.85, 94:0.93, 95:0.46, 97:0.68, 98:0.6, 100:0.76 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C1 — confidence 0.19 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | C | 11 | 0.000 | 0.6673 | 0.94 | 118:0.46, 119:0.58, 121:0.62, 122:0.48, 123:0.55, 124:0.78, 125:0.72, 126:0.94, 127:0.84, 128:0.92, 129:0.45 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | D | 11 | 0.000 | 0.6673 | 0.94 | 118:0.46, 119:0.58, 121:0.62, 122:0.48, 123:0.55, 124:0.78, 125:0.72, 126:0.94, 127:0.84, 128:0.92, 129:0.45 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C4 — confidence 0.13 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 7 | 0.429 | 0.7386 | 0.95 | 86:0.72, 87:0.95, 90:0.5, 91:0.78, 93:0.84, 94:0.91, 95:0.47 |
| E (heavy) | D | 5 | 0.000 | 0.786 | 0.94 | 124:0.74, 125:0.65, 126:0.94, 127:0.78, 128:0.82 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 7 | 0.429 | 0.7386 | 0.95 | 86:0.72, 87:0.95, 90:0.5, 91:0.78, 93:0.84, 94:0.91, 95:0.47 |
| F (heavy) | C | 5 | 0.000 | 0.786 | 0.94 | 124:0.74, 125:0.65, 126:0.94, 127:0.78, 128:0.82 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C3 — confidence 0.11 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | C | 13 | 0.000 | 0.6123 | 0.88 | 90:0.68, 93:0.78, 94:0.56, 95:0.39, 96:0.48, 97:0.49, 99:0.58, 100:0.88, 101:0.7, 102:0.38, 103:0.78, 104:0.84, 106:0.42 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | D | 13 | 0.000 | 0.6123 | 0.88 | 90:0.68, 93:0.78, 94:0.56, 95:0.39, 96:0.48, 97:0.49, 99:0.58, 100:0.88, 101:0.7, 102:0.38, 103:0.78, 104:0.84, 106:0.42 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C9 — confidence 0.1 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 8 | 0.375 | 0.7 | 0.95 | 84:0.44, 86:0.72, 87:0.95, 90:0.53, 91:0.78, 93:0.84, 94:0.9, 95:0.44 |
| E (heavy) | C | 2 | 0.000 | 0.49 | 0.5 | 70:0.48, 71:0.5 |
| E (heavy) | D | 2 | 0.000 | 0.845 | 0.94 | 124:0.75, 126:0.94 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 8 | 0.375 | 0.7 | 0.95 | 84:0.44, 86:0.72, 87:0.95, 90:0.53, 91:0.78, 93:0.84, 94:0.9, 95:0.44 |
| F (heavy) | C | 2 | 0.000 | 0.845 | 0.94 | 124:0.75, 126:0.94 |
| F (heavy) | D | 2 | 0.000 | 0.49 | 0.5 | 70:0.48, 71:0.5 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C2 — confidence 0.07 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 9 | 0.444 | 0.6567 | 0.9 | 94:0.48, 97:0.61, 98:0.55, 100:0.82, 101:0.7, 104:0.9, 105:0.73, 107:0.66, 108:0.46 |
| E (heavy) | C | 4 | 0.500 | 0.64 | 0.79 | 52:0.62, 55:0.55, 57:0.6, 61:0.79 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 9 | 0.444 | 0.6567 | 0.9 | 94:0.48, 97:0.61, 98:0.55, 100:0.82, 101:0.7, 104:0.9, 105:0.73, 107:0.66, 108:0.46 |
| F (heavy) | D | 4 | 0.500 | 0.64 | 0.79 | 52:0.62, 55:0.55, 57:0.6, 61:0.79 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C6 — confidence 0.055 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 8 | 0.125 | 0.6625 | 0.87 | 109:0.42, 112:0.61, 114:0.74, 115:0.87, 118:0.58, 119:0.68, 121:0.74, 123:0.66 |
| E (heavy) | C | 8 | 0.000 | 0.665 | 0.87 | 38:0.69, 40:0.83, 42:0.43, 43:0.66, 44:0.87, 45:0.58, 47:0.65, 50:0.61 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 8 | 0.125 | 0.6625 | 0.87 | 109:0.42, 112:0.61, 114:0.74, 115:0.87, 118:0.58, 119:0.68, 121:0.74, 123:0.66 |
| F (heavy) | D | 8 | 0.000 | 0.665 | 0.87 | 38:0.69, 40:0.83, 42:0.43, 43:0.66, 44:0.87, 45:0.58, 47:0.65, 50:0.61 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C5 — confidence 0.045 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 7 | 0.000 | 0.6143 | 0.88 | 139:0.64, 140:0.53, 142:0.38, 143:0.51, 144:0.7, 146:0.88, 147:0.66 |
| E (heavy) | C | 7 | 0.000 | 0.61 | 0.85 | 12:0.6, 13:0.48, 15:0.49, 16:0.85, 17:0.45, 19:0.72, 20:0.68 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 7 | 0.000 | 0.6143 | 0.88 | 139:0.64, 140:0.53, 142:0.38, 143:0.51, 144:0.7, 146:0.88, 147:0.66 |
| F (heavy) | D | 7 | 0.000 | 0.61 | 0.85 | 12:0.6, 13:0.48, 15:0.49, 16:0.85, 17:0.45, 19:0.72, 20:0.68 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

### C8 — confidence 0.03 (judge rank 9)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains E:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| E (heavy) | A | 7 | 0.000 | 0.6557 | 0.84 | 150:0.82, 151:0.63, 152:0.46, 153:0.66, 154:0.62, 155:0.56, 156:0.84 |
| E (heavy) | C | 5 | 0.000 | 0.632 | 0.86 | 4:0.48, 5:0.86, 6:0.68, 8:0.64, 10:0.5 |

**`antibody.2.pdb`** — chains F:heavy, binding mode `straddling`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| F (heavy) | B | 7 | 0.000 | 0.6557 | 0.84 | 150:0.82, 151:0.63, 152:0.46, 153:0.66, 154:0.62, 155:0.56, 156:0.84 |
| F (heavy) | D | 5 | 0.000 | 0.632 | 0.86 | 4:0.48, 5:0.86, 6:0.68, 8:0.64, 10:0.5 |

> Heavy-only VHH: H3 center and H1/H2 rims; no light chain.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| judge | `case_4a7bba_GJ_rep2` | 4 | 0 | 1 |
| advocate C7 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C1 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C4 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C3 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C9 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C2 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C6 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C5 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |
| advocate C8 | `case_4a7bba_GR_rep1` | 1 | 0 | 7 |

