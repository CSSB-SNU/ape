# H2441 — gatherer answer (unscored)

Case `case_253bc2` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-07-31

Input prediction: `data/staged_casp17_no_native/H2441.pdb`

Input SHA-256: `37e38c82b5192825be5d1ed9d412076bf5a8fb5ddade49d20c5ae532bead12ae`

Briefing: `data/briefing/casp17_nocutoff/H2441/search_results.json` · SHA-256 `e71284ba0254f948a2858cd5ce7a2bef005f866757a5fc232612ccdafa9f26ca`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C8 | 1 | 0.31 | 16 | side | The L6/end-alpha2-equivalent allosteric cleft, formed by two exposed... |
| C5 | 2 | 0.15 | 19 | side | The exposed L3/L10 substrate-groove rim and accessible zinc-site edge |
| C9 | 3 | 0.11 | 21 | side | The mouth of the catalytic groove, spanning exposed hydrophobic L3 to... |
| C4 | 4 | 0.1 | 16 | side | The outer face of mobile L10 and its L9-side buttress |
| C6 | 5 | 0.07 | 22 | side | The L3-ceiling-to-L10 catalytic cleft, including the fold-back... |
| C7 | 6 | 0.07 | 16 | side | The outer L10/C-terminal buttress face outside the metal groove |
| C2 | 7 | 0.07 | 16 | side | A distal helix/loop face centered on the exposed A:120-A:135 scaffold... |
| C1 | 8 | 0.06 | 19 | side | The solvent-exposed C-terminal scaffold seam on the back of the B1... |
| C3 | 9 | 0.06 | 15 | side | The exposed N-terminal cap of the soluble construct on the native... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has Tier A localization. C8 gained a modest lead from the only surface-specific homologous antibody precedent, discounted to 52.9% full-segment and 66.7% determinant identity. C5/C6/C9 collectively retained comparable mass because they best match Nb17's hydrophobic H3, but their mass was split because they are overlapping drawings and they conflict to varying degrees with uncompetitive kinetics. L10 function kept C4/C7 live; exposure alone could not elevate C1/C2/C3.

## C8 — rank 1

The L6/end-alpha2-equivalent allosteric cleft, formed by two exposed hydrophobic strips and a polar rim.

Residues: A:103, A:104, A:106, A:107, A:108, A:109, A:76, A:79, A:80, A:81, A:82, A:83, A:84, A:85, A:86, A:87

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 76:0.55, 79:0.72, 80:0.7, 81:0.62, 82:0.35, 83:0.78, 84:0.86, 85:0.92, 86:0.78, 87:0.88, 103:0.72, 104:0.4, 106:0.74, 107:0.96, 108:0.9, 109:0.92

## C5 — rank 2

The exposed L3/L10 substrate-groove rim and accessible zinc-site edge.

Residues: A:190, A:192, A:193, A:194, A:195, A:196, A:223, A:224, A:38, A:39, A:40, A:41, A:42, A:43, A:44, A:45, A:46, A:95, A:96

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 38:0.55, 39:0.75, 40:0.87, 41:0.82, 42:0.72, 43:0.96, 44:0.68, 45:0.65, 46:0.5, 95:0.42, 96:0.78, 190:0.62, 192:0.72, 193:0.9, 194:0.82, 195:0.78, 196:0.88, 223:0.45, 224:0.32

## C9 — rank 3

The mouth of the catalytic groove, spanning exposed hydrophobic L3 to proximal polar L10 while excluding buried zinc ligands.

Residues: A:184, A:190, A:192, A:193, A:194, A:195, A:196, A:223, A:37, A:38, A:39, A:40, A:41, A:42, A:43, A:44, A:45, A:46, A:67, A:95, A:96

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 37:0.78, 38:0.8, 39:0.82, 40:0.92, 41:0.85, 42:0.75, 43:0.97, 44:0.7, 45:0.72, 46:0.8, 67:0.4, 95:0.45, 96:0.8, 184:0.38, 190:0.7, 192:0.78, 193:0.92, 194:0.84, 195:0.82, 196:0.9, 223:0.48

## C4 — rank 4

The outer face of mobile L10 and its L9-side buttress.

Residues: A:157, A:158, A:160, A:164, A:193, A:194, A:195, A:196, A:197, A:198, A:199, A:200, A:201, A:204, A:207, A:208

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 157:0.52, 158:0.25, 160:0.58, 164:0.68, 193:0.65, 194:0.74, 195:0.82, 196:0.88, 197:0.68, 198:0.78, 199:0.8, 200:0.92, 201:0.86, 204:0.65, 207:0.55, 208:0.38

## C6 — rank 5

The L3-ceiling-to-L10 catalytic cleft, including the fold-back N-terminal ledge and accessible zinc-pocket rim.

Residues: A:184, A:190, A:192, A:193, A:194, A:195, A:196, A:223, A:37, A:38, A:39, A:40, A:41, A:42, A:43, A:44, A:45, A:46, A:7, A:8, A:95, A:96

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 7:0.5, 8:0.62, 37:0.65, 38:0.72, 39:0.78, 40:0.9, 41:0.88, 42:0.8, 43:0.97, 44:0.7, 45:0.72, 46:0.78, 95:0.52, 96:0.82, 184:0.45, 190:0.7, 192:0.76, 193:0.92, 194:0.86, 195:0.81, 196:0.9, 223:0.5

## C7 — rank 6

The outer L10/C-terminal buttress face outside the metal groove.

Residues: A:187, A:189, A:190, A:192, A:193, A:194, A:195, A:196, A:198, A:199, A:200, A:201, A:240, A:241, A:242, A:243

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 187:0.55, 189:0.88, 190:0.78, 192:0.75, 193:0.85, 194:0.72, 195:0.82, 196:0.84, 198:0.62, 199:0.76, 200:0.92, 201:0.86, 240:0.55, 241:0.83, 242:0.68, 243:0.6

## C2 — rank 7

A distal helix/loop face centered on the exposed A:120-A:135 scaffold segment.

Residues: A:116, A:117, A:119, A:120, A:121, A:123, A:124, A:125, A:126, A:127, A:128, A:129, A:131, A:132, A:133, A:135

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 116:0.35, 117:0.42, 119:0.28, 120:0.75, 121:0.48, 123:0.85, 124:0.9, 125:0.78, 126:0.82, 127:0.55, 128:0.8, 129:0.72, 131:0.88, 132:0.78, 133:0.74, 135:0.42

## C1 — rank 8

The solvent-exposed C-terminal scaffold seam on the back of the B1 metallo-beta-lactamase fold: a basic/mixed ridge linking the post-L10 scaffold to the terminal helix, behind rather than inside the dinuclear catalytic groove.

Residues: A:185, A:186, A:187, A:204, A:207, A:208, A:211, A:214, A:215, A:217, A:218, A:226, A:227, A:228, A:229, A:230, A:233, A:234, A:237

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 185:0.45, 186:0.58, 187:0.72, 204:0.55, 207:0.82, 208:0.58, 211:0.86, 214:0.9, 215:0.62, 217:0.78, 218:0.64, 226:0.48, 227:0.5, 228:0.76, 229:0.88, 230:0.82, 233:0.84, 234:0.38, 237:0.62

## C3 — rank 9

The exposed N-terminal cap of the soluble construct on the native membrane-anchor side.

Residues: A:10, A:11, A:12, A:13, A:14, A:15, A:16, A:18, A:3, A:4, A:5, A:6, A:7, A:8, A:9

Advocate: `case_253bc2_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- B → A: 3:0.45, 4:0.52, 5:0.7, 6:0.62, 7:0.78, 8:0.72, 9:0.8, 10:0.6, 11:0.82, 12:0.9, 13:0.85, 14:0.75, 15:0.68, 16:0.4, 18:0.35

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_253bc2/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2441/case_253bc2_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2441/case_253bc2_GJ_rep1`

