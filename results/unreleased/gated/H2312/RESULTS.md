# H2312 — gatherer answer (unscored)

Case `case_3a23b5` · set `casp17` · retrieval `gated` · CASP entry 2026-05-13

Input prediction: `data/staged_casp17_no_native/H2312.pdb`

Input SHA-256: `3ba79066f0aa7015920828a3678d94af5f532471fde42bb38b00795e45f94b8b`

Briefing: `data/briefing/casp17/H2312/search_results.json` · SHA-256 `505309f67a804eec52cc306f4ab96c9a054e3d78c8918d0dd82eabf7012e4beb`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C2 | 1 | 0.17 | 18 | side | A glycan-clear, assembly-created cleft where the N-terminal GT-B... |
| C5 | 2 | 0.14 | 19 | side | The compact acceptor-facing lip of the active EXT2 GT-A groove... |
| C4 | 3 | 0.12 | 20 | side | The exposed catalytic face of the C-terminal EXT1 GT-A... |
| C1 | 4 | 0.11 | 17 | side | The exposed lower rim of the N-terminal EXT1 GT-B... |
| C6 | 5 | 0.1 | 14 | side | A membrane-proximal conformational seam between the resolved EXT1 N... |
| C9 | 6 | 0.09 | 15 | side | The upper/entry lobe of the EXT1 GT-B GlcA-transferase cleft... |
| C3 | 7 | 0.08 | 19 | side | The broad donor/acceptor trench of the C-terminal EXT2 GT-A... |
| C8 | 8 | 0.08 | 18 | side | The upper aromatic/acidic rim of the EXT1 GT-A GlcNAc-transferase... |
| C7 | 9 | 0.07 | 21 | side | The acidic catalytic basin and hydrophobic/basic walls of the major... |
| C10 | 10 | 0.04 | 21 | side | The lower donor/acceptor lobe of the EXT1 GT-B GlcA-transferase... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has a line about this binder, so the distribution remains a broad Tier B prior over surfaces. The ten proposals were first collapsed into five physical neighborhoods so repeated drawings did not multiply a neighborhood's probability. Mass within each neighborhood was then divided using the unchanged inherited footprint's assembly exposure, connectivity, paratope-scale extent, glycan and membrane context, and weak pose-free chemistry. C2 led on clean geometry, C5 led the catalytic variants, and C10 was separated negatively by a direct geometric failure.

## C2 — rank 1

A glycan-clear, assembly-created cleft where the N-terminal GT-B domains of EXT1 and EXT2 meet, centered on the A:307 and B:31/B:35 lips of the heterodimer seam.

Residues: A:300, A:301, A:302, A:303, A:305, A:307, A:308, A:311, B:25, B:26, B:29, B:31, B:32, B:35, B:36, B:37, B:38, B:39

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 300:0.55, 301:0.4, 302:0.35, 303:0.72, 305:0.35, 307:0.87, 308:0.48, 311:0.55
- C → B: 25:0.38, 26:0.64, 29:0.72, 31:0.88, 32:0.76, 35:0.74, 36:0.5, 37:0.66, 38:0.58, 39:0.45

## C5 — rank 2

The compact acceptor-facing lip of the active EXT2 GT-A groove, centered on the B:522 Glu/B:523 Trp shelf and B:585–B:609 rim.

Residues: B:506, B:518, B:520, B:521, B:522, B:523, B:524, B:525, B:526, B:531, B:585, B:586, B:587, B:588, B:590, B:606, B:607, B:608, B:609

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 506:0.68, 518:0.52, 520:0.58, 521:0.65, 522:0.92, 523:0.94, 524:0.7, 525:0.76, 526:0.64, 531:0.58, 585:0.55, 586:0.65, 587:0.72, 588:0.88, 590:0.74, 606:0.68, 607:0.72, 608:0.82, 609:0.87

## C4 — rank 3

The exposed catalytic face of the C-terminal EXT1 GT-A GlcNAc-transferase domain, narrowed to the acidic/aromatic rim around its DxD/sugar-recognition pocket.

Residues: A:466, A:485, A:487, A:489, A:567, A:570, A:573, A:574, A:600, A:601, A:602, A:611, A:612, A:616, A:617, A:618, A:619, A:620, A:622, A:623

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 466:0.4, 485:0.62, 487:0.68, 489:0.45, 567:0.5, 570:0.68, 573:0.58, 574:0.46, 600:0.87, 601:0.79, 602:0.75, 611:0.66, 612:0.84, 616:0.72, 617:0.61, 618:0.83, 619:0.73, 620:0.78, 622:0.66, 623:0.63

## C1 — rank 4

The exposed lower rim of the N-terminal EXT1 GT-B β1,4-glucuronyltransferase donor/acceptor cleft—the mixed aromatic/charged face surrounding the UDP-GlcA and growing-heparan-sulfate path.

Residues: A:187, A:189, A:191, A:200, A:219, A:220, A:223, A:239, A:240, A:243, A:244, A:245, A:258, A:260, A:265, A:266, A:269

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 187:0.35, 189:0.83, 191:0.55, 200:0.36, 219:0.65, 220:0.7, 223:0.58, 239:0.72, 240:0.82, 243:0.88, 244:0.84, 245:0.78, 258:0.58, 260:0.7, 265:0.86, 266:0.8, 269:0.73

## C6 — rank 5

A membrane-proximal conformational seam between the resolved EXT1 N terminus and the exposed rim of EXT2's inactive pseudo-GT-B domain.

Residues: A:1, A:3, A:4, A:5, A:6, A:7, B:197, B:199, B:200, B:201, B:203, B:204, B:205, B:207

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 1:0.65, 3:0.78, 4:0.62, 5:0.66, 6:0.55, 7:0.64
- C → B: 197:0.7, 199:0.63, 200:0.72, 201:0.5, 203:0.68, 204:0.86, 205:0.72, 207:0.66

## C9 — rank 6

The upper/entry lobe of the EXT1 GT-B GlcA-transferase cleft, centered on the A:82/A:84 catalytic loop and exposed A:85–A:123 shelf.

Residues: A:116, A:120, A:122, A:123, A:189, A:191, A:200, A:82, A:84, A:85, A:86, A:87, A:88, A:89, A:90

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 82:0.42, 84:0.47, 85:0.79, 86:0.88, 87:0.56, 88:0.82, 89:0.78, 90:0.55, 116:0.7, 120:0.86, 122:0.76, 123:0.72, 189:0.68, 191:0.55, 200:0.45

## C3 — rank 7

The broad donor/acceptor trench of the C-terminal EXT2 GT-A α1,4-GlcNAc-transferase domain, refined onto its exposed UDP/oligosaccharide rim.

Residues: B:400, B:401, B:402, B:475, B:506, B:521, B:522, B:523, B:531, B:560, B:561, B:564, B:565, B:588, B:590, B:606, B:607, B:608, B:609

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 400:0.52, 401:0.62, 402:0.58, 475:0.65, 506:0.55, 521:0.6, 522:0.88, 523:0.91, 531:0.72, 560:0.66, 561:0.75, 564:0.68, 565:0.55, 588:0.86, 590:0.77, 606:0.73, 607:0.7, 608:0.78, 609:0.84

## C8 — rank 8

The upper aromatic/acidic rim of the EXT1 GT-A GlcNAc-transferase pocket, centered on A:600–A:623 and excluding buried floor residues.

Residues: A:568, A:570, A:573, A:574, A:600, A:601, A:602, A:611, A:612, A:614, A:616, A:617, A:618, A:619, A:620, A:622, A:623, A:626

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 568:0.62, 570:0.68, 573:0.58, 574:0.48, 600:0.82, 601:0.79, 602:0.75, 611:0.78, 612:0.87, 614:0.63, 616:0.8, 617:0.66, 618:0.88, 619:0.78, 620:0.81, 622:0.7, 623:0.72, 626:0.52

## C7 — rank 9

The acidic catalytic basin and hydrophobic/basic walls of the major EXT2 GT-A GlcNAc-transferase pocket, narrowed to a 27.3 Å H3-centered core.

Residues: B:475, B:531, B:554, B:555, B:556, B:558, B:560, B:561, B:562, B:564, B:565, B:590, B:598, B:604, B:605, B:606, B:607, B:608, B:609, B:610, B:612

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 475:0.73, 531:0.63, 554:0.68, 555:0.72, 556:0.76, 558:0.55, 560:0.8, 561:0.82, 562:0.62, 564:0.74, 565:0.66, 590:0.77, 598:0.58, 604:0.75, 605:0.78, 606:0.84, 607:0.82, 608:0.88, 609:0.89, 610:0.5, 612:0.7

## C10 — rank 10

The lower donor/acceptor lobe of the EXT1 GT-B GlcA-transferase cleft, narrowed onto the continuous A:187–A:269 aromatic/charged face.

Residues: A:187, A:189, A:191, A:198, A:200, A:201, A:204, A:205, A:234, A:237, A:238, A:239, A:240, A:241, A:242, A:243, A:244, A:245, A:265, A:266, A:269

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 187:0.4, 189:0.78, 191:0.55, 198:0.82, 200:0.42, 201:0.55, 204:0.75, 205:0.7, 234:0.62, 237:0.68, 238:0.66, 239:0.74, 240:0.88, 241:0.82, 242:0.7, 243:0.86, 244:0.88, 245:0.82, 265:0.78, 266:0.72, 269:0.76

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_3a23b5/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2312/case_3a23b5_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2312/case_3a23b5_GJ_rep1`

