# H2344 — gatherer answer (unscored)

Case `case_679778` · set `casp17` · retrieval `gated` · CASP entry 2026-06-03

Input prediction: `data/staged_casp17_no_native/H2344.pdb`

Input SHA-256: `18733617ed7c4b96b45ff3352f72763afcd6932570e14f1956abaeff946190b8`

Briefing: `data/briefing/casp17/H2344/search_results.json` · SHA-256 `e01658771c612bd446896a8f683ccea6f403b94ecf685db0566f7e4ef7b38f51`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C8 | 1 | 0.18 | 19 | side | The shared nectin-1/core receptor groove of the gD Ig-like domain... |
| C3 | 2 | 0.17 | 17 | side | The N-to-A-prime interloop lateral cleft on the outside of the gD... |
| C1 | 3 | 0.14 | 15 | side | The seam where the mobile C-terminal ectodomain latch folds back onto... |
| C2 | 4 | 0.13 | 15 | side | The conserved receptor-overlap groove on the upper Ig-like core... |
| C6 | 5 | 0.11 | 14 | side | The short N-terminal peptide turn that forms the HVEM-facing tip of... |
| C7 | 6 | 0.1 | 18 | side | The exposed distal ectodomain extension or profusion latch of gD... |
| C5 | 7 | 0.09 | 18 | side | The mobile N-terminal receptor hairpin and return arm of gD: the... |
| C4 | 8 | 0.08 | 20 | side | The full E317-like receptor-overlap face: the upper Ig-core groove... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had Tier A evidence about this binder, so this remains a broad prior over surfaces. The narrow separation came from comparative calculations on every supplied footprint: connectivity, native-context accessibility risk, exact footprint extent versus the 39.29 A supplied paratope span, and coarse actual-paratope chemistry. I treated C2/C4/C8 as nested drawings of one receptor-groove family rather than counting their repeated E317 evidence three times; C5/C6 and C1/C7 likewise share surface priors. The receptor family received the largest cluster mass because three independent binders validate it, but the measured E317 transfer is weak (44.4% all-CDR identity, 16.7% H3), preventing concentration. C8 narrowly leads as the connected broad drawing; C3 is nearly tied because its cleft best matches the protruding H3 at a coarse level.

## C8 — rank 1

The shared nectin-1/core receptor groove of the gD Ig-like domain, organized around the Y38-D215-R222-F223 hotspot and the C:26-C:29, C:132-C:140 and C:220-C:238 supporting rims.

Residues: C:132, C:139, C:140, C:215, C:220, C:221, C:222, C:223, C:224, C:227, C:231, C:235, C:238, C:26, C:27, C:28, C:29, C:38, C:39

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 26:0.52, 27:0.74, 28:0.6, 29:0.48, 38:0.93, 39:0.55, 132:0.47, 139:0.65, 140:0.7, 215:0.9, 220:0.62, 221:0.84, 222:0.98, 223:0.97, 224:0.55, 227:0.46, 231:0.45, 235:0.63, 238:0.58
- B → C: 26:0.52, 27:0.74, 28:0.6, 29:0.48, 38:0.93, 39:0.55, 132:0.47, 139:0.65, 140:0.7, 215:0.9, 220:0.62, 221:0.84, 222:0.98, 223:0.97, 224:0.55, 227:0.46, 231:0.45, 235:0.63, 238:0.58

## C3 — rank 2

The N-to-A-prime interloop lateral cleft on the outside of the gD Ig-like core, with a hydrophobic 47-57 wall, a polar C:103-C:105 wall, and a lower 159-180 rim.

Residues: C:103, C:104, C:105, C:159, C:161, C:163, C:178, C:180, C:47, C:48, C:49, C:50, C:53, C:54, C:55, C:56, C:57

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 47:0.62, 48:0.78, 49:0.82, 50:0.55, 53:0.63, 54:0.67, 55:0.94, 56:0.58, 57:0.43, 103:0.66, 104:0.96, 105:0.94, 159:0.55, 161:0.42, 163:0.58, 178:0.62, 180:0.45
- B → C: 47:0.62, 48:0.78, 49:0.82, 50:0.55, 53:0.63, 54:0.67, 55:0.94, 56:0.58, 57:0.43, 103:0.66, 104:0.96, 105:0.94, 159:0.55, 161:0.42, 163:0.58, 178:0.62, 180:0.45

## C1 — rank 3

The seam where the mobile C-terminal ectodomain latch folds back onto the non-receptor, fusion-trigger face of gD: a core ridge around the C66-C189 disulfide and MC2-sensitive site abutting the distal C-terminal strip.

Residues: C:186, C:244, C:245, C:246, C:248, C:264, C:265, C:266, C:267, C:268, C:269, C:271, C:272, C:64, C:67

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 64:0.52, 67:0.95, 186:0.72, 244:0.58, 245:0.62, 246:0.86, 248:0.38, 264:0.58, 265:0.52, 266:0.73, 267:0.82, 268:0.79, 269:0.74, 271:0.64, 272:0.34
- B → C: 64:0.52, 67:0.95, 186:0.72, 244:0.58, 245:0.62, 246:0.86, 248:0.38, 264:0.58, 265:0.52, 266:0.73, 267:0.82, 268:0.79, 269:0.74, 271:0.64, 272:0.34

## C2 — rank 4

The conserved receptor-overlap groove on the upper Ig-like core, centered on the alpha3/PRFI ridge around C:221-C:224 and connected to the C:38/C:132/C:215 wall.

Residues: C:132, C:139, C:140, C:215, C:220, C:221, C:222, C:223, C:224, C:227, C:231, C:235, C:238, C:27, C:38

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 27:0.72, 38:0.91, 132:0.54, 139:0.65, 140:0.7, 215:0.82, 220:0.56, 221:0.82, 222:0.97, 223:0.96, 224:0.52, 227:0.46, 231:0.48, 235:0.68, 238:0.62
- B → C: 27:0.72, 38:0.91, 132:0.54, 139:0.65, 140:0.7, 215:0.82, 220:0.56, 221:0.82, 222:0.97, 223:0.96, 224:0.52, 227:0.46, 231:0.48, 235:0.68, 238:0.62

## C6 — rank 5

The short N-terminal peptide turn that forms the HVEM-facing tip of gD, centered on the ADPNRF motif C:12-C:17 rather than the whole receptor groove.

Residues: C:10, C:11, C:12, C:13, C:14, C:15, C:16, C:17, C:18, C:19, C:6, C:7, C:8, C:9

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 6:0.35, 7:0.55, 8:0.58, 9:0.42, 10:0.5, 11:0.62, 12:0.6, 13:0.9, 14:0.95, 15:0.94, 16:0.96, 17:0.9, 18:0.78, 19:0.55
- B → C: 6:0.35, 7:0.55, 8:0.58, 9:0.42, 10:0.5, 11:0.62, 12:0.6, 13:0.9, 14:0.95, 15:0.94, 16:0.96, 17:0.9, 18:0.78, 19:0.55

## C7 — rank 6

The exposed distal ectodomain extension or profusion latch of gD, centered on a proline-rich acidic turn C:254-C:269 just before the membrane-proximal remainder of the native ectodomain.

Residues: C:251, C:252, C:254, C:255, C:256, C:257, C:258, C:259, C:260, C:261, C:262, C:263, C:264, C:265, C:266, C:267, C:268, C:269

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 251:0.35, 252:0.55, 254:0.7, 255:0.85, 256:0.92, 257:0.64, 258:0.68, 259:0.93, 260:0.75, 261:0.76, 262:0.42, 263:0.55, 264:0.72, 265:0.58, 266:0.74, 267:0.82, 268:0.68, 269:0.55
- B → C: 251:0.35, 252:0.55, 254:0.7, 255:0.85, 256:0.92, 257:0.64, 258:0.68, 259:0.93, 260:0.75, 261:0.76, 262:0.42, 263:0.55, 264:0.72, 265:0.58, 266:0.74, 267:0.82, 268:0.68, 269:0.55

## C5 — rank 7

The mobile N-terminal receptor hairpin and return arm of gD: the HVEM-binding 7-22 segment continuing into the 24-29 rim that also approaches the shared HVEM/nectin receptor face.

Residues: C:10, C:11, C:12, C:13, C:14, C:15, C:16, C:17, C:18, C:19, C:20, C:21, C:22, C:24, C:26, C:27, C:28, C:29

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 10:0.5, 11:0.6, 12:0.58, 13:0.88, 14:0.93, 15:0.92, 16:0.95, 17:0.88, 18:0.82, 19:0.6, 20:0.77, 21:0.86, 22:0.83, 24:0.6, 26:0.55, 27:0.64, 28:0.5, 29:0.4
- B → C: 10:0.5, 11:0.6, 12:0.58, 13:0.88, 14:0.93, 15:0.92, 16:0.95, 17:0.88, 18:0.82, 19:0.6, 20:0.77, 21:0.86, 22:0.83, 24:0.6, 26:0.55, 27:0.64, 28:0.5, 29:0.4

## C4 — rank 8

The full E317-like receptor-overlap face: the upper Ig-core groove around C:221-C:224 plus the N-terminal 26-39, 132-140, 215-220 and 231-238 rims covered by a conventional Fab.

Residues: C:132, C:139, C:140, C:215, C:218, C:220, C:221, C:222, C:223, C:224, C:227, C:231, C:235, C:238, C:26, C:27, C:28, C:29, C:38, C:39

Advocate: `case_679778_GR_rep3` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 26:0.5, 27:0.75, 28:0.62, 29:0.48, 38:0.92, 39:0.55, 132:0.5, 139:0.68, 140:0.72, 215:0.84, 218:0.45, 220:0.6, 221:0.84, 222:0.98, 223:0.96, 224:0.52, 227:0.48, 231:0.51, 235:0.7, 238:0.65
- B → C: 26:0.5, 27:0.75, 28:0.62, 29:0.48, 38:0.92, 39:0.55, 132:0.5, 139:0.68, 140:0.72, 215:0.84, 218:0.45, 220:0.6, 221:0.84, 222:0.98, 223:0.96, 224:0.52, 227:0.48, 231:0.51, 235:0.7, 238:0.65

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_679778/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2344/case_679778_GR_rep3`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2344/case_679778_GJ_rep3`

