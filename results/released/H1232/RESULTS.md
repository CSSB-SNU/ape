# H1232 — gather batched answer

Case `case_d99ff5` · set `casp16` · retrieval cutoff **2024-06-13**

Antibody: `antibody.1.pdb` (C:mixed), `antibody.2.pdb` (D:mixed) · antigen chains A, B

Truth: **38 residues** over A, B (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C1** at confidence 0.62 — precision **0.800**, recall **0.632**, **F1 0.706** (24 of 30 predicted residues are in the 38-residue truth). The best pocket the answer contains is **C1**, precision **0.800**, F1 **0.706**, sitting at judge rank 1.

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
| **C1** | 1 | 0.62 | 0.72 | 30 | 0.800 | 0.632 | 0.706 | `per_antibody` | The apical loop-3 face of the protru |
| **C2** | 2 | 0.27 | 0.45 | 20 | 0.900 | 0.474 | 0.621 | `per_antibody` | A compact tertiary epitope on one sp |
| **C3** | 3 | 0.05 | 0.1 | 34 | 0.529 | 0.474 | 0.500 | `per_antibody` | A broad quaternary functional side f |
| **C5** | 4 | 0.03 | 0.07 | 36 | 0.500 | 0.474 | 0.486 | `per_antibody` | The canonical quaternary neutralizat |
| **C7** | 5 | 0.015 | 0.03 | 30 | 0.400 | 0.316 | 0.353 | `per_antibody` | The discrete PL-2-class quaternary e |
| **C4** | 6 | 0.008 | 0.02 | 24 | 0.000 | 0.000 | 0.000 | `per_antibody` | An exposed monomer-contained lateral |
| **C6** | 7 | 0.007 | 0.02 | 20 | 0.000 | 0.000 | 0.000 | `per_antibody` | A compact monomeric lateral face cen |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> A Tier A line exists: exact 4B6 escape localizes the binder to D136/N137, sharply favoring candidates that contain that vicinity. It does not distinguish C1/C2/C3/C5 by itself. Assembly-aware geometry did: C1 makes D136 central in a fully exposed, connected 20 A patch and follows the exposed partner-protomer surface that shapes D136; C2 is the credible single-protomer alternative; C3/C5 place the exact pair at the edge of a footprint slightly larger than this paratope's maximum CDR C-alpha span. PL-2 evidence was treated only as Tier B precedent, discounted by 82-87% side-chain identity over the candidate surfaces, P35 obstruction, and the fact that it concerns another antibody.

## Which antibody binds which antigen residues

### C1 — confidence 0.62 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 8 | 1.000 | 0.755 | 0.98 | 133:0.55, 134:0.43, 135:0.76, 136:0.98, 137:0.98, 138:0.88, 139:0.84, 140:0.62 |
| C (mixed) | B | 7 | 0.571 | 0.56 | 0.83 | 148:0.68, 149:0.83, 150:0.58, 152:0.34, 187:0.38, 188:0.5, 189:0.61 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | A | 7 | 0.571 | 0.56 | 0.83 | 148:0.68, 149:0.83, 150:0.58, 152:0.34, 187:0.38, 188:0.5, 189:0.61 |
| D (mixed) | B | 8 | 1.000 | 0.755 | 0.98 | 133:0.55, 134:0.43, 135:0.76, 136:0.98, 137:0.98, 138:0.88, 139:0.84, 140:0.62 |

> Heavy-dominant: H3/H2 cover 133-140; light CDRs cover the opposite-protomer rim. D136, N137 and M149 lie at the paratope center or boundary.

### C2 — confidence 0.27 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 10 | 0.900 | 0.67 | 0.99 | 133:0.58, 134:0.44, 135:0.77, 136:0.98, 137:0.99, 138:0.87, 139:0.83, 140:0.64, 141:0.24, 142:0.36 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | B | 10 | 0.900 | 0.67 | 0.99 | 133:0.58, 134:0.44, 135:0.77, 136:0.98, 137:0.99, 138:0.87, 139:0.83, 140:0.64, 141:0.24, 142:0.36 |

> H3/H2 cover 133-139; L3/L1 close over 140-142, with both chains converging on 135-137 and 140.

### C3 — confidence 0.05 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `straddling`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 13 | 0.385 | 0.7954 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 150:0.7, 153:0.49 |
| C (mixed) | B | 4 | 1.000 | 0.72 | 0.9 | 136:0.58, 137:0.76, 138:0.64, 139:0.9 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `straddling`, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | A | 4 | 1.000 | 0.72 | 0.9 | 136:0.58, 137:0.76, 138:0.64, 139:0.9 |
| D (mixed) | B | 13 | 0.385 | 0.7954 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 150:0.7, 153:0.49 |

> H1/H2/H3 cover 32-37, 85-86, 103 and 124/126; light CDRs reach 150/153 and opposite 136-139.

### C5 — confidence 0.03 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `straddling`, 18 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 14 | 0.357 | 0.7414 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 129:0.04, 150:0.7, 153:0.49 |
| C (mixed) | B | 4 | 1.000 | 0.72 | 0.9 | 136:0.58, 137:0.76, 138:0.64, 139:0.9 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `straddling`, 18 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | A | 4 | 1.000 | 0.72 | 0.9 | 136:0.58, 137:0.76, 138:0.64, 139:0.9 |
| D (mixed) | B | 14 | 0.357 | 0.7414 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 129:0.04, 150:0.7, 153:0.49 |

> Heavy dominates the main protomer; light covers 129/150/153 and neighboring 136-139.

### C7 — confidence 0.015 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 14 | 0.357 | 0.7414 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 129:0.04, 150:0.7, 153:0.49 |
| C (mixed) | B | 1 | 1.000 | 0.9 | 0.9 | 139:0.9 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `straddling`, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | A | 1 | 1.000 | 0.9 | 0.9 | 139:0.9 |
| D (mixed) | B | 14 | 0.357 | 0.7414 | 0.97 | 32:0.95, 33:0.97, 34:0.48, 35:0.74, 36:0.61, 37:0.76, 85:0.96, 86:0.96, 103:0.83, 124:0.96, 126:0.93, 129:0.04, 150:0.7, 153:0.49 |

> Heavy CDRs dominate the main face; light covers 129/150/153 and opposite D139; both meet at G32.

### C4 — confidence 0.008 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `single-chain`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 12 | 0.000 | 0.6825 | 0.91 | 72:0.82, 73:0.91, 75:0.87, 76:0.73, 78:0.78, 79:0.66, 88:0.72, 89:0.52, 91:0.42, 93:0.59, 116:0.48, 118:0.69 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `single-chain`, 12 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | B | 12 | 0.000 | 0.6825 | 0.91 | 72:0.82, 73:0.91, 75:0.87, 76:0.73, 78:0.78, 79:0.66, 88:0.72, 89:0.52, 91:0.42, 93:0.59, 116:0.48, 118:0.69 |

> Heavy covers 72-79; light extends across 88-93 to 116/118; both converge on 73/75/78/79.

### C6 — confidence 0.007 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains C:mixed, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| C (mixed) | A | 10 | 0.000 | 0.713 | 0.94 | 62:0.33, 67:0.72, 69:0.77, 70:0.69, 72:0.92, 73:0.94, 75:0.88, 76:0.74, 78:0.65, 79:0.49 |

**`antibody.2.pdb`** — chains D:mixed, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| D (mixed) | B | 10 | 0.000 | 0.713 | 0.94 | 62:0.33, 67:0.72, 69:0.77, 70:0.69, 72:0.92, 73:0.94, 75:0.88, 76:0.74, 78:0.65, 79:0.49 |

> Heavy covers E62 and 67-70; both converge on 72/73/75; light finishes 76-79.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| judge | `case_d99ff5_GJ_rep2` | 1 | 1 | 0 |
| advocate C1 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C2 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C3 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C5 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C7 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C4 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |
| advocate C6 | `case_d99ff5_GR_rep1` | 1 | 0 | 6 |

