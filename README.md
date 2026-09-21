# East Asian metro dataset / 东亚地铁数据库 / 東亞地鐵數據庫 / 東アジアの地下鉄データセット / 동아시아 지하철 데이터셋

Sixty-two metro networks of East Asia in two graph spaces, with the line-level inclusion rule that decided what each network contains. This is the dataset of record for the manuscript *Accessibility Analysis of East Asian Metro Systems* (Hanyu Cheng, Rajat Verma, Oded Cats, Delft University of Technology, Transport and Planning department).

The coverage is 45 cities in mainland China, Hong Kong, Macau, 7 networks in Japan, 4 in South Korea and 4 in Taiwan, holding 7,419 stations on 417 route records. The networks run from single-line systems of 15 stations to Shanghai with 414 stations on 23 lines and Beijing with 399 on 28, and the median network has 90 stations on 4 lines.  `data_sources.md` names every source with its licence and points to the rebuild instructions.

## Version

The files are the version of 15 September 2026. `metadata.md` lists every correction applied to them with its grounds, and gives the totals: 62 networks, 7,419 stations, each network a single connected component.

## Reference state

Network extent and station sets are those in operation on 24 September 2025. Service statements were admitted only where published on or before 30 September 2025. The dataset is a repair of that 2025 snapshot, not a refresh to a later date.

Scale
|                |                      Stations |                            Route records |
|----------------|-------------------------------|------------------------------------------|
| Total          |                         7,419 |                                      417 |
| Median network |                            90 |                                        4 |
| Quartiles      |                    38 and 188 |                                 2 and 10 |
| Smallest       | 15 (Dongguan, Macau, Taizhou) | 1 (Dongguan, Taichung, Taizhou, Taoyuan) |
| Largest        |                414 (Shanghai) |                             28 (Beijing) |
  

## the metadata

| Path | Content |
|---|---|
| `l-space_representation/` | **The 62 networks in L-space, 7,419 stations.** Stations as nodes, in-vehicle links as directed edges. In-vehicle times and frequencies rebuilt from operator timetables and published interval statements, with the corrections listed in `metadata.md` applied. This is what the manuscript reports. |
| `p-space_representation/` | The same 62 networks in P-space: one edge for every origin and destination joined by a service without a transfer, carrying the frequency, the waiting time and its source. |
| `east_asian_metro_route.csv` | **The line-level inclusion register**, 420 rows, one per route record. For every line: city, local and English name, operator, technology, legal class, mode, station count, great-circle length, commercial speed proxy, trains per hour, headway and its source, the share of the service day filled rather than published, the outcome of the three tests (`T1_uitp_line_criteria`, `T2_designated_urban_system`, `T3_scope` with `T3_basis`), the fare flag and the verdict. 418 rows are included, 2 are excluded. |
| `metadata.md` | The record of the published files: the reference dates, the totals, every correction with its grounds and its effect on the station counts, and the provenance of the corrected values. |
| `OPEN_DECISIONS.md` | Two inclusion decisions (Changchun Line 3, the Chinese membership test) and how they were resolved. |
| `docs/INCLUSION_RULE.md` | The full statement of the inclusion rule, with the instrument used in each jurisdiction and the counts it produces. |
| `docs/FREQUENCY_SOURCES.md` | Where every frequency and headway comes from, network by network and route by route, with the URL and date of each statement and the validation against the CAMET 2025 annual report. `docs/frequency_sources_by_route.csv` is the per-route table behind it. |
| `docs/DATA_DICTIONARY.md` | The meaning of every node, link and graph field. It was written for the annotated networks of the companion repository, whose node and link fields are the same as here. |
| `data_sources.md` | Every source behind the files, its licence, and the attribution it requires. |

## The inclusion criteria in one paragraph

A line enters a city's network if it passes two tests, and a third attribute is recorded without
filtering. T1 is the technology-neutral line criterion of the International Association of Public
Transport: a guided, electrically powered passenger railway on an exclusive right of way, with
trains of at least two cars and at least one hundred passengers. T2 is membership of the urban rail
transit system that the city's own jurisdiction designates, so suburban and commuter railways are
excluded as systems and through-running services are truncated at the system boundary. T3 records
whether a line is urban or metropolitan in scope. Metropolitan lines stay in the main sample and are
removed in a sensitivity sample. The register gives the result of each test for every line, and
`docs/INCLUSION_RULE.md` states the rule in full.

## Reading a network

Files are NetworkX node-link JSON, one per city, UTF-8, city names as in the file name
(`Hong Kong-L.json` carries a space, `Ürümqi-L.json` a diacritic).

```python
import json, networkx as nx
G = nx.node_link_graph(json.load(open("l-space_representation/Tokyo-L.json", encoding="utf-8")))
```

L-space: stations as nodes, in-vehicle links as directed edges with `duration_avg` in seconds.
P-space: the same stations, one edge for every origin and destination joined by a service without a
transfer, carrying `veh` (trains per hour by route and direction), `avg_wait` (minutes, half the
combined headway) and `wait_source`. Every file records in its `graph` attributes its node and link
counts as published and, where a correction touched it, the correction. Any older totals block
in a file is superseded by that record.

## Conventions

An in-vehicle link time is measured departure to departure, so it includes the dwell at the far
end. A frequency is the number of weekday services between 05:00 and 24:00 divided by nineteen
hours, and the waiting time is half the resulting headway. Coordinates are WGS-84 throughout.

## Where the data come from

The 47 Chinese networks, including Hong Kong and Macau, were compiled from the Amap subway
service, with in-vehicle times read from first- and last-train progressions and frequencies
transcribed from the interval statements operators publish. The Korean networks come from the
national GTFS release of the Korea Transport Database, the Japanese networks from the operators'
GTFS feeds or published timetables, the Chinese Taipei networks from the Transport Data eXchange, and
Kobe's station set from Vijlbrief et al. (2022). `data_sources.md` names every source with its licence, and `docs/FREQUENCY_SOURCES.md` traces every frequency to the statement, feed or table it was read from.
The transcribed interval statements, the annotated networks with full provenance blocks, and the
code that builds everything are in the companion repository
`https://github.com/hanyuchengatdelft/east-asian-metro-accessibility`.

## Every network is a single component

Since the corrections of 15 September 2026 every published network is one connected component. The
nine-station northern section of Foshan Line 3, not physically joined to the rest of the network at
the reference date, is not represented in the files, and the register says so on its row. The
grounds are recorded in `metadata.md`.

## Licence and citation

Data and documentation are released under Creative Commons Attribution 4.0 International, see `LICENSE`. Cite the dataset as set out in `CITATION.cff` and the paper for the analysis. Attribution requirements inherited from individual sources are listed in `data_sources.md` and must be carried over. In particular, work that uses the Tokyo or Yokohama networks must reproduce the attribution sentence of the Public Transportation Open Data Center given there.

## References
China Association of Metros. (2026). *Statistical and analytical report on urban rail transit, 2025* (城市轨道交通2025年度统计和分析报告). https://www.camet.org.cn/xytj/tjxx/789653532090437.shtml
UITP. (2025). *Global metro figures 2024* (Statistics Brief). International Association of Public Transport. https://www.uitp.org/wp-content/uploads/sites/7/2025/08/20250822_Global-Metro-Figures_Statistics-Brief_WEB.pdf

Vijlbrief, S., Cats, O., Krishnakumari, P., van Cranenburgh, S., & Massobrio, R. (2022a). *A curated data set of L-space representations for 51 metro networks worldwide* (Version 1) [Data set]. 4TU.ResearchData. https://doi.org/10.4121/21316824.v1

Vijlbrief, S., Cats, O., Krishnakumari, P., van Cranenburgh, S., & Massobrio, R. (2022b). *A curated data set of P-space representations for 51 metro networks worldwide* (Version 2) [Data set]. 4TU.ResearchData. https://doi.org/10.4121/21316950.v2

von Ferber, C., Holovatch, T., Holovatch, Y., & Palchykov, V. (2009). Public transport networks: Empirical analysis and modeling. *The European Physical Journal B, 68*, 261–275. https://doi.org/10.1140/epjb/e2009-00090-x
  
