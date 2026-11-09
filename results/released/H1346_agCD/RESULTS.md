# H1346_agCD — gather batched answer

Case `case_fed304` · set `casp17` · retrieval cutoff **2026-05-21**

Antibody: `antibody.pdb` (A:heavy, B:light) · antigen chains C, D

Truth: **17 residues** over D (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C1** at confidence 0.42 — precision **0.696**, recall **0.941**, **F1 0.800** (16 of 23 predicted residues are in the 17-residue truth). The best pocket the answer contains is **C1**, precision **0.696**, F1 **0.800**, sitting at judge rank 1.

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
| **C1** | 1 | 0.42 | 0.48 | 23 | 0.696 | 0.941 | 0.800 | `side` | The broad solvent-exposed outer plat |
| **C4** | 2 | 0.31 | 0.38 | 17 | 0.000 | 0.000 | 0.000 | `side` | The V-kappa/C-kappa elbow junction a |
| **C2** | 3 | 0.12 | 0.22 | 21 | 0.000 | 0.000 | 0.000 | `side` | The functional idiotope spanning the |
| **C3** | 4 | 0.06 | 0.15 | 19 | 0.000 | 0.000 | 0.000 | `side` | A single-antigen-chain idiotope on t |
| **C5** | 5 | 0.04 | 0.1 | 26 | 0.000 | 0.000 | 0.000 | `side` | The complete anti-BCMA paratope idio |
| **C6** | 6 | 0.03 | 0.08 | 13 | 0.000 | 0.000 | 0.000 | `side` | A compact single-chain V-kappa idiot |
| **C7** | 7 | 0.02 | 0.06 | 17 | 0.000 | 0.000 | 0.000 | `side` | The broader solvent-exposed V-kappa  |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate has a Tier A line about A/B. The distribution is therefore a contextual prior over surfaces: the same linvoseltamab specimen reportedly used an anti-kappa Fab, moving 0.73 total mass to C1/C4. C1 leads on uniform intact-assembly exposure and a conventional-antibody broad-face prior; C4 gains weaker different-VHH hinge precedent and gross charge complementarity. Structural filters favor C2 among the overlapping C2/C3/C5 apex variants and C6 over C7, but do not overcome the missing binder identity.

## Which antibody binds which antigen residues

### C1 — confidence 0.42 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 23 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | D | 15 | 0.933 | 0.718 | 0.95 | 152:0.45, 153:0.72, 154:0.62, 155:0.78, 156:0.42, 157:0.9, 158:0.92, 160:0.43, 185:0.76, 186:0.67, 188:0.73, 189:0.95, 190:0.84, 191:0.88, 192:0.7 |
| B (light) | D | 15 | 0.600 | 0.6847 | 0.95 | 157:0.9, 158:0.92, 181:0.34, 183:0.55, 184:0.62, 185:0.76, 186:0.67, 188:0.73, 189:0.95, 190:0.84, 209:0.6, 211:0.4, 212:0.53, 213:0.8, 214:0.66 |

> Heavy-dominant, approximately two-thirds heavy-chain contact: A:H3/H2 anchor D:153-D:160 and D:188-D:192, while B:L1/L3 close the D:181-D:186 and D:209-D:214 rim.

Pooled from 2 phase-1 patches, which drew different residues — 4 shared and 26 disputed at pooling. What the advocate then kept of each:

- `P1` (17 res) — 16 kept, 1 dropped · distal kappa-constant face around D:189-D:192 and D:
- `P8` (17 res) — 11 kept, 6 dropped · mid-CL outer face centered on D:157-D:158

### C4 — confidence 0.31 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | D | 12 | 0.000 | 0.6942 | 0.95 | 109:0.45, 110:0.82, 111:0.67, 113:0.48, 143:0.7, 144:0.9, 145:0.48, 146:0.8, 198:0.58, 200:0.88, 201:0.62, 203:0.95 |
| B (light) | D | 12 | 0.000 | 0.7083 | 0.95 | 144:0.9, 145:0.48, 146:0.8, 198:0.58, 200:0.88, 201:0.62, 203:0.95, 204:0.78, 205:0.82, 206:0.55, 207:0.72, 208:0.42 |

> Heavy-dominant: A:H3/H2 bridge D:109-D:146 to D:198-D:203; B:L1/L3 close the D:203-D:208 edge. D:144-D:146 and D:198-D:203 are both-chain center contacts.

### C2 — confidence 0.12 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 21 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 8 | 0.000 | 0.8337 | 0.98 | 100:0.6, 101:0.88, 103:0.92, 104:0.92, 105:0.98, 106:0.97, 107:0.58, 108:0.82 |
| A (heavy) | D | 5 | 0.000 | 0.666 | 0.83 | 30:0.4, 92:0.83, 93:0.68, 94:0.78, 95:0.64 |
| B (light) | C | 14 | 0.000 | 0.6664 | 0.98 | 31:0.48, 32:0.32, 33:0.25, 53:0.45, 54:0.72, 56:0.67, 57:0.55, 58:0.4, 101:0.88, 103:0.92, 104:0.92, 105:0.98, 106:0.97, 108:0.82 |

> Heavy-dominant but genuinely straddling: A:H3/H2 anchor C:H3 and reach D:L3, while B:L1/L3 cover the C:H1/H2 rim; C:101 and C:103-C:108 lie at the both-chain center.

Pooled from 2 phase-1 patches, which drew different residues — 11 shared and 15 disputed at pooling. What the advocate then kept of each:

- `P10` (24 res) — 20 kept, 4 dropped · straddling anti-idiotope across the linvoseltamab iB
- `P2` (13 res) — 12 kept, 1 dropped · linvoseltamab variable-domain combining-site idiotop

### C3 — confidence 0.06 (judge rank 4)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 19 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 10 | 0.000 | 0.731 | 0.99 | 100:0.65, 101:0.9, 102:0.35, 103:0.94, 104:0.94, 105:0.99, 106:0.98, 107:0.6, 108:0.84, 114:0.12 |
| B (light) | C | 15 | 0.000 | 0.674 | 0.99 | 30:0.38, 31:0.56, 32:0.36, 33:0.3, 53:0.5, 54:0.74, 56:0.68, 57:0.57, 58:0.43, 101:0.9, 103:0.94, 104:0.94, 105:0.99, 106:0.98, 108:0.84 |

> Heavy-dominant, about 60:40: A:H3/H2 cover C:H3, while B:L1/L3 cover the C:H1/H2 flank; C:101 and C:103-C:108 are both-chain center contacts.

Pooled from 2 phase-1 patches, which drew different residues — 17 shared and 8 disputed at pooling. What the advocate then kept of each:

- `P3` (19 res) — 17 kept, 2 dropped · heavy-variable-only idiotope on the exposed C:H3/H2 
- `P7` (23 res) — 19 kept, 4 dropped · VH-dominant anti-BCMA idiotope

### C5 — confidence 0.04 (judge rank 5)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 26 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | C | 8 | 0.000 | 0.845 | 0.99 | 100:0.62, 101:0.9, 103:0.93, 104:0.93, 105:0.99, 106:0.98, 107:0.58, 108:0.83 |
| A (heavy) | D | 8 | 0.000 | 0.5475 | 0.84 | 28:0.42, 30:0.45, 31:0.25, 52:0.28, 92:0.84, 93:0.69, 94:0.79, 95:0.66 |
| B (light) | C | 16 | 0.000 | 0.63 | 0.99 | 28:0.24, 30:0.38, 31:0.55, 32:0.32, 33:0.25, 53:0.46, 54:0.72, 56:0.66, 57:0.54, 58:0.4, 101:0.9, 103:0.93, 104:0.93, 105:0.99, 106:0.98, 108:0.83 |

> Heavy-dominant despite the two-chain antigen footprint: A:H3/H2 anchor C:H3 and D:L1/L3, while B:L1/L3/H1 cover C:H1/H2. The C:H3 crest is reached by both paratope chains.

### C6 — confidence 0.03 (judge rank 6)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | D | 9 | 0.000 | 0.6544 | 0.9 | 26:0.4, 27:0.67, 28:0.76, 30:0.6, 92:0.9, 93:0.76, 94:0.84, 95:0.72, 96:0.24 |
| B (light) | D | 8 | 0.000 | 0.58 | 0.9 | 28:0.76, 30:0.6, 31:0.32, 52:0.3, 67:0.58, 69:0.42, 92:0.9, 93:0.76 |

> Heavy-dominant: A:H3 covers the D:L1/L3 center, with B:L1/L3 on the D:67/D:69 and D:27-D:31 rim; D:28 and D:92-D:93 are both-chain center contacts.

### C7 — confidence 0.02 (judge rank 7)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, B:light, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | D | 9 | 0.000 | 0.6133 | 0.9 | 27:0.58, 28:0.7, 30:0.56, 92:0.9, 93:0.77, 94:0.85, 95:0.74, 96:0.22, 98:0.2 |
| B (light) | D | 12 | 0.000 | 0.4958 | 0.9 | 28:0.7, 30:0.56, 31:0.28, 49:0.3, 52:0.54, 53:0.32, 54:0.42, 56:0.34, 67:0.58, 68:0.24, 92:0.9, 93:0.77 |

> Heavy-dominant at the L3/L1 center: A:H3 covers D:28-D:30 and D:92-D:95, while B:L1/L3/H1 spread over D:49-D:68; D:28 and D:92-D:93 are both-chain contacts.

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| judge | `case_fed304_GJ_rep2` | 0 | 0 | 0 |
| advocate C1 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C4 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C2 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C3 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C5 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C6 | `case_fed304_GR_rep1` | 2 | 0 | 7 |
| advocate C7 | `case_fed304_GR_rep1` | 2 | 0 | 7 |

