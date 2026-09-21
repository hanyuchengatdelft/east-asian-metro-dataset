# Sources and licences

Every source behind the published files, with what it covers, the licence it carries and whether the
raw form is redistributable. Derived values in this repository are always accompanied by the source
URL and date in the corresponding table.

## Network topology and stations

| Source | Covers | Licence | Raw data published here |
|---|---|---|---|
| Amap subway service (`map.amap.com/service/subway`) | 45 mainland Chinese networks, Hong Kong, Macau | provider terms, no redistribution | no, only the derived networks |
| Ministry of Transport open data platform (TDX), Taiwan | Taipei, Kaohsiung, Taichung, Taoyuan | open government data, attribution | no, the archived responses stay local |
| Operator GTFS feeds, Japan | Tokyo, Yokohama, Kyoto, Sapporo | operator open data, see the Japanese section below | no |
| Operator published timetables, Japan | Sendai, Fukuoka, Kobe | CC BY 4.0 (Sendai), CC BY 2.1 JP (Fukuoka, Kobe) | no, the converted feeds stay local, the derived networks are published |
| Korea Transport Database national GTFS, 2023 release | Seoul, Busan, Daegu, Incheon | KTDB terms | no |
| Vijlbrief et al. 2022, 4TU 10.4121/21316824 | Kobe station set | CC BY | no, cite the deposit |
| CPTOND 2025, Wang et al., Scientific Data 13:188 | cross-check of the Chinese networks | CC BY 4.0 | no, cite the deposit |

## Service attributes

| Source | Covers | Licence | Link |
|---|---|---|---|
| Operator interval notices, published timetables and government relays | Chinese line frequencies | quoted with URL and date under fair citation | the transcriptions, in `data/bands` |
| Amap bus-line interval bands | secondary Chinese frequencies | provider terms | the derived bands only |
| China Association of Metros, annual statistical report 2025 | calibration of 45 mainland networks | association publication, cited | no |

How every frequency is sourced, network by network and route by route, with the URL and date of each statement and the check against the association's minimum peak headway and planned daily runs, is in `frequency_sources.md`, with the per-route table `../data/route_frequency_sources.csv`.
| Public Transportation Open Data Center (公共交通オープンデータセンター) | verification of Tokyo and Yokohama | 公共交通オープンデータ基本ライセンス (Tokyo Metro, Yokohama Municipal, Yurikamome), CC BY 4.0 (Toei) | no raw data, only the aggregated comparison tables in `data/verification` |

Japanese attribution, required when this dataset's Japanese networks or the verification tables are used:

> 本成果物の作成に際して、公共交通オープンデータセンターにおいて提供されるデータ（東京メトロ、横浜市交通局、ゆりかもめ）を利用しました。
> 東京都交通局・公共交通オープンデータ協議会、東京都交通局 列車時刻表・駅時刻表・駅情報、クリエイティブ・コモンズ・ライセンス 表示4.0国際。

The Fukuoka feed was produced with the open-source converter `kuwayamamasayuki/GTFS-FukuokaCitySubway`
(MIT licence) applied to the operator's published Excel timetables.

## Reference date

Every service attribute describes the state of the network on 30 September 2025. Statements published
after that date are kept in the transcriptions for the record, flagged, and not applied.
