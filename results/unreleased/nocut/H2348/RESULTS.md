# H2348 — gatherer answer (unscored)

Case `case_4ade9a` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-05

Input prediction: `data/staged_casp17_no_native/H2348.pdb`

Input SHA-256: `ce3adf48ca6a518ad9b1c0b7ee6fd0899f7d12f01d7aa968c11b92ad459c41e7`

Briefing: `data/briefing/casp17_nocutoff/H2348/search_results.json` · SHA-256 `764bf0cb501957b0a6bbb2036c672dc856ac4be1b5e0aed11fd8847f842bf759`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C4 | 1 | 0.21 | 17 | side | The glycan-sparse lateral half of D1 site III: a flat Ig-domain... |
| C5 | 2 | 0.2 | 15 | side | The extreme distal ridge of the N-terminal Ig-like D1 domain: the... |
| C6 | 3 | 0.18 | 20 | side | The glycan-free outer ridge across the acute D4-D5 bend of the... |
| C2 | 4 | 0.17 | 19 | side | The cytokine-binding-homology-region site-II face across the D2-D3... |
| C1 | 5 | 0.1 | 15 | side | The glycan-clear outer face of the second membrane-proximal... |
| C3 | 6 | 0.08 | 19 | side | The broad distal cap of the N-terminal Ig-like D1 domain forming the... |
| C7 | 7 | 0.06 | 15 | side | The D3 receptor-receptor component of composite site II: the... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had a clone-localizing Tier A line; the binder-specific patent finding is equally true of all seven. The result is therefore a diffuse Tier-B prior. A uniform comparison of coverage, RSA, planarity, side-chain facing, and exposed-CDR chemistry separated a close leading group: C4's one-facing geometry, C5's different-Fab precedent, C6's paratope-specific bulk chemistry, and C2's functional plus nanobody precedent. None justified concentration.

## C4 — rank 1

The glycan-sparse lateral half of D1 site III: a flat Ig-domain beta-sheet/loop surface centered on an H49-F50 aromatic ledge and the N92-Y94-G95 functional rim rather than the distal tip.

Residues: A:12, A:13, A:15, A:48, A:49, A:50, A:51, A:74, A:75, A:76, A:78, A:80, A:92, A:94, A:95, A:97, A:99

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 12:0.41, 13:0.48, 15:0.35, 48:0.64, 49:0.86, 50:0.91, 51:0.73, 74:0.52, 75:0.57, 76:0.62, 78:0.76, 80:0.4, 92:0.74, 94:0.82, 95:0.73, 97:0.46, 99:0.42
- C → A: 12:0.41, 13:0.48, 15:0.35, 48:0.64, 49:0.86, 50:0.91, 51:0.73, 74:0.52, 75:0.57, 76:0.62, 78:0.76, 80:0.4, 92:0.74, 94:0.82, 95:0.73, 97:0.46, 99:0.42

## C5 — rank 2

The extreme distal ridge of the N-terminal Ig-like D1 domain: the exposed N-terminal edge packed against the D34-Y35-F36-H37 and F86-Q91 loops at the receptor top.

Residues: A:1, A:2, A:3, A:34, A:35, A:36, A:37, A:4, A:86, A:87, A:88, A:89, A:90, A:91, A:92

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 1:0.46, 2:0.52, 3:0.64, 4:0.59, 34:0.62, 35:0.94, 36:0.57, 37:0.83, 86:0.93, 87:0.79, 88:0.91, 89:0.83, 90:0.73, 91:0.68, 92:0.63
- C → A: 1:0.46, 2:0.52, 3:0.64, 4:0.59, 34:0.62, 35:0.94, 36:0.57, 37:0.83, 86:0.93, 87:0.79, 88:0.91, 89:0.83, 90:0.73, 91:0.68, 92:0.63

## C6 — rank 3

The glycan-free outer ridge across the acute D4-D5 bend of the membrane-proximal signaling leg, formed by the R350-W351-K352 loop, R373 loop, and F399/Q400-to-D480 folded ridge.

Residues: A:314, A:349, A:350, A:351, A:352, A:353, A:371, A:372, A:373, A:375, A:391, A:397, A:398, A:399, A:400, A:401, A:402, A:429, A:479, A:480

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 314:0.35, 349:0.4, 350:0.73, 351:0.96, 352:0.89, 353:0.66, 371:0.56, 372:0.63, 373:0.83, 375:0.61, 391:0.32, 397:0.55, 398:0.77, 399:0.87, 400:0.79, 401:0.59, 402:0.56, 429:0.63, 479:0.55, 480:0.56
- C → A: 314:0.35, 349:0.4, 350:0.73, 351:0.96, 352:0.89, 353:0.66, 371:0.56, 372:0.63, 373:0.83, 375:0.61, 391:0.32, 397:0.55, 398:0.77, 399:0.87, 400:0.79, 401:0.59, 402:0.56, 429:0.63, 479:0.55, 480:0.56

## C2 — rank 4

The cytokine-binding-homology-region site-II face across the D2-D3 elbow: an aromatic/hydrophobic D2 core and adjacent D3 buttress used by IL-6-family cytokine-alpha-receptor complexes (literature: 1P9M, 1PVH, 8D82; PMC7378365).

Residues: A:141, A:142, A:143, A:144, A:145, A:146, A:147, A:163, A:165, A:166, A:167, A:168, A:169, A:170, A:171, A:173, A:191, A:196, A:230

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 141:0.5, 142:0.9, 143:0.82, 144:0.84, 145:0.86, 146:0.53, 147:0.39, 163:0.72, 165:0.9, 166:0.58, 167:0.77, 168:0.86, 169:0.96, 170:0.84, 171:0.8, 173:0.48, 191:0.49, 196:0.55, 230:0.61
- C → A: 141:0.5, 142:0.9, 143:0.82, 144:0.84, 145:0.86, 146:0.53, 147:0.39, 163:0.72, 165:0.9, 166:0.58, 167:0.77, 168:0.86, 169:0.96, 170:0.84, 171:0.8, 173:0.48, 191:0.49, 196:0.55, 230:0.61

## C1 — rank 5

The glycan-clear outer face of the second membrane-proximal fibronectin-type-III leg domain, D5, where exposed beta-turns meet on the lower signaling leg of a tall class-I cytokine receptor (computed: analyze_refinement.py; literature: PMC7378365, 2020-07-16).

Residues: A:402, A:403, A:404, A:422, A:423, A:425, A:426, A:427, A:429, A:452, A:454, A:455, A:456, A:479, A:480

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 402:0.42, 403:0.64, 404:0.61, 422:0.57, 423:0.66, 425:0.93, 426:0.77, 427:0.89, 429:0.72, 452:0.73, 454:0.87, 455:0.28, 456:0.63, 479:0.68, 480:0.57
- C → A: 402:0.42, 403:0.64, 404:0.61, 422:0.57, 423:0.66, 425:0.93, 426:0.77, 427:0.89, 429:0.72, 452:0.73, 454:0.87, 455:0.28, 456:0.63, 479:0.68, 480:0.57

## C3 — rank 6

The broad distal cap of the N-terminal Ig-like D1 domain forming the composite site-III face in an IL-11-family signaling assembly, spanning the N-terminal edge, Y35/F36 ridge, and F86-Q95 shoulder (RCSB 8D82).

Residues: A:2, A:3, A:35, A:36, A:4, A:48, A:5, A:78, A:80, A:85, A:86, A:88, A:89, A:90, A:91, A:92, A:93, A:94, A:95

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 2:0.45, 3:0.58, 4:0.56, 5:0.42, 35:0.88, 36:0.49, 48:0.58, 78:0.65, 80:0.37, 85:0.25, 86:0.9, 88:0.91, 89:0.82, 90:0.73, 91:0.66, 92:0.77, 93:0.56, 94:0.68, 95:0.63
- C → A: 2:0.45, 3:0.58, 4:0.56, 5:0.42, 35:0.88, 36:0.49, 48:0.58, 78:0.65, 80:0.37, 85:0.25, 86:0.9, 88:0.91, 89:0.82, 90:0.73, 91:0.66, 92:0.77, 93:0.56, 94:0.68, 95:0.63

## C7 — rank 7

The D3 receptor-receptor component of composite site II: the cytokine-binding-module face contacting a cognate alpha receptor after cytokine capture, with an upper E212/E213/K219 lobe folded beside an E253/D254-S257/R259-Q265 lower lobe.

Residues: A:211, A:212, A:213, A:214, A:219, A:253, A:254, A:257, A:258, A:259, A:260, A:261, A:263, A:265, A:266

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 211:0.29, 212:0.83, 213:0.86, 214:0.69, 219:0.79, 253:0.87, 254:0.78, 257:0.73, 258:0.65, 259:0.8, 260:0.63, 261:0.62, 263:0.72, 265:0.85, 266:0.73
- C → A: 211:0.29, 212:0.83, 213:0.86, 214:0.69, 219:0.79, 253:0.87, 254:0.78, 257:0.73, 258:0.65, 259:0.8, 260:0.63, 261:0.62, 263:0.72, 265:0.85, 266:0.73

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_4ade9a/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2348/case_4ade9a_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2348/case_4ade9a_GJ_rep1`

