# East Asian metro dataset / 东亚地铁数据库 / 東亞地鐵數據庫 / 東アジアの地下鉄データセット / 동아시아 지하철 데이터셋

Sixty-two metro networks of East Asia in two graph spaces, with the line-level inclusion rule that decided what each network contains. This is the dataset of record for the manuscript *Accessibility Analysis of East Asian Metro Systems* (Hanyu Cheng, Rajat Verma, Oded Cats, Delft University of Technology, Transport and Planning).
The networks cover major networks in East Asia, precisely, 45 cities in mainland China (including Hong Kong and Macau), 7 cities in Japan, 4 in South Korea and 4 in Chinese Taipei.  The version 2 lineage, which the manuscript reports, holds 7,428 stations. Every file in this repository is listed with its SHA-256 in `MANIFEST.csv`.

## Reference state

Network extent and station sets are those in operation on 24 September 2025. Service statements were admitted only where published on or before 30 September 2025. The dataset is a repair of that 2025 snapshot, not a refresh to a later date.

## the metadata

| Path | Content |
|---|---|
| `L2_v2/`, `P2_v2/` | **The version 2 lineage, 62 networks, 7,428 stations.** In-vehicle times and frequencies rebuilt from operator timetables and published interval statements, with the seven inclusion-rule corrections applied. This is what the manuscript reports. |
| `L2/`, `P2/` | The version 1 lineage, 62 networks, 7,400 stations. The state analysed in the submitted manuscript, with the same corrections applied, kept so that the effect of the corrections can be separated from the effect of the version 2 rebuild. |
| `inclusion_table_frozen.csv` | **The line-level inclusion register**, 420 rows, one per route record. For every line: city, local and English name, operator, technology, legal class, mode, station count, great-circle length, commercial speed proxy, trains per hour, headway and its source, the share of the service day filled rather than published, the outcome of the three tests (`T1_uitp_line_criteria`, `T2_designated_urban_system`, `T3_scope` with `T3_basis`), the fare flag and the verdict. 418 rows are included, 2 are excluded. |
| `table1_frozen.csv` | Table 1 of the manuscript recomputed on the frozen version 1 files for all 62 networks (`new_*` columns) beside the values printed in the submitted manuscript (`old_*`). |
| `ea_summary_frozen.json` | East Asian means and standard deviations of the Table 1 indicators, against the submitted values. |
| `indicator_impact_v1.json` | Before and after indicators for the six cities the corrections changed. |
| `reference_network_audit.csv` | The audit of the 51 European and North American reference networks of Vijlbrief et al. (2022) against the inclusion rule, 44 of which enter the regional comparison. |
| `recompute_all.py`, `recompute_log.txt` | The script that produced `table1_frozen.csv` and its log. It imports the reproduction pipeline of the companion repository and is kept here as the record of the computation. |
| `validate_frozen_dataset.ipynb` | Read-only checks of every numerical claim the manuscript makes about the sample, printing PASS or FAIL. |
| `FREEZE_MANIFEST.md` | The seven corrections with their grounds, the station totals before and after, and what remained open at the freeze. |
| `OPEN_DECISIONS.md` | The two decisions weighed at the freeze (Changchun Line 3, the Chinese membership test) and how they were resolved. |
| `docs/INCLUSION_RULE.md` | The full statement of the inclusion rule, with the instrument used in each jurisdiction and the counts it produces. |
| `docs/DATA_DICTIONARY.md` | The meaning of every node, link and graph field. It was written for the annotated networks of the companion repository, whose node and link fields are the same as here. |
| `SOURCES.md` | Every source behind the files, its licence, and the attribution it requires. |

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
G = nx.node_link_graph(json.load(open("L2_v2/Tokyo-L.json", encoding="utf-8")))
```

L-space: stations as nodes, in-vehicle links as directed edges with `duration_avg` in seconds.
P-space: the same stations, one edge for every origin and destination joined by a service without a
transfer, carrying `veh` (trains per hour by route and direction), `avg_wait` (minutes, half the
combined headway) and `wait_source`. Every file carries a `graph.freeze` block with its frozen node
and link counts and, where a correction touched it, the correction. Older `v1_totals` and
`v2_totals` blocks in the version 2 files predate the freeze and are superseded by that block.

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
Kobe's station set from Vijlbrief et al. (2022). `SOURCES.md` names every source with its licence.
The transcribed interval statements, the annotated networks with full provenance blocks, and the
code that builds everything are in the companion repository
`https://github.com/hanyuchengatdelft/east-asian-metro-accessibility`.

## Two networks are not single components

Hefei in the version 1 lineage is 165 and 7 stations, so its time diameter is fitted on 165. Foshan
in the version 2 lineage is 56 and 9 after the tram exclusion, the nine being the northern Line 3
section not yet physically joined. Neither condition was created by the freeze, and both are
recorded in `FREEZE_MANIFEST.md`.

## Licence and citation

Data and documentation are released under Creative Commons Attribution 4.0 International, see
`LICENSE`. Cite the dataset as set out in `CITATION.cff` and the paper for the analysis.
Attribution requirements inherited from individual sources are listed in `SOURCES.md` and must be
carried over. In particular, work that uses the Tokyo or Yokohama networks must reproduce the
attribution sentence of the Public Transportation Open Data Center given there.
