# H2343 — gatherer answer (unscored)

Case `case_f1b810` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-01

Input prediction: `data/staged_casp17_no_native/H2343.pdb`

Input SHA-256: `3c70ae6e0bdda9d0a1014d29975873fe008fbe5bd9aebb5949da78b06aeabf11`

Briefing: `data/briefing/casp17_nocutoff/H2343/search_results.json` · SHA-256 `6b66efca006e54eee3aa1b9a3ad4f04da4207f25dccedfbc9f13d1ef0c954955`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C4 | 1 | 0.76 | 17 | side | The conformational antigenic-domain-A patch on the non-neutralizing... |
| C8 | 2 | 0.12 | 10 | side | The glycan-bearing beta7/post-VR3 back-layer lobe of HCV E2 antigenic... |
| C1 | 3 | 0.05 | 10 | side | The glycan-adjacent beta8/C-terminal rim of the HCV E2... |
| C6 | 4 | 0.035 | 14 | side | The glycan-edged exposed rim of the pVR3/domain-A lobe adjacent to... |
| C7 | 5 | 0.012 | 12 | side | The AR3-like hydrophobic cleft on the HCV E2 neutralizing face... |
| C3 | 6 | 0.01 | 15 | side | The HCV E2 front-layer receptor face immediately downstream of AS412... |
| C2 | 7 | 0.008 | 14 | side | A composite rim of the HCV E2 CD81 receptor-binding site where the... |
| C5 | 8 | 0.005 | 12 | side | The flexible N-terminal AS412/epitope-I flap of HCV E2, a conserved... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: Tier A was available: exact-HCDR3 recognition makes CBH-4G's conformational domain-A/non-neutralizing phenotype relevant, separating the back-face candidates from receptor-face candidates. The CBH-4G-specific Y632NS affinity loss transfers exactly to C:225 but supports both overlapping C4 and C8. Candidate-neutral geometry then separated them: C4 is a compact connected patch centered on C:225 (12/17 residues within 10 Å, no internal sequon), whereas C8 is 31.39 Å wide, only 3/10 residues are within 10 Å, and it includes a buried residue and a sequon. Generic accessibility and chemistry did not decide the order.

## C4 — rank 1

The conformational antigenic-domain-A patch on the non-neutralizing HCV E2 back face, centered on the exposed Y632-equivalent aromatic at the C-terminal back-layer beta-strand/loop scaffold.

Residues: C:221, C:223, C:225, C:227, C:228, C:229, C:230, C:232, C:254, C:256, C:258, C:259, C:260, C:274, C:275, C:276, C:278

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 221:0.48, 223:0.62, 225:0.95, 227:0.72, 228:0.78, 229:0.85, 230:0.84, 232:0.9, 254:0.32, 256:0.44, 258:0.66, 259:0.76, 260:0.68, 274:0.46, 275:0.58, 276:0.42, 278:0.62
- B → C: 221:0.48, 223:0.62, 225:0.95, 227:0.72, 228:0.78, 229:0.85, 230:0.84, 232:0.9, 254:0.32, 256:0.44, 258:0.66, 259:0.76, 260:0.68, 274:0.46, 275:0.58, 276:0.42, 278:0.62

## C8 — rank 2

The glycan-bearing beta7/post-VR3 back-layer lobe of HCV E2 antigenic domain A, at the junction between the pVR3 rim and C-terminal non-neutralizing face.

Residues: C:215, C:216, C:217, C:218, C:219, C:220, C:221, C:222, C:223, C:225

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 215:0.46, 216:0.24, 217:0.22, 218:0.66, 219:0.82, 220:0.5, 221:0.86, 222:0.05, 223:0.64, 225:0.76
- B → C: 215:0.46, 216:0.24, 217:0.22, 218:0.66, 219:0.82, 220:0.5, 221:0.86, 222:0.05, 223:0.64, 225:0.76

## C1 — rank 3

The glycan-adjacent beta8/C-terminal rim of the HCV E2 non-neutralizing back face, shifted C-terminally from the canonical domain-A aromatic center.

Residues: C:238, C:240, C:241, C:242, C:243, C:244, C:245, C:246, C:247, C:248

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 238:0.2, 240:0.68, 241:0.86, 242:0.76, 243:0.82, 244:0.88, 245:0.24, 246:0.7, 247:0.74, 248:0.64
- B → C: 238:0.2, 240:0.68, 241:0.86, 242:0.76, 243:0.82, 244:0.88, 245:0.24, 246:0.7, 247:0.74, 248:0.64

## C6 — rank 4

The glycan-edged exposed rim of the pVR3/domain-A lobe adjacent to the buried H77 581–584 folding-determinant segment on the HCV E2 back face.

Residues: C:161, C:164, C:165, C:166, C:167, C:168, C:169, C:170, C:179, C:52, C:55, C:58, C:60, C:62

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 52:0.42, 55:0.48, 58:0.72, 60:0.52, 62:0.54, 161:0.34, 164:0.68, 165:0.72, 166:0.56, 167:0.24, 168:0.76, 169:0.78, 170:0.7, 179:0.44
- B → C: 52:0.42, 55:0.48, 58:0.72, 60:0.52, 62:0.54, 161:0.34, 164:0.68, 165:0.72, 166:0.56, 167:0.24, 168:0.76, 169:0.78, 170:0.7, 179:0.44

## C7 — rank 5

The AR3-like hydrophobic cleft on the HCV E2 neutralizing face, formed where front-layer elements meet the back-layer alpha2 rim and overlap the CD81 receptor-binding surface.

Residues: C:18, C:19, C:20, C:205, C:206, C:208, C:21, C:27, C:28, C:31, C:32, C:33

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 18:0.56, 19:0.24, 20:0.48, 21:0.72, 27:0.58, 28:0.68, 31:0.92, 32:0.94, 33:0.66, 205:0.84, 206:0.62, 208:0.44
- B → C: 18:0.56, 19:0.24, 20:0.48, 21:0.72, 27:0.58, 28:0.68, 31:0.92, 32:0.94, 33:0.66, 205:0.84, 206:0.62, 208:0.44

## C3 — rank 6

The HCV E2 front-layer receptor face immediately downstream of AS412, spanning a glycan-adjacent polar ridge and exposed Phe/Tyr shoulder.

Residues: C:16, C:17, C:18, C:19, C:20, C:21, C:22, C:23, C:24, C:25, C:27, C:28, C:31, C:32, C:33

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 16:0.48, 17:0.38, 18:0.5, 19:0.24, 20:0.58, 21:0.72, 22:0.76, 23:0.82, 24:0.68, 25:0.55, 27:0.52, 28:0.66, 31:0.88, 32:0.9, 33:0.62
- B → C: 16:0.48, 17:0.38, 18:0.5, 19:0.24, 20:0.58, 21:0.72, 22:0.76, 23:0.82, 24:0.68, 25:0.55, 27:0.52, 28:0.66, 31:0.88, 32:0.9, 33:0.62

## C2 — rank 7

A composite rim of the HCV E2 CD81 receptor-binding site where the flexible AS412/epitope-I flap lies against the crown of the sequence-distant CD81-binding loop.

Residues: C:10, C:11, C:112, C:113, C:114, C:115, C:116, C:118, C:120, C:122, C:123, C:124, C:8, C:9

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 8:0.48, 9:0.78, 10:0.72, 11:0.66, 112:0.66, 113:0.7, 114:0.48, 115:0.62, 116:0.58, 118:0.84, 120:0.9, 122:0.78, 123:0.22, 124:0.45
- B → C: 8:0.48, 9:0.78, 10:0.72, 11:0.66, 112:0.66, 113:0.7, 114:0.48, 115:0.62, 116:0.58, 118:0.84, 120:0.9, 122:0.78, 123:0.22, 124:0.45

## C5 — rank 8

The flexible N-terminal AS412/epitope-I flap of HCV E2, a conserved linear receptor-site element that can form a beta-hairpin or extended peptide when antibody-captured.

Residues: C:1, C:10, C:11, C:12, C:2, C:3, C:4, C:5, C:6, C:7, C:8, C:9

Advocate: `case_f1b810_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 1:0.42, 2:0.64, 3:0.68, 4:0.48, 5:0.62, 6:0.26, 7:0.7, 8:0.75, 9:0.95, 10:0.9, 11:0.86, 12:0.2
- B → C: 1:0.42, 2:0.64, 3:0.68, 4:0.48, 5:0.62, 6:0.26, 7:0.7, 8:0.75, 9:0.95, 10:0.9, 11:0.86, 12:0.2

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_f1b810/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2343/case_f1b810_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2343/case_f1b810_GJ_rep1`

