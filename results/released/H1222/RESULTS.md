# H1222 — gather batched answer

Case `case_2e3a2a` · set `casp16` · retrieval cutoff **2024-06-04**

Antibody: `antibody.pdb` (B:heavy, C:light) · antigen chains A

Truth: **22 residues** over A (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C1** at confidence 0.44 — precision **0.667**, recall **0.545**, **F1 0.600** (12 of 18 predicted residues are in the 22-residue truth). The best pocket the answer contains is **C2**, precision **0.947**, F1 **0.878**, sitting at judge rank 3.

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
| **C1** | 1 | 0.44 | 0.6 | 18 | 0.667 | 0.545 | 0.600 | `side` | The disulfide-stabilized receptor-bi |
| **C3** | 2 | 0.31 | 0.5 | 15 | 0.933 | 0.636 | 0.757 | `side` | The conserved hydrophobic-aromatic N |
| **C2** | 3 | 0.25 | 0.42 | 19 | 0.947 | 0.818 | 0.878 | `side` | A conserved conformational face that |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate had a line about this binder: every published epitope was for another antibody. What remained was a broad Tier B prior over three neighboring RSV G surfaces. Independent calculations on the supplied separate structures provided the modest separation: C1 was most compact and had the only favorable coarse charge complementarity; C3 was more coverable than C2; C2's close 3G12 precedent was discounted because it is conformation-sensitive and binder-specific only to 3G12. Accessibility alone was nearly identical and was not used to rank them.

## Which antibody binds which antigen residues

### C1 — confidence 0.44 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 18 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 14 | 0.643 | 0.6536 | 0.94 | 19:0.76, 22:0.84, 23:0.62, 24:0.81, 25:0.78, 26:0.13, 27:0.94, 28:0.88, 29:0.91, 30:0.14, 31:0.8, 32:0.77, 33:0.31, 34:0.46 |
| C (light) | A | 11 | 0.818 | 0.5809 | 0.88 | 17:0.1, 18:0.68, 19:0.76, 20:0.07, 21:0.72, 22:0.84, 23:0.62, 24:0.81, 25:0.78, 26:0.13, 28:0.88 |

> Heavy-biased, about 65:35 in contact contribution. H2/H3 cover A:27-A:29 and the A:31/A:32 rim; L1/L3 cover the polar A:18-A:23 shoulder, with both chains converging over A:22-A:28.

Pooled from 7 phase-1 patches, which drew different residues — 0 shared and 35 disputed at pooling. What the advocate then kept of each:

- `P1` (18 res) — 18 kept, 0 dropped · Cystine-noose/CX3C face (antigenic site gamma1/gamma
- `P3` (24 res) — 8 kept, 16 dropped · Folded N/C-flank face outside the noose (CB017.5-lik
- `P4` (12 res) — 3 kept, 9 dropped · Compact HFEVFNFVP/N-noose junction
- `P5` (20 res) — 4 kept, 16 dropped · Discontinuous conserved N flank plus basic C-termina
- `P6` (20 res) — 4 kept, 16 dropped · N/C flank bridge
- `P7` (15 res) — 15 kept, 0 dropped · γ2 cysteine-noose/CX3C face
- `P8` (16 res) — 16 kept, 0 dropped · Compact cystine-noose/CX3C face

### C3 — confidence 0.31 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 15 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 13 | 0.923 | 0.6285 | 0.93 | 9:0.93, 10:0.76, 11:0.91, 12:0.86, 13:0.81, 14:0.62, 15:0.57, 16:0.42, 17:0.11, 18:0.72, 19:0.85, 20:0.07, 21:0.54 |
| C (light) | A | 4 | 1.000 | 0.7925 | 0.93 | 7:0.77, 8:0.71, 9:0.93, 10:0.76 |

> Heavy-dominant, about 72:28. L1/L3 cap A:7-A:10, both chains share A:9/A:10, and H1/H2/H3 run along A:11-A:21, placing the proline-rich H2/H3 ridge over the conserved hydrophobic strip.

### C2 — confidence 0.25 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains B:heavy, C:light, 19 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| B (heavy) | A | 14 | 0.929 | 0.6657 | 0.95 | 7:0.82, 8:0.7, 9:0.95, 10:0.79, 11:0.92, 12:0.84, 13:0.83, 14:0.64, 15:0.58, 16:0.43, 17:0.13, 18:0.77, 19:0.84, 20:0.08 |
| C (light) | A | 11 | 0.909 | 0.47 | 0.84 | 15:0.58, 16:0.43, 17:0.13, 18:0.77, 19:0.84, 20:0.08, 21:0.73, 22:0.76, 23:0.49, 26:0.12, 33:0.24 |

> Strongly heavy-biased, about 70:30. H2/H3 and H1 cover A:7-A:19, with both chains meeting at A:15-A:20; L1/L3 close over the A:21-A:23/A:26/A:33 polar and folded-back rim.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_2e3a2a_GR_rep1` | 1 | 0 | 4 |
| judge | `case_2e3a2a_GJ_rep2` | 0 | 0 | 0 |
| advocate C1 | `case_2e3a2a_GR_rep1` | 1 | 0 | 4 |
| advocate C3 | `case_2e3a2a_GR_rep1` | 1 | 0 | 4 |
| advocate C2 | `case_2e3a2a_GR_rep1` | 1 | 0 | 4 |

