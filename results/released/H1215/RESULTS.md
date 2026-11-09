# H1215 — gather batched answer

Case `case_f91454` · set `casp16` · retrieval cutoff **2024-05-21**

Antibody: `antibody.pdb` (A:heavy) · antigen chains B

Truth: **22 residues** over B (`usable=yes`). F1 is against the union of every truth chain.

Judge rank 1 is **C4** at confidence 0.18 — precision **0.000**, recall **0.000**, **F1 0.000** (0 of 13 predicted residues are in the 22-residue truth). The best pocket the answer contains is **C6**, precision **0.438**, F1 **0.368**, sitting at judge rank 5.

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
| **C4** | 1 | 0.18 | 0.45 | 13 | 0.000 | 0.000 | 0.000 | `side` | A compact top-cap ridge where the 16 |
| **C8** | 2 | 0.16 | 0.38 | 18 | 0.000 | 0.000 | 0.000 | `side` | The curved C-terminal barrel seam: t |
| **C1** | 3 | 0.15 | 0.35 | 17 | 0.000 | 0.000 | 0.000 | `side` | The aromatic lateral seam of the GFP |
| **C5** | 4 | 0.14 | 0.35 | 18 | 0.000 | 0.000 | 0.000 | `side` | A corrugated distal barrel-end cleft |
| **C6** | 5 | 0.11 | 0.28 | 16 | 0.438 | 0.318 | 0.368 | `side` | A flat aromatic-acidic lateral barre |
| **C3** | 6 | 0.09 | 0.25 | 16 | 0.250 | 0.182 | 0.210 | `side` | The flat polar-positive former oligo |
| **C7** | 7 | 0.09 | 0.2 | 20 | 0.000 | 0.000 | 0.000 | `side` | The barrel edge homologous to the pu |
| **C2** | 8 | 0.08 | 0.24 | 20 | 0.000 | 0.000 | 0.000 | `side` | A broad upper-lateral loop field cen |

`confidence` is P(this pocket is where the antibody binds); the judge's entries sum to 1. `p(rests_on)` is P(the one assumption that, if false, moves this pocket down) — absolute, not normalised, and a ceiling on the confidence beside it. The assumption itself is `pocket.rests_on`, and `pocket.where_the_mass_goes_if_it_fails` names which pocket takes the weight if it breaks.

> No candidate had Tier A evidence about the supplied binder. The distribution is therefore deliberately broad and is a prior over exposed, one-paratope-sized surfaces. Independent same-basis measurements modestly favored compact, fully exposed patches whose charge and aromatic capacities suit this long mixed-chemistry H3 (C4, C8, C1, C5). C7's apparent documentary advantage was discounted after direct auditing showed only 15.0% side-chain identity over the transferred 3K1K contact positions and an unrelated VHH. Functional-site and generic nanobody precedents did not localize, and all candidates passed whole-paratope reach, so no probability exceeds 0.18.

## Which antibody binds which antigen residues

### C4 — confidence 0.18 (judge rank 1)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 13 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 13 | 0.000 | 0.6362 | 0.95 | 105:0.5, 146:0.35, 147:0.18, 150:0.7, 168:0.85, 172:0.3, 174:0.62, 175:0.82, 176:0.7, 177:0.9, 178:0.95, 180:0.9, 237:0.5 |

> VHH-only: H3 covers the 174-180 crest and aromatic flanks; H2 supports the K168/W150 side.

### C8 — confidence 0.16 (judge rank 2)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 18 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 18 | 0.000 | 0.5833 | 0.95 | 41:0.25, 43:0.3, 44:0.4, 80:0.5, 81:0.42, 82:0.25, 150:0.7, 152:0.55, 208:0.35, 223:0.86, 225:0.95, 228:0.78, 229:0.8, 230:0.55, 232:0.4, 235:0.9, 236:0.72, 237:0.82 |

> VHH-only: H3 covers W223/K225/D229/E235/L236/Y237; H2/H1 support W150/R152 and the 41-44/80-82 edges.

### C1 — confidence 0.15 (judge rank 3)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 17 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 17 | 0.000 | 0.4576 | 0.9 | 44:0.42, 46:0.22, 48:0.45, 147:0.32, 148:0.12, 149:0.38, 150:0.88, 152:0.48, 208:0.55, 209:0.15, 210:0.66, 211:0.18, 221:0.5, 223:0.9, 225:0.55, 236:0.4, 237:0.62 |

> VHH-only: 100% heavy-chain contact. H3 covers W150/W223; H2 and H1 support the charged perimeter.

### C5 — confidence 0.14 (judge rank 4)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 18 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 18 | 0.000 | 0.5839 | 0.9 | 105:0.45, 106:0.35, 135:0.35, 136:0.55, 137:0.85, 139:0.18, 141:0.4, 142:0.65, 143:0.7, 144:0.75, 146:0.48, 172:0.28, 174:0.65, 175:0.9, 176:0.82, 177:0.9, 178:0.7, 180:0.55 |

> VHH-only: H3 occupies the D137/N175/G176/K177 cleft; H1/H2 contact the two lips.

### C6 — confidence 0.11 (judge rank 5)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 16 | 0.438 | 0.5687 | 0.82 | 22:0.55, 24:0.7, 30:0.35, 31:0.65, 35:0.5, 37:0.32, 52:0.58, 54:0.82, 55:0.8, 56:0.72, 57:0.78, 59:0.45, 126:0.35, 214:0.38, 216:0.55, 217:0.6 |

> VHH-only: H3 spans the 52-57 center; H1/H2 reach the 22-37 and 214-217 rims.

### C3 — confidence 0.09 (judge rank 6)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 16 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 16 | 0.250 | 0.5494 | 0.88 | 24:0.5, 28:0.45, 29:0.35, 99:0.5, 101:0.62, 103:0.75, 107:0.4, 109:0.25, 111:0.84, 113:0.58, 128:0.52, 130:0.88, 132:0.68, 133:0.5, 182:0.35, 184:0.62 |

> VHH-only: H3 lies across 99-133; H1/H2 support the 24-29 and 182-184 edges.

### C7 — confidence 0.09 (judge rank 7)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 20 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 20 | 0.000 | 0.5325 | 0.92 | 146:0.45, 147:0.25, 148:0.1, 149:0.28, 150:0.82, 168:0.55, 170:0.15, 172:0.3, 174:0.65, 175:0.88, 176:0.82, 177:0.92, 178:0.9, 180:0.75, 208:0.4, 209:0.12, 210:0.58, 219:0.38, 221:0.55, 223:0.8 |

> VHH-only: H3 centers on 174-180; H2 supports 146-168; H1/H2 cover 208-223. The footprint necessarily uses more than H3.

### C2 — confidence 0.08 (judge rank 8)

Mapping basis: `side`  — one union vector, split by each residue's `heavy`/`light`/`both` side.

**`antibody.pdb`** — chains A:heavy, 20 residues scored

| antibody chain | antigen chain | n res | precision | mean conf | max conf | residues (conf) |
|---|---|---|---|---|---|---|
| A (heavy) | B | 20 | 0.000 | 0.6015 | 0.9 | 81:0.38, 88:0.2, 92:0.42, 156:0.35, 158:0.6, 159:0.55, 160:0.72, 161:0.65, 188:0.35, 190:0.45, 191:0.58, 192:0.78, 194:0.82, 195:0.86, 196:0.9, 198:0.72, 199:0.9, 200:0.78, 201:0.62, 202:0.4 |

> VHH-only: H3 covers 192-201; H2/H1 reach the 156-161 and 81-92 flanks.

Pooled from 3 phase-1 patches, which drew different residues — 7 shared and 24 disputed at pooling. What the advocate then kept of each:

- `P10` (17 res) — 14 kept, 3 dropped · Opposite lateral barrel face centered on 194-199
- `P2` (15 res) — 11 kept, 4 dropped · hydrophobic-polar side shelf around 154-202
- `P8` (23 res) — 19 kept, 4 dropped · Upper lateral 158-201 loop field

## Gate audit

| stage | session | gate calls | withheld | post-cutoff dropped |
|---|---|---|---|---|
| organize | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| judge | `case_f91454_GJ_rep2` | 5 | 0 | 0 |
| advocate C4 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C8 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C1 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C5 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C6 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C3 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C7 | `case_f91454_GR_rep1` | 1 | 0 | 2 |
| advocate C2 | `case_f91454_GR_rep1` | 1 | 0 | 2 |

