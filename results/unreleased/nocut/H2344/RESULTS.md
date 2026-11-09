# H2344 — gatherer answer (unscored)

Case `case_679778` · set `casp17` · retrieval `no-cutoff` · CASP entry 2026-06-03

Input prediction: `data/staged_casp17_no_native/H2344.pdb`

Input SHA-256: `18733617ed7c4b96b45ff3352f72763afcd6932570e14f1956abaeff946190b8`

Briefing: `data/briefing/casp17_nocutoff/H2344/search_results.json` · SHA-256 `219c979403254eb778aaaf285ed1a338e86cc2322627ca12f3ab91aaa7876e87`

No experimental truth was read; ranking and footprint are the agent's output.

| pocket | rank | confidence | residues | mapping | name |
|---|---:|---:|---:|---|---|
| C3 | 1 | 0.24 | 19 | side | The receptor-opposite MC5-like fusion-activation face of the gD IgV... |
| C1 | 2 | 0.22 | 18 | side | The receptor-distal N–A′ interloop cleft of alphaherpesvirus gD: a... |
| C2 | 3 | 0.17 | 20 | side | The nectin-1-facing rim of the major gD receptor surface: the... |
| C4 | 4 | 0.15 | 10 | side | The compact proline-rich C-terminal-extension shelf immediately... |
| C7 | 5 | 0.09 | 14 | side | The discontinuous MC2-like fusion-activation face on the... |
| C6 | 6 | 0.08 | 14 | side | The full receptor-overlap/α3-groove face of gD: a broad discontinuous... |
| C5 | 7 | 0.05 | 11 | side | The flexible, glycan-adjacent beginning of the gD C-terminal... |

Pocket confidence is the judge's probability over candidates. Residue confidence is conditional on that pocket being the epitope.

Judge: No candidate has a binder-specific localization line: HAB72 identity and phenotype are Tier A in subject but nonlocalizing. The remaining broad distribution is a Tier B prior over surfaces, separated by one uniform calculation on every exact inherited footprint rather than by advocacy detail. C3/C1 best combine exposure, coverability, type-variable anchors and independent neutralizing precedent; C2/C4 remain serious receptor/activation-site alternatives; C7/C6 are weakened by buried, charge-challenged or disconnected exact footprints; C5 is weakened by native glycan/construct-terminal context and a nonneutralizing linear-epitope precedent.

## C3 — rank 1

The receptor-opposite MC5-like fusion-activation face of the gD IgV domain: a two-lobed surface joining the 50–56 N-terminal/core ledge to the 72–80 loop, with an outer shelf at 82–83 and 123–124. It is a post-receptor gH/gL-control site rather than the nectin/HVEM-binding face.

Residues: C:123, C:124, C:50, C:51, C:52, C:53, C:54, C:55, C:56, C:72, C:74, C:75, C:76, C:77, C:78, C:79, C:80, C:82, C:83

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 50:0.55, 51:0.48, 52:0.58, 53:0.72, 54:0.96, 55:0.78, 56:0.62, 72:0.86, 74:0.75, 75:0.91, 76:0.95, 77:0.7, 78:0.93, 79:0.96, 80:0.74, 82:0.58, 83:0.45, 123:0.36, 124:0.29
- B → C: 50:0.55, 51:0.48, 52:0.58, 53:0.72, 54:0.96, 55:0.78, 56:0.62, 72:0.86, 74:0.75, 75:0.91, 76:0.95, 77:0.7, 78:0.93, 79:0.96, 80:0.74, 82:0.58, 83:0.45, 123:0.36, 124:0.29

## C1 — rank 2

The receptor-distal N–A′ interloop cleft of alphaherpesvirus gD: a composite surface where the N-terminal extension (the 40s–50s ledge), an external IgV-core loop around D104/N105, and the returning C-terminal extension around 202–205 meet.

Residues: C:101, C:102, C:103, C:104, C:105, C:202, C:204, C:205, C:45, C:47, C:48, C:49, C:50, C:52, C:53, C:54, C:55, C:56

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 45:0.44, 47:0.88, 48:0.64, 49:0.93, 50:0.73, 52:0.52, 53:0.68, 54:0.8, 55:0.95, 56:0.7, 101:0.43, 102:0.46, 103:0.84, 104:0.97, 105:0.96, 202:0.34, 204:0.55, 205:0.45
- B → C: 45:0.44, 47:0.88, 48:0.64, 49:0.93, 50:0.73, 52:0.52, 53:0.68, 54:0.8, 55:0.95, 56:0.7, 101:0.43, 102:0.46, 103:0.84, 104:0.97, 105:0.96, 202:0.34, 204:0.55, 205:0.45

## C2 — rank 3

The nectin-1-facing rim of the major gD receptor surface: the N-terminal β2 ledge around Y38/P42/S43 opposed to the C-terminal-extension η2/β3 ledge around 211–223 and the mouth of the α3 pocket. It is the MC23/DL11-class receptor-proximal antigenic face.

Residues: C:116, C:211, C:213, C:215, C:216, C:217, C:218, C:220, C:221, C:222, C:223, C:226, C:35, C:36, C:37, C:38, C:39, C:40, C:42, C:43

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 35:0.52, 36:0.76, 37:0.58, 38:0.95, 39:0.74, 40:0.71, 42:0.68, 43:0.57, 116:0.58, 211:0.58, 213:0.72, 215:0.96, 216:0.9, 217:0.74, 218:0.72, 220:0.77, 221:0.84, 222:0.97, 223:0.93, 226:0.54
- B → C: 35:0.52, 36:0.76, 37:0.58, 38:0.95, 39:0.74, 40:0.71, 42:0.68, 43:0.57, 116:0.58, 211:0.58, 213:0.72, 215:0.96, 216:0.9, 217:0.74, 218:0.72, 220:0.77, 221:0.84, 222:0.97, 223:0.93, 226:0.54

## C4 — rank 4

The compact proline-rich C-terminal-extension shelf immediately upstream of the pro-fusion arm, centred on the HSV-2-specific P246 turn. It is a receptor-distal local activation ridge within the mapped MC2 sequence requirement, specifically the 235–247 shelf presented around the P246 turn.

Residues: C:235, C:237, C:238, C:239, C:240, C:242, C:244, C:245, C:246, C:247

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 235:0.57, 237:0.37, 238:0.71, 239:0.65, 240:0.63, 242:0.75, 244:0.83, 245:0.79, 246:0.98, 247:0.74
- B → C: 235:0.57, 237:0.37, 238:0.71, 239:0.65, 240:0.63, 242:0.75, 244:0.83, 245:0.79, 246:0.98, 247:0.74

## C7 — rank 5

The discontinuous MC2-like fusion-activation face on the receptor-opposite side of gD: an upper basic ledge around R64/R67, a core turn around 184–186, and the C-terminal H242–T249/P246 ridge. Together these form the full three-segment conformational surface.

Residues: C:184, C:185, C:186, C:240, C:242, C:243, C:244, C:245, C:246, C:247, C:248, C:249, C:64, C:67

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 64:0.7, 67:0.74, 184:0.5, 185:0.44, 186:0.6, 240:0.6, 242:0.73, 243:0.87, 244:0.84, 245:0.9, 246:0.99, 247:0.75, 248:0.82, 249:0.58
- B → C: 64:0.7, 67:0.74, 184:0.5, 185:0.44, 186:0.6, 240:0.6, 242:0.73, 243:0.87, 244:0.84, 245:0.9, 246:0.99, 247:0.75, 248:0.82, 249:0.58

## C6 — rank 6

The full receptor-overlap/α3-groove face of gD: a broad discontinuous surface spanning the N-terminal R27/Y38 edge, the Ig-core 132–140 wall, and the C-terminal-extension 215–238 wall. This is the full E317/DL11/nectin-overlap face centred on the α3 groove.

Residues: C:132, C:139, C:140, C:215, C:221, C:222, C:223, C:224, C:227, C:231, C:235, C:238, C:27, C:38

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 27:0.58, 38:0.95, 132:0.46, 139:0.74, 140:0.84, 215:0.96, 221:0.86, 222:0.97, 223:0.95, 224:0.57, 227:0.43, 231:0.39, 235:0.74, 238:0.81
- B → C: 27:0.58, 38:0.95, 132:0.46, 139:0.74, 140:0.84, 215:0.96, 221:0.86, 222:0.97, 223:0.95, 224:0.57, 227:0.43, 231:0.39, 235:0.74, 238:0.81

## C5 — rank 7

The flexible, glycan-adjacent beginning of the gD C-terminal pro-fusion/autoinhibitory arm. In native full-length gD this arm continues toward the membrane and folds back over the receptor face; in the supplied C:1–275 construct, 262–275 is artificially terminal and partly disordered. The refined peptide footprint is C:264–274.

Residues: C:264, C:265, C:266, C:267, C:268, C:269, C:270, C:271, C:272, C:273, C:274

Advocate: `case_679778_GR_rep1` · mapping `side`

Antibody `antibody.pdb`:

- A → C: 264:0.48, 265:0.68, 266:0.83, 267:0.88, 268:0.8, 269:0.88, 270:0.6, 271:0.91, 272:0.54, 273:0.74, 274:0.44
- B → C: 264:0.48, 265:0.68, 266:0.83, 267:0.88, 268:0.8, 269:0.88, 270:0.6, 271:0.91, 272:0.54, 273:0.74, 274:0.44

## Provenance

Packet: `gpt-5.6-high/nocut/gather/packets/case_679778/packet`

Organize: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2344/case_679778_GR_rep1`

Judge: `gpt-5.6-high/gather_refine/post_refactor/unreleased_20261029/nocut/casp17/H2344/case_679778_GJ_rep1`

