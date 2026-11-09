# H2312 — gatherer answer (unscored)

Case `case_3a23b5` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-05-13

Input prediction: `data/staged_casp17_no_native/H2312.pdb`

Input SHA-256: `3ba79066f0aa7015920828a3678d94af5f532471fde42bb38b00795e45f94b8b`

Briefing: `data/briefing/casp17_nocutoff/H2312/search_results.json` · SHA-256 `2b8c71697fd0cc7175a5631c137526c8209032f024f0df47a726889d5e5bdf88`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C1 | 1 | 0.18 | 20 | side | The solvent-open oligosaccharide-acceptor channel of the active... |
| C4 | 2 | 0.16 | 21 | side | The exposed acidic cleft of EXT2's N-terminal pseudo-GT-B domain... |
| C5 | 3 | 0.15 | 27 | side | The outer acceptor-facing rim of active EXT2 GT-A, running from the... |
| C9 | 4 | 0.11 | 24 | side | The substrate-facing aromatic/acidic rim of active EXT1 GT-B... |
| C3 | 5 | 0.09 | 20 | side | A quaternary rim at the junction of the EXT1 N-terminal pseudo-GT-A... |
| C2 | 6 | 0.08 | 18 | side | A mobile, solvent-exposed rim loop on the active EXT1 GT-B cleft... |
| C8 | 7 | 0.07 | 21 | side | The central catalytic throat connecting donor and acceptor subsites... |
| C6 | 8 | 0.06 | 18 | side | A compact membrane-proximal seam between the EXT1 construct N... |
| C7 | 9 | 0.06 | 22 | side | The broad catalytic cleft of active EXT1 GT-B, spanning the A:82/A:84... |
| C10 | 10 | 0.04 | 25 | side | A glycan-bearing quaternary hinge seam where EXT1 A:390–A:397 meets... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had Tier A evidence about 2BAV4, so this remains a broad prior over surfaces rather than a localized call. Uniform calculations compared every footprint with the separately measured 24.10 Å CDR Cα and 28.01 Å side-chain extent, assembly exposure, connectedness, PCA dimensions, exposed charge and aromatics, interchain context, and glycan proximity. C1 separated by the cleanest size, shape, and exposure balance; C4 and C5 by stronger chemistry; C9 by chemistry plus a real glycan constraint. C7/C8 lost on reach or recession, C6 on native-boundary uncertainty, and C10 on the observed glycan. Catalytic function was not allowed to dominate because no evidence says 2BAV4 was selected for inhibition. Overlapping C1/C5/C8 and C7/C9 share functional evidence, so that evidence was not treated as independent localization.

## C1 — rank 1

The solvent-open oligosaccharide-acceptor channel of the active C-terminal GT-A domain of EXT2: the E522/W523 ridge, K588/K590 wall, and H606–E609 rim that cradle the growing heparan-sulfate chain.

Residues: B:519, B:520, B:521, B:522, B:523, B:524, B:587, B:588, B:590, B:598, B:600, B:601, B:602, B:603, B:604, B:605, B:606, B:607, B:608, B:609

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 519:0.36, 520:0.62, 521:0.82, 522:0.94, 523:0.95, 524:0.68, 587:0.66, 588:0.91, 590:0.82, 598:0.35, 600:0.57, 601:0.59, 602:0.78, 603:0.72, 604:0.83, 605:0.69, 606:0.84, 607:0.79, 608:0.61, 609:0.67

## C4 — rank 2

The exposed acidic cleft of EXT2's N-terminal pseudo-GT-B domain, bounded by B:42–B:47, B:68–B:84, and the adjacent B:341/B:345 ridge.

Residues: B:341, B:342, B:345, B:42, B:44, B:45, B:46, B:47, B:68, B:69, B:72, B:75, B:76, B:77, B:78, B:79, B:80, B:81, B:82, B:83, B:84

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 42:0.49, 44:0.66, 45:0.44, 46:0.42, 47:0.48, 68:0.58, 69:0.71, 72:0.72, 75:0.63, 76:0.93, 77:0.58, 78:0.91, 79:0.55, 80:0.84, 81:0.48, 82:0.9, 83:0.77, 84:0.41, 341:0.7, 342:0.38, 345:0.56

## C5 — rank 3

The outer acceptor-facing rim of active EXT2 GT-A, running from the W510/W517/W523 ridge to the B:599–B:612 exit lip.

Residues: B:505, B:506, B:509, B:510, B:511, B:516, B:517, B:518, B:519, B:520, B:521, B:522, B:523, B:524, B:526, B:599, B:600, B:601, B:602, B:603, B:604, B:605, B:606, B:607, B:608, B:609, B:612

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 505:0.35, 506:0.62, 509:0.48, 510:0.81, 511:0.65, 516:0.72, 517:0.87, 518:0.82, 519:0.39, 520:0.66, 521:0.78, 522:0.92, 523:0.91, 524:0.59, 526:0.47, 599:0.4, 600:0.62, 601:0.58, 602:0.83, 603:0.78, 604:0.85, 605:0.72, 606:0.79, 607:0.75, 608:0.6, 609:0.64, 612:0.33

## C9 — rank 4

The substrate-facing aromatic/acidic rim of active EXT1 GT-B, centered on A:209–A:211, A:235–A:250, and A:265–A:269.

Residues: A:189, A:191, A:200, A:209, A:210, A:211, A:235, A:237, A:238, A:239, A:240, A:241, A:242, A:243, A:244, A:245, A:246, A:249, A:250, A:258, A:260, A:265, A:266, A:269

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 189:0.68, 191:0.61, 200:0.48, 209:0.51, 210:0.93, 211:0.78, 235:0.49, 237:0.65, 238:0.77, 239:0.9, 240:0.91, 241:0.84, 242:0.82, 243:0.89, 244:0.88, 245:0.88, 246:0.59, 249:0.38, 250:0.22, 258:0.54, 260:0.55, 265:0.78, 266:0.76, 269:0.57

## C3 — rank 5

A quaternary rim at the junction of the EXT1 N-terminal pseudo-GT-A region and EXT2 N-terminal pseudo-GT-B scaffold, formed by A:26–A:35 facing B:303–B:316.

Residues: A:26, A:27, A:28, A:30, A:31, A:32, A:33, A:34, A:35, B:303, B:304, B:305, B:306, B:308, B:309, B:311, B:312, B:313, B:315, B:316

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 26:0.78, 27:0.7, 28:0.55, 30:0.88, 31:0.82, 32:0.62, 33:0.45, 34:0.42, 35:0.42
- C → B: 303:0.6, 304:0.51, 305:0.9, 306:0.78, 308:0.7, 309:0.86, 311:0.48, 312:0.62, 313:0.52, 315:0.5, 316:0.47

## C2 — rank 6

A mobile, solvent-exposed rim loop on the active EXT1 GT-B cleft, centered on the A:219–A:230 hairpin and adjacent A:189–A:194 ledge.

Residues: A:189, A:191, A:192, A:193, A:194, A:219, A:220, A:221, A:222, A:223, A:224, A:225, A:226, A:227, A:228, A:229, A:230, A:231

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 189:0.46, 191:0.38, 192:0.32, 193:0.49, 194:0.39, 219:0.66, 220:0.63, 221:0.73, 222:0.92, 223:0.9, 224:0.88, 225:0.86, 226:0.88, 227:0.83, 228:0.68, 229:0.6, 230:0.58, 231:0.34

## C8 — rank 7

The central catalytic throat connecting donor and acceptor subsites in active EXT2 GT-A: the D475/D477 wall, R506–W523 throat, E564/D565 floor, and K587–K590 acceptor wall.

Residues: B:456, B:475, B:477, B:505, B:506, B:519, B:520, B:521, B:522, B:523, B:524, B:531, B:562, B:564, B:565, B:587, B:588, B:589, B:590, B:606, B:607

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → B: 456:0.37, 475:0.6, 477:0.43, 505:0.42, 506:0.74, 519:0.36, 520:0.66, 521:0.8, 522:0.95, 523:0.94, 524:0.64, 531:0.42, 562:0.43, 564:0.55, 565:0.43, 587:0.65, 588:0.93, 589:0.35, 590:0.84, 606:0.68, 607:0.64

## C6 — rank 8

A compact membrane-proximal seam between the EXT1 construct N terminus A:1–A:7 and EXT2 around B:199–B:205/B:259–B:262.

Residues: A:1, A:2, A:3, A:4, A:5, A:6, A:7, B:199, B:200, B:201, B:202, B:203, B:204, B:205, B:259, B:260, B:261, B:262

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 1:0.73, 2:0.58, 3:0.92, 4:0.86, 5:0.86, 6:0.8, 7:0.66
- C → B: 199:0.82, 200:0.69, 201:0.84, 202:0.39, 203:0.74, 204:0.86, 205:0.79, 259:0.6, 260:0.52, 261:0.55, 262:0.42

## C7 — rank 9

The broad catalytic cleft of active EXT1 GT-B, spanning the A:82/A:84 and A:119–A:124 donor region, A:187–A:200 wall, and A:239/A:244/A:258–A:269 acceptor rim.

Residues: A:116, A:119, A:120, A:121, A:122, A:123, A:124, A:187, A:189, A:191, A:198, A:200, A:239, A:244, A:258, A:260, A:261, A:265, A:266, A:269, A:82, A:84

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 82:0.37, 84:0.51, 116:0.56, 119:0.46, 120:0.88, 121:0.72, 122:0.82, 123:0.68, 124:0.48, 187:0.58, 189:0.85, 191:0.76, 198:0.91, 200:0.61, 239:0.64, 244:0.63, 258:0.69, 260:0.66, 261:0.62, 265:0.8, 266:0.77, 269:0.68

## C10 — rank 10

A glycan-bearing quaternary hinge seam where EXT1 A:390–A:397 meets EXT2 B:368–B:380 and the B:574 N-glycosylation loop.

Residues: A:390, A:391, A:392, A:393, A:394, A:395, A:396, A:397, B:368, B:369, B:370, B:371, B:372, B:373, B:374, B:375, B:376, B:377, B:378, B:379, B:380, B:574, B:575, B:577, B:578

Advocate: `case_3a23b5_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- C → A: 390:0.77, 391:0.82, 392:0.7, 393:0.86, 394:0.73, 395:0.88, 396:0.54, 397:0.38
- C → B: 368:0.35, 369:0.31, 370:0.56, 371:0.69, 372:0.72, 373:0.78, 374:0.91, 375:0.82, 376:0.8, 377:0.72, 378:0.68, 379:0.42, 380:0.4, 574:0.62, 575:0.53, 577:0.58, 578:0.51

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_3a23b5/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2312/case_3a23b5_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2312/case_3a23b5_GJ_rep1`

