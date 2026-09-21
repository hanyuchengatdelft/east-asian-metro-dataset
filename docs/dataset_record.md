# Dataset record

This file records the state of the published networks: the reference dates, the totals, every correction applied to the files with its grounds, and the provenance of the corrected values.

## Reference state

Network extent and station sets are those in operation on 24 September 2025. Service statements were admitted only where published on or before 30 September 2025. The dataset repairs that 2025 snapshot and does not refresh it to a later date.

## Totals

| Networks | Stations | Directed in-vehicle links | Ordered station pairs with a direct service |
|---:|---:|---:|---:|
| 62 | 7,419 | 16,286 | 213,984 |

Every network is a single connected component. Before the corrections of 12 September 2026 the 62 networks held 7,480 stations. They held 7,428 after them and hold 7,419 after those of 15 September 2026.

## Corrections of 12 September 2026

Each is a case where the inclusion rule and the recorded data disagreed. In every case the data moved.

| City | Change | Stations | Ground |
|---|---|---|---|
| Daegu | Line 1 truncated at 안심 | 91 → 88 | The 안심~하양 section is a designated 광역철도 of the class 도시철도 연장형 광역철도, which MOLIT lists alongside 하남선, 진접선 and 별내선. Those three were already excluded. This is the fourth member of the same class. |
| Xi'an | 西户线 excluded | 238 → 237 | Fails T1: the service is diesel locomotive-hauled, so it is not an electrically powered railway. It also runs on China National Railway Group infrastructure, dispatched by 中国铁路西安局集团, with the city holding the passenger-service right only, the same ground as the excluded Beijing S2 and Shanghai Jinshan Railway. Removes 户县站. 阿房宫南 is retained as a Line 5 station. |
| Seoul | Line 7 truncated at 온수 | 296 → 285 | The 까치울~석남 section belongs to the Incheon designated urban railway and was held in both the Seoul and Incheon files. It is now held once, by Incheon. City assignment, not eligibility. |
| Guangzhou | 广佛线 divided at the municipal boundary | 309 → 292 | All 25 stations were held by both cities. Guangzhou now holds 西塱–沥滘 (8). |
| Foshan | 广佛线 divided at the municipal boundary | 85 → 77 | Foshan now holds 新城东–菊树 (17). |
| Foshan | 南海有轨电车1号线 excluded under T1 | 77 → 65 | The admission rested on an in-house grade-separation derivation with no external citation. The decisive fact, whether its 2.6 km at-grade section carries level crossings, could not be documented, and the rule resolves an undocumented right of way against admission. |

The ground of the Foshan tram exclusion is the undocumented right of way. The study's own record of the line says the decisive fact could not be documented, and that is the ground, not shared lanes.

Incheon is unchanged at 68 stations and retains the Line 7 section. Guangzhou retains its Line 7 section in Shunde whole, because Foshan holds only the interchange station there, which is the same treatment as the Shanghai line into Kunshan.

## Corrections of 15 September 2026

| City | Change | Stations | Ground |
|---|---|---|---|
| Foshan | The nine-station northern Line 3 section (route 5, 联和 to 佛山大学) removed, 65 to 56 stations, 130 to 114 links | 65 → 56 | Not connected to the rest of the network at the reference date. Only the largest connected component of each network is kept. |
| Foshan | Residual tags of the excluded tram stripped: four P-space pairs served only by the tram (礌岗 to 林岳西 and 林岳东, both directions) removed, two Line 1 pairs re-waited without the tram's 6.2 trains per hour, two L-space links untagged | 56, unchanged | The deletion had left phantom direct pairs between metro stations. No indicator moves. |
| Daegu | 31 P-space pairs into 안심 re-counted from 1.105 to 7.68 or 7.74 trains per hour (27.1 to 3.9 min wait). L-space link 각산 to 안심 timed on 147 trips instead of 21. Link 반야월 to 각산 84 to 105 s (downstream dwell restored) | 88, unchanged | The KTDB 2023 feed cuts 126 of the 148 eastbound Line 1 trips at 각산, one stop short of 안심, with the 각산 row flagged as terminal, so only the 21 trips after 21:09 reached 안심 in the count. Trips are completed to the terminus before counting (`ktdb_rebuild_fix.diff`). The corrected values equal the reverse direction edge for edge. |
| Busan | 42 P-space pairs into 양산 re-counted, +0.53 trains per hour (waits 4.35 to 4.04 and 4.42 to 4.10 min). L-space link 남양산 to 양산 timed on 155 trips instead of 145 | 127, unchanged | Same feed artefact: the last ten Line 2 trips toward 양산 end at 남양산. |

## The urban-scope sample

The register records 30 included routes in 15 cities as metropolitan in scope (`T3_scope`). They stay in the networks and are removed in the urban-scope sensitivity sample, which keeps 58 networks, because Jinhua, Taizhou, Taoyuan and Wenzhou have no urban-scope route.

## Register corrections in `../data/route_register.csv`

- Daegu route 1: 35 → 32 stations, T2 recorded as failing on the 안심~하양 section.
- Xi'an route 17: verdict changed to exclude.
- Seoul route 10: 53 → 42 stations, renamed to the Seoul section 장암–온수.
- Guangzhou route 21: 25 → 8 stations, renamed to the Guangzhou section of the Guangfo Line. The `line_en` field previously read "Zhujiang New Town APM", which was wrong: the row is the Guangfo Line, not a six-station people mover.
- Foshan route 2: 25 → 17 stations, renamed to the Foshan section.
- Foshan route 4: T1 changed to fail, verdict changed to exclude.
- 22 rows relabelled from "steel-wheel suburban / regional express" to "steel-wheel urban express (市域快速轨道系统)". The previous label used a word the paper reserves for an excluded institutional category, for lines that are inside 城市轨道交通. No test or verdict changes.
- Foshan route 5, the northern section of Line 3: noted as not represented in the network files, because it was not connected to the network at the reference date.

The register holds 420 rows, 418 included and 2 excluded.

## Provenance of the corrected values

- The fix to the Korean rebuild script, a function `complete_truncated_termini` that completes each trip to its terminus before pairs are counted, is applied in the companion repository as `code/ktdb_rebuild.py`. A rebuild from the KTDB feed therefore reproduces the Daegu and Busan corrections.
- The 31 Daegu and 42 Busan pairs are tabulated in the companion repository with their old and new values, from the patched rebuild and from a direct count of the feed, which agree.

The files in this repository are these corrected files, published on 15 September 2026.
