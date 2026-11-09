# H2362 — gatherer answer (unscored)

Case `case_259152` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-12

Input prediction: `data/staged_casp17_no_native/H2362.pdb`

Input SHA-256: `54e187b986e4696f87e1dd7dd4cd6cd943754471a337aa57a0577c6172827a73`

Briefing: `data/briefing/casp17_nocutoff/H2362/search_results.json` · SHA-256 `51b08b3d656ebb7b7f7f0d284f291dc2a93f171a10cc488b650ef2ac8d2249c3`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C8 | 1 | 0.18 | 16 | side | The compact central core of the UL128/UL130 receptor saddle, centered... |
| C2 | 2 | 0.16 | 22 | side | A discontinuous-but-contiguous receptor-facing ridge across the... |
| C6 | 3 | 0.14 | 25 | side | The central site-5 receptor footprint spanning the basic UL128 lobe... |
| C1 | 4 | 0.12 | 24 | side | The membrane-distal cap of the UL128 accessory subunit, including the... |
| C4 | 5 | 0.11 | 16 | side | A narrow exposed crest at the UL128-UL131A junction, centered on the... |
| C5 | 6 | 0.09 | 18 | side | A folded, discontinuous conformational surface on the central... |
| C9 | 7 | 0.07 | 13 | side | The exposed distal gL-gH scaffold junction immediately below the... |
| C7 | 8 | 0.05 | 20 | side | A charged-aromatic crest along the exposed UL130/UL131A seam on the... |
| C3 | 9 | 0.04 | 15 | side | The broad receptor-facing saddle where the distal UL128 flank meets... |
| C10 | 10 | 0.04 | 14 | side | The central lobe of the gL-UL130 junction on the lateral pentamer... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had Tier A evidence about this binder. The distribution is therefore a broad prior over surfaces conditioned on this paratope. A uniform calculation on the unedited footprints compared CDR and patch diameter/PCA extents, charge, hydrophobic/aromatic composition, assembly versus isolated-chain SASA and sequons. Evidential duplication was discounted: C2/C4/C6 overlap on UL128-UL131A, and C3/C8 overlap on UL128-UL130. C8 led on the joint Tier B profile; C3 and C10 fell because their advocates relied on narrower redraws than the inherited candidates.

## C8 — rank 1

The compact central core of the UL128/UL130 receptor saddle, centered on the exposed B-chain C-terminal ledge and the C-chain RYQM face.

Residues: B:103, B:104, B:107, B:108, B:109, B:110, B:17, B:32, C:135, C:139, C:142, C:143, C:144, C:146, C:174, C:175

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 17:0.62, 32:0.72
- F → C: 135:0.8, 143:0.97, 144:0.99, 146:0.95, 174:0.54, 175:0.46
- G → B: 103:0.36, 104:0.86, 107:0.93, 108:0.96, 109:0.82, 110:0.92
- G → C: 135:0.8, 139:0.87, 142:0.82, 143:0.97, 144:0.99, 146:0.95

## C2 — rank 2

A discontinuous-but-contiguous receptor-facing ridge across the UL128/UL131A seam at the pentamer apex, joining the N-terminal UL128 lobe to the exposed UL131A N-terminal ridge.

Residues: B:20, B:21, B:24, B:64, B:65, B:66, B:67, B:68, B:70, B:71, B:77, B:81, B:82, D:10, D:11, D:12, D:13, D:3, D:4, D:5, D:6, D:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 20:0.76, 21:0.42, 24:0.78, 67:0.9
- F → D: 3:0.55, 4:0.63, 5:0.83, 9:0.93, 10:0.72, 13:0.32
- G → B: 20:0.76, 64:0.66, 65:0.56, 66:0.52, 67:0.9, 68:0.67, 70:0.46, 71:0.4, 77:0.29, 81:0.55, 82:0.34
- G → D: 4:0.63, 5:0.83, 6:0.78, 9:0.93, 10:0.72, 11:0.49, 12:0.55

## C6 — rank 3

The central site-5 receptor footprint spanning the basic UL128 lobe and the N-terminal UL131A shelf at the membrane-distal head.

Residues: B:20, B:21, B:22, B:23, B:24, B:65, B:66, B:67, B:68, B:77, B:79, B:80, B:81, B:82, B:83, D:10, D:11, D:12, D:13, D:15, D:5, D:6, D:7, D:8, D:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 65:0.43, 66:0.69, 67:0.77, 68:0.86, 81:0.98
- F → D: 5:0.48, 6:0.88, 7:0.81, 8:0.7, 9:0.96, 10:0.99, 11:0.9, 12:0.97, 13:0.83, 15:0.59
- G → B: 20:0.54, 21:0.82, 22:0.79, 23:0.91, 24:0.96, 77:0.75, 79:0.87, 80:0.83, 81:0.98, 82:0.92, 83:0.84
- G → D: 9:0.96, 10:0.99, 11:0.9, 12:0.97

## C1 — rank 4

The membrane-distal cap of the UL128 accessory subunit, including the NRP2-a2 calcium-loop contact tip.

Residues: B:10, B:11, B:17, B:2, B:20, B:21, B:22, B:23, B:24, B:25, B:3, B:30, B:32, B:33, B:34, B:35, B:39, B:4, B:41, B:5, B:6, B:7, B:8, B:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 2:0.65, 3:0.84, 4:0.62, 5:0.92, 6:0.96, 7:0.96, 8:0.92, 20:0.88, 22:0.75, 23:0.84, 24:0.9, 25:0.76, 35:0.82, 39:0.43, 41:0.52
- G → B: 3:0.84, 5:0.92, 6:0.96, 7:0.96, 8:0.92, 9:0.75, 10:0.86, 11:0.7, 17:0.54, 20:0.88, 21:0.72, 24:0.9, 30:0.87, 32:0.78, 33:0.91, 34:0.66, 35:0.82

## C4 — rank 5

A narrow exposed crest at the UL128-UL131A junction, centered on the mature-chain T94/K27-equivalent ridge rather than on the outer receptor-binding lobe.

Residues: B:60, B:61, B:64, B:65, B:66, B:67, B:68, B:70, B:71, D:10, D:13, D:15, D:3, D:5, D:6, D:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 60:0.55, 61:0.3, 64:0.72, 65:0.54, 66:0.42, 67:0.91, 68:0.56, 70:0.35
- F → D: 5:0.86, 9:0.94, 10:0.68
- G → B: 67:0.91, 68:0.56, 70:0.35, 71:0.32
- G → D: 3:0.48, 5:0.86, 6:0.75, 9:0.94, 10:0.68, 13:0.48, 15:0.18

## C5 — rank 6

A folded, discontinuous conformational surface on the central ectodomain of the gH fusion regulator, where three distant sequence segments meet around the MSL-109 escape patch.

Residues: E:142, E:143, E:145, E:146, E:147, E:148, E:149, E:150, E:386, E:389, E:392, E:393, E:415, E:416, E:419, E:420, E:423, E:427

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → E: 142:0.35, 143:0.57, 145:0.89, 148:0.92, 386:0.34, 389:0.48, 392:0.42, 393:0.29, 415:0.5, 416:0.67, 419:0.75, 420:0.45, 423:0.87
- G → E: 145:0.89, 146:0.61, 147:0.7, 148:0.92, 149:0.51, 150:0.81, 416:0.67, 419:0.75, 423:0.87, 427:0.36

## C9 — rank 7

The exposed distal gL-gH scaffold junction immediately below the pentamer-specific UL head, beside the weakly resolved NRP2-a1 approach.

Residues: A:33, A:34, A:35, A:37, A:40, A:45, A:46, A:47, A:48, E:31, E:32, E:33, E:34

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → A: 35:0.9, 45:0.25, 46:0.6, 47:0.45, 48:0.35
- F → E: 31:0.72, 32:0.58, 33:0.2, 34:0.18
- G → A: 33:0.52, 34:0.63, 35:0.9, 37:0.52, 40:0.78
- G → E: 31:0.72, 32:0.58

## C7 — rank 8

A charged-aromatic crest along the exposed UL130/UL131A seam on the side of the pentamer-specific head, distinct from the glycan-bearing outer UL130 rim.

Residues: C:42, C:47, C:49, C:50, C:51, C:67, C:69, C:70, C:71, C:78, C:80, C:83, C:84, C:87, C:90, C:92, D:49, D:52, D:54, D:57

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → C: 47:0.7, 69:0.87, 70:0.69, 71:0.63, 78:0.45, 80:0.67, 83:0.57, 84:0.52, 87:0.64, 90:0.62, 92:0.48
- F → D: 49:0.36, 52:0.74, 54:0.62, 57:0.43
- G → C: 42:0.42, 47:0.7, 49:0.78, 50:0.55, 51:0.61, 67:0.72, 69:0.87, 70:0.69, 71:0.63, 87:0.64, 90:0.62
- G → D: 52:0.74

## C3 — rank 9

The broad receptor-facing saddle where the distal UL128 flank meets the C-terminal face of UL130, used by THBD and the loosely positioned NRP2-a1 domain.

Residues: B:104, B:107, B:108, B:109, B:110, B:17, B:32, C:135, C:139, C:142, C:143, C:144, C:146, C:174, C:175

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 17:0.65, 32:0.8
- F → C: 135:0.82, 143:0.97, 144:0.98, 146:0.94, 174:0.5, 175:0.46
- G → B: 104:0.88, 107:0.92, 108:0.95, 109:0.8, 110:0.9
- G → C: 135:0.82, 139:0.86, 142:0.82, 143:0.97, 144:0.98, 146:0.94

## C10 — rank 10

The central lobe of the gL-UL130 junction on the lateral pentamer head, corresponding to antigenic site 7 and separated from the principal NRP2/THBD footprints.

Residues: A:126, A:127, C:20, C:21, C:22, C:23, C:24, C:47, C:49, C:50, C:51, C:53, C:67, C:90

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → C: 21:0.92, 22:0.95, 23:0.91, 24:0.85, 49:0.94, 50:0.97, 51:0.88, 53:0.7, 90:0.5
- G → A: 126:0.62, 127:0.6
- G → C: 20:0.72, 21:0.92, 22:0.95, 23:0.91, 24:0.85, 47:0.78, 49:0.94, 50:0.97, 67:0.72

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_259152/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2362/case_259152_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2362/case_259152_GJ_rep1`

