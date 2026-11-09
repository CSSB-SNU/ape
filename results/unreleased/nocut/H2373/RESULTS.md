# H2373 — gatherer answer (unscored)

Case `case_0a097a` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-22

Input prediction: `data/staged_casp17_no_native/H2373.pdb`

Input SHA-256: `6de101bc89c71ca02e9619508c2a03a96a523de97b34239d24f30aae6c792209`

Briefing: `data/briefing/casp17_nocutoff/H2373/search_results.json` · SHA-256 `17237e993183a0c45c34a649ddd0e77ee2b537117226e6ee1aee035399333a3c`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C1 | 1 | 0.27 | 20 | side | The broad host-receptor-binding face of the gD Ig-like entry domain... |
| C2 | 2 | 0.24 | 16 | side | A receptor-distal fusion-activation face on gD that joins the... |
| C3 | 3 | 0.22 | 17 | side | A receptor-distal fusion-activation site on gD: an exposed Pro54... |
| C5 | 4 | 0.16 | 12 | side | The mobile N-terminal HVEM-binding hairpin of gD, narrowed to the... |
| C4 | 5 | 0.11 | 11 | side | The flexible C-terminal ectodomain/profusion segment of gD, narrowed... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate had a Tier A line about HAB194, so the distribution remains broad and should be read as a prior over five already-antigenic surfaces. The small ordering came from independent measurements on the supplied molecules: C1/C3 best matched the CDR hydrophobic/aromatic character; C2/C5 offered the clearest opposite-charge capacity; C1 alone approached the reach limit; and C4 alone combined an unmodeled glycan/native-context problem with a strong charge/aromatic mismatch. Same-antigen antibody precedents kept every candidate live and prevented the functional-site literature from being treated as localization.

## C1 — rank 1

The broad host-receptor-binding face of the gD Ig-like entry domain: an upper Tyr38/Gln132/Asp215 lobe joins the Pro221–Phe223 receptor ridge and the solvent-facing alpha3 flank through residue 238.

Residues: C:132, C:137, C:139, C:140, C:215, C:220, C:221, C:222, C:223, C:224, C:226, C:227, C:229, C:230, C:231, C:233, C:235, C:238, C:27, C:38

Advocate: `case_0a097a_GR_rep4` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 27:0.34, 38:0.78, 132:0.28, 137:0.38, 139:0.68, 140:0.66, 215:0.64, 220:0.52, 221:0.84, 222:0.94, 223:0.9, 224:0.3, 226:0.42, 227:0.3, 229:0.38, 230:0.34, 231:0.27, 233:0.31, 235:0.5, 238:0.4
- B → C: 27:0.34, 38:0.78, 132:0.28, 137:0.38, 139:0.68, 140:0.66, 215:0.64, 220:0.52, 221:0.84, 222:0.94, 223:0.9, 224:0.3, 226:0.42, 227:0.3, 229:0.38, 230:0.34, 231:0.27, 233:0.31, 235:0.5, 238:0.4

## C2 — rank 2

A receptor-distal fusion-activation face on gD that joins the Arg64/Arg67 basic rim to the Gly243–Tyr248 proline-rich ridge, with an exposed Arg184–Arg186 shoulder. This is the MC2-like side of the gD-to-gH/gL signalling surface.

Residues: C:184, C:185, C:186, C:237, C:240, C:242, C:243, C:244, C:245, C:246, C:247, C:248, C:249, C:63, C:64, C:67

Advocate: `case_0a097a_GR_rep4` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 63:0.43, 64:0.72, 67:0.93, 184:0.3, 185:0.24, 186:0.31, 237:0.2, 240:0.25, 242:0.09, 243:0.67, 244:0.34, 245:0.79, 246:0.91, 247:0.1, 248:0.82, 249:0.36
- B → C: 63:0.43, 64:0.72, 67:0.93, 184:0.3, 185:0.24, 186:0.31, 237:0.2, 240:0.25, 242:0.09, 243:0.67, 244:0.34, 245:0.79, 246:0.91, 247:0.1, 248:0.82, 249:0.36

## C3 — rank 3

A receptor-distal fusion-activation site on gD: an exposed Pro54 ridge faces the Pro74–Gln80 loop and continues toward the Arg82/Gly83 shoulder. It is an MC5-like gH/gL-activation face, spatially compact despite its split sequence segments.

Residues: C:123, C:51, C:52, C:53, C:54, C:55, C:56, C:72, C:74, C:75, C:76, C:77, C:78, C:79, C:80, C:82, C:83

Advocate: `case_0a097a_GR_rep4` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 51:0.27, 52:0.44, 53:0.36, 54:0.94, 55:0.46, 56:0.4, 72:0.24, 74:0.58, 75:0.57, 76:0.79, 77:0.03, 78:0.61, 79:0.76, 80:0.43, 82:0.33, 83:0.24, 123:0.16
- B → C: 51:0.27, 52:0.44, 53:0.36, 54:0.94, 55:0.46, 56:0.4, 72:0.24, 74:0.58, 75:0.57, 76:0.79, 77:0.03, 78:0.61, 79:0.76, 80:0.43, 82:0.33, 83:0.24, 123:0.16

## C5 — rank 4

The mobile N-terminal HVEM-binding hairpin of gD, narrowed to the exposed linear 10–21 ridge that lies within the receptor-forming N terminus and corresponds to a known group-VII/1D3 neutralizing antigenic site.

Residues: C:10, C:11, C:12, C:13, C:14, C:15, C:16, C:17, C:18, C:19, C:20, C:21

Advocate: `case_0a097a_GR_rep4` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 10:0.26, 11:0.56, 12:0.1, 13:0.75, 14:0.47, 15:0.82, 16:0.9, 17:0.17, 18:0.91, 19:0.79, 20:0.73, 21:0.47
- B → C: 10:0.26, 11:0.56, 12:0.1, 13:0.75, 14:0.47, 15:0.82, 16:0.9, 17:0.17, 18:0.91, 19:0.79, 20:0.73, 21:0.47

## C4 — rank 5

The flexible C-terminal ectodomain/profusion segment of gD, narrowed to the exposed 262–272 linear antigenic region that links the folded receptor-binding core to the membrane-proximal continuation and is displaced during receptor-triggering.

Residues: C:262, C:263, C:264, C:265, C:266, C:267, C:268, C:269, C:270, C:271, C:272

Advocate: `case_0a097a_GR_rep4` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 262:0.3, 263:0.5, 264:0.58, 265:0.7, 266:0.84, 267:0.77, 268:0.86, 269:0.88, 270:0.86, 271:0.6, 272:0.4
- B → C: 262:0.3, 263:0.5, 264:0.58, 265:0.7, 266:0.84, 267:0.77, 268:0.86, 269:0.88, 270:0.86, 271:0.6, 272:0.4

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_0a097a/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2373/case_0a097a_GR_rep4`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2373/case_0a097a_GJ_rep5`

