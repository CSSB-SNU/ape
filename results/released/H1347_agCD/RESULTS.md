# H1347_agCD — gather batched answer

Case `case_0f54aa` · set `casp17` · retrieval cutoff **2026-05-21**

Antibody: `antibody.1.pdb` (A:heavy), `antibody.2.pdb` (B:light) · antigen chains C, D

Truth: **22 residues** over C, D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C2** at confidence 0.23 — precision **0.000**, recall **0.000**, **F1 0.000** (0 of 10 predicted residues are in the 22-residue truth). The best pocket the answer contains is **C2**, precision **0.000**, F1 **0.000**, sitting at judge rank 1.

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
| **C2** | 1 | 0.23 | 0.36 | 10 | 0.000 | 0.000 | 0.000 | `per_antibody` | The functional BCMA-contacting parat |
| **C1** | 2 | 0.17 | 0.3 | 12 | 0.000 | 0.000 | 0.000 | `per_antibody` | The clone-specific antigen-combining |
| **C4** | 3 | 0.15 | 0.25 | 11 | 0.000 | 0.000 | 0.000 | `per_antibody` | The complete C-chain variable-domain |
| **C3** | 4 | 0.13 | 0.23 | 9 | 0.000 | 0.000 | 0.000 | `per_antibody` | A compact VH functional idiotope cen |
| **C7** | 5 | 0.12 | 0.2 | 20 | 0.000 | 0.000 | 0.000 | `per_antibody` | Two chain-restricted portions of one |
| **C6** | 6 | 0.08 | 0.16 | 9 | 0.000 | 0.000 | 0.000 | `per_antibody` | The antigen antibody’s VL cap, cente |
| **C5** | 7 | 0.07 | 0.14 | 17 | 0.000 | 0.000 | 0.000 | `per_antibody` | An oblique variable-domain idiotope  |
| **C8** | 8 | 0.05 | 0.1 | 14 | 0.000 | 0.000 | 0.000 | `per_antibody` | The Fab variable/constant elbow and  |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate has Tier A evidence about supplied binder A or B; the result is therefore a broad prior over surfaces, not a localized call. Exact pre-cutoff sequence evidence establishes that antigen C/D are a native BCMB69 Fab pair, so their anomalous supplied separation discounts but cannot exclude C1/C2. The BCMB69-specific anti-idiotype statement and exact native functional map weakly favor the variable apex, with C2's precise functional panel ahead of C1's broader boundary. Within compact alternatives, native heavy-chain dominance weakly favors C4/C3 over C6; C7 gains plausibility from giving two binders two coverable sites but loses it on an arbitrary direction. Accessibility did not separate the compact candidates, and coarse chemistry was too non-specific to score.

## Which antibody binds which antigen residues

### C2 — confidence 0.23 (judge rank 1)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `straddling`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 5 | 0.000 | 0.84 | 0.9 | 34:0.75, 101:0.78, 103:0.88, 104:0.9, 110:0.89 |
| A (heavy) | D | 4 | 0.000 | 0.7975 | 0.91 | 48:0.68, 55:0.74, 90:0.91, 95:0.86 |

**`antibody.2.pdb`** — chains B:light, binding mode `straddling`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | C | 4 | 0.000 | 0.8225 | 0.9 | 34:0.7, 103:0.83, 104:0.86, 110:0.9 |
| B (light) | D | 5 | 0.000 | 0.836 | 0.93 | 48:0.78, 52:0.72, 55:0.85, 90:0.93, 95:0.9 |

> Both independent one-chain binders are modeled as straddling the biological functional paratope. A emphasizes VH H3; B gives more weight to VL L2/L3.

### C1 — confidence 0.17 (judge rank 2)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `straddling`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 6 | 0.000 | 0.8517 | 0.91 | 101:0.72, 103:0.86, 104:0.88, 107:0.9, 109:0.84, 110:0.91 |
| A (heavy) | D | 4 | 0.000 | 0.815 | 0.88 | 90:0.88, 95:0.84, 96:0.78, 97:0.76 |

**`antibody.2.pdb`** — chains B:light, binding mode `straddling`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | C | 5 | 0.000 | 0.8 | 0.87 | 34:0.66, 103:0.8, 104:0.84, 107:0.83, 110:0.87 |
| B (light) | D | 4 | 0.000 | 0.8225 | 0.88 | 90:0.86, 93:0.76, 95:0.88, 97:0.79 |

> The files are separate one-chain binders: antibody.1 contributes heavy-side contacts and antibody.2 light-side contacts. Their biological-Fv footprints overlap centrally, but the supplied C/D union is not coverable.

### C4 — confidence 0.15 (judge rank 3)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 11 | 0.000 | 0.7945 | 0.94 | 34:0.72, 55:0.68, 56:0.62, 101:0.72, 103:0.86, 104:0.88, 107:0.91, 108:0.83, 109:0.84, 110:0.94, 111:0.74 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 11 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | C | 11 | 0.000 | 0.7682 | 0.92 | 34:0.75, 55:0.6, 56:0.66, 101:0.65, 103:0.82, 104:0.85, 107:0.88, 108:0.82, 109:0.78, 110:0.92, 111:0.72 |

> Both binders occupy antigen chain C. Their highly overlapping 21.19 Å footprints are reachable by both measured one-chain paratopes.

### C3 — confidence 0.13 (judge rank 4)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 9 | 0.000 | 0.8133 | 0.94 | 99:0.55, 101:0.72, 103:0.86, 104:0.88, 107:0.92, 108:0.86, 109:0.84, 110:0.94, 111:0.75 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | C | 9 | 0.000 | 0.79 | 0.92 | 99:0.62, 101:0.68, 103:0.82, 104:0.85, 107:0.88, 108:0.84, 109:0.8, 110:0.92, 111:0.7 |

> Both files bind antigen chain C. A contributes heavy-side and B light-side contacts; central overlap is `both`. The footprint is smaller than either one-chain paratope.

### C7 — confidence 0.12 (judge rank 5)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 10 | 0.000 | 0.798 | 0.95 | 32:0.55, 34:0.7, 55:0.52, 101:0.8, 103:0.9, 104:0.92, 107:0.94, 108:0.86, 109:0.84, 110:0.95 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 10 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | D | 10 | 0.000 | 0.779 | 0.92 | 29:0.48, 31:0.6, 48:0.85, 49:0.75, 90:0.92, 92:0.78, 93:0.8, 95:0.91, 96:0.86, 97:0.84 |

> A contributes only heavy-side contacts on antigen C; B contributes only light-side contacts on antigen D. No union residue is `both`, and neither footprint bridges the anomalous C/D separation.

### C6 — confidence 0.08 (judge rank 6)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | D | 9 | 0.000 | 0.7844 | 0.88 | 48:0.72, 49:0.78, 90:0.88, 92:0.64, 93:0.76, 95:0.84, 96:0.88, 97:0.82, 99:0.74 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | D | 9 | 0.000 | 0.8311 | 0.92 | 48:0.82, 49:0.76, 90:0.92, 92:0.78, 93:0.82, 95:0.9, 96:0.84, 97:0.88, 99:0.76 |

> Both footprints occupy antigen chain D. A supplies heavy-side and B light-side contacts; their overlap is `both`. D:111 was dropped as a distant passenger.

### C5 — confidence 0.07 (judge rank 7)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 8 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 8 | 0.000 | 0.6963 | 0.86 | 30:0.62, 31:0.68, 33:0.72, 34:0.83, 55:0.86, 56:0.78, 57:0.5, 59:0.58 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 9 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | D | 9 | 0.000 | 0.7589 | 0.9 | 30:0.58, 31:0.65, 35:0.72, 48:0.9, 49:0.84, 51:0.76, 52:0.81, 53:0.85, 55:0.72 |

> The pooled location is resolved into two independent single-chain footprints: A on C H1/H2 and B on D L1/L2. They do not overlap.

### C8 — confidence 0.05 (judge rank 8)

Mapping basis: `per_antibody`  — the advocate answered each antibody file separately.

**`antibody.1.pdb`** — chains A:heavy, binding mode `single-chain`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 7 | 0.000 | 0.6657 | 0.8 | 13:0.55, 15:0.56, 16:0.6, 121:0.75, 123:0.8, 124:0.68, 125:0.72 |

**`antibody.2.pdb`** — chains B:light, binding mode `single-chain`, 7 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (light) | D | 7 | 0.000 | 0.8 | 0.92 | 120:0.72, 123:0.74, 125:0.9, 126:0.68, 128:0.92, 130:0.8, 131:0.84 |

> A is assigned to a C-chain VH/CH1 junction patch and B to a D-chain VL/CL junction patch. Both are coverable single-chain modes and do not overlap.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| judge | `case_0f54aa_GJ_rep2` | 0 | 0 | 0 |
| advocate C2 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C1 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C4 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C3 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C7 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C6 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C5 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |
| advocate C8 | `case_0f54aa_GR_rep1` | 1 | 0 | 0 |

