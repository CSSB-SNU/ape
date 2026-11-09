# H2373 — gatherer answer (unscored)

Case `case_0a097a` · set `casp17` · retrieval `gated` · CASP entry 2026-06-22

Input prediction: `data/staged_casp17_no_native/H2373.pdb`

Input SHA-256: `6de101bc89c71ca02e9619508c2a03a96a523de97b34239d24f30aae6c792209`

Briefing: `data/briefing/casp17/H2373/search_results.json` · SHA-256 `9f1f099d612174ec79e4f352ae0a0e16059d8647ee3759d325f3d4d1bb941bb6`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C4 | 1 | 0.17 | 16 | side | The composite receptor-binding crown where the N-terminal shoulder... |
| C3 | 2 | 0.16 | 13 | side | The solvent-facing basic arc of the mobile N-terminal extension that... |
| C7 | 3 | 0.14 | 14 | side | A compact conformational epitope joining Tyr38 and the 132/139/140... |
| C2 | 4 | 0.13 | 12 | side | The glycan-free N-to-A-prime interloop on the lateral face of the... |
| C8 | 5 | 0.12 | 16 | side | The two-arm N-terminal HVEM hairpin surface: the C:7-C:15 turn and... |
| C5 | 6 | 0.11 | 12 | side | A nonglycosylated lateral IgV beta-sandwich face formed by the... |
| C1 | 7 | 0.09 | 12 | side | The solvent-exposed end of the C-terminal extension/profusion region... |
| C6 | 8 | 0.08 | 13 | side | The major-neutralizing nectin-binding face centered on the... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had positive Tier-A evidence about this binder; the one binder-specific line only excludes identity with E317. I therefore treated the eight proposals as four surface families, discounted repeated literature within a family, and split family mass using one common calculation on the shipping footprints. C4 narrowly led through combined receptor/antibody precedent and target-paratope chemistry; C3 gained from exposure, compactness and +2 charge; C2 led the lateral family through the exact Nb14 core; C6 lost on footprint coherence. The resulting distribution is intentionally prior-like and diffuse.

## C4 — rank 1

The composite receptor-binding crown where the N-terminal shoulder, IgV core, and folded-back C-terminal extension meet; it contains the nectin-contact ridge and the groove used by the HVEM-binding N terminus.

Residues: C:132, C:134, C:139, C:140, C:214, C:215, C:216, C:218, C:220, C:221, C:222, C:223, C:224, C:35, C:38, C:39

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 38:0.97, 132:0.82, 214:0.43, 215:0.95, 216:0.74, 218:0.55, 220:0.78, 221:0.93, 222:0.99, 223:0.98, 224:0.48
- B → C: 35:0.44, 38:0.97, 39:0.66, 132:0.82, 134:0.43, 139:0.63, 140:0.72, 215:0.95, 221:0.93, 222:0.99

## C3 — rank 2

The solvent-facing basic arc of the mobile N-terminal extension that becomes the HVEM-binding hairpin, centered on C:13-C:24 and continuing onto the C:26-C:29 rim.

Residues: C:13, C:14, C:15, C:16, C:18, C:19, C:20, C:21, C:23, C:24, C:26, C:27, C:29

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 13:0.55, 14:0.46, 15:0.68, 16:0.88, 18:0.94, 19:0.76, 20:0.93, 21:0.82, 24:0.87
- B → C: 15:0.68, 19:0.76, 20:0.93, 21:0.82, 23:0.72, 24:0.87, 26:0.76, 27:0.71, 29:0.56

## C7 — rank 3

A compact conformational epitope joining Tyr38 and the 132/139/140 core flank to the Asp215-Arg222-Phe223 ridge and its 227/231 edge.

Residues: C:132, C:139, C:140, C:215, C:220, C:221, C:222, C:223, C:224, C:227, C:231, C:27, C:38, C:39

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 38:0.97, 132:0.83, 215:0.96, 220:0.8, 221:0.93, 222:0.99, 223:0.98, 224:0.47, 227:0.26, 231:0.21
- B → C: 27:0.48, 38:0.97, 39:0.56, 132:0.83, 139:0.67, 140:0.74, 215:0.96, 221:0.93, 222:0.99

## C2 — rank 4

The glycan-free N-to-A-prime interloop on the lateral face of the IgV-like core, extending across the 47-55 and 102-105 loops: a non-receptor surface implicated in coupling receptor-bound attachment protein to gH/gL.

Residues: C:102, C:103, C:104, C:105, C:47, C:48, C:49, C:50, C:51, C:52, C:54, C:55

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 47:0.82, 48:0.78, 49:0.92, 54:0.78, 55:0.95, 102:0.58, 103:0.73, 104:0.98, 105:0.96
- B → C: 49:0.92, 50:0.72, 51:0.57, 52:0.48, 54:0.78, 55:0.95, 104:0.98

## C8 — rank 5

The two-arm N-terminal HVEM hairpin surface: the C:7-C:15 turn and returning C:23-C:32 segment that form the docking element for a TNF-receptor-family entry receptor.

Residues: C:10, C:11, C:13, C:14, C:15, C:23, C:24, C:26, C:27, C:28, C:29, C:31, C:32, C:7, C:8, C:9

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 7:0.51, 8:0.57, 9:0.46, 10:0.56, 11:0.71, 13:0.75, 14:0.65, 15:0.77, 24:0.89, 27:0.85
- B → C: 11:0.71, 13:0.75, 15:0.77, 23:0.75, 24:0.89, 26:0.89, 27:0.85, 28:0.76, 29:0.81, 31:0.65, 32:0.72

## C5 — rank 6

A nonglycosylated lateral IgV beta-sandwich face formed by the proline-rich C:50-C:57 ridge and neighboring C:72-C:76 and C:178 loops, away from the receptor crown.

Residues: C:178, C:50, C:51, C:52, C:53, C:54, C:55, C:56, C:57, C:72, C:74, C:76

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 53:0.65, 54:0.89, 55:0.91, 56:0.74, 57:0.58, 72:0.47, 74:0.72, 76:0.83
- B → C: 50:0.68, 51:0.57, 52:0.54, 53:0.65, 54:0.89, 55:0.91, 178:0.36

## C1 — rank 7

The solvent-exposed end of the C-terminal extension/profusion region of an alphaherpesvirus gD-like attachment protein: a continuous, membrane-proximal ectodomain tail immediately before the construct tag, rather than the IgV receptor crown.

Residues: C:264, C:265, C:266, C:267, C:268, C:269, C:270, C:271, C:272, C:273, C:274, C:275

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 264:0.28, 265:0.72, 266:0.78, 267:0.74, 268:0.88, 269:0.91, 270:0.87, 271:0.81, 273:0.93
- B → C: 268:0.88, 269:0.91, 270:0.87, 271:0.81, 272:0.54, 273:0.93, 274:0.42, 275:0.25

## C6 — rank 8

The major-neutralizing nectin-binding face centered on the Arg222-Phe223 ridge, where the N-terminal shoulder and C-terminal extension fold against the IgV core.

Residues: C:132, C:214, C:215, C:216, C:217, C:220, C:221, C:222, C:223, C:224, C:27, C:35, C:38

Advocate: `case_0a097a_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 38:0.95, 132:0.77, 215:0.94, 220:0.81, 221:0.94, 222:0.99, 223:0.98, 224:0.51
- B → C: 27:0.45, 35:0.34, 38:0.95, 132:0.77, 214:0.39, 215:0.94, 216:0.74, 217:0.63, 221:0.94, 222:0.99

## Provenance

Packet: `gpt-5.6-high/gather/packets/case_0a097a/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2373/case_0a097a_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/gated/casp17/H2373/case_0a097a_GJ_rep3`

