# Dataset freeze, 12 September 2026

This directory is the frozen dataset for the JTRG major revision. It is produced from `asia/L2`, `asia/P2`, `asia/L2_v2` and `asia/P2_v2` by applying seven corrections, each of which follows from the inclusion rule stated in `Sep report/INCLUSION_ARGUMENT.md`.

**No original file was modified.** The source directories are untouched and this directory is additive.

## Contents

| Path | What it is |
|---|---|
| `L2/`, `P2/` | 62 networks, v1 lineage, corrections applied |
| `L2_v2/`, `P2_v2/` | 62 networks, v2 lineage, corrections applied |
| `inclusion_table_frozen.csv` | 420 rows, the register of record with the corrections stamped |
| `indicator_impact_v1.json` | Recomputed indicators for the changed cities, before and after |

## The seven corrections

Each is a case where the stated rule and the recorded data disagreed. In every case the data moved.

| # | City | Change | Stations | Ground |
|---|---|---|---|---|
| 1 | Daegu | Line 1 truncated at 안심 | 91 → 88 | The 안심~하양 section is a designated 광역철도 of the class 도시철도 연장형 광역철도, which MOLIT lists alongside 하남선, 진접선 and 별내선. Those three were already excluded. This is the fourth member of the same class. |
| 2 | Xi'an | 西户线 excluded | 238 → 237 | Runs on China National Railway Group infrastructure, dispatched by 中国铁路西安局集团, with the city holding the passenger-service right only. Same ground as the already excluded Beijing S2 and Shanghai Jinshan Railway. Removes 户县站. 阿房宫南 is retained as a Line 5 station. |
| 3 | Seoul | Line 7 truncated at 온수 | 296 → 285 | The 까치울~석남 section belongs to the Incheon designated urban railway and was held in both the Seoul and Incheon files. It is now held once, by Incheon. City assignment, not eligibility. |
| 4 | Guangzhou | 广佛线 divided at the municipal boundary | 309 → 292 | All 25 stations were held by both cities. Guangzhou now holds 西塱–沥滘 (8). |
| 5 | Foshan | 广佛线 divided at the municipal boundary | 64 → 56 | Foshan now holds 新城东–菊树 (17). |
| 6 | Foshan v2 | 南海有轨电车1号线 excluded under T1 | further −12 | The v2 admission rested on an in-house grade-separation derivation with no external citation. The decisive fact, whether its 2.6 km at-grade section carries level crossings, could not be documented, and the rule resolves an undocumented right of way against admission. |
| 7 | Beijing v1 | 西郊线 and 亦庄T1有轨电车 removed | 417 → 401 | Added after the China adversarial pass. Both are 有轨电车 with at-grade road crossings, both fail T1, and the register already omitted them. The v2 file was already correct at 399. The v1 file was carrying 16 stations that the inventory of record does not list, and the paper's reported column is the v1 one. |

Correction 6 is recorded on the ground the evidence supports. Do not write that the Foshan line was removed for shared lanes: the study's own record of that line says the decisive fact is undocumented, which is itself the ground.

Incheon is unchanged at 68 stations and retains the Line 7 section. Guangzhou retains its Line 7 section in Shunde whole, because Foshan holds only the interchange station there, which is the same treatment as the Shanghai line into Kunshan.

## Station totals

| Lineage | Before | After | Removed |
|---|---:|---:|---:|
| v1 (`asia/L2`) | 7,456 | **7,400** | 56 |
| v2 (`asia/L2_v2`) | 7,480 | **7,428** | 52 |

All four figures are computed by summing the node counts of the 62 files in each directory. The v1 and v2 removals differ by four because the v2 Beijing file already had the two trams removed, so correction 7 costs v1 sixteen stations and v2 none, while the Foshan tram of correction 6 exists only in v2 and costs it twelve.

**Note for anyone quoting the earlier figure.** The number 7,480 that appears in `INCLUSION_RULE_v3.md` and in the steel-wheel counterfactual is the **v2** total, not the v1 total. The v1 lineage, which is the one the submitted Table 1 reports, has always been 7,456.

Two networks are not single connected components. **Hefei is 165 and 7 in the v1 lineage**, which is the lineage Table 1 reports, so its time diameter is fitted on 165 of its 172 stations. The seven-station component sits on a graph route that has no row in the register, which is the same defect class as correction 7 and is **not yet remediated**. **Foshan v2 is 56 and 9** after correction 6, having been 76 and 9 before it, the nine being the northern Line 3 section that is not yet physically joined. Neither condition was created by these corrections, and both need a stated treatment for disconnected networks.

## Indicator impact, v1 lineage

Recomputed with the Table 1 method: generalised travel time with a 5-minute transfer penalty and a wait weight of 2, the 1-minute budget grid, and the constrained logistic of equation 2.

| City | n | t_M | γ | θ | R² | d₃₀ | τ₅₀ |
|---|---:|---:|---:|---:|---:|---:|---:|
| Daegu before | 91 | 77 | 8.57 | 0.467 | 0.9977 | 0.323 | 0.469 |
| **Daegu after** | **88** | **65** | **7.13** | **0.549** | **0.9969** | **0.337** | **0.544** |
| Foshan before | 64 | 114 | 7.36 | 0.385 | 0.9992 | 0.254 | 0.397 |
| **Foshan after** | **56** | **93** | **6.67** | **0.439** | **0.9990** | **0.288** | **0.447** |
| Guangzhou before | 309 | 183 | 9.55 | 0.336 | 0.9988 | 0.105 | 0.343 |
| **Guangzhou after** | **292** | **183** | **9.83** | **0.324** | **0.9987** | **0.113** | **0.332** |
| Seoul before | 296 | 103 | 10.64 | 0.412 | 0.9996 | 0.205 | 0.414 |
| **Seoul after** | **285** | **97** | **10.57** | **0.426** | **0.9996** | **0.217** | **0.427** |
| Xi'an before | 238 | 270 | 15.94 | 0.200 | 0.9988 | 0.137 | 0.205 |
| **Xi'an after** | **237** | **152** | **9.14** | **0.354** | **0.9985** | **0.138** | **0.361** |
| Beijing before | 417 | 239 | 12.37 | 0.348 | 0.9989 | 0.028 | 0.350 |
| **Beijing after** | **401** | **239** | **13.08** | **0.338** | **0.9985** | **0.030** | **0.340** |

The sigmoid still fits everywhere, with R² at or above 0.9969 in all six.

### Xi'an, which needs its own paragraph in the manuscript

Excluding a single station removes 118 minutes from Xi'an's time diameter, and moves it from rank 1 of 62 to the middle of the distribution. γ falls from 15.94 to 9.14 and θ rises from 0.200 to 0.354.

The cause is that 西户线 is a national-railway commuter service with a headway of roughly two hours sitting inside a metro graph. Its waiting time dominated every path that reached it, and Xi'an's rank-1 time diameter was an artefact of that one line.

This matters beyond Xi'an, because the submitted conclusion names Xi'an among the cluster C3 cities that drive "especially large EA time diameters", and Figure `fig:regions-pc1-vs-logN` uses Xi'an as the PC1 extreme supporting the claim that very high PC1 values are seen only in that cluster. **Xi'an must come out of that sentence.** The cluster claim itself survives with Dalian and Qingdao in the lead.

The independent v2 frequency rebuild moved Xi'an the same way, from 269.8 to 163.6 minutes, for the same underlying reason. Two different corrections, arrived at independently, agree that the published Xi'an figure was an artefact. The inclusion rule is the better ground on which to report it, because it is a boundary decision rather than a data repair.

## The urban-scope sample, recomputed on the frozen files

The scope sensitivity must be restated, because one of its routes is now excluded outright.

| | Before the freeze | On the frozen files |
|---|---:|---:|
| Metropolitan-scope routes in the sample | 31 | **30** |
| of which mainland Chinese | 30 | **29** |
| Cities carrying at least one | 15 | **15** |
| Stations removed, net of interchanges | 354 | **350** |
| v1 sample after removal | | 7,400 → **7,050** |
| Networks in the urban-scope sample | 58 | **58** |

Xi'an 西户线 was a metropolitan-scope route and is now excluded under T1, so it leaves the Tier B count rather than the sensitivity sample. The four cities that empty entirely are unchanged: Jinhua, Taizhou, Taoyuan and Wenzhou.

## Register corrections in `inclusion_table_frozen.csv`

- Daegu route 1: 35 → 32 stations, T2 recorded as failing on the 안심~하양 section.
- Xi'an route 17: verdict changed to exclude.
- Seoul route 10: 53 → 42 stations, renamed to the Seoul section 장암–온수.
- Guangzhou route 21: 25 → 8 stations, renamed to the Guangzhou section of the Guangfo Line. **The `line_en` field previously read "Zhujiang New Town APM", which was wrong: the row is the 25-station Guangfo Line, not a six-station people mover.**
- Foshan route 2: 25 → 17 stations, renamed to the Foshan section.
- Foshan route 4: T1 changed to fail, verdict changed to exclude.
- Beijing: the register already omitted the two tram routes, so no row changes. The graph was brought into line with the register rather than the reverse.
- 22 rows relabelled from "steel-wheel suburban / regional express" to "steel-wheel urban express (市域快速轨道系统)". The previous label used the word that the paper reserves for an excluded institutional category, for lines that are inside 城市轨道交通. No test or verdict changes.

The register holds 420 rows, 418 included and 2 excluded.

## What still has to happen before submission

1. **Recompute Table 1 in full on the frozen files.** Only the six changed cities were recomputed here. The other 56 are unchanged by construction, but the table, the regional summary and the PC1 figure must be regenerated from this directory.
2. **Rewrite the Xi'an sentence** in the conclusion and the PC1 discussion.
3. **`main.tex` lines 276 to 284 still print the pre-rule scope paragraph**, including the phrase Reviewer 2 quoted, and the inclusion appendix is not `\input` into the manuscript. Until that is fixed none of this is visible to a reviewer.
4. **The 22 relabelled rows have five empty operator fields** (Jinhua twice, Taizhou S1, Wenzhou S1 and S2). Do not claim in the manuscript that all 22 are metro-company operated until those are filled.
5. **Foshan v2 disconnection** needs a stated treatment.
6. **Korean designations** for Jinjeop, Hanam, Byeollae, Daegu Line 1 and the Busan-Gimhae control case still rest on secondary sources. The MOLIT metropolitan transport commission pages list all four and are retrievable with a cookie jar.
7. **The China adversarial pass has now run.** It found one freeze-blocking row, Beijing, which has been re-cut as correction 7 above. Two further items are open and are recorded in `OPEN_DECISIONS.md`: Changchun Line 3, and the wording of the Chinese T2 instrument.
8. **Ship this directory's `inclusion_table_frozen.csv` as the inventory of record.** `inclusion_v3/inclusion_table_v3.csv` predates the corrections and still shows Daegu Line 1 at 35 stations, Seoul Line 7 untruncated, Foshan route 4 as include and Xi'an 西户线 as include. It must not travel as supplementary material.
9. Frozen v2 Foshan retains a route id 4 tag on one surviving link, a residue of the tram deletion. No indicator moves, but a replicator recounting route ids finds five where the register lists four. Strip or note it.

## Addendum, 14 September 2026: metadata stamp and publication

Every one of the 248 network files (four trees of 62) received a `graph.freeze` block on 14 September 2026, giving its frozen node and link counts, its lineage and space, whether a correction touched it, and if so which. Nodes and links were not modified. The block was added because the `v2_totals` field inherited from the 10 September build still reported the pre-freeze node count in the five corrected version 2 files (Daegu 91, Foshan 85, Guangzhou 309, Seoul 296, Xi'an 238), which a reader of the raw file would take for the current count. Files were re-serialised in the same compact form. The state before the stamp is archived at `August - revision/data/freeze_backups/dataset_frozen_2026-09-12_before_metadata_2026-09-14.zip`.

`README.md` was added the same day. This directory is published verbatim as `data/frozen_2026-09-12/` of the dataset repository by `dataset_v2/make_repo.py`.
