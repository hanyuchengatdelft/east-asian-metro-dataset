# East Asian metro dataset / 东亚地铁数据库 / 東亞地鐵數據庫 / 東アジアの地下鉄データセット / 동아시아 지하철 데이터셋

## Summary

This repository provides metro network data for 62 East Asian cities in two graph representations, namely the L-space and P-space (von Ferber et al., 2009). Both representations use stations as nodes. In L-space, a link connects two stations that are consecutive stops on at least one route. In P-space, a link connects two stations served by at least one common route, representing travel without a transfer, regardless of the number of intermediate stops.

The dataset accompanies the manuscript Accessibility Analysis of East Asian Metro Systems by Rajat Verma, Hanyu Cheng, and Oded Cats. It is published to support reuse of the data and reproduction of the study’s analyses.

## Inclusion criteria and scope
In this dataset, **East Asia** refers to the “Eastern Asia” subregion (code 030) in the [United Nations M49 geographical classification](https://unstats.un.org/unsd/methodology/m49/). Within this region, we consider cities with **urban rail transit**, defined here as rail-based public passenger transport serving urban areas ([Vuchic, 2007](https://doi.org/10.1002/9780470168066); [Megna and Bracciali, 2022](https://doi.org/10.1007/s40864-021-00163-6)). Where sufficient data are available, we construct a metro network for each city using only lines that meet both of the following criteria:

### Criterion 1: Technical requirements

Drawing on the technical requirements of the International Association of Public Transport (UITP, 2025), we include guided, electrically powered urban passenger services that operate on an exclusive right of way, with trains comprising at least two cars and accommodating at least 100 passengers.

This criterion accommodates technologies beyond conventional steel-wheel metro. These account for 22 of the 418 included lines across 13 cities:

- Straddle monorail: Seven lines in Chongqing (Lines 2 and 3, with an additional branch of Line 3), Wuhu (Lines 1 and 2), Daegu (Line 3) and Tokyo (Tokyo Monorail).
- Rubber-tyred automated guideway transit and people movers: Yurikamome and the Nippori–Toneri Liner in Tokyo, all three Macau lines, the Wenhu Line in Taipei, Busan Line 4, the Sillim Line in Seoul, and the APM lines in Guangzhou and Shanghai.
- Rubber-tyred metro with a central guide rail: All three Sapporo subway lines.
- Medium- and low-speed maglev: Beijing Line S1 and the Changsha Maglev Express.



Restricting the dataset to conventional steel-wheel metro would omit functionally comparable services. Ten city networks would be represented only partially, while the Macau, Sapporo and Wuhu networks would be excluded entirely.

For each city, we review the lines within its designated urban rail transit system. Included lines must meet UITP’s metro criteria, namely "guided, electrically powered urban passenger services operating on an exclusive right of way, with trains of at least two cars and a total capacity of at least 100 passengers."

In short, the dataset use a boder defition to include a few systems that are not conventional steel-wheel metro systems, but explicitly excludes commuter and suburban rail. The diagram below summarises its scope.

![Metro definition: what the dataset includes and excludes](docs/figures/metro_definition_venn.svg)

*Figure 1. Scope of the dataset within urban rail transit. Blue areas indicate included systems while grey areas indicate exclusions.*

The full selection procedure, including network boundaries and exclusions, is documented in the [line-level inclusion rules](docs/inclusion_rule.md).


## Inclusion criteria & scope of the dataset 

For each citis, the whole urban rail transit is being looked at, what remains are the metro line that statisfy UITP defintion on metro " guided, electrically powered urban passenger service operating on an exclusive197 right of way, with trains comprising at least two cars and having a total capacity of at least 100 passenger" are included (for  line-level inclusion rule, go to docs line  for the line-level inclusion rule. 


A line enters a city's network if it passes two tests, and a third attribute is recorded without filtering. T1 is the technology-neutral line criterion of the International Association of Public Transport: a guided, electrically powered passenger railway on an exclusive right of way, with trains of at least two cars and at least one hundred passengers. T2 is membership of the urban rail transit system that the city's own jurisdiction designates, so suburban and commuter railways are excluded as systems and through-running services are truncated at the system boundary. T3 records whether a line is urban or metropolitan in scope. Metropolitan lines stay in the main sample and are removed in a sensitivity sample. The register gives the result of each test for every line, and `docs/inclusion_rule.md` states the rule in full.


## Reference dates
Network extent and station sets reflect the networks in operation on 24 September 2025. Service statements were included only if published on or before 30 September 2025. Where service information from the reference period was unavailable, the best available feed or timetable was used, as documented for each network in `docs/frequency_sources.md`. The main cases are the March 2023 Korean national feed and Sapporo's 2020 timetable.

## Scale
|                |                      Stations |                            Route records |
|----------------|-------------------------------|------------------------------------------|
| Total          |                         7,419 |                                      417 |
| Median network |                            90 |                                        4 |
| Quartiles      |                    38 and 188 |                                 2 and 10 |
| Smallest       | 15 (Dongguan, Macau, Taizhou) | 1 (Dongguan, Taichung, Taizhou, Taoyuan) |
| Largest        |                414 (Shanghai) |                             28 (Beijing) |


## Data source
Five collection routes produced the 62 networks. The platform decides how stations, in-vehicle times and frequencies are obtained, so the table is the key to sections 3 and 4.

| Data platrom | City coverage | Raw data | Missing data |
|---|---|---|---|
| Amap subway service | 45 mainland Chinese networks, Hong Kong, Macau (47) | lines, ordered stations with coordinates and transfer flags, first and last train per station and direction | trips, timetables, headways |
| Operator GTFS feeds, Japan | Tokyo (four operators), Yokohama, Kyoto, Sapporo (4) | stops, trips, stop times, service calendar | nothing further is needed |
| Operator timetables converted to GTFS, Japan | Sendai, Kobe, Fukuoka (3) | per-station departure tables, converted to trips and stop times | Kobe's station set, taken from Vijlbrief et al. (2022) |
| KTDB national GTFS, South Korea | Seoul, Busan, Daegu, Incheon (4) | stops, trips, stop times (March 2023 dataset) | stations opened in 2024 and 2025, and a complete Seoul Line 2 loop |
| TDX Rail/Metro API, Taiwan | Taipei, Taoyuan, Taichung, Kaohsiung (4) | stations, stations per line, station-to-station run and stop times, headway bands per service pattern and day type | trips (the API is not GTFS) |


  
## Meta-data

| Path | Content |
|---|---|
| `data/l-space/` | **The 62 networks in L-space, 7,419 stations.** Stations as nodes, in-vehicle links as directed edges. In-vehicle times and frequencies rebuilt from operator timetables and published interval statements, with the corrections listed in `docs/dataset_record.md` applied. This is what the manuscript reports. |
| `data/p-space/` | The same 62 networks in P-space: one edge for every origin and destination joined by a service without a transfer, carrying the frequency, the waiting time and its source. |
| `data/route_information.csv` | **The line-level inclusion register**, 420 rows, one per route record. For every line: city, local and English name, operator, system type, legal class, service type, station count, great-circle length, commercial speed proxy, trains per hour, headway and its source, the share of the service day filled rather than published, the outcome of the three tests (`T1_uitp_line_criteria`, `T2_designated_urban_system`, `T3_scope` with `T3_basis`), the fare flag and the verdict. 418 rows are included and 2 are excluded. |
| `data/route_frequency_sources.csv` | The per-route table behind the frequencies: for every route, the data source of its frequency and each URL and date the value was read from. It holds 417 rows, the register's 420 less the 2 excluded lines and the 1 included line that is not represented in the network files. |
| `docs/dataset_record.md` | The record of the published files: the reference dates, the totals, every correction with its grounds and its effect on the station counts, and the provenance of the corrected values. |
| `docs/data_sources.md` | Every source behind the files, its licence, and the attribution it requires. |
| `docs/inclusion_rule.md` | The full statement of the inclusion rule, with the instrument used in each jurisdiction and the counts it produces. |
| `docs/frequency_sources.md` | Where every frequency and headway comes from, network by network and route by route, with the URL and date of each statement and the validation against the CAMET 2025 annual report. |
| `docs/data_dictionary.md` | The meaning of every node, link and graph field. It was written for the annotated networks of the companion repository, whose node and link fields are the same as here. |



## Reading a network

Files are NetworkX node-link JSON, one per city, UTF-8, city names as in the file name (`Hong Kong-L.json` carries a space, `Ürümqi-L.json` a diacritic).

```python
import json, networkx as nx
G = nx.node_link_graph(json.load(open("data/l-space/Tokyo-L.json", encoding="utf-8")))
```

L-space: stations as nodes, in-vehicle links as directed edges with `duration_avg` in seconds.
P-space: the same stations, one edge for every origin and destination joined by a service without a transfer, carrying `veh` (trains per hour by route and direction), `avg_wait` (minutes, half the combined headway) and `wait_source`. Every file records in its `graph` attributes its node and link counts as published and, where a correction touched it, the correction. Any older totals block in a file is superseded by that record.

## Conventions

An in-vehicle link time is measured departure to departure, so it includes the dwell at the far
end. A frequency is the number of weekday services between 05:00 and 24:00 divided by nineteen
hours, and the waiting time is half the resulting headway. Coordinates are WGS-84 throughout.

## Data sources
The 47 Chinese networks, including Hong Kong and Macau, were compiled from the Amap subway service, with in-vehicle times read from first- and last-train progressions and frequencies transcribed from the interval statements operators publish. The Korean networks come from the national GTFS release of the Korea Transport Database, the Japanese networks from the operators' GTFS feeds or published timetables, the Chinese Taipei networks from the Transport Data eXchange, and Kobe's station set from Vijlbrief et al. (2022). `docs/data_sources.md` names every source with its licence, and `docs/frequency_sources.md` traces every frequency to the statement, feed or table it was read from. The transcribed interval statements, the annotated networks with full provenance blocks, and the code that builds everything are in the companion repository `https://github.com/hanyuchengatdelft/east-asian-metro-accessibility`.

## Every network is a single component

Since the corrections of 15 September 2026 every published network is one connected component. The
nine-station northern section of Foshan Line 3, not physically joined to the rest of the network at
the reference date, is not represented in the files, and the register says so on its row. The
grounds are recorded in `docs/dataset_record.md`.

## Licence and citation

Data and documentation are released under Creative Commons Attribution 4.0 International, see `LICENSE`. Cite the dataset as set out in `CITATION.cff` and the paper for the analysis. Attribution requirements inherited from individual sources are listed in `docs/data_sources.md` and must be carried over. In particular, work that uses the Tokyo or Yokohama networks must reproduce the attribution sentence of the Public Transportation Open Data Center given there.

## References
China Association of Metros. (2026). *Statistical and analytical report on urban rail transit, 2025* (城市轨道交通2025年度统计和分析报告). https://www.camet.org.cn/xytj/tjxx/789653532090437.shtml

UITP. (2025). *Global metro figures 2024* (Statistics Brief). International Association of Public Transport. https://www.uitp.org/wp-content/uploads/sites/7/2025/08/20250822_Global-Metro-Figures_Statistics-Brief_WEB.pdf

Vijlbrief, S., Cats, O., Krishnakumari, P., van Cranenburgh, S., & Massobrio, R. (2022a). *A curated data set of L-space representations for 51 metro networks worldwide* (Version 1) [Data set]. 4TU.ResearchData. https://doi.org/10.4121/21316824.v1

Vijlbrief, S., Cats, O., Krishnakumari, P., van Cranenburgh, S., & Massobrio, R. (2022b). *A curated data set of P-space representations for 51 metro networks worldwide* (Version 2) [Data set]. 4TU.ResearchData. https://doi.org/10.4121/21316950.v2

von Ferber, C., Holovatch, T., Holovatch, Y., & Palchykov, V. (2009). Public transport networks: Empirical analysis and modeling. *The European Physical Journal B, 68*, 261–275. https://doi.org/10.1140/epjb/e2009-00090-x


<!--For Chinese cities, Classification of Urban Rail Transit~(GB/T 44413--2024) provides the technical classification reference~\citep{GBT44413}, while the Provisions on the Operation and Management of Urban Rail Transit establish the administrative framework~\citep{MOTUrbanRail2018}. We retain qualifying lines within municipal urban rail systems and exclude services operating on national railway infrastructure. The Nanjing S-series lines are retained, with their
metropolitan service scope recorded separately, whereas suburban lines like Xi'an–Huyi railway, Beijing Line~S2 and the Shanghai Jinshan Railway are excluded.

In South Korea, the Urban Railroad Act defines the urban railroad category and requires a master plan for each route that fixes its terminal stations and station locations \citep[Arts.~2(2) and 6(2)]{KoreaUrbanRailroadAct}, 
so line-level boundaries are documentable. Suburban services are excluded on two statutory grounds. General railroads are a separate class~\citep[Art.~2(4)]{KoreaRailroadConstructionAct}, and the Korail-operated services of the Seoul Capital Area and the Airport Railroad belong to it. Sections designated metropolitan railways are excluded because the designation is the Minister's determination, under Article~2(2)(b) of the Special Act, that a section serves transport across two or more provinces~\citep{KoreaMetropolitanTransportAct,KoreaMetropolitanTransportDecree}. The designation leaves urban railroad status intact and is read here as the official record of which sections serve the metropolitan layer rather than the city's own network. The Busan--Gimhae Light Rail crosses a provincial boundary without such a designation and is retained. The Byeollae extension of Line~8 is municipally owned, designated, and excluded.

In Japan, no statute defines a subway as a service category, so the boundary is the ministry's own classification of undertakings. Fare regulation under Article~16(2) of the Railway Business Act places operators in three peer groups, the JR passenger companies, the major private railways and the subway undertakings~\citep{MLITYardstick}, and the ministry's railway statistics enumerate the subway undertakings with route length and stations per subway business~\citep{MLITRailwayStatistics2023}. The dataset covers that group. Tokyo Metro is constituted by its own Act to operate railways mainly underground in and around the special wards \citep{TokyoMetroAct}, whereas JR East is allocated the Tohoku and Kanto regions rather than a city~\citep{JNRReformAct1986}. Through-running services are represented only over the retained undertaking's own sections~\citep{Ito2014ThroughService}, so the Tozai Line runs from Nakano to Nishi-Funabashi, following Tokyo Metro's operating-line inventory \citep{TokyoMetroOperatingLines}. The Yurikamome, the Nippori--Toneri Liner and the Tokyo Monorail are elevated lines outside every subway roster and are retained on the functional criterion alone.

These  Seven are straddle monorail routes, in Chongqing (Lines 2 and 3, the latter with an additional branch), Wuhu (Lines 1 and 2), Daegu (Line 3) and Tokyo (the Tokyo Monorail). Ten are rubber-tyred automated guideway transit or people-mover lines, namely the Yurikamome and Nippori--Toneri Liner in Tokyo, all three Macau lines, the Wenhu Line in Taipei, Busan Line 4, the Sillim Line in Seoul, and the APM lines in Guangzhou and Shanghai. Three are the rubber-tyred lines with a central guide rail that make up the whole Sapporo subway, and two are medium-low-speed maglev services (Beijing Line S1 and the Changsha Maglev Express). Restricting inclusion to conventional steel-wheel lines would omit functionally comparable services and underrepresent metro-equivalent provision in the affected cities. Ten networks would be represented only in part, and the Macau, Sapporo and Wuhu networks would be excluded entirely.
