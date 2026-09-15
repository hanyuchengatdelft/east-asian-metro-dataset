# Frequency and headway sources, network by network

Generated 2026-09-15 by `dataset_v2/make_frequency_sources.py` from the transcribed statements in `dataset_v2/headways/bands/`, the converter reports in `dataset_v2/build/headways_by_segment/`, the route register `supplementary_line_inventory_v2.csv` and the P files of the published dataset of 15 September 2026. The companion table `frequency_sources_by_route.csv` carries, for every route, every band id, URL and date behind its frequency. Nothing in this file is typed by hand: rerun the script after any change to the band files or the converter output.

## 1. How to read this file

Every direct-service pair in the P files carries a `wait_source` label, and every route in the register carries the same label as `headway_source`. The labels mean:

| Label | Meaning |
|---|---|
| `published_interval_band_line` | operator statement, interval bands for the whole line |
| `published_interval_band_section` | operator statement, interval bands per section |
| `published_peak_offpeak_only` | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant |
| `published_average_interval` | operator statement, one average interval |
| `operator_timetable_departures` | departures counted hour by hour on the operator's station timetables |
| `press_quoted_operator_notice` | press or government relay quoting the operator's notice |
| `amap_interval_band` | Amap interval bands (undated, passed the acceptance test) |
| `inherited_from_trunk` | inherited from the trunk route of the same line |
| `transcription_2025_unsourced` | 2025 constant, no source |
| `gtfs_weekday_trips` | weekday trips counted in the GTFS feed |
| `tdx_frequency_bands` | TDX Frequency endpoint bands |
| `v1_value_kept_feed_incomplete` | 2025 value kept, route incomplete in the feed |

For the mainland networks the rules are (a) precedence: the operator's own interval table or timetable, then an operator notice, then a government portal or press article relaying the operator's notice and labelled as such, then Amap interval bands if they pass a five-part acceptance test; (b) admissibility: the newest weekday statement dated on or before 2025-09-30, later notices archived unless they state the value in force before their change, departure counts made after that date admitted at the lowest rank; (c) coverage: minutes of the service day not covered by a published band take the 2025 constant only if it lies between the published peak headway and twice that value, else the longest published off-peak, and the `constant fill` column gives the share of the window filled this way; (d) a published 最小行车间隔 is a minimum, applied to a 60-minute peak core and never read as an all-day mean. The all-day trains per hour of a route is the sum over the 05:00 to 24:00 window divided by 19 hours, and the waiting time of a pair is half the headway of the bottleneck section.

**Validation against the CAMET 2025 annual report.** 中国城市轨道交通协会, 城市轨道交通2025年度统计和分析报告 (31 March 2026), table 8, gives for every mainland city the minimum peak headway in force and the planned and actual daily train runs. Two checks are run per city: the shortest peak headway we transcribed must be at or above the city's reported minimum (a lower bound on any headway in the dataset, 30 s tolerance for whole-minute Amap values), and the daily runs implied by our all-day frequencies, summed over lines and directions, are compared with the report's planned runs, net of the tram, APM and maglev share the report counts in the same total. Section 5 prints both per city.

## 2. Summary by jurisdiction

| Jurisdiction | Networks | Routes | Basis of the routes | Direct pairs by label |
|---|---|---|---|---|
| Mainland China | 45 | 333 | published_peak_offpeak_only 124, press_quoted_operator_notice 58, amap_interval_band 34, published_interval_band_line 32, published_interval_band_section 26, transcription_2025_unsourced 24, operator_timetable_departures 23, inherited_from_trunk 8, published_average_interval 4 | published_peak_offpeak_only 38.4%, press_quoted_operator_notice 15.1%, published_interval_band_section 9.9%, published_interval_band_line 9.5%, transcription_2025_unsourced 8.9%, amap_interval_band 8.2%, operator_timetable_departures 5.7%, inherited_from_trunk 3.9%, published_average_interval 0.4%, transcription_2025_unsourced | published_peak_offpeak_only 0.0% |
| Hong Kong SAR | 1 | 12 | published_interval_band_line 6, published_interval_band_section 4, published_peak_offpeak_only 2 | published_interval_band_line 69.6%, published_interval_band_section 29.9%, published_peak_offpeak_only 0.4% |
| Macau SAR | 1 | 3 | published_average_interval 3 | published_average_interval 100.0% |
| Japan | 7 | 31 | gtfs_weekday_trips 31 | gtfs_weekday_trips 100.0% |
| South Korea | 4 | 25 | gtfs_weekday_trips 24, v1_value_kept_feed_incomplete 1 | gtfs_weekday_trips 89.5%, v1_value_kept_feed_incomplete 10.5% |
| Taiwan | 4 | 13 | tdx_frequency_bands 13 | tdx_frequency_bands 100.0% |

## 3. Networks built from timetable feeds

| Network | Feed and how the frequency is read | Routes | Pairs by label |
|---|---|---|---|
| Tokyo | Tokyo Metro, Toei, Yurikamome and Tokyo Monorail GTFS feeds (ODPT public centre), weekday trips per station pair, a train counts only where it stops (skip-stop rule of 2026-09-06) | 17 | gtfs_weekday_trips 100.0% |
| Yokohama | 横浜市交通局 GTFS, feed_version 20241227 (valid to 2025-12-31) | 2 | gtfs_weekday_trips 100.0% |
| Kyoto | 京都市交通局 GTFS, feed_version 20250701 (valid to 2026-03-31) | 2 | gtfs_weekday_trips 100.0% |
| Sapporo | 札幌市交通局 GTFS version 1.000, calendar 2020 (the 2020 timetable, the only feed the operator publishes) | 3 | gtfs_weekday_trips 100.0% |
| Sendai | 仙台市交通局 station timetables of the city open-data portal, revision 2023-07-01, converted to GTFS by jp_timetable_to_gtfs.py | 2 | gtfs_weekday_trips 100.0% |
| Kobe | 神戸市交通局 open-data timetables, 西神・山手線・北神線 revision 2025-03-15 and 海岸線 revision 2022-09-09, converted to GTFS (node set from the 2006 build) | 2 | gtfs_weekday_trips 100.0% |
| Fukuoka | 福岡市交通局 all-station Excel timetables, revisions 2025-03-15 and 2025-08-02 (Wayback copies of 2025-09-10), converted to GTFS-JP by the GTFS-FukuokaCitySubway tool | 3 | gtfs_weekday_trips 100.0% |
| Seoul | KTDB national GTFS, March 2023 dataset (2024 release), weekday trips; Line 2 loop (route 2) keeps its 2025 frequency because the feed holds 39 trips per direction | 14 | gtfs_weekday_trips 82.7%, v1_value_kept_feed_incomplete 17.3% |
| Incheon | KTDB national GTFS, March 2023 dataset; 277 pairs and the 2024 extension station keep 2025 values the feed cannot produce | 3 | gtfs_weekday_trips 90.0%, v1_value_kept_feed_incomplete 10.0% |
| Busan | KTDB national GTFS, March 2023 dataset; the last 10 Line 2 trips are completed to 양산 (terminus truncation in the feed, corrected 2026-09-15) | 5 | gtfs_weekday_trips 100.0% |
| Daegu | KTDB national GTFS, March 2023 dataset; 126 eastbound Line 1 trips completed to 안심 (terminus truncation in the feed, corrected 2026-09-15) | 3 | gtfs_weekday_trips 100.0% |
| Taipei | TDX Rail/Metro v2 Frequency endpoint, TRTC, captured 2026-08-24, raw responses archived with SHA-256 | 9 | tdx_frequency_bands 100.0% |
| Taoyuan | TDX Rail/Metro v2 Frequency endpoint, TYMC, captured 2026-08-24 | 1 | tdx_frequency_bands 100.0% |
| Taichung | TDX Rail/Metro v2 Frequency endpoint, TMRT, captured 2026-08-24 | 1 | tdx_frequency_bands 100.0% |
| Kaohsiung | TDX Rail/Metro v2 Frequency endpoint, KRTC and KLRT, captured 2026-08-24 | 2 | tdx_frequency_bands 100.0% |

TDX operators with a Frequency record in the archived pull (live or cached response): KRTC, NTMC, TMRT, TRTC, TYMC. Licence: Taiwan Open Government Data License v1.0, attribute 交通部 (MOTC).

## 4. Hong Kong and Macau

**Hong Kong.** 63 transcribed rows, 12 routes. Hosts: web.archive.org 48, mtr.com.hk 15. Dates: 2025-09 48, undated 15.

**Macau.** 3 transcribed rows, 3 routes. Hosts: web.archive.org 3. Dates: 2025-08 3.

Hong Kong: the MTR service-hours page, 48 rows re-cited to the Wayback capture of 2025-09-20 (inside the reference window), 15 rows read live on 2026-08-23 for lines whose values the capture confirms. Macau: the Macao LRT Corporation route page archived 2025-08-25 and the operator's Chinese FAQ archived 2025-10-05, one all-day average interval per line.

## 5. Mainland China: validation against the CAMET 2025 annual report

| City | CAMET minimum peak headway (s) | Shortest transcribed peak headway (min) | Lower bound respected | CAMET planned daily runs | Implied daily runs (ours) | Ratio, net of trams | CAMET service hours |
|---|---|---|---|---|---|---|---|
| Beijing | 120.0 | 1.0 | no | 10586.0 | 9247 | 0.902 | 18.81 |
| Changchun | 265.0 | 5.0 | yes | 2035.0 | 1774 | 0.973 | 16.67 |
| Changsha | 160.0 | 3.65 | yes | 2825.0 | 1774 | 0.705 | 17.16 |
| Changzhou | 360.0 | 6.0 | yes | 563.0 | 528 | 0.939 | 17.0 |
| Chengdu | 120.0 | 2.0 | yes | 6740.0 | 5122 | 0.813 | 17.56 |
| Chongqing | 150.0 | 2.5 | yes | 4999.0 | 4366 | 0.898 | 17.11 |
| Dalian | 210.0 | 3.5 | yes | 1724.0 | 1490 | 0.95 | 16.89 |
| Dongguan | 375.0 | 6.0 | yes | 320.0 | 267 | 0.836 | 17.13 |
| Foshan | 339.0 | 5.0 | no | 1067.0 | 1303 | 1.432 | 17.97 |
| Fuzhou | 270.0 | 4.5 | yes | 1722.0 | 1420 | 0.824 | 17.0 |
| Guangzhou | 125.0 | 2.233 | yes | 8579.0 | 7014 | 0.85 | 17.81 |
| Guiyang | 330.0 | 5.5 | yes | 1178.0 | 1064 | 0.903 | 17.83 |
| Hangzhou | 135.0 | 2.417 | yes | 4959.0 | 4406 | 0.888 | 18.02 |
| Harbin | 119.0 | 3.967 | yes | 1344.0 | 970 | 0.865 | 17.0 |
| Hefei | 208.0 | 3.967 | yes | 2162.0 | 1853 | 0.857 | 18.03 |
| Hohhot | 360.0 | 6.0 | yes | 460.0 | 437 | 0.95 | 16.5 |
| Jinan | 270.0 | 5.0 | yes | 939.0 | 798 | 1.161 | 17.14 |
| Jinhua | 600.0 | 11.163 | yes | 411.0 | 314 | 0.763 | 17.2 |
| Kunming | 230.0 | 4.0 | yes | 1530.0 | 1576 | 1.03 | 17.41 |
| Lanzhou | 240.0 | 6.333 | yes | 593.0 | 477 | 0.804 | 16.5 |
| Luoyang | 360.0 | 7.0 | yes | 473.0 | 414 | 0.875 | 16.0 |
| Nanchang | 236.0 | 3.933 | yes | 1545.0 | 1372 | 0.888 | 18.18 |
| Nanjing | 120.0 | 2.0 | yes | 4474.0 | 4164 | 0.961 | 17.08 |
| Nanning | 210.0 | 3.5 | yes | 1798.0 | 1514 | 0.842 | 16.5 |
| Nantong | 390.0 | 6.833 | yes | 560.0 | 461 | 0.823 | 16.85 |
| Ningbo | 238.0 | 4.0 | yes | 2765.0 | 2060 | 0.745 | 17.32 |
| Qingdao | 145.0 | 3.167 | yes | 2746.0 | 2043 | 0.762 | 17.2 |
| Shanghai | 110.0 | 1.833 | yes | 9957.0 | 7425 | 0.839 | 18.26 |
| Shaoxing | 360.0 | 6.0 | yes | 1242.0 | 536 | 0.432 | 17.17 |
| Shenyang | 175.0 | 2.917 | yes | 2379.0 | 1925 | 1.228 | 17.18 |
| Shenzhen | 115.0 | 1.917 | yes | 7754.0 | 6555 | 0.872 | 18.0 |
| Shijiazhuang | 300.0 | 5.0 | yes | 927.0 | 780 | 0.841 | 16.72 |
| Suzhou | 120.0 | 2.0 | yes | 4357.0 | 2930 | 0.772 | 16.72 |
| Taiyuan | 390.0 | 6.5 | yes | 559.0 | 549 | 0.982 | 16.84 |
| Taizhou | not in table 8 | | | | | | |
| Tianjin | 180.0 | 3.25 | yes | 4020.0 | 3027 | 0.753 | 17.8 |
| Wenzhou | 300.0 | 9.283 | yes | 455.0 | 394 | 0.866 | 17.2 |
| Wuhan | 150.0 | 2.7 | yes | 5196.0 | 4249 | 0.927 | 17.83 |
| Wuhu | 334.0 | 5.567 | yes | 597.0 | 417 | 0.698 | 16.5 |
| Wuxi | 300.0 | 5.0 | yes | 1521.0 | 1060 | 0.697 | 16.56 |
| Xiamen | 160.0 | 2.667 | yes | 1188.0 | 1025 | 0.863 | 17.0 |
| Xian | 120.0 | 2.467 | yes | 4543.0 | 3814 | 0.885 | 17.89 |
| Xuzhou | 330.0 | 5.5 | yes | 890.0 | 777 | 0.873 | 16.5 |
| Zhengzhou | 170.0 | 3.0 | yes | 3611.0 | 3147 | 0.871 | 17.4 |
| Ürümqi | 375.0 | 6.0 | yes | 258.0 | 326 | 1.262 | 16.6 |

The ratio is below one almost everywhere because the report counts every planned run including short-turn, express and depot movements, while our all-day frequency is the bottleneck of each section over 19 hours. It is printed as a plausibility bound, not as a target.

Cities where the shortest transcribed peak falls below the reported minimum, with the route responsible: Beijing (亦庄线, route 21, 1.0 min, operator_timetable_departures); Foshan (广佛线, route 2, 5.0 min, published_peak_offpeak_only).

*Beijing.* The 1.0-minute figure comes from 亦庄线 (route 21), where a partial first or last service hour with two counted departures a minute apart enters the profile; every full-hour count on that line gives 3.75 min or more, and the shortest full-hour peak in the city is 2.0 min on 1号线八通线, 8号线 and 大兴机场线, at the reported 120 s minimum. The 1.72-minute value on 4号线大兴线 is the operator's published 1分43秒 minimum and passes within the 30 s tolerance.

*Foshan.* The 5.0-minute figure is the all-day interval of 广佛线, which is operated by 广州地铁集团 and sits in Guangzhou's row of the report (minimum 125 s); Foshan's own lines 2 and 3 have shortest transcribed peaks of 5.75 and 5.92 min against the 339 s reported for Foshan. For the same reason the 广佛线 runs, counted here in full, push Foshan's ratio above one.

Cities whose implied daily runs exceed the planned runs of the report (ratio above one, flagged for the plausibility review): Foshan 1.432, Jinan 1.161, Kunming 1.03, Shenyang 1.228, Ürümqi 1.262.

## 6. Mainland China, city by city

### Beijing

Operators: 北京京港地铁有限公司; 北京市地铁运营有限公司; 北京市轨道交通运营管理有限公司. 28 routes. Basis: operator_timetable_departures 23, inherited_from_trunk 4, published_interval_band_section 1. URLs opened in the survey log: 130. Band files: Beijing_notice.csv (966 rows), Beijing_amap.csv (160 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 120.0 s, our shortest transcribed peak 1.0 min, lower bound NOT respected; implied daily runs 9247 against 10586.0 planned (ratio net of trams 0.902).

Note: The 1.0-minute figure comes from 亦庄线 (route 21), where a partial first or last service hour with two counted departures a minute apart enters the profile; every full-hour count on that line gives 3.75 min or more, and the shortest full-hour peak in the city is 2.0 min on 1号线八通线, 8号线 and 大兴机场线, at the reported 120 s minimum. The 1.72-minute value on 4号线大兴线 is the operator's published 1分43秒 minimum and passes within the 30 s tolerance.

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线八通线 | departures counted hour by hour on the operator's station timetables | 2.0 | 8.571 | 13.16 | 0.0 | 2026-05-15 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/%E5%85%AB%E9%80%9A%E7%BA%BF-%E7%8E%AF%E7%90%83%E5%BA%A6%E5%81%87%E5%8C%BA%E7%AB%99-%E8%8B%B9%E6%9E%9C%E5%9B%AD%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 2 | 2号线 | inherited from the trunk route of the same line | 3.158 | 8.571 | 10.87 | 0.0 | 2026-07-15 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/2%E5%8F%B7%E7%BA%BF-%E8%A5%BF%E7%9B%B4%E9%97%A8%E7%AB%99-%E8%BD%A6%E5%85%AC%E5%BA%84%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 3 | 2号线 | inherited from the trunk route of the same line | 3.158 | 8.571 | 10.87 | 0.0 | 2026-07-15 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/2%E5%8F%B7%E7%BA%BF-%E8%A5%BF%E7%9B%B4%E9%97%A8%E7%AB%99-%E8%BD%A6%E5%85%AC%E5%BA%84%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 4 | 4号线大兴线 | departures counted hour by hour on the operator's station timetables | 1.717 | 7.667 | 13.99 | 0.0 | 2026-05-28 | operator timetable page; operator website | [mtr.bj.cn](https://www.mtr.bj.cn/service/line/station/5d5a1958b1ea0278b8fffd7f.html) +2 |
| 5 | 5号线 | departures counted hour by hour on the operator's station timetables | 2.143 | 8.571 | 13.97 | 0.0 | 2026-07-15 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/5%E5%8F%B7%E7%BA%BF-%E5%A4%A9%E9%80%9A%E8%8B%91%E5%8C%97%E7%AB%99-%E5%AE%8B%E5%AE%B6%E5%BA%84%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 6 | 7号线 | departures counted hour by hour on the operator's station timetables | 3.0 | 10.0 | 8.63 | 0.0 | 2026-05-20 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/7%E5%8F%B7%E7%BA%BF-%E5%8C%97%E4%BA%AC%E8%A5%BF%E7%AB%99-%E7%8E%AF%E7%90%83%E5%BA%A6%E5%81%87%E5%8C%BA%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 7 | 8号线 | departures counted hour by hour on the operator's station timetables | 2.0 | 10.0 | 10.82 | 0.0 | 2026-05-06 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/8%E5%8F%B7%E7%BA%BF-%E7%80%9B%E6%B5%B7%E7%AB%99-%E6%9C%B1%E8%BE%9B%E5%BA%84%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 8 | 9号线 | departures counted hour by hour on the operator's station timetables | 2.727 | 7.5 | 11.95 | 0.0 | 2026-06-11 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/9%E5%8F%B7%E7%BA%BF-%E5%9B%BD%E5%AE%B6%E5%9B%BE%E4%B9%A6%E9%A6%86%E7%AB%99-%E9%83%AD%E5%85%AC%E5%BA%84%E7%AB%99%E3%80%81%E9%98%8E%E6%9D%91%E4%B8%9C%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 9 | 10号线 | inherited from the trunk route of the same line | 2.105 | 6.75 | 17.39 | 0.0 | 2026-05-27 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/10%E5%8F%B7%E7%BA%BF-%E5%B7%B4%E6%B2%9F%E7%AB%99-%E7%81%AB%E5%99%A8%E8%90%A5%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 10 | 10号线 | inherited from the trunk route of the same line | 2.105 | 6.75 | 17.39 | 0.0 | 2026-05-27 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/10%E5%8F%B7%E7%BA%BF-%E5%B7%B4%E6%B2%9F%E7%AB%99-%E7%81%AB%E5%99%A8%E8%90%A5%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 11 | 11号线 | departures counted hour by hour on the operator's station timetables | 7.333 | 10.0 | 5.63 | 0.0 | 2026-04-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/11%E5%8F%B7%E7%BA%BF-%E6%96%B0%E9%A6%96%E9%92%A2%E7%AB%99-%E6%A8%A1%E5%BC%8F%E5%8F%A3%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 12 | 12号线 | departures counted hour by hour on the operator's station timetables | 3.75 | 7.5 | 9.34 | 0.0 | 2026-05-09 | operator timetable page; press quoting the operator | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/12%E5%8F%B7%E7%BA%BF-%E5%9B%9B%E5%AD%A3%E9%9D%92%E6%A1%A5%E7%AB%99-%E4%B8%9C%E5%9D%9D%E5%8C%97%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +2 |
| 13 | 13号线 | departures counted hour by hour on the operator's station timetables | 3.333 | 9.167 | 9.16 | 0.0 | 2026-05-27 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/13%E5%8F%B7%E7%BA%BF-%E4%B8%9C%E7%9B%B4%E9%97%A8%E7%AB%99-%E8%A5%BF%E7%9B%B4%E9%97%A8%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 14 | 14号线 | departures counted hour by hour on the operator's station timetables | 3.0 | 8.6 | 9.74 | 0.0 | 2026-05-28 | operator timetable page | [mtr.bj.cn](https://www.mtr.bj.cn/service/line/station/5d5a13a4b1ea0278b8fffd04.html) +1 |
| 15 | 15号线 | departures counted hour by hour on the operator's station timetables | 2.727 | 9.0 | 10.0 | 0.0 | 2026-04-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/15%E5%8F%B7%E7%BA%BF-%E4%BF%B8%E4%BC%AF%E7%AB%99-%E6%B8%85%E5%8D%8E%E4%B8%9C%E8%B7%AF%E8%A5%BF%E5%8F%A3%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 16 | 16号线 | departures counted hour by hour on the operator's station timetables | 6.0 | 10.0 | 7.53 | 0.0 | 2026-05-28 | operator timetable page | [mtr.bj.cn](https://www.mtr.bj.cn/service/line/station/5d5a1291b1ea0278b8fffcfc.html) +1 |
| 17 | 19号线 | departures counted hour by hour on the operator's station timetables | 3.75 | 8.333 | 10.24 | 0.0 | 2024-08-08 | operator timetable page | [bii.com.cn](https://www.bii.com.cn/file/2024/08/08/1723130709277.jpg) +1 |
| 18 | 大兴机场线 | departures counted hour by hour on the operator's station timetables | 2.0 | 10.0 | 5.76 | 0.0 | 2026-02-06 | operator timetable page | [bii.com.cn](https://www.bii.com.cn/file/2026/02/06/1770363725395.jpg) +1 |
| 19 | 昌平线 | departures counted hour by hour on the operator's station timetables | 2.308 | 10.0 | 11.24 | 0.0 | 2026-04-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/%E6%98%8C%E5%B9%B3%E7%BA%BF-%E6%98%8C%E5%B9%B3%E8%A5%BF%E5%B1%B1%E5%8F%A3%E7%AB%99-%E8%93%9F%E9%97%A8%E6%A1%A5%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 20 | 房山线 | departures counted hour by hour on the operator's station timetables | 2.222 | 10.0 | 9.71 | 0.0 | 2026-06-11 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/%E6%88%BF%E5%B1%B1%E7%BA%BF-%E4%B8%9C%E7%AE%A1%E5%A4%B4%E5%8D%97%E7%AB%99-%E9%98%8E%E6%9D%91%E4%B8%9C%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 21 | 亦庄线 | departures counted hour by hour on the operator's station timetables | 1.0 | 10.0 | 7.5 | 0.0 | 2026-05-14 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/%E4%BA%A6%E5%BA%84%E7%BA%BF-%E4%BA%A6%E5%BA%84%E7%81%AB%E8%BD%A6%E7%AB%99-%E5%AE%8B%E5%AE%B6%E5%BA%84%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 22 | 首都机场线 | departures counted hour by hour on the operator's station timetables | 4.0 | 12.0 | 4.63 | 0.0 | 2026-06-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/%E9%A6%96%E9%83%BD%E6%9C%BA%E5%9C%BA%E7%BA%BF-2%E5%8F%B7%E8%88%AA%E7%AB%99%E6%A5%BC%E7%AB%99-%E5%8C%97%E6%96%B0%E6%A1%A5%E6%96%B9%E5%90%91.jpg) +1 |
| 24 | 燕房线 | operator statement, interval bands per section | 5.0 | 9.333 | 7.67 | 0.0 | 2026-07-05 | operator timetable page; operator website | [bii.com.cn](https://www.bii.com.cn/file/2026/07/05/1783265011957.png) +2 |
| 25 | S1线 | departures counted hour by hour on the operator's station timetables | 5.0 | 12.0 | 6.74 | 0.0 | 2026-04-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/S1%E7%BA%BF-%E7%9F%B3%E5%8E%82%E7%AB%99-%E8%8B%B9%E6%9E%9C%E5%9B%AD%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 27 | 17号线 | departures counted hour by hour on the operator's station timetables | 6.0 | 8.667 | 7.24 | 0.0 | 2026-05-28 | operator timetable page; operator website | [mtr.bj.cn](https://www.mtr.bj.cn/service/line/station/61ce491bb0972c463ee519cb.html) +2 |
| 28 | 17号线 | departures counted hour by hour on the operator's station timetables | 6.0 | 8.667 | 7.24 | 0.0 | 2026-05-28 | operator timetable page; operator website | [mtr.bj.cn](https://www.mtr.bj.cn/service/line/station/61ce491bb0972c463ee519cb.html) +2 |
| 29 | 6号线 | departures counted hour by hour on the operator's station timetables | 2.143 | 12.5 | 10.66 | 0.0 | 2026-06-29 | operator timetable page | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/6%E5%8F%B7%E7%BA%BF-%E6%BD%9E%E9%98%B3%E7%AB%99-%E9%87%91%E5%AE%89%E6%A1%A5%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +1 |
| 30 | 3号线 | departures counted hour by hour on the operator's station timetables | 3.75 | 8.333 | 9.79 | 0.0 | 2026-07-17 | operator timetable page; press quoting the operator | [eos-beijing-2.cmecloud.cn](https://eos-beijing-2.cmecloud.cn/app-dtstatic/3%E5%8F%B7%E7%BA%BF-%E4%B8%9C%E5%9B%9B%E5%8D%81%E6%9D%A1%E7%AB%99-%E4%B8%9C%E5%9D%9D%E5%8C%97%E7%AB%99%E6%96%B9%E5%90%91-%E5%B7%A5%E4%BD%9C%E6%97%A5.jpg) +2 |

### Changchun

Operators: 长春市公交集团; 长春市轨道交通集团第四分公司. 6 routes. Basis: press_quoted_operator_notice 6. URLs opened in the survey log: 6. Band files: Changchun_notice.csv (16 rows), Changchun_amap.csv (50 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 265.0 s, our shortest transcribed peak 5.0 min, lower bound respected; implied daily runs 1774 against 2035.0 planned (ratio net of trams 0.973).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 5.0 | 6.0 | 8.89 | 0.0 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 2 | 4号线 | press or government relay quoting the operator's notice | 5.5 | 6.5 | 7.46 | 0.0 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 3 | 6号线 | press or government relay quoting the operator's notice | 5.0 | 7.0 | 8.25 | 0.0 | 2024-06-07 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/64306.shtm) |
| 4 | 8号线 | press or government relay quoting the operator's notice | 8.0 | 10.0 | 4.89 | 0.0 | 2021-01-07 | press quoting the operator | [jl.ifeng.com](https://jl.ifeng.com/c/82o543UcdzL) +1 |
| 5 | 3号线 | press or government relay quoting the operator's notice | 5.0 | 6.0 | 8.25 | 0.0 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 6 | 2号线 | press or government relay quoting the operator's notice | 5.0 | 6.0 | 8.5 | 0.0 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |

### Changsha

Operators: 湖南磁浮交通发展公司; 长沙轨道交通集团. 7 routes. Basis: published_peak_offpeak_only 6, inherited_from_trunk 1. URLs opened in the survey log: 10. Band files: Changsha_notice.csv (11 rows), Changsha_amap.csv (14 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 160.0 s, our shortest transcribed peak 3.65 min, lower bound respected; implied daily runs 1774 against 2825.0 planned (ratio net of trams 0.705).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.583 | 6.617 | 8.48 | 0.404 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.65 | 6.073 | 10.03 | 0.763 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 3 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.483 | 8.104 | 6.62 | 0.88 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 7.742 | 7.25 | 0.853 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.283 | 8.368 | 6.58 | 0.881 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 6 | 6号线 | inherited from the trunk route of the same line | 4.183 | 7.742 | 7.15 | 0.015 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 7 | 磁浮快线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.467 | 10.0 | 5.89 | 0.882 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |

### Changzhou

Operator: 常州轨交客运公司. 2 routes. Basis: published_peak_offpeak_only 2. URLs opened in the survey log: 13. Band files: Changzhou_notice.csv (2 rows), Changzhou_amap.csv (44 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 360.0 s, our shortest transcribed peak 6.0 min, lower bound respected; implied daily runs 528 against 563.0 planned (ratio net of trams 0.939).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.762 | 6.79 | 0.744 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.722 | 7.05 | 0.752 | 2020-04-02 | press quoting the operator | [m.cc.bendibao.com](https://m.cc.bendibao.com/traffic/47870.shtm) |

### Chengdu

Operator: 成都轨道交通集团. 18 routes. Basis: transcription_2025_unsourced 11, published_peak_offpeak_only 4, press_quoted_operator_notice 2, amap_interval_band 1. URLs opened in the survey log: 32. Band files: Chengdu_notice.csv (11 rows), Chengdu_amap.csv (22 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 120.0 s, our shortest transcribed peak 2.0 min, lower bound respected; implied daily runs 5122 against 6740.0 planned (ratio net of trams 0.813).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2号线 | 2025 constant, no source |  |  | 12.0 |  |  |  | none |
| 2 | S3(资阳)线 | press or government relay quoting the operator's notice | 15.0 | 20.0 | 3.18 | 0.011 | 2024-09-26 | press quoting the operator | [sina.cn](https://www.sina.cn/news/detail/5082799712769244.html) |
| 3 | 3号线 | 2025 constant, no source |  |  | 10.0 |  |  |  | none |
| 4 | 4号线 | 2025 constant, no source |  |  | 10.0 |  |  |  | none |
| 5 | 5号线 | 2025 constant, no source |  |  | 10.0 |  |  |  | none |
| 6 | 6号线 | 2025 constant, no source |  |  | 7.5 |  |  |  | none |
| 7 | 7号线 | 2025 constant, no source |  |  | 6.67 |  |  |  | none |
| 8 | 7号线 | 2025 constant, no source |  |  | 6.67 |  |  |  | none |
| 9 | 8号线 | 2025 constant, no source |  |  | 7.5 |  |  |  | none |
| 10 | 9号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 8.0 | 8.22 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁9号线&city=<city>&extensions=all) |
| 11 | 10号线 | 2025 constant, no source |  |  | 7.0 |  |  |  | none |
| 12 | 27号线 | 2025 constant, no source |  |  | 8.0 |  |  |  | none |
| 13 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.0 | 3.75 | 15.66 | 0.883 | 2025-04-24 | press quoting the operator | [news.cctv.cn](https://news.cctv.cn/2025/04/24/ARTI2agzpRosSjVlDL8MU2c3250424.shtml) |
| 14 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.0 | 3.75 | 15.73 | 0.883 | 2025-04-24 | press quoting the operator | [news.cctv.cn](https://news.cctv.cn/2025/04/24/ARTI2agzpRosSjVlDL8MU2c3250424.shtml) |
| 15 | 17号线 | 2025 constant, no source |  |  | 8.0 |  |  |  | none |
| 16 | 18号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.917 | 7.25 | 9.8 | 0.308 | 2023-03-26 | press quoting the operator | [sichuan.scol.com.cn](https://sichuan.scol.com.cn/ggxw/202303/58838696.html) |
| 17 | 19号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 6.0 | 10.96 | 0.767 | 2023-11-28 | press quoting the operator | [sc.people.com.cn](http://sc.people.com.cn/n2/2023/1128/c345167-40657810.html) |
| 18 | 18号线 | press or government relay quoting the operator's notice | 3.917 | 8.416 | 8.77 | 0.0 | 2023-03-26 | press quoting the operator | [sichuan.scol.com.cn](https://sichuan.scol.com.cn/ggxw/202303/58838696.html) |

### Chongqing

Operator: 重庆轨道交通集团. 15 routes. Basis: published_peak_offpeak_only 7, published_interval_band_line 2, published_average_interval 2, press_quoted_operator_notice 2, inherited_from_trunk 1, amap_interval_band 1. URLs opened in the survey log: 34. Band files: Chongqing_notice.csv (41 rows), Chongqing_amap.csv (30 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 150.0 s, our shortest transcribed peak 2.5 min, lower bound respected; implied daily runs 4366 against 4999.0 planned (ratio net of trams 0.898).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 3.846 | 14.34 | 0.759 | 2020-01-13 | government portal relaying the operator | [cq.gov.cn](http://cq.gov.cn/ywdt/bmts/202001/t20200113_8655466.html) |
| 2 | 2号线 | inherited from the trunk route of the same line | 9.75 | 9.75 | 5.38 | 0.22 | 2020-03-27 | government portal relaying the operator | [ddknews.gov.cn](http://www.ddknews.gov.cn/ddk_Content/2020-03/27/content_4650847.htm) |
| 3 | 轨道交通3号线(空港线) | Amap interval bands (undated, passed the acceptance test) | 10.0 | 10.0 | 5.05 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通3号线(空港线)&city=<city>&extensions=all) |
| 4 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.5 | 3.158 | 17.8 | 0.702 | 2015-01-30 | press quoting the operator | [politics.people.com.cn](http://politics.people.com.cn/n/2015/0130/c70731-26479868.html) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.5 | 5.66 | 7.47 | 0.884 | 2024-11-27 | government portal relaying the operator | [cq.gov.cn](http://www.cq.gov.cn/ywdt/bmts/202411/t20241127_13837623.html) |
| 6 | 6号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.167 | 3.704 | 14.52 | 0.761 | 2021-05-27 | government portal relaying the operator | [cq.gov.cn](http://cq.gov.cn/ywdt/bmts/202105/t20210527_9335105.html) |
| 7 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 6.667 | 8.3 | 0.766 | 2023-02-01 | government portal relaying the operator | [cq.gov.cn](https://www.cq.gov.cn/ywdt/bmts/202302/t20230201_11556089.html) +1 |
| 8 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.5 | 7.5 | 7.11 | 0.758 | 2023-11-29 | government portal relaying the operator; press quoting the operator | [cq.cnr.cn](https://cq.cnr.cn/xwsd/20231129/t20231129_526502759.shtml) +1 |
| 9 | 18号线 | operator statement, interval bands for the whole line | 5.0 | 8.0 | 7.55 | 0.0 | 2024-06-30 | government portal relaying the operator | [cq.gov.cn](https://www.cq.gov.cn/zwgk/zfxxgkml/zdlyxxgk/jt/jtzx/202406/t20240630_13335005.html) |
| 10 | 璧铜线 | operator statement, one average interval | 18.0 | 18.0 | 2.58 | 0.0 | 2025-01-03 | government portal relaying the operator | [cq.gov.cn](https://www.cq.gov.cn/ywdt/jrcq/202501/t20250103_14043422_app.html) |
| 11 | 轨道交通国博线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 10.0 | 13.5 | 4.4 | 0.401 | 2023-09-01 | press quoting the operator | [epaper.cqcb.com](https://epaper.cqcb.com/html/202309/01/content_427553.html) +1 |
| 12 | 环线 | press or government relay quoting the operator's notice | 4.5 | 6.0 | 7.75 | 0.223 | 2022-03-08 | press quoting the operator | [jiemian.com](https://www.jiemian.com/article/7183241.html) |
| 13 | 环线 | press or government relay quoting the operator's notice | 4.5 | 6.0 | 7.75 | 0.221 | 2022-03-08 | press quoting the operator | [jiemian.com](https://www.jiemian.com/article/7183241.html) |
| 15 | 江跳线 | operator statement, interval bands for the whole line | 10.0 | 15.0 | 3.52 | 0.124 | 2022-08-04 | government portal relaying the operator | [cq.gov.cn](https://www.cq.gov.cn/zwgk/zfxxgkml/hygq/202208/t20220804_10978248.html) |
| 17 | 4号线 | operator statement, one average interval | 10.0 | 10.0 | 4.11 | 0.0 | 2022-06-20 | government portal relaying the operator | [cq.gov.cn](https://www.cq.gov.cn/zwgk/zfxxgkzl/fdzdgknr/zdxm/dtxx/202206/t20220620_10831327.html) |

### Dalian

Operator: 大连地铁集团. 7 routes. Basis: published_peak_offpeak_only 5, press_quoted_operator_notice 1, transcription_2025_unsourced 1. URLs opened in the survey log: 46. Band files: Dalian_notice.csv (44 rows), Dalian_amap.csv (49 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 210.0 s, our shortest transcribed peak 3.5 min, lower bound respected; implied daily runs 1490 against 1724.0 planned (ratio net of trams 0.95).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 6.186 | 8.23 | 0.934 | 2023-04-16 | press quoting the operator | [thepaper.cn](https://www.thepaper.cn/newsDetail_forward_22725320) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.5 | 11.0 | 8.98 | 0.83 | 2023-04-16 | press quoting the operator | [thepaper.cn](https://www.thepaper.cn/newsDetail_forward_22725320) |
| 3 | 地铁3号线支线 | press or government relay quoting the operator's notice | 10.0 | 15.0 | 3.55 | 0.156 | 2021-12-28 | press quoting the operator | [dalian.runsky.com](https://dalian.runsky.com/2021-12/28/content_6170453.html) |
| 4 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.941 | 20.0 | 4.11 | 0.35 | 2024-08-31 | operator website | [dltransgrp.com](https://www.dltransgrp.com/subway/subwayShow.do?newsId=c2831d76535741d79833c653e9db21bb) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.5 | 10.0 | 6.48 | 0.273 | 2023-03-25 | government portal relaying the operator | [news.qq.com](https://news.qq.com/rain/a/20230325A01XHQ00) |
| 6 | 12号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 13.0 | 13.043 | 3.53 | 0.595 | 2023-04-21 | press quoting the operator | [m.gmw.cn](https://m.gmw.cn/2023-04/21/content_1303350694.htm) |
| 7 | 13号线 | 2025 constant, no source |  |  | 4.3 |  |  |  | none |

### Dongguan

Operator: 东莞轨道交通客运公司. 1 routes. Basis: press_quoted_operator_notice 1. URLs opened in the survey log: 8. Band files: Dongguan_notice.csv (3 rows), Dongguan_amap.csv (18 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 375.0 s, our shortest transcribed peak 6.0 min, lower bound respected; implied daily runs 267 against 320.0 planned (ratio net of trams 0.836).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2号线 | press or government relay quoting the operator's notice | 6.0 | 9.0 | 7.04 | 0.0 | 2021-05-07 | press quoting the operator | [pub.timedg.com](https://pub.timedg.com/a/2021-05/07/AP60e970b1e4b04c831916259a.html) |

### Foshan

Operators: 佛山市地铁运营有限公司 (佛山地铁集团子公司); 广州地铁集团有限公司 (广州地铁运营集团有限公司). 3 routes. Basis: published_interval_band_line 1, published_peak_offpeak_only 1, press_quoted_operator_notice 1. URLs opened in the survey log: 17. Band files: Foshan_notice.csv (20 rows), Foshan_amap.csv (30 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 339.0 s, our shortest transcribed peak 5.0 min, lower bound NOT respected; implied daily runs 1303 against 1067.0 planned (ratio net of trams 1.432).

Note: The 5.0-minute figure is the all-day interval of 广佛线, which is operated by 广州地铁集团 and sits in Guangzhou's row of the report (minimum 125 s); Foshan's own lines 2 and 3 have shortest transcribed peaks of 5.75 and 5.92 min against the 339 s reported for Foshan. For the same reason the 广佛线 runs, counted here in full, push Foshan's ratio above one.

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 佛山2号线 | operator statement, interval bands for the whole line | 5.75 | 12.0 | 6.19 | 0.045 | 2025-05-16 | government portal relaying the operator; press quoting the operator | [ipaper.oeeee.com](https://ipaper.oeeee.com/ipaper/A/html/2025-05/16/content_4995.htm) +1 |
| 2 | 广佛线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 5.825 | 9.56 | 0.764 | 2011-07-07 | operator website | [fmetro.net](https://www.fmetro.net/xwzx/gsdt/content_962) |
| 3 | 3号线 | press or government relay quoting the operator's notice | 5.917 | 12.667 | 6.07 | 0.045 | 2025-05-22 | press quoting the operator | [web.archive.org](https://web.archive.org/web/20250522123005/https://www.nfnews.com/content/LozBvxzLon.html) |

### Fuzhou

Operator: 福州地铁集团. 5 routes. Basis: published_interval_band_line 3, press_quoted_operator_notice 2. URLs opened in the survey log: 12. Band files: Fuzhou_notice.csv (30 rows), Fuzhou_amap.csv (128 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 270.0 s, our shortest transcribed peak 4.5 min, lower bound respected; implied daily runs 1420 against 1722.0 planned (ratio net of trams 0.824).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 4.5 | 6.833 | 8.48 | 0.083 | 2023-08-22 | operator WeChat; press quoting the operator | [sohu.com](https://www.sohu.com/a/714011839_121106994) +1 |
| 2 | 2号线 | operator statement, interval bands for the whole line | 4.5 | 6.833 | 8.51 | 0.0 | 2023-08-22 | operator WeChat; press quoting the operator | [sohu.com](https://www.sohu.com/a/714011839_121106994) +1 |
| 3 | 4号线 | press or government relay quoting the operator's notice | 5.5 | 6.833 | 8.07 | 0.0 | 2024-04-28 | press quoting the operator | [clnews.com.cn](https://www.clnews.com.cn/html/3/20240428/662df95412374.shtml) |
| 4 | 5号线 | press or government relay quoting the operator's notice | 6.833 | 7.833 | 6.97 | 0.0 | 2024-04-28 | press quoting the operator | [clnews.com.cn](https://www.clnews.com.cn/html/3/20240428/662df95412374.shtml) |
| 5 | 6号线 | operator statement, interval bands for the whole line | 7.833 | 9.333 | 5.31 | 0.0 | 2023-01-06 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/svCu-QQHXL8ZM3nscl8EPA) |

### Guangzhou

Operators: 广东城际铁路运营有限公司 (广州地铁集团附属); 广州地铁集团有限公司 (广州地铁运营集团有限公司). 22 routes. Basis: published_peak_offpeak_only 10, transcription_2025_unsourced 5, amap_interval_band 3, published_interval_band_line 3, inherited_from_trunk 1. URLs opened in the survey log: 32. Band files: Guangzhou_notice.csv (45 rows), Guangzhou_amap.csv (88 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 125.0 s, our shortest transcribed peak 2.233 min, lower bound respected; implied daily runs 7014 against 8579.0 planned (ratio net of trams 0.85).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | 2025 constant, no source |  |  | 12.0 |  |  |  | none |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.233 | 4.286 | 13.43 | 0.886 | 2019-12-15 | press quoting the operator | [pc.nfnews.com](https://pc.nfnews.com/38/2896248.html) |
| 3 | 3号线 | inherited from the trunk route of the same line | 3.0 | 7.0 | 12.6 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁3号线&city=<city>&extensions=all) |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.333 | 4.666 | 13.02 | 0.884 | 2021-10-13 | press quoting the operator | [static.nfnews.com](https://static.nfnews.com/content/202110/13/c5829379.html) |
| 5 | 5号线 | 2025 constant, no source |  |  | 13.0 |  |  |  | none |
| 6 | 6号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 8.0 | 7.43 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁6号线&city=<city>&extensions=all) |
| 7 | 7号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.317 | 6.0 | 9.33 | 0.827 | 2023-12-28 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/jtfw/content/post_9409437.html) |
| 8 | 8号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.333 | 5.455 | 11.27 | 0.768 | 2020-10-16 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/content/post_6849729.html) |
| 9 | 9号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 8.0 | 8.21 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁9号线&city=<city>&extensions=all) |
| 10 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 8.0 | 8.41 | 0.404 | 2025-06-27 | press quoting the operator | [news.dayoo.com](https://news.dayoo.com/guangzhou/202506/27/139995_54841304.htm) |
| 11 | 11号线 | operator statement, interval bands for the whole line | 5.35 | 7.5 | 7.86 | 0.0 | 2025-09-29 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/jtfw/content/post_10466308.html) +1 |
| 12 | 11号线 | operator statement, interval bands for the whole line | 5.35 | 7.5 | 7.86 | 0.0 | 2025-09-29 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/jtfw/content/post_10466308.html) +1 |
| 13 | 12号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.5 | 6.667 | 8.3 | 0.538 | 2025-06-13 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/jtfw/content/post_10308536.html) |
| 14 | 12号线 | 2025 constant, no source |  |  | 9.0 |  |  |  | none |
| 15 | 3号线 (天河客运站支线) | Amap interval bands (undated, passed the acceptance test) | 3.0 | 7.0 | 12.63 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁3号线&city=<city>&extensions=all) |
| 16 | 14号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.75 | 8.571 | 6.79 | 0.441 | 2024-05-20 | press quoting the operator | [pc.nfnews.com](https://pc.nfnews.com/38/8890197.html) |
| 17 | 18号线 | operator statement, interval bands for the whole line | 4.367 | 35.0 | 2.8 | 0.0 | 2022-04-16 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/content/post_8191281.html) |
| 18 | 21号线 | 2025 constant, no source |  |  | 6.0 |  |  |  | none |
| 19 | 22号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.5 | 10.0 | 5.8 | 0.765 | 2022-03-31 | press quoting the operator | [huacheng.gz-cmc.com](https://huacheng.gz-cmc.com/pages/2022/03/31/1dc3d957d8524336b22cb1eb5d2f28c4.html) |
| 20 | APM线 | 2025 constant, no source |  |  | 18.0 |  |  |  | none |
| 21 | 广佛线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.967 | 5.934 | 11.16 | 0.765 | 2020-11-03 | press quoting the operator | [pc.nfnews.com](https://pc.nfnews.com/40/4243472.html) |
| 22 | 13号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 6.667 | 8.07 | 0.761 | 2025-08-08 | government portal relaying the operator | [gz.gov.cn](https://www.gz.gov.cn/zwfw/zxfw/jtfw/content/post_10393475.html) |

### Guiyang

Operator: . 4 routes. Basis: press_quoted_operator_notice 3, published_peak_offpeak_only 1. URLs opened in the survey log: 8. Band files: Guiyang_notice.csv (20 rows), Guiyang_amap.csv (70 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 330.0 s, our shortest transcribed peak 5.5 min, lower bound respected; implied daily runs 1064 against 1178.0 planned (ratio net of trams 0.903).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 5.5 | 9.0 | 6.39 | 0.02 | 2022-08-29 | press quoting the operator | [m.gy.bendibao.com](https://m.gy.bendibao.com/traffic/60711.shtm) +1 |
| 2 | S1线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.833 | 9.791 | 5.54 | 0.88 | 2025-02-14 | government portal relaying the operator | [finance.sina.cn](https://finance.sina.cn/2025-02-14/detail-inekmitf4264434.d.html) |
| 3 | 2号线 | press or government relay quoting the operator's notice | 5.5 | 9.0 | 7.53 | 0.033 | 2022-08-29 | press quoting the operator | [m.gy.bendibao.com](https://m.gy.bendibao.com/traffic/60711.shtm) +1 |
| 4 | 3号线 | press or government relay quoting the operator's notice | 6.0 | 9.0 | 7.49 | 0.057 | 2023-12-16 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20231216A08M2A00) |

### Hangzhou

Operators: 杭州地铁集团; 杭州杭港地铁有限公司. 15 routes. Basis: published_peak_offpeak_only 12, press_quoted_operator_notice 2, amap_interval_band 1. URLs opened in the survey log: 18. Band files: Hangzhou_notice.csv (33 rows), Hangzhou_amap.csv (38 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 135.0 s, our shortest transcribed peak 2.417 min, lower bound respected; implied daily runs 4406 against 4959.0 planned (ratio net of trams 0.888).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | Amap interval bands (undated, passed the acceptance test) | 3.0 | 5.0 | 11.95 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁1号线&city=<city>&extensions=all) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.5 | 5.455 | 11.84 | 0.855 | 2025-11-17 | government portal relaying the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_31990099) |
| 3 | 4号线 | press or government relay quoting the operator's notice | 2.417 | 6.833 | 9.9 | 0.167 | 2025-07-26 | press quoting the operator | [zjnews.zjol.com.cn](https://zjnews.zjol.com.cn/yc/qmt/202507/t20250726_31137106.shtml) |
| 4 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.833 | 4.101 | 13.42 | 0.942 | 2025-05-14 | government portal relaying the operator | [hzzx.gov.cn](https://www.hzzx.gov.cn/cshz/content/2025-05/14/content_8994352.htm) |
| 5 | 7号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.5 | 6.316 | 8.51 | 0.882 | 2025-11-17 | government portal relaying the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_31990099) |
| 6 | 8号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.75 | 9.0 | 6.63 | 0.292 | 2021-06-28 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20210628A0APB900) |
| 7 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 6.154 | 9.64 | 0.849 | 2025-03-05 | government portal relaying the operator | [hzzx.gov.cn](https://www.hzzx.gov.cn/cshz/content/2025-03/05/content_8873285.htm) +1 |
| 8 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.5 | 7.76 | 0.299 | 2022-02-21 | press quoting the operator | [finance.sina.cn](https://finance.sina.cn/2022-02-21/detail-imcwiwss2135770.d.html) |
| 9 | 16号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 7.059 | 7.72 | 0.696 | 2025-03-05 | government portal relaying the operator | [hzzx.gov.cn](https://www.hzzx.gov.cn/cshz/content/2025-03/05/content_8873285.htm) +1 |
| 10 | 6号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.167 | 5.714 | 9.41 | 0.785 | 2025-03-05 | government portal relaying the operator | [hzzx.gov.cn](https://www.hzzx.gov.cn/cshz/content/2025-03/05/content_8873285.htm) |
| 11 | 6号线 | press or government relay quoting the operator's notice | 9.0 | 9.0 | 6.15 | 0.0 | 2020-12-30 | press quoting the operator | [hwyst.hangzhou.com.cn](https://hwyst.hangzhou.com.cn/xwfb/content/2020-12/30/content_7884255.htm) |
| 12 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 7.0 | 9.44 | 0.39 | 2026-03-25 | government portal relaying the operator; press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20260325A07BJC00) +1 |
| 13 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.8 | 7.0 | 9.53 | 0.529 | 2026-03-25 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20260325A07BJC00) |
| 14 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 6.154 | 9.64 | 0.849 | 2025-03-05 | government portal relaying the operator | [hzzx.gov.cn](https://www.hzzx.gov.cn/cshz/content/2025-03/05/content_8873285.htm) +1 |
| 15 | 19号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.5 | 8.47 | 0.321 | 2025-06-30 | press quoting the operator | [zjnews.zjol.com.cn](https://zjnews.zjol.com.cn/zjnews/202506/t20250630_31082688.shtml) |

### Harbin

Operator: 哈尔滨地铁集团. 5 routes. Basis: published_peak_offpeak_only 3, press_quoted_operator_notice 2. URLs opened in the survey log: 6. Band files: Harbin_notice.csv (10 rows), Harbin_amap.csv (90 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 119.0 s, our shortest transcribed peak 3.967 min, lower bound respected; implied daily runs 970 against 1344.0 planned (ratio net of trams 0.865).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 3.967 | 6.5 | 8.29 | 0.132 | 2023-03-10 | press quoting the operator | [m.sohu.com](https://m.sohu.com/a/652421420_349336) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 5.167 | 6.967 | 8.16 | 0.142 | 2023-03-10 | press quoting the operator | [m.sohu.com](https://m.sohu.com/a/652421420_349336) |
| 3 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.967 | 6.967 | 8.88 | 0.316 | 2024-11-26 | press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_29460046) |
| 4 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.967 | 6.967 | 8.88 | 0.316 | 2024-11-26 | press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_29460046) |
| 5 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.967 | 6.967 | 8.85 | 0.298 | 2024-11-26 | press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_29460046) |

### Hefei

Operator: 合肥城市轨道交通公司. 6 routes. Basis: published_interval_band_line 6. URLs opened in the survey log: 9. Band files: Hefei_notice.csv (18 rows), Hefei_amap.csv (136 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 208.0 s, our shortest transcribed peak 3.967 min, lower bound respected; implied daily runs 1853 against 2162.0 planned (ratio net of trams 0.857).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 4.833 | 6.5 | 9.01 | 0.0 | 2023-09-23 | government portal relaying the operator | [ah.people.com.cn](http://ah.people.com.cn/n2/2023/0923/c227131-40582251.html) |
| 2 | 2号线 | operator statement, interval bands for the whole line | 3.967 | 7.0 | 8.6 | 0.0 | 2023-02-27 | government portal relaying the operator | [ah.anhuinews.com](http://ah.anhuinews.com/gdxw/202302/t20230227_6695446.html) |
| 3 | 3号线 | operator statement, interval bands for the whole line | 4.333 | 7.133 | 8.39 | 0.0 | 2023-09-28 | government portal relaying the operator; press quoting the operator | [tidenews.com.cn](https://tidenews.com.cn/news.html?id=2593672) +1 |
| 4 | 4号线 | operator statement, interval bands for the whole line | 4.833 | 9.0 | 7.29 | 0.0 | 2023-09-23 | government portal relaying the operator | [ah.people.com.cn](http://ah.people.com.cn/n2/2023/0923/c227131-40582251.html) |
| 5 | 5号线 | operator statement, interval bands for the whole line | 5.5 | 8.0 | 7.23 | 0.0 | 2023-09-23 | government portal relaying the operator | [ah.people.com.cn](http://ah.people.com.cn/n2/2023/0923/c227131-40582251.html) |
| 6 | 8号线 | operator statement, interval bands for the whole line | 5.5 | 8.0 | 7.19 | 0.0 | 2024-12-25 | government portal relaying the operator | [ah.people.com.cn](http://ah.people.com.cn/n2/2024/1225/c227142-41086611.html) |

### Hohhot

Operator: . 2 routes. Basis: press_quoted_operator_notice 2. URLs opened in the survey log: 4. Band files: Hohhot_notice.csv (10 rows), Hohhot_amap.csv (44 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 360.0 s, our shortest transcribed peak 6.0 min, lower bound respected; implied daily runs 437 against 460.0 planned (ratio net of trams 0.95).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 6.0 | 15.0 | 5.74 | 0.0 | 2023-04-06 | press quoting the operator | [static.0471tv.org.cn](https://static.0471tv.org.cn/rb/pc/con/202304/07/content_23038.html) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 6.0 | 15.0 | 5.76 | 0.0 | 2023-04-06 | press quoting the operator | [static.0471tv.org.cn](https://static.0471tv.org.cn/rb/pc/con/202304/07/content_23038.html) |

### Jinan

Operator: . 3 routes. Basis: press_quoted_operator_notice 2, amap_interval_band 1. URLs opened in the survey log: 6. Band files: Jinan_notice.csv (7 rows), Jinan_amap.csv (52 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 270.0 s, our shortest transcribed peak 5.0 min, lower bound respected; implied daily runs 798 against 939.0 planned (ratio net of trams 1.161).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | Amap interval bands (undated, passed the acceptance test) | 7.0 | 9.0 | 5.89 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通1号线&city=<city>&extensions=all) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 5.0 | 7.5 | 8.04 | 0.235 | 2024-08-26 | press quoting the operator | [sd.news.cn](http://sd.news.cn/20240826/905d14536ac546d8a085fe98c03da1ef/c.html) |
| 3 | 3号线 | press or government relay quoting the operator's notice | 5.0 | 15.0 | 7.03 | 0.11 | 2024-11-22 | press quoting the operator | [sd.xinhua.org](http://www.sd.xinhua.org/20241122/8e1e9dd6d6494112bb89ecd8da2d2c03/c.html) |

### Jinhua

Operator: . 2 routes. Basis: published_peak_offpeak_only 2. URLs opened in the survey log: 4. Band files: Jinhua_notice.csv (2 rows), Jinhua_amap.csv (10 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 600.0 s, our shortest transcribed peak 11.163 min, lower bound respected; implied daily runs 314 against 411.0 planned (ratio net of trams 0.763).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 金义东线金义段 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 11.163 | 15.0 | 3.96 | 0.865 | 2024-08-26 | press quoting the operator | [sd.news.cn](http://sd.news.cn/20240826/905d14536ac546d8a085fe98c03da1ef/c.html) |
| 2 | 金义东线义东段 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 11.163 | 15.0 | 4.22 | 0.87 | 2024-08-26 | press quoting the operator | [sd.news.cn](http://sd.news.cn/20240826/905d14536ac546d8a085fe98c03da1ef/c.html) |

### Kunming

Operator: 昆明轨道交通有限公司. 7 routes. Basis: amap_interval_band 3, published_peak_offpeak_only 2, inherited_from_trunk 1, press_quoted_operator_notice 1. URLs opened in the survey log: 16. Band files: Kunming_notice.csv (19 rows), Kunming_amap.csv (92 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 230.0 s, our shortest transcribed peak 4.0 min, lower bound respected; implied daily runs 1576 against 1530.0 planned (ratio net of trams 1.03).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | inherited from the trunk route of the same line | 7.667 | 9.667 | 5.96 | 0.261 | 2025-04-20 | press quoting the operator | [yn.xinhuanet.com](http://www.yn.xinhuanet.com/20250420/569121d264a7477ab550db128393ae06/c.html) |
| 2 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.5 | 6.944 | 7.79 | 0.784 | 2025-04-20 | press quoting the operator | [yn.xinhuanet.com](http://www.yn.xinhuanet.com/20250420/569121d264a7477ab550db128393ae06/c.html) |
| 3 | 4号线 | Amap interval bands (undated, passed the acceptance test) | 6.0 | 8.0 | 7.05 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁4号线&city=<city>&extensions=all) |
| 4 | 5号线 | Amap interval bands (undated, passed the acceptance test) | 6.0 | 8.0 | 7.09 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁5号线&city=<city>&extensions=all) |
| 5 | 6号线 | press or government relay quoting the operator's notice | 10.0 | 10.0 | 5.05 | 0.0 | 2025-04-20 | press quoting the operator | [yn.xinhuanet.com](http://www.yn.xinhuanet.com/20250420/569121d264a7477ab550db128393ae06/c.html) |
| 6 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.667 | 9.667 | 6.28 | 0.901 | 2025-04-20 | press quoting the operator | [yn.xinhuanet.com](http://www.yn.xinhuanet.com/20250420/569121d264a7477ab550db128393ae06/c.html) |
| 7 | 2号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 7.0 | 8.49 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁2号线&city=<city>&extensions=all) |

### Lanzhou

Operator: . 2 routes. Basis: published_interval_band_line 1, press_quoted_operator_notice 1. URLs opened in the survey log: 7. Band files: Lanzhou_notice.csv (11 rows), Lanzhou_amap.csv (16 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 240.0 s, our shortest transcribed peak 6.333 min, lower bound respected; implied daily runs 477 against 593.0 planned (ratio net of trams 0.804).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 6.333 | 8.667 | 6.3 | 0.001 | 2021-11-15 | operator website | [lzgdjt.com](https://www.lzgdjt.com/lzgd/detail.jsp?contentId=45945) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 6.333 | 8.667 | 6.24 | 0.0 | 2023-06-29 | press quoting the operator | [gs.people.com.cn](http://gs.people.com.cn/n2/2023/0629/c183348-40475709.html) |

### Luoyang

Operator: 洛阳市轨道交通集团有限责任公司. 2 routes. Basis: published_interval_band_line 2. URLs opened in the survey log: 7. Band files: Luoyang_notice.csv (10 rows), Luoyang_amap.csv (32 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 360.0 s, our shortest transcribed peak 7.0 min, lower bound respected; implied daily runs 414 against 473.0 planned (ratio net of trams 0.875).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 7.0 | 10.0 | 5.35 | 0.0 | 2025-03-28 | operator website | [lysubway.com.cn](https://www.lysubway.com.cn/company_info/detail/2997.html) |
| 2 | 2号线 | operator statement, interval bands for the whole line | 7.0 | 10.0 | 5.44 | 0.0 | 2025-03-28 | operator website | [lysubway.com.cn](https://www.lysubway.com.cn/company_info/detail/2997.html) |

### Nanchang

Operator: 南昌轨道交通集团. 7 routes. Basis: published_peak_offpeak_only 5, published_interval_band_line 2. URLs opened in the survey log: 6. Band files: Nanchang_notice.csv (9 rows), Nanchang_amap.csv (52 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 236.0 s, our shortest transcribed peak 3.933 min, lower bound respected; implied daily runs 1372 against 1545.0 planned (ratio net of trams 0.888).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.933 | 6.0 | 10.9 | 0.3 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 2 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.933 | 6.0 | 10.37 | 0.252 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 3 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.933 | 6.0 | 11.33 | 0.322 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 4 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.3 | 6.0 | 9.68 | 0.774 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |
| 5 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.3 | 6.0 | 7.7 | 0.743 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |
| 6 | 3号线 | operator statement, interval bands for the whole line | 5.4 | 6.0 | 8.92 | 0.0 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |
| 7 | 4号线 | operator statement, interval bands for the whole line | 5.9 | 6.5 | 8.21 | 0.0 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |

### Nanjing

Operator: 南京地铁集团有限公司. 13 routes. Basis: amap_interval_band 5, published_peak_offpeak_only 4, transcription_2025_unsourced 4. URLs opened in the survey log: 30. Band files: Nanjing_notice.csv (28 rows), Nanjing_amap.csv (73 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 120.0 s, our shortest transcribed peak 2.0 min, lower bound respected; implied daily runs 4164 against 4474.0 planned (ratio net of trams 0.961).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | Amap interval bands (undated, passed the acceptance test) | 2.0 | 4.0 | 16.99 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁1号线&city=<city>&extensions=all) +1 |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.5 | 5.128 | 12.14 | 0.768 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 3 | 3号线 | 2025 constant, no source |  |  | 10.5 |  |  |  | none |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.667 | 6.186 | 9.05 | 0.53 | 2018-07-16 | press quoting the operator | [jsnews.jschina.com.cn](https://jsnews.jschina.com.cn/nj/a/201807/t20180716_1761701.shtml) |
| 5 | 5号线 | 2025 constant, no source |  |  | 7.2 |  |  |  | none |
| 6 | 7号线 | Amap interval bands (undated, passed the acceptance test) | 7.0 | 10.0 | 7.12 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁3号线&city=<city>&extensions=all) |
| 7 | 10号线 | Amap interval bands (undated, passed the acceptance test) | 5.0 | 9.0 | 8.59 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁4号线&city=<city>&extensions=all) +1 |
| 11 | S1号线(机场线) | 2025 constant, no source |  |  | 11.7 |  |  |  | none |
| 12 | S3号线(宁和线) | 2025 constant, no source |  |  | 6.3 |  |  |  | none |
| 13 | S6号线(宁句线) | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 10.714 | 5.64 | 0.36 | 2023-04-25 | operator website; press quoting the operator | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) +1 |
| 14 | S7号线(宁溧线) | Amap interval bands (undated, passed the acceptance test) | 14.0 | 14.0 | 3.6 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁S7号线(宁溧线)&city=<city>&extensions=all) |
| 15 | S8号线(宁天线) | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.383 | 8.955 | 6.44 | 0.876 | 2022-09-30 | press quoting the operator | [ourjiangsu.com](http://www.ourjiangsu.com/a/20220930/1664531192871.shtml) |
| 16 | S9号线(宁高线) | Amap interval bands (undated, passed the acceptance test) | 12.0 | 12.0 | 4.21 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁S9号线(宁高线)&city=<city>&extensions=all) |

### Nanning

Operator: 南宁轨道交通集团. 5 routes. Basis: press_quoted_operator_notice 5. URLs opened in the survey log: 13. Band files: Nanning_notice.csv (17 rows), Nanning_amap.csv (153 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 210.0 s, our shortest transcribed peak 3.5 min, lower bound respected; implied daily runs 1514 against 1798.0 planned (ratio net of trams 0.842).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 3.5 | 7.0 | 8.41 | 0.0 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 4.5 | 7.0 | 8.45 | 0.0 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 3 | 3号线 | press or government relay quoting the operator's notice | 4.5 | 7.0 | 8.5 | 0.0 | 2023-04-25 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_4/820.html) |
| 4 | 4号线 | press or government relay quoting the operator's notice | 5.0 | 8.0 | 7.38 | 0.0 | 2025-08-29 | operator website | [ncmtr.com](https://www.ncmtr.com/topic_detail_20/8.html) +1 |
| 5 | 5号线 | press or government relay quoting the operator's notice | 6.0 | 8.0 | 7.01 | 0.0 | 2026-05-13 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20260513A04WV400) +1 |

### Nantong

Operator: . 2 routes. Basis: published_interval_band_line 1, press_quoted_operator_notice 1. URLs opened in the survey log: 15. Band files: Nantong_notice.csv (12 rows), Nantong_amap.csv (10 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 390.0 s, our shortest transcribed peak 6.833 min, lower bound respected; implied daily runs 461 against 560.0 planned (ratio net of trams 0.823).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 6.833 | 10.0 | 6.24 | 0.0 | 2025-04-14 | operator website; press quoting the operator | [m.thepaper.cn](https://m.thepaper.cn/newsDetail_forward_30645785) +1 |
| 2 | 2号线 | press or government relay quoting the operator's notice | 6.833 | 9.833 | 5.84 | 0.0 | 2023-12-24 | press quoting the operator | [ourjiangsu.com](http://www.ourjiangsu.com/a/20231224/1703409361308.shtml) |

### Ningbo

Operator: 宁波轨道交通集团. 7 routes. Basis: press_quoted_operator_notice 5, published_interval_band_line 1, amap_interval_band 1. URLs opened in the survey log: 5. Band files: Ningbo_notice.csv (21 rows), Ningbo_amap.csv (54 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 238.0 s, our shortest transcribed peak 4.0 min, lower bound respected; implied daily runs 2060 against 2765.0 planned (ratio net of trams 0.745).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 4.0 | 10.0 | 7.75 | 0.0 | 2020-12-08 | press quoting the operator | [nb.ifeng.com](https://nb.ifeng.com/c/820lJtubPlg) |
| 2 | 2号线 | operator statement, interval bands for the whole line | 4.333 | 10.0 | 9.33 | 0.0 | 2023-05-08 | government portal relaying the operator; press quoting the operator | [zjnews.zjol.com.cn](https://zjnews.zjol.com.cn/zjnews/202305/t20230506_25711126.shtml) +1 |
| 3 | 3号线 | press or government relay quoting the operator's notice | 4.5 | 10.0 | 5.64 | 0.0 | 2020-12-08 | press quoting the operator | [nb.ifeng.com](https://nb.ifeng.com/c/820lJtubPlg) |
| 4 | 4号线 | press or government relay quoting the operator's notice | 4.417 | 10.0 | 8.09 | 0.0 | 2020-12-08 | press quoting the operator | [nb.ifeng.com](https://nb.ifeng.com/c/820lJtubPlg) |
| 5 | 5号线 | press or government relay quoting the operator's notice | 4.967 | 7.667 | 8.5 | 0.0 | 2021-12-27 | press quoting the operator | [m.jiemian.com](https://m.jiemian.com/article/6952766.html) |
| 6 | 8号线 | press or government relay quoting the operator's notice | 6.0 | 10.0 | 6.53 | 0.0 | 2025-06-27 | press quoting the operator | [m.nb.bendibao.com](https://m.nb.bendibao.com/news/93330.shtm) |
| 7 | 轨道交通7号线 | Amap interval bands (undated, passed the acceptance test) | 9.156 | 9.156 | 6.55 |  |  |  |  |

### Qingdao

Operator: 青岛地铁集团. 9 routes. Basis: press_quoted_operator_notice 9. URLs opened in the survey log: 9. Band files: Qingdao_notice.csv (58 rows), Qingdao_amap.csv (123 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 145.0 s, our shortest transcribed peak 3.167 min, lower bound respected; implied daily runs 2043 against 2746.0 planned (ratio net of trams 0.762).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 3.725 | 8.084 | 8.24 | 0.012 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 2 | 2号线 | press or government relay quoting the operator's notice | 3.167 | 9.75 | 8.94 | 0.033 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 3 | 3号线 | press or government relay quoting the operator's notice | 3.458 | 9.75 | 8.65 | 0.036 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 4 | 4号线 | press or government relay quoting the operator's notice | 5.0 | 16.2 | 7.4 | 0.058 | 2025-06-16 | press quoting the operator | [m.qd.bendibao.com](https://m.qd.bendibao.com/traffic/84210.shtm) |
| 5 | 6号线 | press or government relay quoting the operator's notice | 7.667 | 15.25 | 4.13 | 0.041 | 2025-06-16 | press quoting the operator | [m.qd.bendibao.com](https://m.qd.bendibao.com/traffic/84210.shtm) |
| 6 | 8号线 | press or government relay quoting the operator's notice | 8.416 | 12.083 | 4.52 | 0.022 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 7 | 3号线 | press or government relay quoting the operator's notice | 3.458 | 9.75 | 8.64 | 0.0 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 8 | 蓝谷快线 | press or government relay quoting the operator's notice | 6.292 | 19.667 | 5.59 | 0.027 | 2025-08-29 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250829A021UM00) +1 |
| 9 | 西海岸快线 | press or government relay quoting the operator's notice | 6.042 | 19.333 | 2.87 | 0.029 | 2025-06-16 | press quoting the operator | [m.qd.bendibao.com](https://m.qd.bendibao.com/traffic/84210.shtm) |

### Shanghai

Operator: 上海申通地铁集团有限公司. 23 routes. Basis: published_interval_band_section 22, published_average_interval 1. No survey log: transcribed from the operator's own interval table. Band files: Shanghai.csv (250 rows), Shanghai_amap.csv (391 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 110.0 s, our shortest transcribed peak 1.833 min, lower bound respected; implied daily runs 7425 against 9957.0 planned (ratio net of trams 0.839).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands per section | 2.5 | 6.5 | 12.28 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 2 | 2号线 | operator statement, interval bands per section | 2.5 | 7.5 | 10.79 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 3 | 3号线 | operator statement, interval bands per section | 4.0 | 9.0 | 7.66 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 4 | 4号线 | operator statement, interval bands per section | 4.0 | 11.0 | 7.4 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 5 | 4号线 | operator statement, interval bands per section | 4.0 | 11.0 | 7.4 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 6 | 5号线 | operator statement, interval bands per section | 2.5 | 12.0 | 7.33 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 7 | 6号线 | operator statement, interval bands per section | 2.0 | 11.0 | 9.91 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 8 | 7号线 | operator statement, interval bands per section | 2.0 | 10.5 | 9.82 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 9 | 8号线 | operator statement, interval bands per section | 2.0 | 11.0 | 9.81 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 10 | 9号线 | operator statement, interval bands per section | 1.833 | 9.0 | 9.44 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 11 | 13号线 | operator statement, interval bands per section | 2.75 | 8.0 | 10.28 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 12 | 14号线 | operator statement, interval bands per section | 3.0 | 8.5 | 6.78 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 13 | 15号线 | operator statement, interval bands per section | 3.333 | 9.0 | 8.57 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 14 | 16号线 | operator statement, interval bands per section | 3.5 | 10.0 | 10.22 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 15 | 17号线 | operator statement, interval bands per section | 3.0 | 10.0 | 8.64 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 16 | 18号线 | operator statement, interval bands per section | 2.75 | 10.0 | 8.24 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 17 | 浦江线 | operator statement, interval bands per section | 4.25 | 10.0 | 6.85 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 18 | 10号线 | operator statement, interval bands per section | 7.875 | 12.0 | 5.19 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 19 | 10号线 | operator statement, interval bands per section | 2.5 | 10.0 | 8.9 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 20 | 11号线 | operator statement, interval bands per section | 6.0 | 12.0 | 5.06 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 21 | 11号线 | operator statement, interval bands per section | 2.0 | 12.0 | 10.03 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 22 | 12号线 | operator statement, interval bands per section | 2.75 | 7.5 | 10.3 | 0.0 | read 2026-07-25 | operator website | [service.shmetro.com](https://service.shmetro.com/hcskb/index.htm) |
| 23 | 市域机场线 | operator statement, one average interval | 17.815 | 17.815 | 3.37 |  |  |  |  |

### Shaoxing

Operator: . 2 routes. Basis: press_quoted_operator_notice 2. URLs opened in the survey log: 9. Band files: Shaoxing_notice.csv (6 rows), Shaoxing_amap.csv (10 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 360.0 s, our shortest transcribed peak 6.0 min, lower bound respected; implied daily runs 536 against 1242.0 planned (ratio net of trams 0.432).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 (含支线) | press or government relay quoting the operator's notice | 6.0 | 15.0 | 7.62 | 0.0 | 2024-04-01 | press quoting the operator | [zjnews.zjol.com.cn](https://zjnews.zjol.com.cn/zjnews/202404/t20240401_26748587.shtml) +1 |
| 2 | 2号线 | press or government relay quoting the operator's notice | 8.0 | 8.0 | 6.49 | 0.0 | 2023-07-26 | press quoting the operator | [tidenews.com.cn](https://tidenews.com.cn/news.html?id=2533830) |

### Shenyang

Operator: 沈阳地铁巴士公交公司. 6 routes. Basis: published_peak_offpeak_only 6. URLs opened in the survey log: 19. Band files: Shenyang_notice.csv (10 rows), Shenyang_amap.csv (21 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 175.0 s, our shortest transcribed peak 2.917 min, lower bound respected; implied daily runs 1925 against 2379.0 planned (ratio net of trams 1.228).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.917 | 5.396 | 10.55 | 0.884 | 2025-06-04 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250604A08OCL00) |
| 2 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.667 | 8.334 | 6.47 | 0.879 | 2024-12-29 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/F4Lqpl87FZY32R9sFy1H7w) |
| 3 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.75 | 7.188 | 7.91 | 0.886 | 2023-09-27 | press quoting the operator | [m.gmw.cn](https://m.gmw.cn/2023-09/27/content_1303526189.htm) |
| 4 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.5 | 7.37 | 0.885 | 2023-04-27 | government portal relaying the operator | [shenyang.gov.cn](https://www.shenyang.gov.cn/zwgk/zwdt/bxgz/202304/t20230427_4456421.html) |
| 5 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.117 | 7.646 | 7.43 | 0.886 | 2023-04-27 | government portal relaying the operator | [shenyang.gov.cn](https://www.shenyang.gov.cn/zwgk/zwdt/bxgz/202304/t20230427_4456421.html) |
| 6 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.0 | 8.0 | 10.52 | 0.884 | 2025-06-29 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Dq1oKg5ZBo-kWvTuEWOXyA) |

### Shenzhen

Operators: 深圳市地铁集团有限公司; 港铁轨道交通(深圳)有限公司. 16 routes. Basis: published_peak_offpeak_only 9, published_interval_band_section 2, amap_interval_band 2, published_interval_band_line 2, published_average_interval 1. URLs opened in the survey log: 24. Band files: Shenzhen_notice.csv (47 rows), Shenzhen_amap.csv (100 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 115.0 s, our shortest transcribed peak 1.917 min, lower bound respected; implied daily runs 6555 against 7754.0 planned (ratio net of trams 0.872).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线/罗宝线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 1.917 | 2.727 | 19.86 | 0.431 | 2025-06-29 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Dq1oKg5ZBo-kWvTuEWOXyA) |
| 2 | 2号线/8号线 | operator statement, interval bands per section | 2.5 | 6.417 | 9.14 | 0.0 | 2025-06-29 | operator website; operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Dq1oKg5ZBo-kWvTuEWOXyA) +1 |
| 3 | 3号线/龙岗线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.0 | 3.529 | 15.61 | 0.942 | 2025-06-29 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/Dq1oKg5ZBo-kWvTuEWOXyA) |
| 4 | 4号线/龙华线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.4 | 6.0 | 13.07 | 0.332 | 2023-11-23 | press quoting the operator | [finance.sina.com.cn](https://finance.sina.com.cn/jjxw/2023-11-23/doc-imzvreks5479038.shtml) +1 |
| 5 | 5号线/环中线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.0 | 4.1 | 13.56 | 0.854 | 2025-06-04 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20250604A08OCL00) |
| 6 | 6号线/光明线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.333 | 6.0 | 10.04 | 0.925 | 2024-12-29 | government portal relaying the operator; operator WeChat; press quoting the operator | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/F4Lqpl87FZY32R9sFy1H7w) +2 |
| 7 | 6号线支线 | operator statement, one average interval | 7.717 | 7.717 | 6.79 | 0.0 | 2023-04-27 | government portal relaying the operator | [shenyang.gov.cn](https://www.shenyang.gov.cn/zwgk/zwdt/bxgz/202304/t20230427_4456421.html) |
| 8 | 7号线/西丽线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.333 | 7.583 | 9.44 | 0.292 | 2025-02-12 | press quoting the operator | [thepaper.cn](https://www.thepaper.cn/newsDetail_forward_30141433) |
| 9 | 9号线/梅林线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 8.0 | 7.01 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁9号线&city=<city>&extensions=all) |
| 10 | 10号线/坂田线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.167 | 7.5 | 9.87 | 0.311 | 2025-02-12 | government portal relaying the operator; press quoting the operator | [thepaper.cn](https://www.thepaper.cn/newsDetail_forward_30141433) +2 |
| 11 | 11号线/机场线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.183 | 5.0 | 11.44 | 0.914 | 2025-06-30 | government portal relaying the operator | [sz.gov.cn](https://www.sz.gov.cn/cn/xxgk/bmtx/content/post_12255035.html) |
| 12 | 12号线/南宝线 | operator statement, interval bands per section | 3.8 | 6.0 | 9.44 | 0.0 | 2024-01-02 | government portal relaying the operator | [jtys.sz.gov.cn](http://jtys.sz.gov.cn/ydmh/jtzx/zyhy_1510/content/post_11081873.html) |
| 13 | 14号线/东部快线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.333 | 6.334 | 10.08 | 0.865 | 2025-06-30 | government portal relaying the operator | [sz.gov.cn](https://www.sz.gov.cn/cn/xxgk/bmtx/content/post_12255035.html) |
| 14 | 16号线/龙坪线 | operator statement, interval bands for the whole line | 4.833 | 7.5 | 8.08 | 0.0 | 2025-09-29 | operator website | [szmc.net](https://www.szmc.net/home/xinwenzhongxin/gongsixinwen/202509/105275.html) |
| 15 | 20号线 | operator statement, interval bands for the whole line | 7.75 | 8.451 | 6.04 | 0.205 | 2025-05-22 | government portal relaying the operator; press quoting the operator | [jtys.sz.gov.cn](https://jtys.sz.gov.cn/ydmh/jtcx/dtcx_180970/cxtx/content/post_12190669.html) +1 |
| 16 | 13号线/石岩线 | Amap interval bands (undated, passed the acceptance test) | 5.0 | 6.0 | 9.0 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁13号线(石岩线)&city=<city>&extensions=all) |

### Shijiazhuang

Operator: 石家庄市轨道交通有限责任公司. 3 routes. Basis: published_interval_band_line 3. URLs opened in the survey log: 9. Band files: Shijiazhuang_notice.csv (12 rows), Shijiazhuang_amap.csv (48 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 300.0 s, our shortest transcribed peak 5.0 min, lower bound respected; implied daily runs 780 against 927.0 planned (ratio net of trams 0.841).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 2号线 | operator statement, interval bands for the whole line | 6.5 | 8.0 | 6.65 | 0.0 | 2024-09-30 | operator website | [sjzmetro.cn](http://www.sjzmetro.cn/service/notice/7899.html) +1 |
| 2 | 3号线 | operator statement, interval bands for the whole line | 6.5 | 8.0 | 6.53 | 0.0 | 2024-09-30 | operator website | [sjzmetro.cn](http://www.sjzmetro.cn/service/notice/7899.html) +1 |
| 3 | 1号线 | operator statement, interval bands for the whole line | 5.0 | 8.0 | 7.28 | 0.0 | 2024-09-30 | operator website | [sjzmetro.cn](http://www.sjzmetro.cn/service/notice/7899.html) +1 |

### Suzhou

Operator: 苏州市轨道交通集团有限公司. 9 routes. Basis: published_peak_offpeak_only 6, amap_interval_band 2, press_quoted_operator_notice 1. URLs opened in the survey log: 10. Band files: Suzhou_notice.csv (18 rows), Suzhou_amap.csv (159 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 120.0 s, our shortest transcribed peak 2.0 min, lower bound respected; implied daily runs 2930 against 4357.0 planned (ratio net of trams 0.772).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.0 | 4.95 | 12.43 | 0.443 | 2022-09-04 | operator website | [sz-mtr.com](https://www.sz-mtr.com/service/information/notice/202210/992A7FF5.html) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.5 | 7.101 | 9.42 | 0.886 | 2022-09-04 | operator website | [sz-mtr.com](https://www.sz-mtr.com/service/information/notice/202210/992A7FF5.html) |
| 3 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.001 | 8.26 | 0.767 | 2022-07-14 | operator website | [sz-mtr.com](https://www.sz-mtr.com/service/information/notice/202210/7F41B1A6.html) |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.333 | 7.101 | 8.46 | 0.367 | 2026-08-05 | government portal relaying the operator; operator website | [suzhou.gov.cn](https://www.suzhou.gov.cn/szsrmzf/mszx/202608/40056068bce34b68b418b25cf29221cc.shtml) +1 |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.299 | 7.68 | 0.443 | 2022-07-14 | operator website | [sz-mtr.com](https://www.sz-mtr.com/service/information/notice/202210/7F41B1A6.html) |
| 6 | 6号线 | Amap interval bands (undated, passed the acceptance test) | 6.0 | 7.0 | 7.78 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通6号线&city=<city>&extensions=all) |
| 7 | 7号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.001 | 7.77 | 0.276 | 2024-11-29 | press quoting the operator | [news.2500sz.com](https://news.2500sz.com/doc/2024/11/29/1120220.shtml) |
| 8 | 8号线 | Amap interval bands (undated, passed the acceptance test) | 6.0 | 7.0 | 7.78 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通8号线&city=<city>&extensions=all) |
| 9 | 11号线 | press or government relay quoting the operator's notice | 7.0 | 8.0 | 7.14 | 0.236 | 2023-06-14 | press quoting the operator | [news.qq.com](https://news.qq.com/rain/a/20230614A05T4F00) |

### Taiyuan

Operator: . 2 routes. Basis: published_interval_band_line 1, press_quoted_operator_notice 1. URLs opened in the survey log: 18. Band files: Taiyuan_notice.csv (6 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 390.0 s, our shortest transcribed peak 6.5 min, lower bound respected; implied daily runs 549 against 559.0 planned (ratio net of trams 0.982).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 6.5 | 6.5 | 7.77 | 0.0 | 2025-02-18 | operator WeChat | [mp.weixin.qq.com](https://mp.weixin.qq.com/s/4GgR0_QsmFn1NJHhAPlsRw) |
| 2 | 2号线 | press or government relay quoting the operator's notice | 6.5 | 8.0 | 6.68 | 0.0 | 2023-12-20 | press quoting the operator | [sx.xinhuanet.com](http://www.sx.xinhuanet.com/20231221/803b8927c5bd4a5784750a7be894fe82/c.html) |

### Taizhou

Operator: . 1 routes. Basis: published_peak_offpeak_only 1. URLs opened in the survey log: 5. Band files: Taizhou_notice.csv (3 rows), Taizhou_amap.csv (16 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.5 | 9.39 | 6.9 | 0.314 | 2023-12-20 | press quoting the operator | [sx.xinhuanet.com](http://www.sx.xinhuanet.com/20231221/803b8927c5bd4a5784750a7be894fe82/c.html) |

### Tianjin

Operator: 天津轨道交通运营集团有限公司. 12 routes. Basis: published_peak_offpeak_only 7, amap_interval_band 4, press_quoted_operator_notice 1. URLs opened in the survey log: 26. Band files: Tianjin_notice.csv (17 rows), Tianjin_amap.csv (214 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 180.0 s, our shortest transcribed peak 3.25 min, lower bound respected; implied daily runs 3027 against 4020.0 planned (ratio net of trams 0.753).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.25 | 4.525 | 11.95 | 0.88 | 2023-03-15 | press quoting the operator | [cnr.cn](https://www.cnr.cn/tj/tjyw/20230316/t20230316_526184572.shtml) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.2 | 7.5 | 7.57 | 0.391 | 2026-04-22 | press quoting the operator | [tidenews.com.cn](https://tidenews.com.cn/tmh_news.html?id=69e8dcf7385477000171adac) |
| 3 | 3号线 | press or government relay quoting the operator's notice | 4.8 | 7.5 | 8.53 | 0.25 | 2025-01-11 | press quoting the operator | [tj.people.com.cn](http://tj.people.com.cn/n2/2025/0112/c375366-41105343.html) +1 |
| 4 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.8 | 6.667 | 8.92 | 0.707 | 2023-03-15 | press quoting the operator | [cnr.cn](https://www.cnr.cn/tj/tjyw/20230316/t20230316_526184572.shtml) |
| 5 | 6号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 8.0 | 8.24 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁6号线&city=<city>&extensions=all) |
| 6 | 4号线 | Amap interval bands (undated, passed the acceptance test) | 10.0 | 10.0 | 5.26 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁4号线&city=<city>&extensions=all) |
| 7 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.5 | 8.0 | 8.14 | 0.276 | 2021-12-27 | press quoting the operator | [tj.sina.cn](http://tj.sina.cn/news/2021-12-27/detail-ikyamrmz1430622.d.html) |
| 8 | 6号线 | Amap interval bands (undated, passed the acceptance test) | 5.0 | 10.0 | 6.87 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁6号线&city=<city>&extensions=all) |
| 9 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.5 | 6.667 | 9.01 | 0.71 | 2023-03-15 | press quoting the operator | [cnr.cn](https://www.cnr.cn/tj/tjyw/20230316/t20230316_526184572.shtml) |
| 10 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.5 | 7.6 | 0.883 | 2022-11-17 | press quoting the operator | [tj.people.com.cn](http://tj.people.com.cn/n2/2022/1117/c375366-40198472.html) |
| 11 | 津静线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 10.0 | 15.0 | 4.05 | 0.258 | 2024-09-28 | press quoting the operator | [epaper.tianjinwe.com](https://epaper.tianjinwe.com/tjrb/html/2024-09/28/content_143082_1339151.htm) |
| 12 | 11号线 | Amap interval bands (undated, passed the acceptance test) | 5.0 | 9.0 | 7.31 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁11号线&city=<city>&extensions=all) |

### Wenzhou

Operator: . 2 routes. Basis: published_interval_band_line 1, published_peak_offpeak_only 1. URLs opened in the survey log: 4. Band files: Wenzhou_notice.csv (6 rows), Wenzhou_amap.csv (34 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 300.0 s, our shortest transcribed peak 9.283 min, lower bound respected; implied daily runs 394 against 455.0 planned (ratio net of trams 0.866).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1线 | operator statement, interval bands for the whole line | 9.283 | 10.0 | 4.52 | 0.229 | 2025-05-06 | government portal relaying the operator | [leaders.people.com.cn](http://leaders.people.com.cn/n1/2025/0506/c58278-40473845.html) |
| 2 | S2线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 9.283 | 10.0 | 5.23 | 0.271 | 2025-05-06 | government portal relaying the operator | [leaders.people.com.cn](http://leaders.people.com.cn/n1/2025/0506/c58278-40473845.html) |

### Wuhan

Operator: 武汉地铁集团有限公司. 12 routes. Basis: published_peak_offpeak_only 6, amap_interval_band 3, transcription_2025_unsourced 3. URLs opened in the survey log: 8. Band files: Wuhan_notice.csv (9 rows), Wuhan_amap.csv (68 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 150.0 s, our shortest transcribed peak 2.7 min, lower bound respected; implied daily runs 4249 against 5196.0 planned (ratio net of trams 0.927).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.3 | 4.858 | 11.85 | 0.825 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) +1 |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.7 | 4.532 | 12.99 | 0.827 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) +1 |
| 3 | 3号线 | Amap interval bands (undated, passed the acceptance test) | 4.0 | 6.0 | 8.95 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通3号线&city=<city>&extensions=all) |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.7 | 4.435 | 12.41 | 0.941 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 5.231 | 10.83 | 0.77 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) |
| 6 | 7号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.5 | 5.964 | 8.98 | 0.941 | 2023-02-13 | government portal relaying the operator | [jtj.wuhan.gov.cn](https://jtj.wuhan.gov.cn/jtzx/zwdt/202302/t20230213_2151487.shtml) |
| 7 | 8号线 | 2025 constant, no source |  |  | 8.88 |  |  |  | none |
| 8 | 11号线 | 2025 constant, no source |  |  | 8.59 |  |  |  | none |
| 9 | 16号线 | Amap interval bands (undated, passed the acceptance test) | 9.0 | 9.0 | 5.58 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通16号线&city=<city>&extensions=all) |
| 10 | 19号线 | Amap interval bands (undated, passed the acceptance test) | 9.0 | 9.0 | 5.7 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=轨道交通19号线&city=<city>&extensions=all) |
| 11 | 阳逻线 | 2025 constant, no source |  |  | 8.29 |  |  |  | none |
| 12 | 6号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 7.238 | 7.36 | 0.942 | 2023-02-13 | government portal relaying the operator | [jtj.wuhan.gov.cn](https://jtj.wuhan.gov.cn/jtzx/zwdt/202302/t20230213_2151487.shtml) |

### Wuhu

Operator: . 2 routes. Basis: published_peak_offpeak_only 2. URLs opened in the survey log: 6. Band files: Wuhu_notice.csv (2 rows), Wuhu_amap.csv (8 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 334.0 s, our shortest transcribed peak 5.567 min, lower bound respected; implied daily runs 417 against 597.0 planned (ratio net of trams 0.698).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.817 | 11.634 | 5.29 | 0.746 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.567 | 11.134 | 5.66 | 0.749 | 2025-03-06 | government portal relaying the operator | [wuhan.gov.cn](https://www.wuhan.gov.cn/hdjl/rdhy/202503/t20250306_2548208.shtml) |

### Wuxi

Operator: 无锡市地铁集团有限公司. 4 routes. Basis: published_peak_offpeak_only 3, press_quoted_operator_notice 1. URLs opened in the survey log: 11. Band files: Wuxi_notice.csv (10 rows), Wuxi_amap.csv (67 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 300.0 s, our shortest transcribed peak 5.0 min, lower bound respected; implied daily runs 1060 against 1521.0 planned (ratio net of trams 0.697).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 (含 S1线 贯通运营) | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.5 | 7.67 | 0.429 | 2023-12-02 | press quoting the operator | [sina.cn](https://www.sina.cn/news/detail/4974439865780381.html) |
| 3 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 7.5 | 8.07 | 0.258 | 2024-10-30 | press quoting the operator | [m.163.com](https://m.163.com/dy/article/JFOA2TEQ0512GU5O.html) |
| 4 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.742 | 10.0 | 6.53 | 0.287 | 2024-07-04 | government portal relaying the operator | [wnd.gov.cn](https://www.wnd.gov.cn/doc/2024/07/04/4343501.shtml) |
| 5 | 4号线 | press or government relay quoting the operator's notice | 8.0 | 9.8 | 5.6 | 0.0 | 2021-12-22 | press quoting the operator | [m.wx.bendibao.com](https://m.wx.bendibao.com/traffic/59238.shtm) |

### Xiamen

Operator: 厦门轨道交通集团. 3 routes. Basis: published_interval_band_line 1, published_peak_offpeak_only 1, published_interval_band_section 1. URLs opened in the survey log: 6. Band files: Xiamen_notice.csv (12 rows), Xiamen_amap.csv (46 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 160.0 s, our shortest transcribed peak 2.667 min, lower bound respected; implied daily runs 1025 against 1188.0 planned (ratio net of trams 0.863).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 4.167 | 7.5 | 10.02 | 0.233 | 2024-07-19 | government portal relaying the operator; press quoting the operator | [fj.sina.cn](https://fj.sina.cn/hulitoutiao/2024-07-19/detail-incerrqz5375760.d.html) +1 |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.667 | 7.5 | 9.0 | 0.879 | 2023-07-01 | press quoting the operator | [fjdaily.com](https://www.fjdaily.com/app/content/2023-07/01/content_1943403.html) |
| 3 | 3号线 | operator statement, interval bands per section | 5.5 | 13.833 | 5.95 | 0.246 | 2021-07-12 | government portal relaying the operator; press quoting the operator | [fjdaily.com](https://www.fjdaily.com/app/content/2021-07/12/content_1073472.html) +1 |

### Xian

Operator: 西安地下铁道客运公司. 12 routes. Basis: published_peak_offpeak_only 12. URLs opened in the survey log: 10. Band files: Xian_notice.csv (18 rows), Xian_amap.csv (10 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 120.0 s, our shortest transcribed peak 2.467 min, lower bound respected; implied daily runs 3814 against 4543.0 planned (ratio net of trams 0.885).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.967 | 6.0 | 10.2 | 0.886 | 2023-07-01 | press quoting the operator | [fjdaily.com](https://www.fjdaily.com/app/content/2023-07/01/content_1943403.html) |
| 2 | 2号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.467 | 5.0 | 12.34 | 0.887 | 2023-07-01 | press quoting the operator | [fjdaily.com](https://www.fjdaily.com/app/content/2023-07/01/content_1943403.html) |
| 3 | 3号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.5 | 5.0 | 12.0 | 0.883 | 2021-06-18 | government portal relaying the operator | [investxiamen.org.cn](https://www.investxiamen.org.cn/detail/4078.html) |
| 4 | 4号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 3.483 | 6.316 | 9.31 | 0.883 | 2018-11-20 | press quoting the operator | [chinametro.net](https://www.chinametro.net/index.php?m=mobilenewscon&id=539&aid=46077) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.167 | 8.571 | 6.98 | 0.883 | 2021-06-18 | government portal relaying the operator | [investxiamen.org.cn](https://www.investxiamen.org.cn/detail/4078.html) |
| 6 | 6号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 2.733 | 4.444 | 13.06 | 0.824 | 2024-07-19 | government portal relaying the operator; press quoting the operator | [fj.sina.cn](https://fj.sina.cn/hulitoutiao/2024-07-19/detail-incerrqz5375760.d.html) +2 |
| 7 | 8号(环)线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.3 | 5.375 | 10.56 | 0.887 | 2024-12-26 | government portal relaying the operator; press quoting the operator | [pub.cnwest.com](http://pub.cnwest.com/data/content/2025/01/3946.html) +1 |
| 8 | 8号(环)线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.3 | 5.375 | 10.56 | 0.887 | 2024-12-26 | government portal relaying the operator; press quoting the operator | [pub.cnwest.com](http://pub.cnwest.com/data/content/2025/01/3946.html) +1 |
| 9 | 9号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.667 | 7.084 | 7.36 | 0.875 | 2025-09-29 | press quoting the operator | [epaper.sanqin.com](https://epaper.sanqin.com/html/pic/202509/29/36846c03-4a42-4d54-a373-dc411c415edb.pdf) |
| 10 | 10号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.05 | 8.604 | 6.22 | 0.879 | 2025-09-29 | press quoting the operator | [epaper.sanqin.com](https://epaper.sanqin.com/html/pic/202509/29/36846c03-4a42-4d54-a373-dc411c415edb.pdf) +1 |
| 14 | 14号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.9 | 8.625 | 6.07 | 0.879 | 2025-09-29 | press quoting the operator | [epaper.sanqin.com](https://epaper.sanqin.com/html/pic/202509/29/36846c03-4a42-4d54-a373-dc411c415edb.pdf) |
| 16 | 16号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 7.417 | 9.271 | 5.62 | 0.875 | 2025-09-29 | press quoting the operator | [epaper.sanqin.com](https://epaper.sanqin.com/html/pic/202509/29/36846c03-4a42-4d54-a373-dc411c415edb.pdf) |

### Xuzhou

Operator: . 3 routes. Basis: press_quoted_operator_notice 2, published_interval_band_line 1. URLs opened in the survey log: 6. Band files: Xuzhou_notice.csv (11 rows), Xuzhou_amap.csv (26 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 330.0 s, our shortest transcribed peak 5.5 min, lower bound respected; implied daily runs 777 against 890.0 planned (ratio net of trams 0.873).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | operator statement, interval bands for the whole line | 5.5 | 8.667 | 6.82 | 0.0 | 2025-03-21 | operator WeChat; press quoting the operator | [sina.cn](https://www.sina.cn/news/detail/5146692757750392.html) +1 |
| 2 | 2号线 | press or government relay quoting the operator's notice | 6.5 | 8.667 | 6.8 | 0.003 | 2022-12-30 | press quoting the operator | [sohu.com](https://www.sohu.com/a/622921928_121117454) |
| 3 | 3号线 | press or government relay quoting the operator's notice | 6.5 | 9.0 | 6.8 | 0.0 | 2024-12-03 | press quoting the operator | [js.xinhuanet.com](http://www.js.xinhuanet.com/20241203/97e57f50e823403685b6225ec68308d6/c.html) +1 |

### Zhengzhou

Operator: 郑州轨道交通客运公司. 14 routes. Basis: amap_interval_band 7, published_peak_offpeak_only 5, press_quoted_operator_notice 1, published_interval_band_line 1. URLs opened in the survey log: 28. Band files: Zhengzhou_notice.csv (40 rows), Zhengzhou_amap.csv (127 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 170.0 s, our shortest transcribed peak 3.0 min, lower bound respected; implied daily runs 3147 against 3611.0 planned (ratio net of trams 0.871).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | Amap interval bands (undated, passed the acceptance test) | 3.0 | 8.0 | 9.49 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁1号线&city=<city>&extensions=all) |
| 2 | 2号线 | Amap interval bands (undated, passed the acceptance test) | 3.0 | 10.0 | 10.13 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁2号线&city=<city>&extensions=all) |
| 3 | 3号线 | press or government relay quoting the operator's notice | 4.75 | 10.0 | 8.26 | 0.172 | 2025-02-06 | press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/m/2025-02-06/detail-ineiparm4438034.d.html) |
| 4 | 4号线 | Amap interval bands (undated, passed the acceptance test) | 10.0 | 15.0 | 4.31 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁4号线&city=<city>&extensions=all) |
| 5 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 8.0 | 8.09 | 0.771 | 2023-02-23 | operator website; press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/z/2023-02-23/detail-imyhrutf0335780.d.html) +1 |
| 6 | 5号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 4.0 | 8.0 | 8.09 | 0.771 | 2023-02-23 | operator website; press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/z/2023-02-23/detail-imyhrutf0335780.d.html) +1 |
| 7 | 6号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 5.0 | 9.333 | 7.49 | 0.299 | 2025-07-07 | government portal relaying the operator; press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/z/2025-07-07/detail-infeqytq9953598.d.html) +1 |
| 8 | 7号线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 6.0 | 9.433 | 7.12 | 0.304 | 2025-07-07 | press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/z/2025-07-07/detail-infeqytq9953598.d.html) +1 |
| 9 | 8号线 | Amap interval bands (undated, passed the acceptance test) | 7.0 | 9.0 | 6.25 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁8号线&city=<city>&extensions=all) |
| 10 | 12号线 | Amap interval bands (undated, passed the acceptance test) | 12.0 | 12.0 | 4.54 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁12号线&city=<city>&extensions=all) |
| 11 | 14号线 | Amap interval bands (undated, passed the acceptance test) | 11.0 | 17.0 | 3.37 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁14号线&city=<city>&extensions=all) |
| 12 | 城郊线 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 9.0 | 16.173 | 3.37 | 0.743 | 2023-02-20 | press quoting the operator | [henan.sina.cn](https://henan.sina.cn/news/z/2023-02-20/detail-imyhhxhc7470023.d.html) |
| 13 | 郑许线 | operator statement, interval bands for the whole line | 10.0 | 15.0 | 3.58 | 0.071 | 2023-12-28 | government portal relaying the operator; press quoting the operator | [shifanqu.xuchang.gov.cn](https://shifanqu.xuchang.gov.cn/shms/014002/20240101/88f6240e-8a68-40fe-ba44-56e1660c9e47.html) +1 |
| 14 | 10号线 | Amap interval bands (undated, passed the acceptance test) | 9.0 | 10.0 | 5.85 | 0.0 | read 2026-09-06 | Amap | [restapi.amap.com](https://restapi.amap.com/v3/bus/linename?keywords=地铁10号线&city=<city>&extensions=all) |

### Ürümqi

Operator: . 2 routes. Basis: press_quoted_operator_notice 1, published_peak_offpeak_only 1. URLs opened in the survey log: 18. Band files: Ürümqi_notice.csv (15 rows), Ürümqi_amap.csv (22 rows). Amap bands from the one-off pull of 2026-08-22 to 2026-08-24.

CAMET 2025: minimum peak headway 375.0 s, our shortest transcribed peak 6.0 min, lower bound respected; implied daily runs 326 against 258.0 planned (ratio net of trams 1.262).

| Route | Line | Basis | Peak (min) | Off-peak (min) | Trains/h | Constant fill | Statement date (or read date) | Type | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 1号线 | press or government relay quoting the operator's notice | 6.0 | 10.0 | 5.26 | 0.0 | 2024-06-18 | press quoting the operator | [view.inews.qq.com](https://view.inews.qq.com/a/20240618A0A7R800) |
| 2 | 机场捷运 | operator statement, peak (and off-peak) values only, remainder filled by the bounded 2025 constant | 15.0 | 15.0 | 3.3 | 0.489 | 2025-07-31 | government portal relaying the operator | [cjxww.cn](http://www.cjxww.cn/new/cjwnews/cjwcnNews/202507/t20250731_29877324.html) |

## 7. Routes on the 2025 constant, and the evidence staged for them

These routes carry the frequency transcribed in 2025 whose derivation was never recorded. Each is bounded by the CAMET minimum of its city. The rows staged on 2026-09-07 in `dataset_v2/headways/bands/staging_2026-09-07/` (official replies on 人民网领导留言板 and government portals, operator WeChat posts, press relays, each with the verbatim sentence, URL and date) are listed beside them. They are not applied: promoting them needs a decision on statements dated before 2024 and a rerun of the converter for the five cities.

| City | Route | Line | Constant (trains/h, min) | Staged rows | Newest staged statement | Staged types | Staged value(s) |
|---|---|---|---|---|---|---|---|
| Chengdu | 1 | 2号线 | 12.0, 5.0 | 1 | 2021-06-10 | operator WeChat | 2.25 min |
| Chengdu | 3 | 3号线 | 10.0, 6.0 | 1 | 2018-12-26 | government portal relaying the operator | 3.167 min |
| Chengdu | 4 | 4号线 | 10.0, 6.0 | 1 | 2023-03-13 | government portal relaying the operator | 2.25 min |
| Chengdu | 5 | 5号线 | 10.0, 6.0 | 2 | 2025-04-27 | written reply by the operator or bureau | 6.667 min, 6.667-13.333 min |
| Chengdu | 6 | 6号线 | 7.5, 8.0 | 1 | 2021-08-20 | written reply by the operator or bureau | 8 min |
| Chengdu | 7 | 7号线 | 6.67, 9.0 | 1 | 2017-12-04 | press quoting the operator | 3.5 min |
| Chengdu | 8 | 7号线 | 6.67, 9.0 | 1 | 2017-12-04 | press quoting the operator | 3.5 min |
| Chengdu | 9 | 8号线 | 7.5, 8.0 | 0 |  |  |  |
| Chengdu | 11 | 10号线 | 7.0, 8.6 | 1 | 2017-09-05 | secondary compilation | 8.25 min |
| Chengdu | 12 | 27号线 | 8.0, 7.5 | 0 |  |  |  |
| Chengdu | 15 | 17号线 | 8.0, 7.5 | 1 | 2023-09-17 | press quoting the operator | 3.917 min |
| Dalian | 7 | 13号线 | 4.3, 14.0 | 2 | 2025-06-05 | written reply by the operator or bureau | 10 min, 30 min |
| Guangzhou | 1 | 1号线 | 12.0, 5.0 | 0 |  |  |  |
| Guangzhou | 5 | 5号线 | 13.0, 4.6 | 3 | 2025-09-10 | operator WeChat; written reply by the operator or bureau | 2 min, 2-5 min, 7-8 min |
| Guangzhou | 14 | 12号线 | 9.0, 6.7 | 1 | 2025-06-27 | press quoting the operator | 6 min |
| Guangzhou | 18 | 21号线 | 6.0, 10.0 | 3 | 2025-01-07 | written reply by the operator or bureau | 30 min, 4 min, 7.5 min |
| Guangzhou | 20 | APM线 | 18.0, 3.3 | 1 | 2010-11-08 | press quoting the operator | 7 min |
| Nanjing | 3 | 3号线 | 10.5, 5.7 | 1 | 2015-03-30 | press quoting the operator | 8.75 min |
| Nanjing | 5 | 5号线 | 7.2, 8.3 | 0 |  |  |  |
| Nanjing | 11 | S1号线(机场线) | 11.7, 5.1 | 2 | 2025-06-11 | written reply by the operator or bureau | 10-12 min, 8.5 min |
| Nanjing | 12 | S3号线(宁和线) | 6.3, 9.5 | 1 | 2023-04-10 | operator website | 6-12 min |
| Wuhan | 7 | 8号线 | 8.88, 6.8 | 2 | 2025-08-29 | government portal relaying the operator; press quoting the operator | 5.3 min, 6.3 min |
| Wuhan | 8 | 11号线 | 8.59, 7.0 | 1 | 2025-02-14 | government portal relaying the operator | 5.8 min |
| Wuhan | 11 | 阳逻线 | 8.29, 7.2 | 1 | 2021-04-27 | press quoting the operator | 6.7 min |

