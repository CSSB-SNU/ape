# H2362 — gatherer answer (unscored)

Case `case_259152` · set `casp17` · retrieval `gated` · CASP entry 2026-06-12

Input prediction: `data/staged_casp17_no_native/H2362.pdb`

Input SHA-256: `54e187b986e4696f87e1dd7dd4cd6cd943754471a337aa57a0577c6172827a73`

Briefing: `data/briefing/casp17/H2362/search_results.json` · SHA-256 `b0140a751ca600dc0d1ce7f02d3095b3776329fd300b1010c950088508d8f896`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C5 | 1 | 0.17 | 19 | side | A compact exposed apex jointly formed by UL130 and the C-terminal... |
| C3 | 2 | 0.15 | 23 | side | The broad membrane-distal UL128/UL131A ridge, including the... |
| C6 | 3 | 0.14 | 17 | side | The folded membrane-distal receptor/antigenic face of UL128, where... |
| C2 | 4 | 0.12 | 19 | side | The compact membrane-distal tip of the single UL128 chemokine-like... |
| C10 | 5 | 0.1 | 19 | side | An exposed sequence-discontinuous interdomain groove on gH, formed by... |
| C4 | 6 | 0.08 | 18 | side | The N-terminal outer face of the UL130 chemokine-like domain... |
| C8 | 7 | 0.08 | 17 | side | The broad concave lateral face jointly formed by the N- and... |
| C7 | 8 | 0.07 | 22 | side | The exposed base where the lateral/C-terminal face of UL128 rests... |
| C1 | 9 | 0.06 | 17 | side | The membrane-distal, receptor-proximal quaternary apex where UL128... |
| C9 | 10 | 0.03 | 19 | side | The membrane-proximal C-terminal heel of gH, including... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had Tier A evidence about this binder, so the distribution remains broad. Weak separation came from calculations applied uniformly to all fixed footprints: coverability, assembly exposure and burial, glycan sequons, and exposed-SASA-weighted chemistry against this Fab. C5 led on compact positive/polar complementarity; C3 and C6 combined favorable chemistry with independent HCMV antibody and functional precedent. Over-wide C1/C8 footprints and membrane/charge concerns for C9 moved them down. Published maps of other antibodies were treated only as Tier B precedent.

## C5 — rank 1

A compact exposed apex jointly formed by UL130 and the C-terminal crown of UL131A.

Residues: C:106, C:107, C:108, C:109, C:111, C:112, C:113, D:103, D:107, D:111, D:78, D:80, D:82, D:83, D:84, D:85, D:86, D:87, D:90

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → C: 111:0.75, 112:0.45, 113:0.55
- F → D: 78:0.55, 80:0.7, 82:0.35, 83:0.4, 84:0.94, 85:0.95, 86:0.55, 87:0.5, 90:0.48, 103:0.3, 107:0.22, 111:0.55
- G → C: 106:0.45, 107:0.25, 108:0.78, 109:0.58, 111:0.75, 112:0.45, 113:0.55
- G → D: 80:0.7, 82:0.35, 83:0.4, 84:0.94, 85:0.95

## C3 — rank 2

The broad membrane-distal UL128/UL131A ridge, including the attachment-proximal B:67/D:9 knob and adjacent shallow B:88/D:24 face.

Residues: B:65, B:67, B:68, B:70, B:81, B:83, B:86, B:87, B:88, B:90, B:92, D:10, D:11, D:12, D:13, D:24, D:25, D:3, D:4, D:5, D:6, D:8, D:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 81:0.72, 83:0.18, 86:0.22, 87:0.2, 88:0.68, 90:0.8, 92:0.7
- F → D: 3:0.55, 4:0.3, 5:0.7, 6:0.62, 8:0.18, 9:0.88, 10:0.55, 11:0.25, 12:0.6, 13:0.45, 24:0.78, 25:0.55
- G → B: 65:0.45, 67:0.75, 68:0.35, 70:0.2, 81:0.72, 83:0.18, 86:0.22, 87:0.2, 88:0.68, 90:0.8, 92:0.7
- G → D: 9:0.88, 10:0.55

## C6 — rank 3

The folded membrane-distal receptor/antigenic face of UL128, where discontinuous loops bring the K47/K92 and T94 equivalents together.

Residues: B:15, B:17, B:20, B:21, B:23, B:24, B:25, B:30, B:32, B:60, B:64, B:65, B:67, B:77, B:78, B:81, B:82

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 20:0.9, 21:0.55, 23:0.65, 24:0.8, 60:0.68, 64:0.85, 65:0.75, 67:0.9, 77:0.5, 78:0.45, 81:0.85, 82:0.42
- G → B: 15:0.6, 17:0.5, 20:0.9, 21:0.55, 23:0.65, 24:0.8, 25:0.68, 30:0.85, 32:0.6, 64:0.85, 65:0.75, 67:0.9

## C2 — rank 4

The compact membrane-distal tip of the single UL128 chemokine-like subunit, corresponding to the classical site-1 face.

Residues: B:10, B:11, B:14, B:20, B:21, B:23, B:24, B:25, B:39, B:41, B:42, B:43, B:44, B:45, B:7, B:77, B:78, B:79, B:81

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 20:0.65, 21:0.45, 23:0.7, 24:0.9, 42:0.78, 43:0.5, 44:0.62, 45:0.5, 77:0.4, 78:0.35, 79:0.35, 81:0.72
- G → B: 7:0.5, 10:0.72, 11:0.7, 14:0.55, 20:0.65, 21:0.45, 23:0.7, 24:0.9, 25:0.8, 39:0.38, 41:0.88, 42:0.78, 43:0.5

## C10 — rank 5

An exposed sequence-discontinuous interdomain groove on gH, formed by the E:145-156 loop and an opposing E:379-389/E:415-416 wall.

Residues: E:145, E:147, E:148, E:150, E:151, E:152, E:153, E:154, E:155, E:156, E:158, E:379, E:382, E:383, E:386, E:388, E:389, E:415, E:416

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → E: 150:0.9, 151:0.62, 152:0.7, 153:0.88, 154:0.9, 379:0.55, 382:0.55, 383:0.4, 386:0.85, 388:0.55, 389:0.7, 415:0.45, 416:0.25
- G → E: 145:0.5, 147:0.35, 148:0.72, 150:0.9, 151:0.62, 152:0.7, 153:0.88, 154:0.9, 155:0.9, 156:0.78, 158:0.4, 386:0.85

## C4 — rank 6

The N-terminal outer face of the UL130 chemokine-like domain, centered on its exposed loop/turn cluster.

Residues: C:12, C:13, C:15, C:18, C:19, C:20, C:21, C:22, C:23, C:24, C:25, C:26, C:29, C:50, C:51, C:53, C:56, C:57

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → C: 20:0.85, 21:0.45, 22:0.8, 23:0.9, 24:0.65, 25:0.6, 26:0.6, 29:0.3, 50:0.4, 51:0.45, 53:0.5, 56:0.4, 57:0.45
- G → C: 12:0.4, 13:0.5, 15:0.65, 18:0.8, 19:0.65, 20:0.85, 21:0.45, 22:0.8, 23:0.9, 24:0.65

## C8 — rank 7

The broad concave lateral face jointly formed by the N- and C-terminal lobes of UL128 and the outer face of UL130.

Residues: B:104, B:107, B:108, B:17, B:30, B:32, B:33, C:139, C:142, C:143, C:144, C:145, C:146, C:174, C:175, C:176, C:177

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 104:0.65, 107:0.58, 108:0.88
- F → C: 139:0.45, 142:0.55, 143:0.92, 145:0.28, 174:0.42, 175:0.78, 176:0.3, 177:0.55
- G → B: 17:0.7, 30:0.45, 32:0.78, 33:0.55, 104:0.65, 107:0.58, 108:0.88
- G → C: 142:0.55, 143:0.92, 144:0.9, 146:0.62

## C7 — rank 8

The exposed base where the lateral/C-terminal face of UL128 rests against gL, used by NRP2 a1 and the THBD lectin-like domain.

Residues: A:109, A:113, A:115, A:116, A:117, A:118, B:107, B:108, B:109, B:110, B:111, B:112, B:114, B:115, B:133, B:136, B:138, B:139, B:140, B:141, B:142, B:143

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → A: 109:0.55, 113:0.28, 115:0.35, 116:0.55, 117:0.62, 118:0.35
- F → B: 111:0.7, 112:0.65, 114:0.4
- G → A: 117:0.62
- G → B: 107:0.45, 108:0.65, 109:0.72, 110:0.85, 111:0.7, 112:0.65, 114:0.4, 115:0.48, 133:0.4, 136:0.45, 138:0.85, 139:0.75, 140:0.55, 141:0.5, 142:0.35, 143:0.3

## C1 — rank 9

The membrane-distal, receptor-proximal quaternary apex where UL128 and UL131A meet on the pentamer head.

Residues: B:23, B:24, B:25, B:77, B:78, B:79, B:81, B:82, D:10, D:11, D:12, D:13, D:5, D:6, D:7, D:8, D:9

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → B: 24:0.9, 79:0.45, 81:0.9, 82:0.38
- F → D: 5:0.55, 6:0.78, 7:0.3, 8:0.18, 9:0.88, 10:0.65, 11:0.25, 12:0.58, 13:0.38
- G → B: 23:0.6, 24:0.9, 25:0.68, 77:0.55, 78:0.4, 79:0.45, 81:0.9
- G → D: 6:0.78, 9:0.88

## C9 — rank 10

The membrane-proximal C-terminal heel of gH, including folded-together surfaces represented by full-length gH peptides 677-684 and 705-708.

Residues: E:650, E:651, E:654, E:655, E:657, E:658, E:659, E:660, E:661, E:662, E:665, E:680, E:682, E:683, E:686, E:690, E:691, E:692, E:693

Advocate: `case_259152_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- F → E: 658:0.55, 659:0.65, 660:0.9, 661:0.6, 662:0.82, 665:0.55, 680:0.42, 682:0.32, 683:0.38, 686:0.65, 690:0.55, 691:0.3, 692:0.25, 693:0.45
- G → E: 650:0.35, 651:0.65, 654:0.8, 655:0.7, 657:0.35, 658:0.55, 659:0.65, 660:0.9, 661:0.6, 662:0.82

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_259152/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2362/case_259152_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2362/case_259152_GJ_rep1`

