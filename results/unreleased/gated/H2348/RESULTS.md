# H2348 — gatherer answer (unscored)

Case `case_4ade9a` · set `casp17` · retrieval `gated` · CASP entry 2026-06-05

Input prediction: `data/staged_casp17_no_native/H2348.pdb`

Input SHA-256: `ce3adf48ca6a518ad9b1c0b7ee6fd0899f7d12f01d7aa968c11b92ad459c41e7`

Briefing: `data/briefing/casp17/H2348/search_results.json` · SHA-256 `4d17b3e4689d4bdb8848154699de80e2748b0d365b2fba62f69b2f96cbbee826`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C3 | 1 | 0.2 | 21 | side | The cytokine site-2 face of the D2–D3 cytokine-binding homology... |
| C6 | 2 | 0.15 | 15 | side | A compact glycan-poor outward face of FNIII domain D4 joining... |
| C4 | 3 | 0.14 | 15 | side | The membrane-distal cap of D1: the exposed N terminus and convergent... |
| C1 | 4 | 0.12 | 24 | side | The broad site-3 face of gp130's membrane-distal D1... |
| C5 | 5 | 0.11 | 20 | side | A charged/polar D3 shoulder at the site-IIIb/co-receptor side of the... |
| C2 | 6 | 0.09 | 20 | side | A compact outward non-ligand face on membrane-proximal FNIII domain... |
| C9 | 7 | 0.08 | 20 | side | An elongated exposed D5 face centered on D414-N415-W418 and closed by... |
| C7 | 8 | 0.06 | 16 | side | The convex bend-proximal D4 face centered on the exposed... |
| C8 | 9 | 0.05 | 17 | side | A compact polar shoulder on the noncanonical D3 face, joining... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No pre-cutoff line localizes this binder; the exact-sequence patent identifies gp130 only and is equally true of all nine candidates. The result is therefore a shallow prior over viable surfaces, not a concentrated epitope call. C3 leads because three independent Tier B axes converge: recurrent site-2 function, other-antibody/domain precedent, and measured glycan-clear positive/aromatic complementarity to this paratope. C6 follows on D4 precedent plus compact complementarity. C4 and C1 share D1 mass rather than providing independent confirmation; C4 gets the stronger share because a different Fab has a residue-level map there. Glycan proximity lowers C7 and C8, and lack of a named face function lowers C2, C8, and C9.

## C3 — rank 1

The cytokine site-2 face of the D2–D3 cytokine-binding homology region, centered on A:W142/A:Y168/A:F169 and extending to the D3 rim around A:K228/A:S229.

Residues: A:117, A:118, A:119, A:141, A:142, A:143, A:144, A:145, A:163, A:165, A:167, A:168, A:169, A:170, A:171, A:191, A:196, A:226, A:228, A:229, A:230

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 117:0.64, 118:0.9, 119:0.68, 145:0.75, 163:0.92, 165:0.9, 167:0.66, 168:0.78, 169:0.95, 170:0.72, 171:0.88, 191:0.45, 226:0.67, 228:0.88, 229:0.9, 230:0.57
- C → A: 141:0.53, 142:0.72, 143:0.68, 144:0.88, 145:0.75, 163:0.92, 165:0.9, 167:0.66, 168:0.78, 169:0.95, 196:0.6

## C6 — rank 2

A compact glycan-poor outward face of FNIII domain D4 joining A:330–342 to the spatially adjacent A:381–389 loop around P334/F335/K340 and L383/K386/D388.

Residues: A:330, A:331, A:333, A:334, A:335, A:340, A:341, A:342, A:381, A:383, A:384, A:385, A:386, A:388, A:389

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 334:0.87, 335:0.94, 340:0.92, 341:0.52, 342:0.62, 381:0.65, 383:0.84, 384:0.6, 385:0.44, 386:0.84, 388:0.86
- C → A: 330:0.49, 331:0.6, 333:0.47, 334:0.87, 335:0.94, 340:0.92, 381:0.65, 389:0.47

## C4 — rank 3

The membrane-distal cap of D1: the exposed N terminus and convergent 34–42 and 84–92 loops at the top of the receptor.

Residues: A:1, A:2, A:34, A:35, A:36, A:37, A:42, A:84, A:86, A:87, A:88, A:89, A:90, A:91, A:92

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 34:0.77, 35:0.96, 36:0.64, 37:0.91, 42:0.53, 86:0.92, 87:0.73, 88:0.95, 89:0.92, 90:0.66
- C → A: 1:0.56, 2:0.54, 35:0.96, 37:0.91, 84:0.49, 86:0.92, 87:0.73, 88:0.95, 89:0.92, 91:0.7, 92:0.64

## C1 — rank 4

The broad site-3 face of gp130's membrane-distal D1 immunoglobulin-like domain, formed by the N-terminal edge and exposed loops around the aromatic 34–37 and 84–95 ridges.

Residues: A:12, A:2, A:30, A:31, A:34, A:35, A:36, A:37, A:4, A:42, A:49, A:78, A:8, A:80, A:84, A:86, A:87, A:88, A:89, A:90, A:91, A:92, A:94, A:95

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 31:0.62, 34:0.76, 35:0.95, 36:0.63, 37:0.9, 42:0.55, 49:0.47, 84:0.48, 86:0.91, 87:0.72, 88:0.94, 89:0.91, 90:0.69
- C → A: 2:0.45, 4:0.46, 8:0.55, 12:0.42, 30:0.56, 31:0.62, 35:0.95, 37:0.9, 78:0.43, 80:0.38, 86:0.91, 87:0.72, 88:0.94, 89:0.91, 91:0.71, 92:0.68, 94:0.49, 95:0.44

## C5 — rank 5

A charged/polar D3 shoulder at the site-IIIb/co-receptor side of the cytokine-binding module, centered on E253-D254-S257-T258-R259-S260 and joined to the A:204/A:219/A:223/A:226/A:232 lobe.

Residues: A:204, A:205, A:219, A:221, A:223, A:226, A:232, A:252, A:253, A:254, A:256, A:257, A:258, A:259, A:260, A:261, A:263, A:265, A:278, A:282

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 219:0.61, 232:0.72, 252:0.68, 253:0.92, 254:0.86, 256:0.54, 257:0.8, 258:0.76, 259:0.92, 260:0.84, 278:0.46, 282:0.6
- C → A: 204:0.56, 205:0.24, 219:0.61, 221:0.48, 223:0.64, 226:0.62, 253:0.92, 254:0.86, 257:0.8, 258:0.76, 259:0.92, 260:0.84, 261:0.66, 263:0.6, 265:0.78

## C2 — rank 6

A compact outward non-ligand face on membrane-proximal FNIII domain D5, centered on A:R425/A:E426/A:S427 and closed by the A:454–456 and A:479–486 loops.

Residues: A:402, A:403, A:404, A:406, A:407, A:422, A:423, A:425, A:426, A:427, A:429, A:452, A:454, A:455, A:456, A:479, A:480, A:484, A:485, A:486

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 406:0.7, 407:0.73, 425:0.96, 426:0.86, 427:0.91, 429:0.84, 456:0.72, 480:0.59, 486:0.53
- C → A: 402:0.55, 403:0.61, 404:0.44, 407:0.73, 422:0.58, 423:0.58, 425:0.96, 426:0.86, 427:0.91, 452:0.5, 454:0.65, 455:0.41, 479:0.57, 480:0.59, 484:0.31, 485:0.41

## C9 — rank 7

An elongated exposed D5 face centered on D414-N415-W418 and closed by H456-R457-Y459 and the D5/D6-edge K493 region.

Residues: A:406, A:407, A:409, A:410, A:411, A:412, A:413, A:414, A:415, A:416, A:418, A:420, A:422, A:423, A:455, A:456, A:457, A:459, A:488, A:493

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 406:0.6, 407:0.7, 409:0.77, 410:0.43, 411:0.6, 412:0.68, 413:0.74, 414:0.92, 415:0.94, 416:0.66, 418:0.78, 420:0.7, 456:0.76, 457:0.78, 459:0.87, 493:0.6
- C → A: 411:0.6, 412:0.68, 413:0.74, 414:0.92, 415:0.94, 416:0.66, 418:0.78, 422:0.54, 423:0.57, 455:0.43, 456:0.76, 457:0.78, 459:0.87, 488:0.36

## C7 — rank 8

The convex bend-proximal D4 face centered on the exposed H318-Q320-Y322 cap and extending along A:313–326 and A:363–371 toward the D4–D5 turn.

Residues: A:313, A:314, A:315, A:316, A:318, A:319, A:320, A:321, A:322, A:324, A:326, A:363, A:364, A:366, A:368, A:371

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 318:0.94, 319:0.82, 320:0.96, 321:0.64, 322:0.92, 363:0.43, 364:0.67, 366:0.58, 368:0.18, 371:0.29
- C → A: 313:0.46, 314:0.54, 315:0.58, 316:0.74, 318:0.94, 319:0.82, 320:0.96, 321:0.64, 322:0.92, 324:0.43, 326:0.4

## C8 — rank 9

A compact polar shoulder on the noncanonical D3 face, joining A:209–223 to the spatially adjacent A:259–263 and A:293–296 flank.

Residues: A:205, A:207, A:209, A:210, A:211, A:212, A:213, A:214, A:219, A:221, A:223, A:259, A:260, A:261, A:263, A:293, A:296

Advocate: `case_4ade9a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 209:0.72, 211:0.51, 212:0.92, 213:0.96, 214:0.84, 219:0.86, 259:0.74, 260:0.74, 293:0.94
- C → A: 205:0.23, 207:0.49, 210:0.56, 211:0.51, 212:0.92, 213:0.96, 214:0.84, 219:0.86, 221:0.49, 223:0.64, 260:0.74, 261:0.57, 263:0.6, 293:0.94, 296:0.68

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_4ade9a/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2348/case_4ade9a_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2348/case_4ade9a_GJ_rep1`

