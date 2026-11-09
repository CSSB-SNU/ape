# H1204 — gather batched answer

Case `case_2c69fc` · set `casp16` · retrieval cutoff **2024-05-02**

Antibody: `antibody.1.pdb` (A:heavy), `antibody.2.pdb` (B:heavy) · antigen chains C, D, E, F

Truth: **44 residues** over C, D, E, F (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C9** at confidence 0.2 — precision **0.000**, recall **0.000**, **F1 0.000** (0 of 22 predicted residues are in the 44-residue truth). The best pocket the answer contains is **C1**, precision **0.571**, F1 **0.444**, sitting at judge rank 9.

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
| **C9** | 1 | 0.2 | 0.32 | 22 | 0.000 | 0.000 | 0.000 | `per_antibody` | The exposed beta-globin N-terminal p |
| **C3** | 2 | 0.14 | 0.25 | 30 | 0.000 | 0.000 | 0.000 | `per_antibody` | A duplicated beta-globin exterior fa |
| **C4** | 3 | 0.12 | 0.22 | 26 | 0.538 | 0.318 | 0.400 | `per_antibody` | The beta-subunit A/H outer face, whe |
| **C6** | 4 | 0.11 | 0.2 | 32 | 0.000 | 0.000 | 0.000 | `per_antibody` | A broad exterior alpha-globin face f |
| **C10** | 5 | 0.1 | 0.18 | 24 | 0.333 | 0.182 | 0.235 | `per_antibody` | The alpha-globin A/GH outer face, wh |
| **C2** | 6 | 0.09 | 0.17 | 30 | 0.000 | 0.000 | 0.000 | `per_antibody` | A pair of outer clefts at the alpha1 |
| **C7** | 7 | 0.08 | 0.16 | 30 | 0.000 | 0.000 | 0.000 | `per_antibody` | The solvent-facing alpha-globin CD c |
| **C5** | 8 | 0.07 | 0.13 | 18 | 0.111 | 0.045 | 0.065 | `per_antibody` | A compact Lys/His-rich outer face of |
| **C1** | 9 | 0.05 | 0.11 | 28 | 0.571 | 0.364 | 0.444 | `per_antibody` | The solvent-facing rim of the alpha1 |
| **C8** | 10 | 0.04 | 0.08 | 32 | 0.000 | 0.000 | 0.000 | `per_antibody` | The exposed rim of each alpha1-beta2 |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate had Tier A evidence about this binder, so the result remains a broad surface prior. Common measurements removed coverability as a discriminator because all ten fit the 26.42 A CDR field. Assembly burial penalized C8/C1/C2, gross charge penalized C5, and compact exposure plus independent exact-surface antibody precedent modestly favored C9.

## Which antibody binds which antigen residues

### C9 — confidence 0.2 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 11 | 0.000 | 0.75 | 0.99 | 2:0.26, 3:0.73, 5:0.74, 6:0.89, 7:0.99, 8:0.92, 9:0.91, 10:0.87, 11:0.63, 13:0.75, 14:0.56 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 11 | 0.000 | 0.75 | 0.99 | 2:0.26, 3:0.73, 5:0.74, 6:0.89, 7:0.99, 8:0.92, 9:0.91, 10:0.87, 11:0.63, 13:0.75, 14:0.56 |

> Heavy-only VHHs; H3 centres on beta7-9 and H1/H2 flank the peptide.

### C3 — confidence 0.14 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 15 | 0.000 | 0.7213 | 0.94 | 3:0.76, 5:0.62, 6:0.84, 7:0.94, 8:0.56, 9:0.75, 10:0.83, 11:0.63, 13:0.81, 14:0.66, 73:0.3, 74:0.89, 77:0.81, 78:0.85, 80:0.57 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 15 | 0.000 | 0.7213 | 0.94 | 3:0.76, 5:0.62, 6:0.84, 7:0.94, 8:0.56, 9:0.75, 10:0.83, 11:0.63, 13:0.81, 14:0.66, 73:0.3, 74:0.89, 77:0.81, 78:0.85, 80:0.57 |

> Heavy-only VHHs; H3 bridges the acidic lobes and H1/H2 support the hydrophobic shoulders.

### C4 — confidence 0.12 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 13 | 0.538 | 0.6023 | 0.94 | 10:0.57, 11:0.49, 13:0.68, 14:0.83, 17:0.8, 18:0.94, 20:0.13, 118:0.41, 119:0.86, 121:0.32, 122:0.93, 124:0.59, 126:0.28 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 13 | 0.538 | 0.6023 | 0.94 | 10:0.57, 11:0.49, 13:0.68, 14:0.83, 17:0.8, 18:0.94, 20:0.13, 118:0.41, 119:0.86, 121:0.32, 122:0.93, 124:0.59, 126:0.28 |

> Heavy-only VHHs; H3 centres on beta18/119/122 and H1/H2 cover the two helix rims.

### C6 — confidence 0.11 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | E | 16 | 0.000 | 0.6844 | 0.95 | 12:0.43, 13:0.63, 15:0.79, 16:0.66, 17:0.56, 19:0.7, 20:0.89, 21:0.83, 23:0.31, 61:0.53, 65:0.95, 68:0.92, 69:0.72, 72:0.82, 73:0.85, 80:0.36 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | F | 16 | 0.000 | 0.6844 | 0.95 | 12:0.43, 13:0.63, 15:0.79, 16:0.66, 17:0.56, 19:0.7, 20:0.89, 21:0.83, 23:0.31, 61:0.53, 65:0.95, 68:0.92, 69:0.72, 72:0.82, 73:0.85, 80:0.36 |

> Heavy-only VHHs; H3 centres on alpha65/68 and H1/H2 cover the A- and E-helix lobes.

### C10 — confidence 0.1 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | E | 12 | 0.333 | 0.6083 | 0.96 | 10:0.19, 13:0.73, 16:0.77, 17:0.95, 19:0.43, 21:0.31, 113:0.31, 114:0.46, 115:0.72, 116:0.88, 117:0.96, 119:0.59 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | F | 12 | 0.333 | 0.6083 | 0.96 | 10:0.19, 13:0.73, 16:0.77, 17:0.95, 19:0.43, 21:0.31, 113:0.31, 114:0.46, 115:0.72, 116:0.88, 117:0.96, 119:0.59 |

> Heavy-only VHHs; H3 bridges alpha17/117 and H1/H2 pack the small-residue core.

### C2 — confidence 0.09 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 3 | 0.000 | 0.58 | 0.76 | 95:0.28, 98:0.7, 147:0.76 |
| A (heavy) | F | 12 | 0.000 | 0.7342 | 0.95 | 41:0.73, 44:0.48, 45:0.75, 46:0.83, 47:0.82, 48:0.93, 49:0.95, 50:0.9, 51:0.65, 52:0.52, 54:0.45, 55:0.8 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 3 | 0.000 | 0.58 | 0.76 | 95:0.28, 98:0.7, 147:0.76 |
| B (heavy) | E | 12 | 0.000 | 0.7342 | 0.95 | 41:0.73, 44:0.48, 45:0.75, 46:0.83, 47:0.82, 48:0.93, 49:0.95, 50:0.9, 51:0.65, 52:0.52, 54:0.45, 55:0.8 |

> Heavy only; H3 crosses the junction while H1/H2 support the two walls.

### C7 — confidence 0.08 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | E | 15 | 0.000 | 0.738 | 0.91 | 44:0.49, 45:0.63, 46:0.83, 47:0.79, 48:0.91, 49:0.76, 50:0.81, 51:0.89, 52:0.59, 54:0.64, 55:0.83, 57:0.87, 58:0.51, 61:0.8, 62:0.72 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | F | 15 | 0.000 | 0.738 | 0.91 | 44:0.49, 45:0.63, 46:0.83, 47:0.79, 48:0.91, 49:0.76, 50:0.81, 51:0.89, 52:0.59, 54:0.64, 55:0.83, 57:0.87, 58:0.51, 61:0.8, 62:0.72 |

> Heavy-only VHHs; H3 follows the mixed charged core, with H1/H2 on its aromatic and basic edges.

### C5 — confidence 0.07 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 9 | 0.111 | 0.7911 | 0.94 | 57:0.51, 59:0.78, 60:0.89, 62:0.92, 63:0.61, 64:0.85, 66:0.89, 67:0.94, 68:0.73 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 9 | 0.111 | 0.7911 | 0.94 | 57:0.51, 59:0.78, 60:0.89, 62:0.92, 63:0.61, 64:0.85, 66:0.89, 67:0.94, 68:0.73 |

> Heavy-only VHHs; H3 crosses the basic face and H1/H2 provide aromatic shoulders.

### C1 — confidence 0.05 (judge rank 9)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 5 | 0.800 | 0.588 | 0.88 | 117:0.22, 118:0.7, 121:0.88, 122:0.78, 124:0.36 |
| A (heavy) | E | 9 | 0.444 | 0.6456 | 0.94 | 17:0.43, 19:0.36, 21:0.67, 24:0.8, 113:0.55, 115:0.72, 116:0.89, 117:0.94, 119:0.45 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `straddling`, 14 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 5 | 0.800 | 0.588 | 0.88 | 117:0.22, 118:0.7, 121:0.88, 122:0.78, 124:0.36 |
| B (heavy) | F | 9 | 0.444 | 0.6456 | 0.94 | 17:0.43, 19:0.36, 21:0.67, 24:0.8, 113:0.55, 115:0.72, 116:0.89, 117:0.94, 119:0.45 |

> Heavy only: each file is a one-chain VHH. H3 should dominate the centre, with unequal H1/H2 flanks.

### C8 — confidence 0.04 (judge rank 10)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 11 | 0.000 | 0.6209 | 0.9 | 91:0.66, 92:0.46, 95:0.9, 96:0.74, 97:0.55, 98:0.43, 143:0.41, 144:0.79, 145:0.71, 146:0.36, 147:0.82 |
| A (heavy) | F | 5 | 0.000 | 0.496 | 0.76 | 37:0.41, 38:0.51, 39:0.31, 41:0.76, 45:0.49 |

**`antibody.2.pdb`** — chains B:heavy, binding mode `straddling`, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | D | 11 | 0.000 | 0.6209 | 0.9 | 91:0.66, 92:0.46, 95:0.9, 96:0.74, 97:0.55, 98:0.43, 143:0.41, 144:0.79, 145:0.71, 146:0.36, 147:0.82 |
| B (heavy) | E | 5 | 0.000 | 0.496 | 0.76 | 37:0.41, 38:0.51, 39:0.31, 41:0.76, 45:0.49 |

> Heavy-only VHHs; H3 crosses the junction and H1/H2 support its beta and alpha rims.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| judge | `case_2c69fc_GJ_rep2` | 2 | 1 | 2 |
| advocate C9 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C3 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C4 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C6 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C10 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C2 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C7 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C5 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C1 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |
| advocate C8 | `case_2c69fc_GR_rep1` | 3 | 0 | 13 |

