# H2335 — gatherer answer (unscored)

Case `case_d48c74` · set `casp17` · retrieval `gated` · CASP entry 2026-05-27

Input prediction: `data/staged_casp17_no_native/H2335.pdb`

Input SHA-256: `f216450f2774ea363d9dfeeb1e478d506d906f539f384bf370d4b65ff32c11bb`

Briefing: `data/briefing/casp17/H2335/search_results.json` · SHA-256 `b0dea935f69c91b0e53c3c91d2fd212f5956d760276c3166d7c198ef62ac5bc6`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C2 | 1 | 0.2 | 17 | side | The external heel of gH, where a hydrophobic WMPP ridge, a nearby... |
| C7 | 2 | 0.18 | 13 | side | A compact two-lobe conformational epitope on gH domain IV near the... |
| C1 | 3 | 0.14 | 14 | side | The distal, solvent-facing lobe of the gO receptor-binding face: a... |
| C3 | 4 | 0.12 | 15 | side | The compact hydrophobic-polar pocket on the outer gH heel, joining... |
| C5 | 5 | 0.1 | 19 | side | A compact diagonal core on the inner gH DII-DIII kink, extending from... |
| C9 | 6 | 0.09 | 22 | side | The polar core of the gH DII-DIII kink: an exposed charged network... |
| C8 | 7 | 0.07 | 16 | side | The broader antigenic face of gH domain IV at the C-terminal... |
| C6 | 8 | 0.06 | 18 | side | The broad gH DII-DIII kink face, specifically the reachable diagonal... |
| C4 | 9 | 0.04 | 13 | side | A receptor-facing composite seam where a basic gO ridge approaches... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had a Tier A line about this binder. I retained a broad prior over four surface classes, then split overlapping variants using exact shipped-footprint exposure, assembly burial, glycan constraints, connectivity, extent, and a deliberately weak pose-free chemistry comparison.

## C2 — rank 1

The external heel of gH, where a hydrophobic WMPP ridge, a nearby exposed TPN turn, and an acidic DIII/DIV-side rim form one shallow discontinuous pocket on the membrane-proximal fusion-regulator half of gH.

Residues: B:142, B:144, B:145, B:146, B:147, B:149, B:385, B:386, B:387, B:388, B:391, B:414, B:415, B:418, B:419, B:422, B:426

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 147:0.94, 386:0.3, 387:0.48, 388:0.82, 391:0.52, 414:0.66, 415:0.34, 418:0.62, 419:0.28, 422:0.93, 426:0.3
- E → B: 142:0.64, 144:0.95, 145:0.56, 146:0.42, 147:0.94, 149:0.68, 385:0.62, 388:0.82, 391:0.52, 414:0.66, 418:0.62, 422:0.93

## C7 — rank 2

A compact two-lobe conformational epitope on gH domain IV near the C-terminal ectodomain: an exposed DPYNE-containing lobe paired in 3D with the terminal acidic turn.

Residues: B:653, B:654, B:657, B:658, B:659, B:660, B:661, B:664, B:682, B:685, B:689, B:690, B:691

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 659:0.94, 660:0.64, 661:0.9, 682:0.22, 685:0.84, 689:0.48, 690:0.36, 691:0.24
- E → B: 653:0.58, 654:0.52, 657:0.62, 658:0.68, 659:0.94, 660:0.64, 661:0.9, 664:0.46, 685:0.84

## C1 — rank 3

The distal, solvent-facing lobe of the gO receptor-binding face: a charged proteinaceous patch at the fourth contact site used by a multi-domain entry receptor, immediately beside the gO-gL seam but on the exposed gO side of it.

Residues: A:313, A:317, A:318, A:321, A:322, A:323, A:325, A:327, A:328, A:331, A:334, A:335, A:346, A:348

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → A: 321:0.88, 323:0.92, 325:0.28, 327:0.62, 331:0.84, 334:0.58, 335:0.36, 346:0.54, 348:0.42
- E → A: 313:0.68, 317:0.82, 318:0.76, 321:0.88, 322:0.72, 323:0.92, 327:0.62, 328:0.48, 331:0.84, 334:0.58

## C3 — rank 4

The compact hydrophobic-polar pocket on the outer gH heel, joining the WMPP loop to the Q/W/R/Q/D lobe at the DIII/DIV side of the boot-shaped fusion regulator.

Residues: B:142, B:143, B:144, B:145, B:146, B:147, B:148, B:391, B:414, B:415, B:418, B:419, B:422, B:426, B:429

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 147:0.94, 148:0.24, 391:0.4, 414:0.74, 415:0.38, 418:0.7, 419:0.3, 422:0.96, 426:0.42, 429:0.2
- E → B: 142:0.62, 143:0.18, 144:0.96, 145:0.58, 146:0.42, 147:0.94, 148:0.24, 391:0.4, 414:0.74, 418:0.7, 422:0.96

## C5 — rank 5

A compact diagonal core on the inner gH DII-DIII kink, extending from an acidic/polar upper ridge through the mixed B:305-B:309 center to the exposed B:364/B:365 and B:529-B:538 seam.

Residues: B:196, B:197, B:198, B:199, B:200, B:218, B:265, B:305, B:306, B:308, B:309, B:363, B:364, B:365, B:529, B:530, B:533, B:534, B:538

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 200:0.66, 308:0.86, 363:0.48, 364:0.88, 365:0.78, 529:0.32, 530:0.46, 533:0.7, 534:0.28, 538:0.46
- E → B: 196:0.76, 197:0.62, 198:0.8, 199:0.64, 200:0.66, 218:0.5, 265:0.34, 305:0.62, 306:0.74, 308:0.86, 309:0.82, 364:0.88

## C9 — rank 6

The polar core of the gH DII-DIII kink: an exposed charged network linking B:194-B:222 to the B:259-B:265 turn and B:300-B:313 lobe, excluding the remote lower flank.

Residues: B:194, B:196, B:197, B:198, B:199, B:200, B:201, B:218, B:220, B:221, B:222, B:261, B:264, B:265, B:300, B:304, B:305, B:306, B:308, B:309, B:311, B:313

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 194:0.42, 196:0.8, 197:0.6, 198:0.84, 199:0.68, 200:0.76, 201:0.24, 264:0.48, 265:0.62, 308:0.86, 313:0.56
- E → B: 198:0.84, 200:0.76, 218:0.64, 220:0.82, 221:0.28, 222:0.24, 261:0.66, 264:0.48, 265:0.62, 300:0.42, 304:0.5, 305:0.6, 306:0.78, 308:0.86, 309:0.82, 311:0.34

## C8 — rank 7

The broader antigenic face of gH domain IV at the C-terminal ectodomain, encompassing the exposed DPYNE lobe, adjacent hydrophobic rim, and glycan-bounded terminal lobe.

Residues: B:653, B:654, B:657, B:658, B:659, B:660, B:661, B:664, B:665, B:666, B:677, B:679, B:682, B:685, B:689, B:690

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 659:0.95, 660:0.66, 661:0.92, 665:0.48, 666:0.36, 677:0.2, 679:0.22, 682:0.2, 685:0.82, 689:0.46, 690:0.34
- E → B: 653:0.66, 654:0.54, 657:0.62, 658:0.7, 659:0.95, 660:0.66, 661:0.92, 664:0.54, 665:0.48, 666:0.36, 685:0.82

## C6 — rank 8

The broad gH DII-DIII kink face, specifically the reachable diagonal from B:195-B:200 through B:305-B:365 to the B:507/B:529-B:553 lower seam.

Residues: B:195, B:196, B:198, B:200, B:305, B:306, B:308, B:309, B:363, B:364, B:365, B:507, B:529, B:530, B:533, B:534, B:538, B:553

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 195:0.12, 196:0.68, 198:0.78, 200:0.66, 308:0.88, 363:0.46, 364:0.86, 365:0.74, 507:0.2, 529:0.3, 530:0.46, 533:0.68, 534:0.28, 538:0.44, 553:0.18
- E → B: 198:0.78, 200:0.66, 305:0.58, 306:0.8, 308:0.88, 309:0.8, 364:0.86

## C4 — rank 9

A receptor-facing composite seam where a basic gO ridge approaches the exposed edge of gL: a two-subunit junction in the membrane-distal attachment module rather than a buried assembly core.

Residues: A:120, A:121, A:165, A:167, A:168, A:94, A:95, A:96, C:62, C:63, C:64, C:65, C:67

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → A: 165:0.7, 167:0.62, 168:0.82
- D → C: 62:0.3, 63:0.28, 64:0.68, 65:0.18, 67:0.76
- E → A: 94:0.58, 95:0.86, 96:0.74, 120:0.46, 121:0.34, 165:0.7, 167:0.62, 168:0.82
- E → C: 64:0.68, 67:0.76

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_d48c74/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2335/case_d48c74_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2335/case_d48c74_GJ_rep1`

