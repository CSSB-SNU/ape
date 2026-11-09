# H2349 — gatherer answer (unscored)

Case `case_e333d6` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-05

Input prediction: `data/staged_casp17_no_native/H2349.pdb`

Input SHA-256: `ed3bcb0b0799f7f8db3a7695ea1da3ddce30d9c2312cdd2e5d844f6e396bdd86`

Briefing: `data/briefing/casp17_nocutoff/H2349/search_results.json` · SHA-256 `b7744ba9eed23f884929670e84213478fdfebc3fc94cf39cec30b7cf355ba753`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C2 | 1 | 0.22 | 20 | side | The compact aromatic hotspot on the D2 half of the cytokine-binding... |
| C1 | 2 | 0.16 | 23 | side | The ligand-facing elbow of the two-domain cytokine-binding homology... |
| C4 | 3 | 0.16 | 14 | side | The narrow apical site-III face of D1: an N-terminal edge opposed to... |
| C3 | 4 | 0.14 | 23 | side | The membrane-distal head of the N-terminal Ig-like D1 domain, where... |
| C5 | 5 | 0.11 | 17 | side | A glycan-free exposed sheet/loop face on membrane-proximal FNIII... |
| C7 | 6 | 0.11 | 24 | side | The broad aromatic crown of D1, extending from Y35/F36/H37 through... |
| C6 | 7 | 0.1 | 18 | side | A nonglycosylated lateral ridge spanning the C-terminal edge of D3... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has a Tier A line about this binder. The unanimous HyHEL-63 identification was false and was removed rather than allowed to concentrate the distribution. What remains is a broad prior over surfaces, modestly separated by one uniform calculation and by other-binder precedent: C2's compact planar aromatic D2 face led; C1 paid for an under-supported D3 rim; C4/C3/C7 divided the probability of one overlapping D1 site-III surface; C5 stayed live because excellent accessibility can matter even without a named function or mapped antibody; C6 paid for glycan proximity and a speculative consequence. Functional-site detail was not allowed to substitute for localization.

## C2 — rank 1

The compact aromatic hotspot on the D2 half of the cytokine-binding homology region, centered on the site-II loops rather than the broader D2-D3 elbow.

Residues: A:117, A:118, A:119, A:141, A:142, A:143, A:144, A:145, A:146, A:147, A:148, A:163, A:164, A:165, A:166, A:167, A:168, A:169, A:170, A:171

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 117:0.45, 118:0.58, 119:0.46, 141:0.3, 142:0.9, 143:0.52, 144:0.66, 145:0.78, 146:0.92, 147:0.84, 148:0.63, 163:0.55, 164:0.42, 165:0.74, 166:0.66, 167:0.76, 168:0.9, 169:0.96, 170:0.72, 171:0.62
- C → A: 117:0.45, 118:0.58, 119:0.46, 141:0.3, 142:0.9, 143:0.52, 144:0.66, 145:0.78, 146:0.92, 147:0.84, 148:0.63, 163:0.55, 164:0.42, 165:0.74, 166:0.66, 167:0.76, 168:0.9, 169:0.96, 170:0.72, 171:0.62

## C1 — rank 2

The ligand-facing elbow of the two-domain cytokine-binding homology region, running from the D2 aromatic/EF-loop platform across the D2-D3 junction onto the proximal D3 rim.

Residues: A:118, A:119, A:141, A:142, A:143, A:145, A:146, A:163, A:165, A:166, A:167, A:168, A:169, A:170, A:171, A:173, A:191, A:196, A:197, A:199, A:228, A:229, A:230

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 118:0.62, 119:0.48, 141:0.32, 142:0.82, 143:0.48, 145:0.67, 146:0.84, 163:0.52, 165:0.78, 166:0.64, 167:0.78, 168:0.89, 169:0.95, 170:0.76, 171:0.72, 173:0.42, 191:0.52, 196:0.68, 197:0.66, 199:0.38, 228:0.56, 229:0.63, 230:0.48
- C → A: 118:0.62, 119:0.48, 141:0.32, 142:0.82, 143:0.48, 145:0.67, 146:0.84, 163:0.52, 165:0.78, 166:0.64, 167:0.78, 168:0.89, 169:0.95, 170:0.76, 171:0.72, 173:0.42, 191:0.52, 196:0.68, 197:0.66, 199:0.38, 228:0.56, 229:0.63, 230:0.48

## C4 — rank 3

The narrow apical site-III face of D1: an N-terminal edge opposed to the Y35/F36/H37 and F86-Q92 loops at the receptor tip.

Residues: A:1, A:2, A:3, A:34, A:35, A:36, A:37, A:86, A:87, A:88, A:89, A:90, A:91, A:92

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 1:0.52, 2:0.65, 3:0.42, 34:0.75, 35:0.94, 36:0.82, 37:0.88, 86:0.95, 87:0.82, 88:0.91, 89:0.85, 90:0.65, 91:0.86, 92:0.68
- C → A: 1:0.52, 2:0.65, 3:0.42, 34:0.75, 35:0.94, 36:0.82, 37:0.88, 86:0.95, 87:0.82, 88:0.91, 89:0.85, 90:0.65, 91:0.86, 92:0.68

## C3 — rank 4

The membrane-distal head of the N-terminal Ig-like D1 domain, where the N-terminal edge and apical loops converge into the site-III cytokine-recruitment platform.

Residues: A:1, A:2, A:29, A:3, A:30, A:31, A:34, A:35, A:36, A:37, A:42, A:5, A:80, A:84, A:86, A:87, A:88, A:89, A:90, A:91, A:92, A:94, A:95

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 1:0.42, 2:0.58, 3:0.45, 5:0.28, 29:0.42, 30:0.48, 31:0.62, 34:0.66, 35:0.92, 36:0.74, 37:0.86, 42:0.6, 80:0.48, 84:0.35, 86:0.92, 87:0.78, 88:0.86, 89:0.76, 90:0.6, 91:0.84, 92:0.72, 94:0.55, 95:0.34
- C → A: 1:0.42, 2:0.58, 3:0.45, 5:0.28, 29:0.42, 30:0.48, 31:0.62, 34:0.66, 35:0.92, 36:0.74, 37:0.86, 42:0.6, 80:0.48, 84:0.35, 86:0.92, 87:0.78, 88:0.86, 89:0.76, 90:0.6, 91:0.84, 92:0.72, 94:0.55, 95:0.34

## C5 — rank 5

A glycan-free exposed sheet/loop face on membrane-proximal FNIII domain D5, beside the D4-D5 activation-coupling bend rather than the distal ligand-binding module.

Residues: A:406, A:407, A:409, A:411, A:412, A:413, A:416, A:420, A:422, A:423, A:452, A:454, A:455, A:456, A:457, A:459, A:461

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 406:0.42, 407:0.46, 409:0.86, 411:0.74, 412:0.55, 413:0.82, 416:0.38, 420:0.48, 422:0.62, 423:0.52, 452:0.45, 454:0.63, 455:0.6, 456:0.74, 457:0.9, 459:0.86, 461:0.62
- C → A: 406:0.42, 407:0.46, 409:0.86, 411:0.74, 412:0.55, 413:0.82, 416:0.38, 420:0.48, 422:0.62, 423:0.52, 452:0.45, 454:0.63, 455:0.6, 456:0.74, 457:0.9, 459:0.86, 461:0.62

## C7 — rank 6

The broad aromatic crown of D1, extending from Y35/F36/H37 through the Y42/H49/F50 shoulder to the F86-Q92 site-III loop.

Residues: A:1, A:2, A:3, A:34, A:35, A:36, A:37, A:4, A:41, A:42, A:49, A:5, A:50, A:51, A:8, A:84, A:86, A:87, A:88, A:89, A:90, A:91, A:92, A:95

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 1:0.32, 2:0.42, 3:0.35, 4:0.28, 5:0.25, 8:0.42, 34:0.55, 35:0.88, 36:0.68, 37:0.82, 41:0.48, 42:0.72, 49:0.7, 50:0.82, 51:0.56, 84:0.35, 86:0.93, 87:0.78, 88:0.86, 89:0.76, 90:0.58, 91:0.82, 92:0.72, 95:0.38
- C → A: 1:0.32, 2:0.42, 3:0.35, 4:0.28, 5:0.25, 8:0.42, 34:0.55, 35:0.88, 36:0.68, 37:0.82, 41:0.48, 42:0.72, 49:0.7, 50:0.82, 51:0.56, 84:0.35, 86:0.93, 87:0.78, 88:0.86, 89:0.76, 90:0.58, 91:0.82, 92:0.72, 95:0.38

## C6 — rank 7

A nonglycosylated lateral ridge spanning the C-terminal edge of D3 and adjoining D4 FNIII face at the D3-D4 hinge, outside canonical site II and site III.

Residues: A:302, A:303, A:305, A:306, A:307, A:330, A:331, A:333, A:334, A:335, A:340, A:341, A:342, A:381, A:383, A:384, A:386, A:388

Advocate: `case_e333d6_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 302:0.45, 303:0.78, 305:0.58, 306:0.84, 307:0.48, 330:0.55, 331:0.6, 333:0.45, 334:0.78, 335:0.9, 340:0.87, 341:0.55, 342:0.58, 381:0.58, 383:0.72, 384:0.62, 386:0.68, 388:0.48
- C → A: 302:0.45, 303:0.78, 305:0.58, 306:0.84, 307:0.48, 330:0.55, 331:0.6, 333:0.45, 334:0.78, 335:0.9, 340:0.87, 341:0.55, 342:0.58, 381:0.58, 383:0.72, 384:0.62, 386:0.68, 388:0.48

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_e333d6/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2349/case_e333d6_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2349/case_e333d6_GJ_rep1`

