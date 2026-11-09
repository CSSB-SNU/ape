# H2374 — gatherer answer (unscored)

Case `case_6a7664` · set `casp17` · retrieval `gated` · CASP entry 2026-06-22

Input prediction: `data/staged_casp17_no_native/H2374.pdb`

Input SHA-256: `cce06a976275bf0894b0dae47679691f93a74bbcd1b28cd9b17fe6bfe49200de`

Briefing: `data/briefing/casp17/H2374/search_results.json` · SHA-256 `6da47e89d19b7042483ab1c9442ed32a899f59c40f45416b4c36e0ae0c6c84d7`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C4 | 1 | 0.28 | 15 | side | The type-common major neutralizing face of the gD Ig-like core... |
| C6 | 2 | 0.17 | 13 | side | The compact hydrophobic/polar hotspot within the conserved... |
| C3 | 3 | 0.14 | 15 | side | The broad nectin-1 receptor-binding face of the gD Ig-like core... |
| C7 | 4 | 0.12 | 13 | side | A compact, type-common lateral gD face implicated in direct... |
| C8 | 5 | 0.1 | 20 | side | The non-receptor-binding N-terminal-to-A-prime interloop groove on... |
| C5 | 6 | 0.08 | 13 | side | The mobile N-terminal hairpin that folds around the TNFR-family... |
| C1 | 7 | 0.06 | 9 | side | The flexible, proline-rich C-terminal ectodomain tail: a continuous... |
| C2 | 8 | 0.05 | 14 | side | A discontinuous, proline-rich lateral face on the gD core and... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No source localizes HAB13: the patent is about this binder but supplies phenotype only, and every residue-level map concerns another antibody or a receptor. The distribution is therefore a Tier-B prior over surfaces. What separated it was the conjunction of phenotype compatibility, conventional-Fab rather than nanobody/receptor precedent, exact handed-footprint accessibility and extent, and a duplicate-surface correction: C3, C4, and C6 are nested drawings of one receptor-overlap face and share 0.59 total probability rather than counting as three independent confirmations. C4 is the most coherent boundary within that group.

## C4 — rank 1

The type-common major neutralizing face of the gD Ig-like core, coextensive with the nectin receptor interface and the DL11/E317 antigenic community.

Residues: C:139, C:140, C:215, C:216, C:220, C:221, C:222, C:223, C:226, C:227, C:235, C:238, C:27, C:38, C:39

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 27:0.54, 38:0.9, 215:0.88, 220:0.72, 221:0.88, 222:0.97, 223:0.96, 226:0.56, 227:0.43, 235:0.51, 238:0.55
- B → C: 27:0.54, 38:0.9, 39:0.72, 139:0.67, 140:0.64, 215:0.88, 216:0.58, 220:0.72, 222:0.97, 223:0.96

## C6 — rank 2

The compact hydrophobic/polar hotspot within the conserved receptor-binding face, centred on the Pro221-Arg222-Phe223-Ile224 ridge and its Y38/D139/D215 rim.

Residues: C:139, C:140, C:215, C:220, C:221, C:222, C:223, C:226, C:235, C:238, C:27, C:38, C:39

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 38:0.88, 215:0.89, 220:0.76, 221:0.9, 222:0.98, 223:0.97, 226:0.58, 235:0.5, 238:0.54
- B → C: 27:0.45, 38:0.88, 39:0.68, 139:0.68, 140:0.66, 215:0.89, 220:0.76, 222:0.98, 223:0.97

## C3 — rank 3

The broad nectin-1 receptor-binding face of the gD Ig-like core, including the N-terminal rim and the alpha3/receptor-contact ridge.

Residues: C:139, C:140, C:215, C:216, C:220, C:221, C:222, C:223, C:226, C:227, C:235, C:238, C:27, C:38, C:39

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 27:0.58, 38:0.88, 215:0.86, 220:0.7, 221:0.86, 222:0.96, 223:0.95, 226:0.55, 227:0.42, 235:0.52, 238:0.56
- B → C: 27:0.58, 38:0.88, 39:0.7, 139:0.66, 140:0.62, 215:0.86, 216:0.58, 220:0.7, 222:0.96, 223:0.95

## C7 — rank 4

A compact, type-common lateral gD face implicated in direct interaction with or activation of gH/gL, represented by the MC5 antigenic site around 54 and 75-79.

Residues: C:50, C:51, C:52, C:53, C:54, C:55, C:74, C:75, C:76, C:78, C:79, C:80, C:82

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 53:0.72, 54:0.92, 55:0.84, 74:0.79, 75:0.69, 76:0.9, 78:0.62, 79:0.86, 80:0.72, 82:0.54
- B → C: 50:0.61, 51:0.54, 52:0.66, 53:0.72, 54:0.92, 55:0.84, 75:0.69, 76:0.9

## C8 — rank 5

The non-receptor-binding N-terminal-to-A-prime interloop groove on the gD fusion-triggering face.

Residues: C:102, C:103, C:104, C:105, C:163, C:176, C:178, C:180, C:47, C:48, C:49, C:50, C:51, C:52, C:53, C:54, C:55, C:56, C:57, C:59

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 47:0.48, 48:0.84, 49:0.95, 50:0.88, 55:0.95, 102:0.46, 103:0.52, 104:0.97, 105:0.97, 176:0.22, 178:0.58
- B → C: 49:0.95, 50:0.88, 51:0.7, 52:0.74, 53:0.72, 54:0.8, 55:0.95, 56:0.6, 57:0.42, 59:0.54, 104:0.97, 105:0.97, 163:0.38, 178:0.58, 180:0.26

## C5 — rank 6

The mobile N-terminal hairpin that folds around the TNFR-family receptor HVEM during one mode of alphaherpesvirus entry.

Residues: C:11, C:13, C:14, C:15, C:24, C:26, C:27, C:28, C:29, C:31, C:32, C:7, C:8

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 11:0.8, 24:0.9, 26:0.92, 27:0.94, 28:0.83, 29:0.78, 31:0.58, 32:0.65
- B → C: 7:0.58, 8:0.65, 11:0.8, 13:0.82, 14:0.76, 15:0.66, 24:0.9, 26:0.92, 27:0.94

## C1 — rank 7

The flexible, proline-rich C-terminal ectodomain tail: a continuous antigenic site within the glycoprotein's profusion region.

Residues: C:267, C:268, C:269, C:270, C:271, C:272, C:273, C:274, C:275

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 268:0.72, 269:0.82, 270:0.9, 271:0.84, 273:0.94
- B → C: 267:0.48, 270:0.9, 271:0.84, 272:0.75, 273:0.94, 274:0.62, 275:0.48

## C2 — rank 8

A discontinuous, proline-rich lateral face on the gD core and alpha3/C-terminal ridge, adjacent to but distinct from the receptor-binding face and implicated in transmitting the fusion trigger.

Residues: C:237, C:239, C:240, C:241, C:242, C:243, C:244, C:245, C:246, C:247, C:248, C:249, C:64, C:67

Advocate: `case_6a7664_GR_rep5` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 67:0.7, 237:0.38, 239:0.44, 240:0.52, 241:0.62, 242:0.87, 243:0.72, 244:0.85, 245:0.91, 246:0.92, 247:0.78, 248:0.89
- B → C: 64:0.78, 67:0.7, 243:0.72, 245:0.91, 246:0.92, 248:0.89, 249:0.61

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_6a7664/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2374/case_6a7664_GR_rep5`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2374/case_6a7664_GJ_rep5`

