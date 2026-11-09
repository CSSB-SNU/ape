# H2335 — gatherer answer (unscored)

Case `case_d48c74` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-05-27

Input prediction: `data/staged_casp17_no_native/H2335.pdb`

Input SHA-256: `f216450f2774ea363d9dfeeb1e478d506d906f539f384bf370d4b65ff32c11bb`

Briefing: `data/briefing/casp17_nocutoff/H2335/search_results.json` · SHA-256 `4c6eb598fb307223a9315af31439ba34c45b16345678bd0c3aeed39bcafa9e64`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C1 | 1 | 0.16 | 13 | side | The exposed two-lobed gH heel: the WMPP loop faces a polar/aromatic... |
| C3 | 2 | 0.15 | 18 | side | The exposed gH DII/DIII kink, joining an aromatic/charged lobe near... |
| C6 | 3 | 0.14 | 14 | side | The membrane-proximal C-terminal gH DIV face recognized by 3G16... |
| C5 | 4 | 0.12 | 17 | side | The broader gH DIII/DIV heel hotspot comprising the WMPP loop, an... |
| C7 | 5 | 0.11 | 15 | side | The compact charged DII lobe of the central gH kink: an exposed... |
| C8 | 6 | 0.1 | 14 | side | The membrane-distal gH-gL composite seam: an exposed rim around gH... |
| C9 | 7 | 0.09 | 22 | side | A two-lobed receptor-adjacent gO surface joining an N-terminal lobe... |
| C4 | 8 | 0.08 | 17 | side | A quaternary PDGFR-alpha site-2 rim where the basic gO DI ridge... |
| C2 | 9 | 0.05 | 22 | side | The N-terminal hydrophobic/basic lobe of gO's PDGFR-alpha site-3... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has a Tier A line about this binder. I retained a broad prior and used only modest Tier B separation: antibody precedent, assembly exposure, coverability, glycan/membrane penalties, and duplicate-boundary structure. C1/C5 are one heel class, C3/C7 one central class, and C4/C9 overlap on gO. Query CDR chemistry was broadly compatible with every candidate and was explicitly treated as non-discriminating.

## C1 — rank 1

The exposed two-lobed gH heel: the WMPP loop faces a polar/aromatic lobe around W415-D422 near the DIII/DIV heel, corresponding to the MSL-109 neutralizing surface class.

Residues: B:142, B:144, B:145, B:146, B:147, B:148, B:414, B:415, B:418, B:419, B:422, B:426, B:429

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 144:0.96, 147:0.94, 414:0.78, 415:0.58, 418:0.64, 419:0.42, 422:0.9, 426:0.5, 429:0.54
- E → B: 142:0.72, 144:0.96, 145:0.88, 146:0.66, 147:0.94, 148:0.38, 414:0.78, 422:0.9

## C3 — rank 2

The exposed gH DII/DIII kink, joining an aromatic/charged lobe near B:194-B:222 to an adjacent polar lip near B:259-B:267—the central neutralizing region typified by 13H11.

Residues: B:179, B:194, B:196, B:197, B:198, B:199, B:200, B:201, B:203, B:218, B:220, B:221, B:222, B:259, B:261, B:264, B:265, B:267

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 179:0.38, 196:0.82, 198:0.92, 199:0.86, 201:0.76, 218:0.82, 220:0.94, 221:0.58, 222:0.42, 259:0.38, 261:0.88, 264:0.72, 265:0.86, 267:0.52
- E → B: 194:0.76, 196:0.82, 197:0.68, 198:0.92, 199:0.86, 200:0.9, 201:0.76, 203:0.54, 218:0.82, 220:0.94, 261:0.88, 265:0.86

## C6 — rank 3

The membrane-proximal C-terminal gH DIV face recognized by 3G16, comprising adjacent segments around B:653-B:665 and B:682-B:685.

Residues: B:653, B:654, B:656, B:657, B:658, B:659, B:660, B:661, B:664, B:665, B:682, B:683, B:684, B:685

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 657:0.68, 658:0.7, 659:0.96, 660:0.65, 661:0.94, 664:0.72, 665:0.68, 682:0.4, 683:0.08, 684:0.3, 685:0.9
- E → B: 653:0.65, 654:0.8, 656:0.45, 657:0.68, 658:0.7, 659:0.96, 660:0.65, 661:0.94, 685:0.9

## C5 — rank 4

The broader gH DIII/DIV heel hotspot comprising the WMPP loop, an aromatic shelf at B:385-B:391 and the W415/D422 lobe.

Residues: B:142, B:143, B:144, B:145, B:146, B:147, B:148, B:149, B:385, B:387, B:388, B:391, B:415, B:418, B:419, B:422, B:426

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 144:0.97, 147:0.95, 385:0.62, 387:0.44, 388:0.66, 391:0.34, 415:0.62, 419:0.55, 422:0.92, 426:0.38
- E → B: 142:0.72, 143:0.1, 144:0.97, 145:0.92, 146:0.7, 147:0.95, 148:0.42, 149:0.66, 415:0.62, 418:0.55, 419:0.55, 422:0.92

## C7 — rank 5

The compact charged DII lobe of the central gH kink: an exposed B:194-B:203 hydrophobic/aromatic center bordered by the acidic B:218-B:222 turn.

Residues: B:190, B:194, B:195, B:196, B:197, B:198, B:199, B:200, B:201, B:203, B:218, B:219, B:220, B:221, B:222

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 195:0.12, 196:0.9, 198:0.92, 199:0.86, 201:0.78, 218:0.8, 219:0.06, 220:0.94, 221:0.6, 222:0.38
- E → B: 190:0.42, 194:0.78, 196:0.9, 197:0.7, 198:0.92, 199:0.86, 200:0.92, 201:0.78, 203:0.58, 220:0.94

## C8 — rank 6

The membrane-distal gH-gL composite seam: an exposed rim around gH B:31-B:44 and gL C:22-C:31 surrounding the buried inter-subunit core.

Residues: B:31, B:35, B:38, B:39, B:41, B:42, B:43, B:44, C:22, C:23, C:26, C:27, C:28, C:31

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → B: 35:0.38, 38:0.84, 39:0.2, 41:0.5, 42:0.86, 43:0.82, 44:0.18
- D → C: 22:0.72, 23:0.4, 26:0.92, 27:0.82, 28:0.52, 31:0.68
- E → B: 31:0.72, 35:0.38, 38:0.84
- E → C: 26:0.92, 27:0.82, 28:0.52, 31:0.68

## C9 — rank 7

A two-lobed receptor-adjacent gO surface joining an N-terminal lobe around A:65-A:78 to a DI lobe around A:189-A:219—the local CS2-like anti-gO surface.

Residues: A:189, A:190, A:192, A:193, A:194, A:196, A:200, A:212, A:213, A:214, A:215, A:216, A:217, A:219, A:65, A:66, A:68, A:69, A:70, A:72, A:76, A:78

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → A: 193:0.92, 194:0.12, 196:0.86, 219:0.8
- E → A: 65:0.8, 66:0.58, 68:0.9, 69:0.72, 70:0.78, 72:0.42, 76:0.68, 78:0.2, 189:0.45, 190:0.55, 192:0.58, 193:0.92, 196:0.86, 200:0.44, 212:0.3, 213:0.25, 214:0.96, 215:0.94, 216:0.38, 217:0.18, 219:0.8

## C4 — rank 8

A quaternary PDGFR-alpha site-2 rim where the basic gO DI ridge A:207/A:211/A:214/A:215 lies beside the acidic/hydrophobic gL rim C:67-C:74.

Residues: A:189, A:193, A:207, A:211, A:212, A:213, A:214, A:215, A:216, A:217, A:219, C:67, C:68, C:70, C:72, C:73, C:74

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → A: 212:0.72, 213:0.68, 215:0.94, 216:0.58
- D → C: 67:0.58, 68:0.48, 70:0.84, 72:0.8, 73:0.82, 74:0.35
- E → A: 189:0.25, 193:0.25, 207:0.88, 211:0.92, 212:0.72, 213:0.68, 214:0.96, 215:0.94, 216:0.58, 217:0.18, 219:0.16
- E → C: 68:0.48, 70:0.84

## C2 — rank 9

The N-terminal hydrophobic/basic lobe of gO's PDGFR-alpha site-3 groove, restricted to one Fab-sized part of the receptor surface.

Residues: A:109, A:110, A:114, A:116, A:62, A:63, A:64, A:65, A:66, A:68, A:69, A:70, A:86, A:89, A:90, A:91, A:93, A:94, A:95, A:96, A:98, A:99

Advocate: `case_d48c74_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- D → A: 62:0.62, 63:0.74, 64:0.78, 65:0.66, 66:0.7, 68:0.72, 69:0.55, 70:0.78, 91:0.82, 93:0.8, 96:0.7, 99:0.76, 114:0.38, 116:0.35
- E → A: 63:0.74, 66:0.7, 70:0.78, 86:0.3, 89:0.28, 90:0.55, 91:0.82, 93:0.8, 94:0.73, 95:0.82, 96:0.7, 98:0.72, 99:0.76, 109:0.48, 110:0.5

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_d48c74/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2335/case_d48c74_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2335/case_d48c74_GJ_rep1`

