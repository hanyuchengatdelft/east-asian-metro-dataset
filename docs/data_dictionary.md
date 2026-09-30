# Data dictionary, `asia/L2_v2_annotated` and `asia/P2_v2_annotated`

Generated 2026-08-22 v2 by `dataset_v2/annotate.py` on the repaired files `asia/L2_v2` and `asia/P2_v2`, built by `dataset_v2/repair.py`. Node and link values differ from the submitted state wherever a repair applies. Every change is listed per city and operation in `dataset_v2/build/changelog_v2.csv` (Supplementary Table S4) and inside each file under `graph.repairs`, and changed nodes and links keep `v1_id`, `v1_lat`, `v1_lon` or `v1_duration_avg` next to the new value.

## Graph-level fields (`graph`)

| Field | Meaning |
|---|---|
| city, city_local_name, jurisdiction, jurisdiction_code | identity |
| legal_umbrella, designation_instrument, metro_term_in_jurisdiction | the legal category the network belongs to and the instrument that defines it |
| source_platform, source_description, source_url, collection_window, reference_network_date | provenance, per network |
| coordinate_system | WGS-84 throughout |
| in_vehicle_time_basis, waiting_time_basis | how duration_avg and avg_wait were obtained, including placeholder warnings |
| inclusion_rule_version, inclusion_rule | the line-level rule applied; see `routes[].verdict` |
| n_stations, n_routes, n_links | counts |
| cross_city_overlap | stations shared with another sampled city |
| known_defects | list of verified defects in this file |
| excluded_services | urban rail services in the city that are outside the sample, with the test each fails |
| routes | per-route block, see below |
| field_dictionary | short per-field notes carried inside each file |

## Route-level fields (`graph.routes[route_id]`)

| Field | Meaning |
|---|---|
| line_local, line_en | line name in the local language and in English |
| operator | the company or public body running passenger services on the line on 24 September 2025, as distinct from the owner, concessionaire or parent group. Written as English name (local-language name), with two operators separated by "; " and the section each runs given in `note`. Where no official English name was verified, the English is a descriptive translation and `note` says so. Last column of `data/route_information.csv`. Blank for Guiyang S1, where the passenger operator is unresolved |
| system_type | the technical system type of the line (系统制式): wheel, guideway and propulsion only. One of: `steel-wheel metro`, `steel-wheel linear-motor metro`, `steel-wheel light rail`, `steel-wheel tram`, `steel-wheel locomotive-hauled rail`, `rubber-tyred metro with central guide rail`, `rubber-tyred automated guideway transit`, `straddle-beam monorail`, `low- and medium-speed maglev`. Service role, automation, capacity and legal designation are not system types and are recorded in `service_type`, `note`, `capacity_per_train`, `capacity_class_national` and `legal_class`. The GB/T 44413-2024 suburban rapid rail class (Table 4 row 9) is kept in `legal_class`, and its lines are `steel-wheel metro` here with `service_type` suburban/regional. Replaces the column `technology` |
| legal_class | the jurisdiction's own class for the line, in English with the provision it rests on, several classes separated by "; ". Law titles follow the official English versions: Railway Business Act and Act on Rail Tracks (Japanese Law Translation), Urban Railroad Act, Mass Rapid Transit Act, Mass Transit Railway Ordinance. The Chinese class names come from GB/T 44413-2024 *Classification of urban rail transit*, which gives no English terms, so their English is a descriptive translation. Macau's Law 18/2019 has official Chinese and Portuguese texts only |
| service_type | the role the line plays in the network, a classification made for this dataset and not a universal taxonomy. One of: `urban`, `suburban/regional` (a designated 市域 or regional line), `dedicated airport express` (a line whose purpose is airport access, usually with few stations and often a separate fare, as distinct from a line that merely serves an airport). T3 sets every `suburban/regional` row to Tier B, the only way this column enters the inclusion tests. Replaces the column `mode`. `docs/inclusion_rule.md` predates the rename and still says `technology` and `mode`, read them as `system_type` and `service_type` |
| n_stations, n_links, is_loop | topology |
| length_km_greatcircle | sum of straight-line link lengths, a lower bound on track length |
| in_vehicle_min_sum | sum of duration_avg over the route's links |
| commercial_speed_proxy_kmh | length_km_greatcircle / in_vehicle_min_sum, a lower bound |
| trains_per_hour, headway_min, headway_source | median P-space veh for the route, 60 / veh, and where it came from |
| constant_fill_share | share of the weekday service minutes the band converter filled with the 2025 constant because no published row covered them (v2, converted Chinese routes only; above 0.25 the label is published_peak_offpeak_only) |
| T1_uitp_line_criteria | pass or fail: technology-neutral UITP line criteria; fails only for street running |
| T2_designated_urban_system | pass or fail: membership of the city's designated urban rail transit system |
| T3_scope | urban, or metropolitan (Tier B) |
| fare_flag | premium separate fare, where applicable |
| verdict | what the rule says about the line; nothing is removed from the file |
| name_source, assignment_confidence, amap_line_id, vote_share, station_coverage | provenance of the name (Amap cities) |
| note | free text, including DEFECT notes |

## Link-level fields

| File | Field | Meaning |
|---|---|---|
| both | node.name | station name as delivered by the source (Amap search decorations retained) |
| both | node.lat_lon | WGS-84 decimal degrees |
| L | duration_avg | in-vehicle seconds between adjacent stations; Amap cities: first/last-train progression (run plus dwell, whole minutes); GTFS and TDX cities: timetable averages |
| L | d | NOT a length: equals 10 x duration_avg in 58 of 62 files (36 km/h assumption). Use coordinates instead |
| L | n_vehicles | PLACEHOLDER: constant 50 in every file |
| L | route_I_counts | route ids serving the link; names in graph.routes |
| L | route_names | line names serving the link (added) |
| P | veh | trains per hour by route and direction |
| P | avg_wait | expected waiting time in minutes, equals 30 / veh (half headway) on every edge |

## Placeholders and fabricated fields, in one place

- `d` is 10 x `duration_avg` in 58 of 62 files. It is not a measured length.
- `n_vehicles` is 50 everywhere.
- `avg_wait` is a single network-wide value in 4 files, and in 0 of those it is the 7.5-minute default. The affected files carry the warning in `graph.waiting_time_basis` and in every route's `headway_source`.
- Tokyo's `duration_avg` and `veh` were rebuilt from the operators' GTFS feeds (repair R6), so the flat 120 s of the submitted file is gone. Since 2026-09-06 a train counts towards `veh` on a station pair only if it stops at both stations, which corrects 1,883 edges where express trains had been counted at stations they pass (memo 23).
- Sendai, Fukuoka and Kobe were rebuilt on 2026-09-06 from the operators' own published timetables, converted to GTFS and run through the same rebuild as Yokohama, Kyoto and Sapporo. Kobe's node set is still the 2006 build, its service attributes are 2025.

## What counts as a direct service

A `P` edge exists between two stations when at least one scheduled service calls at both without a transfer, and `veh`
counts those services. Three consequences are worth stating.

- A train that passes a station without stopping does not count for pairs at that station. The Japanese feeds mark such
  a call explicitly and the build honours the mark.
- Reserved-seat services that require a fee on top of the fare do count, because a passenger can board them. In the
  sample this is 23 weekday trains in Tokyo: the Odakyu Romancecar on the Chiyoda line, the TH Liner on the Hibiya
  line and the S-TRAIN on the Yurakucho line. They affect 85 of the 1,394 pairs on those three lines and contribute at
  most 0.32 trains per hour. Lines whose whole service carries a premium fare are flagged instead, in the line
  inventory.
- A through service that continues onto another line is counted for the pairs within each line separately, because a
  timetable trip is the unit of a one-seat ride. Where an operator splits a through train at a junction, as Fukuoka
  does at 中洲川端, pairs spanning the junction are absent. This matches the v1 files.

## Direction

Both spaces are stored directed. Every L link has a reverse link, but 10.4 per cent of them carry a different
`duration_avg` by direction, and every P edge has a reverse edge, but 62.8 per cent carry a different `avg_wait`.
This is a real difference from v1, where the figures were 1.55 per cent and 0.12 per cent, because a network given
a single constant frequency cannot vary by direction. Fifty-three of the 62 cities gain directional variation in v2.
`veh` is keyed by direction with one entry per route per directed edge, so `avg_wait = 30 / sum(veh)` never sums the
two directions together. The Table 1 pipeline nevertheless symmetrises the graph, because `data_loader.load_city`
ends with `.to_undirected()`. Measured on 2026-09-10, running the same cost matrix directed instead moves t_M by at
most 2 minutes and d_30 by at most 0.008. Yokohama routes 1 and 2 are a separate, genuine defect, where `veh` sums
both directions and the waiting times are correspondingly too short.

## Cross-city overlaps

Guangzhou and Foshan share 21 stations (the Guangfo Line). Seoul and Incheon share 11 (Line 7 까치울–석남). Hangzhou and Shaoxing share 1. These networks are not independent observations.
