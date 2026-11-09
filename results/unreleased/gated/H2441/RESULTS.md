# H2441 — gatherer answer (unscored)

Case `case_253bc2` · set `casp17` · retrieval `gated` · CASP entry 2026-07-31

Input prediction: `data/staged_casp17_no_native/H2441.pdb`

Input SHA-256: `37e38c82b5192825be5d1ed9d412076bf5a8fb5ddade49d20c5ae532bead12ae`

Briefing: `data/briefing/casp17/H2441/search_results.json` · SHA-256 `5827c87d5386d58165199f41b0dc2d6859022ecaa626ad84eae73bd0a67053e2`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C7 | 1 | 0.24 | 11 | side | The exposed alpha3-L8-beta8-equivalent lobe—the aromatic/proline-rich... |
| C6 | 2 | 0.19 | 18 | side | The compact catalytic-groove mouth where hydrophobic flapping loop L3... |
| C5 | 3 | 0.16 | 16 | side | A distal mixed hydrophobic/aromatic lobe joining the NDM-specific... |
| C8 | 4 | 0.15 | 20 | side | The broad active-site mouth bridging exposed L3, the H120/L6-side... |
| C1 | 5 | 0.08 | 18 | side | The membrane-side terminal/L10 exterior of the NDM-family fold, where... |
| C2 | 6 | 0.06 | 13 | side | A compact distal polar terrace on the solvent-exposed back of one... |
| C4 | 7 | 0.05 | 16 | side | The broad solvent-exposed back terrace of the metallo-beta-lactamase... |
| C3 | 8 | 0.04 | 14 | side | The C-terminal basic underside, where outer L10, a distal turn and... |
| C9 | 9 | 0.03 | 27 | side | The full active-site slot: complete exposed L3, shallow zinc-side... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has binder-specific localization. The nine drawings collapse into four overlapping face families: C1/C3, C2/C4, C5/C7 and C6/C8/C9. Final ordering used advocacy-footprint exposure, extent and chemistry, followed by independent same-antigen antibody precedent and NDM allosteric function. C7 won narrowly; C6 is the best active-mouth alternative. Literature detail alone did not decide the order.

## C7 — rank 1

The exposed alpha3-L8-beta8-equivalent lobe—the aromatic/proline-rich half of the broader beta8/beta9 region recognized by other anti-NDM antibodies.

Residues: A:139, A:141, A:142, A:143, A:144, A:145, A:146, A:148, A:149, A:151, A:154

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 139:0.42, 141:0.95, 142:0.47, 143:0.89, 144:0.88, 145:0.82, 146:0.51, 148:0.75, 149:0.86, 151:0.48, 154:0.45

## C6 — rank 2

The compact catalytic-groove mouth where hydrophobic flapping loop L3 faces the polar L10 rim above the dinuclear-zinc floor.

Residues: A:184, A:190, A:192, A:193, A:194, A:195, A:196, A:223, A:38, A:40, A:41, A:42, A:43, A:45, A:46, A:95, A:96, A:97

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 38:0.55, 40:0.94, 41:0.86, 42:0.72, 43:0.96, 45:0.7, 46:0.38, 95:0.5, 96:0.88, 97:0.2, 184:0.27, 190:0.54, 192:0.82, 193:0.93, 194:0.78, 195:0.72, 196:0.83, 223:0.48

## C5 — rank 3

A distal mixed hydrophobic/aromatic lobe joining the NDM-specific alpha3-L8-beta8 sector to nearby turns and the C-terminal return.

Residues: A:137, A:138, A:139, A:141, A:143, A:144, A:145, A:148, A:149, A:151, A:154, A:172, A:173, A:174, A:214, A:215

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 137:0.35, 138:0.86, 139:0.72, 141:0.95, 143:0.68, 144:0.9, 145:0.82, 148:0.82, 149:0.66, 151:0.5, 154:0.67, 172:0.77, 173:0.7, 174:0.52, 214:0.75, 215:0.58

## C8 — rank 4

The broad active-site mouth bridging exposed L3, the H120/L6-side flank, and the solvent-facing L10 wall above the zinc centre.

Residues: A:125, A:126, A:192, A:193, A:194, A:195, A:196, A:197, A:223, A:38, A:39, A:40, A:41, A:42, A:43, A:44, A:45, A:46, A:95, A:96

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 38:0.42, 39:0.86, 40:0.9, 41:0.91, 42:0.88, 43:0.96, 44:0.58, 45:0.76, 46:0.42, 95:0.45, 96:0.87, 125:0.78, 126:0.55, 192:0.82, 193:0.93, 194:0.8, 195:0.76, 196:0.86, 197:0.4, 223:0.46

## C1 — rank 5

The membrane-side terminal/L10 exterior of the NDM-family fold, where the folded mature N terminus, solvent-facing outside of substrate loop L10, and C-terminal return converge.

Residues: A:185, A:186, A:187, A:189, A:190, A:225, A:226, A:228, A:230, A:233, A:237, A:241, A:242, A:5, A:6, A:7, A:8, A:9

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 5:0.42, 6:0.48, 7:0.72, 8:0.77, 9:0.4, 185:0.32, 186:0.5, 187:0.84, 189:0.9, 190:0.8, 225:0.35, 226:0.45, 228:0.62, 230:0.68, 233:0.51, 237:0.55, 241:0.7, 242:0.38

## C2 — rank 6

A compact distal polar terrace on the solvent-exposed back of one alpha-beta half of the metallo-beta-lactamase sandwich, opposite the zinc groove.

Residues: A:103, A:106, A:107, A:108, A:109, A:128, A:131, A:67, A:68, A:69, A:72, A:73, A:76

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 67:0.4, 68:0.72, 69:0.92, 72:0.47, 73:0.42, 76:0.78, 103:0.88, 106:0.66, 107:0.78, 108:0.72, 109:0.68, 128:0.38, 131:0.42

## C4 — rank 7

The broad solvent-exposed back terrace of the metallo-beta-lactamase alpha-beta/beta-alpha sandwich, opposite the zinc groove.

Residues: A:103, A:106, A:107, A:108, A:109, A:131, A:132, A:148, A:149, A:69, A:76, A:79, A:80, A:83, A:84, A:85

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 69:0.5, 76:0.55, 79:0.72, 80:0.82, 83:0.84, 84:0.65, 85:0.79, 103:0.61, 106:0.56, 107:0.74, 108:0.7, 109:0.68, 131:0.8, 132:0.78, 148:0.46, 149:0.55

## C3 — rank 8

The C-terminal basic underside, where outer L10, a distal turn and the final beta/coil return form a membrane-side platform.

Residues: A:175, A:186, A:187, A:189, A:217, A:228, A:229, A:230, A:233, A:237, A:240, A:241, A:242, A:243

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 175:0.3, 186:0.35, 187:0.78, 189:0.9, 217:0.42, 228:0.55, 229:0.62, 230:0.66, 233:0.7, 237:0.76, 240:0.57, 241:0.88, 242:0.48, 243:0.67

## C9 — rank 9

The full active-site slot: complete exposed L3, shallow zinc-side floor, L6-side contact and extended L10 substrate-recognition rim.

Residues: A:125, A:184, A:190, A:192, A:193, A:194, A:195, A:196, A:197, A:198, A:199, A:201, A:223, A:37, A:38, A:39, A:40, A:41, A:42, A:43, A:44, A:45, A:46, A:66, A:95, A:96, A:97

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 37:0.38, 38:0.46, 39:0.76, 40:0.91, 41:0.88, 42:0.85, 43:0.95, 44:0.55, 45:0.73, 46:0.4, 66:0.16, 95:0.4, 96:0.84, 97:0.18, 125:0.68, 184:0.28, 190:0.6, 192:0.8, 193:0.94, 194:0.79, 195:0.75, 196:0.86, 197:0.5, 198:0.35, 199:0.31, 201:0.33, 223:0.44

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_253bc2/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2441/case_253bc2_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2441/case_253bc2_GJ_rep1`

