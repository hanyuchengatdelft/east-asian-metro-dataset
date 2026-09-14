# 20. The line-level inclusion rule

**Document of record.** Prepared 2 September 2026 for JTRG-D-26-01225, reviewer comments R2-1, R2-2 and R2-3.

This memo consolidates and **supersedes `07_INCLUSION_RULE.md` (22 August 2026) wherever the two differ**. It carries forward 07's statement of the rule unchanged in substance, adds the two decisions taken after 07 was written (1 September, the four v2 additions and the Foshan Nanhai override, and 2 September, the broad technology-neutral framing of the word "metro"), replaces every count in 07 with counts computed this session from the dataset, and records the disposition of the 2 September inclusion audit.

**Provenance of every number below.** All counts, unless the sentence names another file, are computed in this session from
`August - revision/analysis/inclusion_table_v2.csv`, 420 rows, 30 columns,
sha256 `235d2094bcdd334926ed16d3a89f2ad3afc0a294b575aabcc301a869c9e7699f`, rebuilt on 2 September with the Macau technology correction of 7.4, the Taoyuan basis rewrite of 7.5 (g) and the Nanhai derivation note of 4.2. The superseded build is sha256 `8b05ad6378d686c695e4accaa0170190e1816b62a7706f9011b6dd949d6139fb`.
A byte-identical copy ships as `data_package_2026-09-01/supplementary_tables/inclusion_table_v2.csv` and as `supplementary_line_inventory_v2.csv`, the reviewer-facing Supplementary Table S1.

**Status of the numbers.** The counts in section 5 are of record **as of this CSV**. Five route-identity repairs listed in section 7.5 will move the route total when they are applied. Nothing in section 9 should be typeset into the manuscript until the v2.1 rebuild has been run and the counts re-read.

---

## 0. The rule, paste-ready

> **The line is the unit of inclusion.** A line enters a city's network if it passes two tests, and a third attribute is recorded for it without filtering.
>
> **T1, the UITP line criteria, applied technology-neutrally.** The line is a guided, electrically powered urban passenger service running on an exclusive right of way, with trains of at least two cars and a total capacity of at least 100 passengers. UITP states in the same paragraph that systems based on light rail vehicles, monorail or magnetic levitation are included if they meet all other criteria, so straddle monorail, medium-low-speed maglev, automated guideway transit and fully segregated light rail all pass. T1 fails only for street running, shared lanes and unguided operation, that is on the right of way and never on the vehicle class.
>
> **T2, membership of the city's designated urban rail transit system.** The designated system is the category each jurisdiction defines for itself: 城市轨道交通 under GB/T 44413-2024 in mainland China, 도시철도 under 도시철도법 in Korea, 大眾捷運系統 under 大眾捷運法 in Taiwan, 都市高速鉄道 as a 都市施設 under 都市計画法 in Japan, the MTR franchise in Hong Kong, and the 輕軌交通系統 of Law 18/2019 in Macau. National, regional and suburban railways are excluded **as systems and not line by line**, following UITP's exclusion of the Paris RER and the Berlin S-Bahn and Roth et al.'s exclusion of the RER and NetworkRail, even where a line such as the JR Yamanote would pass T1 on every functional measure. Through-running services are truncated at the boundary of the designated system.
>
> **T3, service scope, recorded and never used to filter.** A line is urban where its commercial speed proxy is at or below 60 km/h, which is the boundary GB/T 44413-2024 Table 1 draws between 城区轨道交通 and 市域或都市圈轨道交通, and metropolitan otherwise or where the line is itself designated 市域快轨 or an equivalent regional express. Metropolitan lines are labelled Tier B, **retained in the main sample**, and reported again in a sensitivity sample from which they are removed. Tier B is a statement about service scope and never about vehicle technology.
>
> **The fare flag.** A line whose fare is premium and not integrated with the rest of the network carries a fare flag. Flagged lines are retained. The flag is a transparency measure of our own, so that a reader who wishes to remove them can identify them.
>
> The assignment of every line, with its technology, legal class, headway and the outcome of each test, is published as Supplementary Table S1.

House style throughout this memo and in every paste-ready block: no em-dashes, no semicolons, British or neutral spelling.

---

## 1. Why a legal definition cannot define the sample

The six jurisdictions in the sample do not share a category called "metro". They share a category meaning "the urban rail transit system of this city", and they disagree with one another about what technology belongs inside it. A sample defined by any one national label would therefore be defined differently in each country, which is exactly the institutional inconsistency Reviewer 2 warned against.

| Jurisdiction | Statutory or franchise category | Instrument | What the category covers | Does it define "metro" or "subway"? |
|---|---|---|---|---|
| Mainland China | 城市轨道交通 | GB/T 44413-2024 clause 3.1 for the category, 采用专用轨道导向运行以服务通勤为主要目标的城市公共客运交通系统, and clause 5.1 for the ten system types, plus inclusion in the city's NDRC-approved 城市轨道交通建设规划 | ten system types: 地铁, 轻轨, 跨座式单轨, 悬挂式单轨, 自动导向轨道, 有轨电车, 导轨式胶轮电车, 中低速磁浮, 市域快速轨道, 高速磁浮 | Yes for 地铁, but narrowly. Table 4 row 1 makes 地铁系统 steel wheel on steel rail, 大运能, 城区 scope, 35 to 60 km/h. On that reading Chongqing Lines 2 and 3 are not 地铁, although CAMET counts them inside the Chongqing network and one fare covers them |
| Korea | 도시철도 | 도시철도법 제2조 | railway, monorail, tram, linear induction and maglev built inside a 도시교통권역, as against 광역철도 and 일반철도 | No. The umbrella is broader than metro and includes trams |
| Taiwan | 大眾捷運系統 | 大眾捷運法 第3條 | guided route, dedicated vehicles, frequent mass rapid service, split by whether the right of way is completely independent | No. The definition is functional and technology is deliberately absent |
| Japan | 都市高速鉄道, a 都市施設 | 都市計画法 第11条 | 地下鉄, 都市モノレール, 新交通システム | **No, and there is no definition of 地下鉄 anywhere in Japanese law.** See below |
| Hong Kong | the MTR franchise | Mass Transit Railway Ordinance Cap. 556, Rail Merger Ordinance 2007 | whatever the franchise covers | No. It is a franchise boundary with no technical test, and it covers the Light Rail and the Airport Express alongside the heavy metro |
| Macau | 輕軌交通系統 | Law 18/2019 | the LRT system | No. The name says light rail and the system is in fact a rubber-tyred automated people mover |

### 1.1 The Japan finding

Japan is the case that closes the argument. No Japanese statute held in this repository defines 地下鉄. What is on disk is MLIT's 鉄道統計年報 operator classification, which classes undertakings as JR, 民鉄, 公営 and 第三セクター rather than by mode and reports モノレール and 新交通システム as separate system categories, so the ministry counts by undertaking and by system category and never by a defined category called subway. The stronger negative, that neither 鉄道事業法 nor 都市計画法 第11条 contains such a definition, is very likely right and neither statute is on disk, so it is a pending download in section 10 and **carries the same do-not-paste marker as source 8 until one of them is held.** If the largest metro market in the sample has no legal definition of the thing being counted, then no legal label can define the sample.

A sentence attributed to MLIT, 「地下鉄についての明確な定義はない」, circulates in our own working notes (`metro_definition_synthesis.md` line 102) and has been copied into the `graph.metro_term_in_jurisdiction` field of fourteen shipped JSON files. **It has no URL and no access date on disk.** It must not go into the paper in that form. The supportable version is the one written above, which rests on the 鉄道統計年報 classification that is on disk rather than on a quotation nobody can chase or on two statutes nobody here holds. Chasing the MLIT page, and downloading 鉄道事業法 and 都市計画法 第11条, are listed actions in section 7.5.

### 1.2 The JAMETRO inconsistency, computed from the roster on disk

The Japan Subway Association roster held at `August - revision/How each country defines the metro/JP/JP.txt` gives the per-operator route kilometres. Summing them this session:

| Grouping | Operators | Route km |
|---|---:|---:|
| The ten municipal and Metro subway undertakings (Sapporo, Sendai, Toei, Yokohama, Nagoya, Kyoto, Kobe, Fukuoka, Tokyo Metro, Osaka Metro) | 10 | 765.9 |
| The JAMETRO headline membership | 15 | 851.5 |
| The roster as printed, including 首都圏新都市鉄道 (Tsukuba Express) | 16 | 909.8 |

The 851.5 km figure that JAMETRO states in its own prose is the fifteen-operator sum, which the roster on disk reproduces exactly. The inconsistency is in what the fifteen contain. JAMETRO counts the Hiroshima Astram Line, which is automated guideway transit, as a subway. It counts Hokuso, Saitama Rapid and Toyo Rapid, which are through-running suburban extensions that MLIT does not count. It counts the Minatomirai Line, four kilometres of conventional railway in tunnel, and prints the Tsukuba Express, a 58.3 km commuter railway, on the same page. No technical test produces that list, and no technical test excludes the Rinkai Line, which is almost wholly in tunnel and is not on it.

UITP's own Japan total settles which boundary an international comparison actually uses. *Global Metro Figures*, page 4, verbatim from the PDF on disk: "Japan ranks third (973km), followed by the Republic of Korea (926km)". A national total of 973 km cannot be the ten subway undertakings (765.9 km) and cannot include JR East, whose Greater Tokyo network alone runs well past a thousand kilometres. It is consistent only with the subway layer plus the monorail and people-mover layer, and without the national and private suburban railways. That is T1 plus T2.

### 1.3 What follows

The rule cannot be **legal-first**, because there is no shared legal category to be first about. It is **functional-first with legal corroboration**. T1 is a published functional definition. T2 uses each jurisdiction's own boundary for the thing all six do possess, which is the designated urban system, so the exclusion of suburban rail is symmetric rather than a foreign standard imposed on one country. T3 uses a number a national standard supplies, and records rather than removes.

---

## 2. The post-filter method, stated as a procedure

The rule is applied as a **post-filter**, not as a search specification. We do not go looking for "metros" and hope the source data agrees. We take the candidate set the source platform gives us, then apply a published border to it, then record what the border did. Every step is reproducible from files in the repository.

**Step 1. Build the candidate set from the source platform, and say which platform.**
For the 47 mainland Chinese and Hong Kong and Macau networks the candidate set is the Amap rail-transit layer. For Korea it is the Korea Transport Database feed, for Japan the Open Data Platform for Public Transportation, for Taiwan the Transport Data eXchange, and for Kobe the Vijlbrief et al. 2022 build. The candidate set is honest provenance and it is not the criterion. Its contents are recorded per city in `supplementary_network_sources.csv`.

**Step 2. Apply T1 to every candidate line.** The test is on the right of way, not the vehicle. Pass or fail is recorded in `T1_uitp_line_criteria`, and a pass that required a judgement is recorded as an override in `dataset_v2/registry.py` with its evidence. There is exactly one such override in the sample, the Foshan Nanhai line, treated openly in section 4.

**Step 3. Apply T2 to every line that passed T1.** Membership of the designated system. Lines that fail are not silently dropped. Each is written into `registry.EXCLUDED` for its city with the failed test and a reason, so the reader can see the rule was applied rather than inherited. The register currently holds 85 entries across 41 cities, coded T2 29, T1 18, GAP 17, SEP 9, NOT_OPEN 7, MRG 4 and T3 1, and it is rendered per city in `inclusion_table_v2.md`. The single T3-coded entry is the Shanghai Maglev 磁浮示范运营线, which is absent from the 2025 file and is labelled by scope rather than filtered by it. The code is a misuse of the T3 label and will be recoded, since a line absent from the data is a GAP. This is audit uid SH-01, and 7.5 records the alternative disposition.

**Step 4. Record T3 and the fare flag for every line that passed both tests.** The commercial speed proxy is computed from the file itself as great-circle route length over summed in-vehicle time, and compared with the 60 km/h boundary. Where the proxy cannot be trusted, which is the case for routes of fewer than four stations and for routes whose stations were mislocated in the 2025 files, the scope is settled by the line's own designation and the reason is written into `T3_basis`. Neither T3 nor the fare flag removes anything.

**Step 5. Publish the per-line record.** One row per route with 30 fields, including the three tests, the basis for T3, the verdict, the technology, the legal class naming the jurisdiction's instrument, the headway with its source, the name provenance and the assignment confidence. The same block is written inside every deposited JSON file under `graph.routes`, so the reviewer-facing table and the deposit cannot drift apart.

**Why a post-filter and not a search.** A search specification would have to name in advance what counts, which is the thing in dispute. A post-filter can be audited, because the candidate set, the border and the outcome are three separate artefacts that a reader can check against one another. It also makes the rule portable: the same three tests can be re-run over the Vijlbrief European and North American set, which publishes no inclusion criteria at all, which is the only defensible way to make the cross-regional comparison the paper draws.

---

## 3. Technology neutrality

### 3.1 UITP's wording, verbatim

From `LR/01_regional_global_overviews/20250822_Global-Metro-Figures_Statistics-Brief_WEB.pdf`, methodological note, read this session:

> "In this statistics brief, metros are defined by UITP as 'high capacity urban guided transport systems, mostly on rails, powered with electricity and running on an exclusive right-of-way, with trains composed of a minimum of two cars and with a total capacity of at least 100 passengers per train'. Suburban railways (such as the Paris RER, Berlin S-Bahn, and Kuala Lumpur International Airport express line) are not included. Systems that are based on light rail vehicles, monorail, or magnetic levitation (maglev) technology are included if they meet all other above-mentioned criteria. Suspended systems are not included. A total of 237 urban guided networks are covered in this brief, divided into the following: 217 metro networks; 15 monorails; 8 people movers; 5 light rails; and 2 maglev systems. For simplicity, they are all referred to as 'metros' here."

Three things in that paragraph do the work. The definition **names no technology as a requirement**, only guidance, traction, right of way and train size. Its one nod to technology, "mostly on rails", is hedged by "mostly", which is precisely what leaves room for the rubber-tyred and maglev systems the same paragraph then admits by name. The exclusions are of a **system class**, suburban railway, illustrated by two networks and one airport express, not of a vehicle. And the closing sentence is the decisive one: UITP counts monorails, people movers, light rails and maglevs alongside metros and **refers to all of them as metros**.

**One caution, and it is a real one.** The itemised counts do not sum to the stated total. 217 plus 15 plus 8 plus 5 plus 2 is 247, against a stated 237. Do not reproduce the breakdown as a sum. Quote the total and the breakdown as UITP publishes them, or quote neither.

### 3.2 The Chinese standard says the same thing in its own way

GB/T 44413-2024, read this session from the PDF on disk, clause 5.1 lists ten 系统制式 inside 城市轨道交通, from 地铁系统 through 跨座式单轨系统 and 中低速磁浮系统 to 市域快速轨道系统. Clause 5.2.1 Table 1 then classifies **by service level and not by technology**: 城区轨道交通, 城区范围, 适用旅行速度 ≤60 km/h, against 市域或都市圈轨道交通, 市域、都市圈范围, ＞60 km/h. The technology column of Table 1 is a list of permitted types under each service level, not a boundary. That is precisely the shape of our T1 and T3: technology open, scope bounded.

CAMET's own accounting agrees. Summing the 2025 mode table on disk (`china_metro/data calibration/camet2025_table3_mode_km.csv`, 58 mainland cities), 地铁 accounts for 10,004.89 km against 市域快轨 1,706.00 km, with 有轨电车 641.11 km, 轻轨 225.80 km, 导轨式胶轮 186.98 km, 跨座式单轨 144.65 km, 胶轮导轨 (云巴) 79.91 km, 磁浮 57.86 km, 悬挂式单轨 10.50 km and AGT 10.19 km reported as separate modes inside the same 13,067.92 km umbrella, the ten summing to it exactly. The Chinese statistics separate scope from technology exactly as T3 does.

### 3.3 Why generalised travel time makes this a service question

The paper measures reachability between stations over increasing generalised travel time budgets. Generalised travel time is composed of in-vehicle time, waiting time taken as half the headway, and a transfer penalty. Every one of those three is a property of the **service**, and none of them is a property of the guideway.

A passenger boarding Chongqing Line 2 at 较场口 does not experience a straddle monorail. They experience a line with a short headway that interchanges with Line 1 in the same paid area on the same fare, and their generalised travel time to any other station in Chongqing is identical to what it would be if the same service ran on steel wheels. Removing the line would not change any passenger's journey, it would change only our description of it, and it would produce an accessibility figure for a network nobody rides. The same holds for Daegu Line 3, for the Taipei Wenhu Line, for the Yurikamome, and for the whole Macau system.

The attributes that **do** change generalised travel time are segregation from road traffic, which sets whether in-vehicle time is reliable, service scope, which sets how far a single boarding reaches, headway, which sets the waiting term, and fare integration, which sets whether a transfer is a transfer or a new journey. The rule tests the first of those in T1, records the second in T3, publishes the third per route with its source, and flags the fourth. Vehicle technology is absent because it is causally absent from the quantity being measured, and that is the substantive argument, not a convenience.

### 3.4 The one honest limit of neutrality

Technology neutrality is not a licence to admit anything guided. T1 still fails street running and shared lanes, because a vehicle stopping at traffic lights has an in-vehicle time that is not a network property. UITP also excludes suspended systems outright, and we follow that, which is why the Wuhan 光谷空轨 is out. Neutrality is about refusing to privilege steel wheel on steel rail, not about abandoning the right-of-way test.

---

## 4. Worked cases

All fields below are read from `inclusion_table_v2.csv` this session. "Proxy" is `commercial_speed_proxy_kmh`, "n" is `n_stations`.

### 4.1 In the sample on T1 technology neutrality

| Case | Row | Technology in the file | n | Proxy | T1 | T2 | T3 | Why it is in |
|---|---|---|---:|---:|---|---|---|---|
| Chongqing Line 2 | Chongqing r2 | straddle monorail | 25 | 26.7 | pass | pass | urban | 跨座式单轨系统, GB/T Table 4 row 3, inside 城市轨道交通. UITP admits monorail by name |
| Chongqing Line 3 | Chongqing r4 | straddle monorail | 39 | 31.1 | pass | pass | urban | same. r3, the 空港线 section, 7 stations, proxy 39.9, is the same line stored separately |
| Wuhu Line 1 | Wuhu r1 | straddle monorail | 25 | 23.7 | pass | pass | urban | the whole Wuhu system is monorail. A technology-strict rule would delete the city |
| Wuhu Line 2 | Wuhu r2 | straddle monorail | 11 | 32.5 | pass | pass | urban | same |
| Daegu Line 3 | Daegu r3 | straddle monorail | 30 | 27.7 | pass | pass | urban | 도시철도 under 도시철도법 제2조, which admits monorail explicitly |
| Busan-Gimhae LRT | Busan r5 | rubber-tyred AGT / APM | 21 | 31.7 | pass | pass | urban | 도시철도. Busan Line 4 (r4, AGT, 14 stations, 27.2) is the same case |
| Taipei Wenhu Line | Taipei r2 | rubber-tyred AGT / APM | 24 | 29.7 | pass | pass | urban | 大眾捷運系統, completely independent right of way under 大眾捷運法 第3條 |
| Seoul Sillim Line | Seoul r13 | rubber-tyred AGT / APM | 11 | 26.2 | pass | pass | urban | 도시철도, privately operated, which shows T2 is about designation and not ownership |
| Seoul Ui-Sinseol Line | Seoul r14 | driverless light metro | 13 | 28.5 | pass | pass | urban | same |
| Yurikamome | Tokyo r15 | rubber-tyred AGT / APM | 16 | 24.3 | pass | pass | urban | 新交通システム inside 都市高速鉄道. Reviewer 2 named this line, and the answer is that it is in, not that it is a lesser tier |
| Nippori-Toneri Liner | Tokyo r16 | rubber-tyred AGT / APM | 13 | 27.1 | pass | pass | urban | operated by the Toei bureau, its rail facilities built as a 都市計画都市高速鉄道事業 |
| Tokyo Monorail | Tokyo r17 | straddle monorail | 11 | 38.9 | pass | pass | urban | a single 17.8 km urban undertaking with its own fares and no through-running, and 79 percent owned by JR East, which must be stated, because T2 is about the undertaking and not the shareholder. **Both figures are hand-coded in `registry.py` and carry no external citation**, so they are safe in this internal worked-cases table and must not enter section 9 until the source marked pending in section 10 is on disk |
| Macau, whole system | Macau r1, r2, r3 | rubber-tyred AGT / automated people mover, corrected on 2 September, see 7.4 | 13, 2, 2 | 20.6, 33.7, 47.6 | pass | pass | urban, and urban (proxy unreliable) on r2 and r3 | 輕軌交通系統 under Law 18/2019. Under any technology-strict rule Macau leaves the sample entirely |
| Shanghai Pujiang Line | Shanghai r17 | rubber-tyred AGT / APM | 6 | 26.9 | pass | pass | urban | 城市轨道交通, metro fare, interchange with Line 8 at 沈杜公路 |
| Guangzhou APM | Guangzhou r20 | rubber-tyred AGT / APM | 9 | 25.2 | pass | pass | urban | Zhujiang New Town APM, inside the Guangzhou network |
| Beijing S1 maglev | Beijing r25 | medium-low-speed maglev | 8 | 23.1 | pass | pass | urban | 中低速磁浮系统, GB/T Table 4 permits it at 城区 scope, metro fare, proxy well under 60 |

### 4.2 The one T1 override, stated honestly

| Case | Row | Recorded as | n | Proxy | Verdict |
|---|---|---|---:|---:|---|
| Foshan 南海有轨电车1号线 | Foshan r4 | technology "street tram", legal_class 城市轨道交通: 有轨电车系统 (GB/T Table 4 row 6), mode "tram", **T1 pass by override** | 15 | 23.9 | include |

This is the row a reviewer will stop on, and it must be presented rather than defended. The line is locally classed 有轨电车 and the GB/T class in the row says so. It passes T1 by a **recorded override** on the ground that its right of way is fully exclusive, roughly 79 percent grade separated with underground and elevated sections and the remainder at grade behind barriers, and that it functions as an at-grade metro with a transfer to the 广佛线 at 𧒽岗. The override, its evidence and its date are written into the row's `note` field and into `registry.py`, so it is auditable rather than silent.

Three facts must travel with it. First, the 79 percent figure is **our own derivation** from the published segment lengths, 11.3 km of the 14.3 km route, and it carries no external citation, so the prose must either say "predominantly grade separated" or give the denominator and name the derivation. **Done:** the qualification is now in the row's `note` through `T1_OVERRIDE`, and the appendix fragment gives the denominator. Second, the registry itself records that the presence or absence of level crossings on the at-grade section is undocumented. Third, the technology label "street tram" beside a T1 pass reads as a self-contradiction and should be changed. The recommendation is in section 7.4.

The override is also the reason the rule cannot be stated as "trams are excluded". It is stated as "street running and shared lanes are excluded", which is a test on the right of way, and this line passes it.

### 4.3 Out on T2, the system test

| Case | Where it is recorded | Reason |
|---|---|---|
| JR Yamanote Line | `registry.EXCLUDED["Tokyo"]`, code T2 | **The concession.** 34.5 km on dedicated track inside the 23 wards, two to four minute headways, fully fare integrated. It passes T1 on every functional measure and is out because JR East is the successor to the national railway and runs shinkansen, intercity, regional and freight over one network. This is the same ground on which UITP excludes the RER and the S-Bahn and Roth et al. exclude the RER and NetworkRail. State it in the paper in one sentence, because a Tokyo-literate reviewer looks for it first and finding it pre-empted is far more convincing than a rule that pretends the case does not arise |
| Tokyu, Odakyu, Keio, Seibu, Tobu, Keisei, Keikyu, Sotetsu | same register, T2 | 大手私鉄 suburban railways of 35 to 460 km across several prefectures. Their through-running onto Metro and Toei is truncated at the metro boundary, which the data already does |
| Saitama Rapid, Toyo Rapid, Hokuso | same register, T2 | through-running extensions into Saitama and Chiba, separate undertakings. JAMETRO counts them as subways, MLIT does not, which is the inconsistency of section 1.2 in one line |
| Korail sections of Seoul Lines 1, 3 and 4 (경부선, 경인선, 경원선, 일산선, 과천선, 안산선) | `registry.EXCLUDED["Seoul"]`, T2 | 일반철도 operated by the national railway. The Seoul file is truncated at the Seoul Metro boundary, so Line 1 is 서울역 to 청량리, Line 3 is 지축 to 오금, Line 4 is 당고개 to 남태령 |
| Sinbundang Line | same register, T2 | privately operated by Neo Trans, and out because it is designated 광역철도 and not 도시철도. The clearest single demonstration that T2 turns on designation and not on ownership, since privately operated Seoul Line 9, the Sillim Line and the Ui-Sinseol Line are all 도시철도 and all in |
| AREX | same register, T2 | reclassified from 도시철도 to 일반철도 on 9 May 2014 |
| GTX-A | same register, T2 | 광역급행철도 |
| Hong Kong Light Rail | `registry.EXCLUDED["Hong Kong"]`, coded **T1** | 68 stops with street-running sections. Note this is a T1 exclusion and not a T2 one. It is inside the MTR franchise, so T2 admits it, and it fails on the right of way. Hong Kong Tramways and the Peak Tram are the same case |
| Hong Kong Express Rail Link | same register, T2 | MTR-operated but part of the national high-speed network |
| Beijing 市郊铁路 S2, 副中心线, 怀密线, 通密线, 东北环线 | `registry.EXCLUDED["Beijing"]`, T2 | China Railway Beijing Group services on national railway track |

### 4.4 In the sample, recorded Tier B on scope

Every row below is **in the main sample**. Tier B is the scope label, and it never removes anything from the headline results.

| Case | Rows | Basis recorded in T3_basis |
|---|---|---|
| Chengdu S3 资阳线 | Chengdu r2 | "S3 Chengdu-Ziyang line, 市域 intercity; proxy unreliable (impossible link)" |
| Chengdu Line 18 | Chengdu r16, r18 | "speed proxy 75 km/h above 60" and "speed proxy 81 km/h above 60". One line stored under two route ids |
| Chengdu Line 19 | Chengdu r17 | "Line 19, 160 km/h airport express; proxy unreliable (mislocated stations)" (to be rewritten, see 7.5 (g), which drops "airport express" and rests the label on the 市域快线 designation) |
| Guangzhou Line 18 | Guangzhou r17 | "Line 18, 160 km/h express to Nansha; proxy unreliable (mislocated stations)" |
| Guangzhou Line 22 | Guangzhou r19 | "Line 22, 160 km/h express; proxy unreliable (mislocated stations)" |
| Zhengzhou 城郊线 | Zhengzhou r12 | "designated 市域 / regional line" |
| Zhengzhou 郑许线 | Zhengzhou r13 | "designated 市域 / regional line", and it crosses into Xuchang |
| Nanjing S1, S3, S6, S7, S8, S9 | Nanjing r11 to r16 | "designated 市域 / regional line", six records, the largest Tier B block in one city |
| Wenzhou S1 and S2 | Wenzhou r1, r2 | "designated 市域 / regional line". These are the whole of Wenzhou |
| Taoyuan Airport MRT | Taoyuan r1 | "51 km cross-municipality corridor Taipei-Taoyuan-Zhongli with express and commuter patterns, the label rests on the corridor and not on the all-stop speed proxy of 34.1 km/h that the file records (audit TAOYUAN-01, open for decision)". The basis string was rewritten on 2 September, because the one it replaced claimed a 40 km/h proxy the file does not show. **Still contested, see 7.5 item (g)**, because the recorded proxy is below the boundary, so the Tier B label rests on the corridor argument alone |
| Chongqing 璧铜线 and 江跳线, Dalian Line 13, Jinhua 金义东线 both sections, Qingdao Line 8, 蓝谷快线 and 西海岸快线, Suzhou Line 11, Taizhou S1, Tianjin 津静线, Xian 西户线 | 12 further rows | "designated 市域 / regional line" in every case |
| Shanghai 市域机场线 | Shanghai r23 | "speed proxy 76 km/h above 60". Added in the 1 September v2 additions, which is why it is absent from every count published before that date |
| Beijing 大兴机场线 | Beijing r18 | "Daxing Airport Express, 160 km/h; proxy unusable (25 km link stored as 2 min)". The only row carrying both the Tier B label and the fare flag |

### 4.5 The four fare-flagged rows

| Row | Line | T3 scope | Also Tier B? |
|---|---|---|---|
| Beijing r18 | 大兴机场线 Daxing Airport Express | metropolitan (Tier B) | yes, the only one |
| Beijing r22 | 首都机场线 Capital Airport Express | urban | no |
| Changsha r7 | 磁浮快线 Maglev Express | urban (proxy unreliable, 3 stations) | no |
| Hong Kong r6 | 机场快线 Airport Express | urban | no |

All four are **retained**. The flag and the Tier B label are independent attributes, and only Beijing r18 carries both. Note also that a fourth dedicated airport express, Shanghai 市域机场线 (r23), is Tier B and carries **no** fare flag, so the two attributes cannot be read off one another.

**A correction to how the flag is justified.** The verdict string in the CSV currently reads "include, flagged: premium fare not integrated (UITP precedent: KLIA Express excluded)". UITP does name the Kuala Lumpur International Airport express line as an exclusion, verified verbatim above, but it names it as a **removal**, and we retain. Citing UITP as the precedent for a flag we do not act on is a misattribution a reviewer can catch. Rewrite the verdict string and the memo wording as "include, flagged: premium separate fare, not fare-integrated with the rest of the network", and describe the flag as our own transparency measure.

### 4.6 Removed from the submitted sample

| Case | What happened |
|---|---|
| Beijing 西郊线 and 亦庄T1有轨电车 | Present in the submitted files as v1 routes 23 and 26, both technology "street tram", both recorded **exclude: fails T1**. In v2 they are removed by repair rather than carried as exclude rows, which is why v2 shows zero T1 failures inside the table. Removing them also fixes a data defect, since the Yizhuang tram is the source of the 16.5 km link traversed in two minutes that contaminated Line 17. **Documentary gap:** there is currently no entry for either tram in `registry.EXCLUDED["Beijing"]`, verified this session, so the exclusion has no trace in the reviewer-facing register. Fix listed in 7.5 (e) |

---

## 5. What the rule does to the sample

All figures computed this session from `inclusion_table_v2.csv` unless another file is named.

### 5.1 Headline

| Quantity | Value |
|---|---:|
| Route records | 420 |
| Cities | 62 |
| Columns per record | 30 |
| T1 pass | 420 of 420 |
| T2 pass | 420 of 420 |
| Verdict: include | 386 |
| Verdict: include as Tier B (metropolitan scope), report in sensitivity sample | 31 |
| Verdict: include, flagged premium fare | 3 |
| Verdict: exclude | 0 |
| `fare_flag` non-empty | 4 |
| Stations, 62 networks (`asia/L2_v2`) | 7,480 |

The verdict column resolves in priority order, scope before fare, which is why the Tier B and fare-flagged Beijing Daxing row appears under Tier B and the fare-flagged verdict count is 3 against 4 flagged rows.

**One headline sentence, for reuse everywhere:** 420 route records across 62 cities, all passing T1 and T2, of which 31 records (30 distinct lines in 16 cities) are Tier B by scope and 4 carry the premium-fare flag.

### 5.2 T3 scope

| `T3_scope` | Records |
|---|---:|
| urban | 377 |
| metropolitan (Tier B) | 31 |
| urban (proxy unreliable) | 12 |

`speed_proxy_reliable` is False on 14 records. Twelve of those are the "urban (proxy unreliable)" stubs, all carrying the identical basis "speed proxy unreliable: fewer than 4 stations": Changsha r7 磁浮快线 (3 stations), Chengdu r14 1号线 (3) and r15 17号线 (3), Hong Kong r1 迪士尼线 (2), r11 东铁线 落马洲支线 (2) and r12 将军澳线 康城支线 (3), Macau r2 石排湾线 (2) and r3 横琴线 (2), Nanchang r1 1号线 (3), Taipei r4 新北投支線 (2) and r6 小碧潭支線 (2), Ürümqi r2 机场捷运 (2). The remaining two unreliable rows are Beijing r18 大兴机场线 (3 stations, proxy 118.2) and Xian r17 西户线 (2 stations, proxy 58.9), both settled as Tier B by designation rather than by the number.

Note what the stub list contains. Five are branches or shuttles of ordinary metro lines (Hong Kong 迪士尼线, 落马洲支线 and 康城支线, Taipei 新北投支線 and 小碧潭支線) and two are fragments of ordinary lines stored under a second route id (Chengdu 1号线, Nanchang 1号线, both carrying `shares_line_with_routes`), so seven of the twelve are not lines in their own right at all. None of the twelve is a borderline inclusion decision. The unreliability is a measurement artefact of very short routes, not a scope ambiguity.

### 5.3 Tier B by city

31 records, 30 distinct city-and-line pairs, across **16 cities**. Chengdu Line 18 accounts for the difference, being stored under two route ids.

| City | Tier B records | | City | Tier B records |
|---|---:|---|---|---:|
| Nanjing | 6 | | Beijing | 1 |
| Chengdu | 4 | | Dalian | 1 |
| Qingdao | 3 | | Shanghai | 1 |
| Chongqing | 2 | | Suzhou | 1 |
| Guangzhou | 2 | | Taizhou | 1 |
| Jinhua | 2 | | Taoyuan | 1 |
| Wenzhou | 2 | | Tianjin | 1 |
| Zhengzhou | 2 | | Xian | 1 |

### 5.4 The sensitivity sample

Four cities consist **only** of Tier B routes and therefore have no network at all once Tier B is removed: **Jinhua, Taizhou, Taoyuan, Wenzhou**.

| Sample | Cities | Stations | Source |
|---|---:|---:|---|
| Main sample, all lines | 62 | 7,480 | `asia/L2_v2`, counted this session |
| Tier A sensitivity sample, Tier B removed | 58 | 7,126 | `asia/L2_v2_tierA`, 58 files, counted this session |

The sensitivity sample loses 4 cities and 354 stations, which is 4.73 percent of the stations. That is the entire cost of the scope question, and it is small. It is worth saying so explicitly in the response, because it converts a contested definitional argument into a measured robustness check.

### 5.5 Technology census

Technology is a recorded attribute and plays no part in any verdict. The census over the 420 records:

| Technology | Records |
|---|---:|
| steel-wheel metro | 354 |
| steel-wheel suburban / regional express | 22 |
| rubber-tyred AGT / automated people mover | 11 |
| steel-wheel light rail (轻轨), fully segregated | 7 |
| straddle monorail | 7 |
| steel-wheel linear-motor metro | 5 |
| steel-wheel dedicated airport express | 4 |
| rubber-tyred metro with central guide rail | 3 |
| medium-low-speed maglev | 2 |
| steel-wheel driverless light metro | 2 |
| steel-wheel driverless medium-capacity metro | 2 |
| street tram | 1 |

All 22 suburban and regional express records are Tier B. The single "street tram" record is the Foshan Nanhai override of section 4.2, and it should be relabelled before publication, see 7.4. All three Macau rows were recorded as steel-wheel metro and are in fact a rubber-tyred automated people mover, see 7.4. That correction is applied in the census above, which moved from 357 steel-wheel metro and 8 AGT to **354 steel-wheel metro and 11 rubber-tyred AGT**. The corrected pair is the one to quote everywhere.

### 5.6 The change from the submitted state

| | v1, submitted (`inclusion_table.csv`) | v2 (`inclusion_table_v2.csv`) |
|---|---:|---:|
| Route records | 417 | 420 |
| Cities | 62 | 62 |
| Stations | 7,456 | 7,480 |
| Include | 382 | 386 |
| Tier B | 30 | 31 |
| Fare-flagged verdict | 3 | 3 |
| Exclude, fails T1 | 2 | 0 |

Cities whose route or station counts moved, computed from `inclusion_summary.csv` against `inclusion_summary_v2.csv`:

| City | v1 routes / stations / Tier B | v2 routes / stations / Tier B | What changed |
|---|---|---|---|
| Beijing | 30 / 417 / 1 | 28 / 399 / 1 | the two street trams removed |
| Foshan | 3 / 64 / 0 | 5 / 85 / 0 | two v2 additions, the Nanhai line and the Line 3 northern section |
| Guangzhou | 21 / 309 / 2 | 22 / 309 / 2 | Line 13 split out of a conflated record, stations unchanged |
| Hefei | 7 / 172 / 0 | 6 / 172 / 0 | a duplicate 4号线 record dropped |
| Nantong | 1 / 43 / 0 | 2 / 42 / 0 | Line 2 split out of Line 1, one unopened station removed |
| Ningbo | 6 / 137 / 0 | 7 / 156 / 0 | Line 7 added |
| Shanghai | 22 / 411 / 0 | 23 / 414 / 1 | 市域机场线 added, and it is Tier B |

Kobe is **kept** and its 2006 Vijlbrief vintage disclosed. The study reports **62 networks**. There is no 61-network case.

---

## 6. Approaches considered and rejected

| Approach | Why it fails |
|---|---|
| **Operator brand, or "what is on the official metro map"** | Asymmetric by construction. Chinese operators put 市域快轨 lines on their metro maps and sell one fare across them, Japanese operators do not put JR suburban lines on theirs. Adopting brand would keep the Chinese regional tier and drop the Japanese urban tier, which is the branding problem in a new costume. It is also operator-published, so it hands the sample definition to the subjects of the study |
| **OSM administrative boundary, or any admin clip** | Non-comparable across countries and non-comparable within one. Chengdu 成都市 is `admin_level` 5, a prefecture-level city so large that the S3 line to Ziyang begins inside it, so an admin rule keeps part of a line the scope argument wants recorded as regional. Tokyo 東京都 is `admin_level` 4, a prefecture whose boundary severs the through-running into Kanagawa, Saitama and Chiba, so the same rule cuts legitimate metro. The two errors run in opposite directions in the two largest countries in the sample. It is also the wrong unit: the whole line is the unit of inclusion, and clipping stations by a polygon severs the legitimate suburban tails of genuine metro lines |
| **Functional Urban Area** | Wrong layer. An FUA is a dense core plus its commuting zone, which is the suburban tier itself, so an FUA mask would keep every 市域快轨 line and settle nothing. If a geographic layer is ever wanted it should be the urban-centre core and only as corroboration, never as a clipping mask |
| **"Strict metro", heavy rail only** | **There is no source for it.** That is the finding, not a rhetorical point. UITP goes the other way in writing. Derrible and Kennedy define metros as urban rail with exclusive right of way whether underground, at grade or elevated, with no technology test. Taiwan's 大眾捷運法 第3條 is functional and omits technology deliberately. Japan has no definition at all. Only GB/T 44413 gives 地铁 a narrow technical meaning, and CAMET publishes the Chongqing monorails inside the Chongqing network anyway. So a paper that says "we restricted to metros in the strict sense" invites the question "strict according to whom" and has no answer that survives all six jurisdictions. Measured on the 62 networks, the strict rule would also delete Macau and Wuhu entirely and remove roughly a third of Daegu, a quarter of Chongqing, a sixth of Taipei and a seventh of Tokyo, and every line it removes is fully segregated, fare integrated and branded as metro by its own operator |
| **A purely legal rule, that is "whatever each country calls a metro"** | Defeated by section 1. There is no shared category, Japan has no definition, and Korea's 도시철도 umbrella would admit street trams while Taiwan's 大眾捷運系統 admits non-completely-independent light rail. A legal-first rule produces six different samples and calls them one |
| **A measured spacing and speed screen that filters** | Proposed in `metro_terminology_decision.md` sections 2 to 4 and **not adopted**. Two defects. It would exclude 郑许线 and Chengdu S3 from the sample, which contradicts the 22 August decision to keep all line types and report Tier B as a sensitivity sample, and its threshold was never set from the distribution, so the screen as written has no number in it. The measured attributes are retained, but as **T3, which records and does not filter**. The spacing audit remains worth running as corroboration for the T3 boundary, and is listed as an open question |

---

## 7. Document reconciliation

### 7.1 The drift, D1 to D8, checked against the files

| ID | Claim | Verdict this session |
|---|---|---|
| D1 | `02_RESPONSE_DRAFTS.md` and `revision_plan_definition_and_dataset.md` section 4 use a **technology** tier scheme (Tier A strict, Tier B adds AGT, monorail, maglev, airport express) that contradicts 07's **scope** tiers | **Confirmed.** Both documents also state that both tiers exclude street-running trams and light rail without exception, which the Nanhai override reverses, and `02` states that the Gimpo Goldline is excluded as commuter or regional railway, which 07 section 4 contradicts by listing it as another city's designated 도시철도. Neither file may be used as source text |
| D2 | Counts drift: 07 says 417 and 415, memo 09 says 415, the CSV has 420 | **Confirmed and quantified.** 417 (v1) to 420 (v2). Tier B 30 to 31 with Shanghai 市域机场线. Foshan 3 to 5, Shanghai 22 to 23, Ningbo 6 to 7, Guangzhou 21 to 22, and two changes the brief did not list, **Beijing 30 to 28** with the trams removed and **Hefei 7 to 6** with a duplicate 4号线 dropped. Tier B spans **16 cities, not 15**, because Shanghai joins |
| D3 | `02_RESPONSE_DRAFTS.md` assumes 61 networks with Kobe dropped | **Confirmed** at two places in that file. It is reversed by the 22 August decision. The submitted Table 1 already has 62 rows including Kobe, so the only place 61 still leaks is the 4TU deposit |
| D4 | The Nanhai row reads technology "street tram", legal_class 有轨电车系统, mode "tram", T1 "pass" | **Confirmed verbatim** from the CSV. The row's `note` does carry the override reason, so it is not undocumented, but the technology label still reads as a contradiction on the face of the table. Relabel, see 7.4 |
| D5 | main.tex 3.4 says Daejeon, Gimpo and Gwangju were excluded for absence of data, but they are in the KTDB feed on disk | **Confirmed, and worse than stated.** Counted this session from `ktdb_subway_lines.json`: 대전1호선 22 stops, 광주1호선 20 stops, 김포도시철도 10 stops, and two further unsampled 도시철도 systems, 의정부경전철 15 and 용인경전철 15. Five of the six cities the sentence names have no availability defence, because `registry.MISSING_CITIES` records Osaka as "not collected, Osaka Metro GTFS available via ODPT" and Nagoya as "not collected, the city publishes open data through its catalogue", and `inclusion_table_v2.md` prints both strings in the reviewer-facing table. Only Pyongyang is genuinely absent |
| D6 | main.tex 3.4 contains the "tightly coordinated" sentence R2-2 attacked | **Confirmed.** Line 278 still reads "Commuter rail lines are excluded if they are not directly operated by the metro operator or are not tightly coordinated with connecting metro lines." That is an operator-and-coordination test that appears nowhere in the rule of record, is unmeasurable, and is the exact sentence the reviewer challenged |
| D7 | The limitations paragraph attributes the commuter-rail exclusion to "a strict metro definition" | **Confirmed** at line 712. It is the opposite of the framing of record. The definition is deliberately broad, and the exclusion runs on system membership |
| D8 | Memo 09's per-city table is pre-additions | **Confirmed.** Four city rows move (Foshan, Guangzhou, Ningbo, Shanghai) and six totals move. Guangzhou's station count does not move, because its extra route is a split |

Two further findings not in the D-list but of the same kind. `main.tex` line 277 misquotes UITP, keeping the exclusive right of way but dropping the two train-size criteria and the technology-neutrality clause and adding "fully grade-separated", "at least medium capacity" and "at high frequency", none of which UITP states. And `main.tex` line 284 asserts that 62 systems were sampled "out of the 68 metro systems operating in the East Asia region", where the denominator 68 has no source anywhere in the workspace.

### 7.2 What is superseded, and on what

| Document | Superseded on | Still usable for |
|---|---|---|
| `07_INCLUSION_RULE.md` | **Its numbers**, sections 5, 8 and 9. Also its section 5 exclude row, which no longer describes any record | **The rule itself**, sections 0 to 4 and 6, which this memo carries forward unchanged. The per-jurisdiction table, the worked Tokyo and Seoul boundaries, and the residue list |
| `06_SCOPE_DECISION.md` | **In full**, not only sections 8 and 9 as its own banner says. Its sections 3 and 5 carry a technology-strict Tier A that was costed and then rejected, and its section 5 proposes dropping the three airport expresses that are in fact retained | Its section 1, the argument that "strictly metro" has no citable source, which is reproduced in section 6 above and remains the strongest single paragraph in the file |
| `02_RESPONSE_DRAFTS.md` | **In full on scope, tiers, trams, airport expresses and Kobe.** Every tier statement in it is the technology scheme | Its R2-3, R2-4, R2-8 and R2-10 drafts, which this audit did not touch |
| `revision_plan_definition_and_dataset.md` | Decisions **D2, D3, D4 and D5** and the whole of **sections 4 and 5**, including the LaTeX-ready subsection, which states the technology-tier boundary as manuscript text | Its work-package structure and timeline |
| `metro_definition_synthesis.md` | **Sections 11 to 13**, the A1 to A5 two-tier definition, the line-level decision table built on it, and the section 13 vocabulary rule that forbids "rapid transit". Note the file is internally inconsistent: its line 228 already defines Tier B by scope, in agreement with 07 | Sections 1 to 10, the jurisdiction-by-jurisdiction synthesis, **with the caveat in 7.6** |
| `metro_terminology_decision.md` | **Sections 2 to 4.** Its section 3 criterion makes a measured spacing-and-speed screen the decision rule and its section 4 worked cases exclude 郑许线 and Chengdu S3, both of which contradict T3 and the retained-Tier-B decision | Its section 1 decision on the word "metro", its section 5 rejected approaches, which are reproduced and extended in section 6 above, and its section 7 bibliography |
| `09_VALIDATION_AND_TRANSPARENCY.md` | **Nothing on the rule.** It uses the scope meaning of Tier B correctly throughout | Everything, once the counts are patched. It is stale only on numbers |
| `submitted_version/main.tex` | Section 3.4 definition paragraphs and the limitations paragraph | Replacement text in section 9 below |
| `README.md` (analysis) | Its "five decisions that unblock the rest" section, which presents all five as open and records the Kobe correction in the direction later reversed | The file inventory |

Every superseded document needs a banner at its head naming this memo, because at present a reader landing on `06` or on the synthesis finds a fully worked, internally consistent and wrong tier scheme with no warning.

### 7.3 The numbers now of record

These supersede every count in `07`, `09`, `06`, `02`, the synthesis, the revision plan, the data-package README and the network-sources table.

| Quantity | Of record | Where the stale value still appears |
|---|---:|---|
| Route records | **420** | 07 sections 5 and 8 say 417 and 415, 09 section 1 says 415 in three rows, `DATA_PACKAGE_README.md` line 28 says 417, `supplementary_network_sources.csv` sums to 417 |
| Cities | **62** | 02 says 61 in two places |
| Stations | **7,480** | the network-sources CSV sums to 7,456, `DATA_PACKAGE_README.md` line 13 gives 7,437, and 09 states no station total |
| Columns per record | **30** | 09 line 12 says 28 |
| Include | **386** | 07 says 385, 09 says 382 |
| Tier B records | **31** | 07 and 09 say 30 |
| Tier B distinct lines | **30** | 07 and 09 say 29 |
| Tier B cities | **16** | 07 and 09 say 15, both omitting Shanghai |
| Fare-flagged rows | **4** | correct in 09, absent from 06 which proposes removal |
| Fare-flagged verdicts | **3** | correct where stated |
| T1 failures in the table | **0** | 07 section 5 still carries an exclude row for the two Beijing trams |
| Cities in the Tier A sensitivity sample | **58** | 06 section 3 says 59 losing three cities, omitting Wenzhou |
| Stations in the Tier A sample | **7,126** | 06 carries a v1 figure |
| Technology census | as in 5.5 | 09 gives the pre-additions census, missing the street-tram row and one airport express |

### 7.4 The Nanhai technology relabel, and the Macau technology correction

**Nanhai.** The row's inclusion outcome is correct and must not change. What is wrong is the printed technology string. Recommendation:

- `technology`: change `street tram` to **`segregated pre-metro (tram vehicle on exclusive right of way)`**. Implement as a new vocabulary constant beside the existing technology constants in `registry.py`, applied through a small `TECH_OVERRIDE` dict keyed `("Foshan","4")` so it cannot be swallowed by the v2 bypass.
- `mode`: change `tram` to **`pre-metro`**.
- `legal_class`: **leave unchanged** at 城市轨道交通: 有轨电车系统 (GB/T 44413-2024 Table 4 row 6). It is the honest local class and changing it would be the actual misrepresentation.
- `note`: keep the existing override text, and add that the grade-separation share is our own derivation from segment lengths.

That combination is defensible in front of a reviewer: the row says plainly "this line is legally a tram and it is in the sample because its right of way is exclusive", which is the rule doing its job rather than an exception hiding.

**Macau. Applied 2 September.** All three Macau rows carried `technology = steel-wheel metro`, which contradicts the registry's own jurisdiction note, since the Macau LRT is a rubber-tyred automated people mover. A `TECH_OVERRIDE` dict was added to `registry.py` with one entry per key, so that a repeated key cannot silently replace an earlier one, and `annotate.py` applies it outside the v2 name bypass. Nothing else moved: T1 is technology-neutral, so pass, pass, urban and include all stand. The census now reads **354 steel-wheel metro and 11 rubber-tyred AGT**, and that corrected pair must be used in every memo, response paragraph and supplementary caption that quotes the census.

### 7.5 Action register

The full register of the 2 September audit, 506 raw findings, 391 confirmed after three-lens adversarial verification and 115 refuted, is at
`August - revision/analysis/audit/INCLUSION_AUDIT_FINDINGS_2026-09-02.md`. **Cite that file rather than this table for any individual item.** The classes below account for the **130 findings that were transmitted with content**, and the representative uids let a reader find the detail. The remaining 261 confirmed findings were returned as a count only, with no uid, category, claim, file or fix attached to any of them, and that is recorded as a known hole in section 4 of the register itself (register lines 37 and 796). The action list here is therefore complete only for the 130.

**No confirmed finding overturns the rule.** Not one changes a T1 or T2 outcome, and three touch a T3 outcome, QD-01 and WUXI-2 by correcting a misidentified line, and TAOYUAN-01 as a decision rather than a correction. What the audit found is data, labelling and documentation defects, plus one genuine scope question (Taoyuan).

| Class | What it is | Representative uids | Disposition |
|---|---|---|---|
| **(a) Metric definition, table-wide** | `length_km_greatcircle` and `in_vehicle_min_sum` are summed over **directed** links, so both are twice the one-way value, while the legend calls the first a lower bound on track length. Median ratio to walked path 2.000 | SAP-01, SEL-01, WEN-01, TZ-02, BUSAN-1, CC-3, CZ-1, DAEGU-2 | **Action.** One fix in `annotate.py`: deduplicate by unordered station pair before summing. Regenerate the CSV, the md and the package copy, and reword the legend. Changes no verdict and no speed proxy. Fix once, then re-read every km figure quoted anywhere |
| **(b) Route identity, splits and merges** | Records that hold two lines, or one line twice | CQ-1 (Chongqing loop plus 6号线东站段 double counted), GZ-1 (Line 10 holds the Line 14 Knowledge City branch), WUXI-1 (Line 4 holds S1 锡澄线), SHA-01 (Shaoxing branch merged into the main line, 135 P pairs wrongly no-transfer), ZZ-1 (Zhengzhou 5号线 stored twice), XMN-01 (Xiamen phantom link) | **Action, and it moves the route total.** Three splits add three records, one duplicate removal takes one away. Arithmetically 420 plus 3 minus 1 is **422**, but that is a projection and **not a number of record** until the rebuild runs. WUXI-1 and QD-01 each move a designated 市域快轨 line into Tier B, so 31 becomes 33, or 32 if TAOYUAN-01 is resolved to urban. None of these is a number of record until the rebuild runs, and the Tier A sample changes with them. **Do not typeset section 9 before this is done** |
| **(c) Label errors with no rule consequence** | Wrong line name, wrong technology, wrong provenance token on a row whose verdict is correct | GZ-2 and registry#F1 (广佛线 printed as "Zhujiang New Town APM"), HK-1 (route 12 is the 坑口–宝琳 section), MO-1 and registry#F3 (Macau technology), KOBE-1 (headway source token), CHA-1 (Changsha maglev Amap id), D4 (Nanhai) | **Action.** All are one-line registry edits plus a regenerate. GZ-2 is the most visible, because the table currently prints two different lines under one English name |
| **(d) Stations in the file that were not open at the reference date** | Deferred or post-reference stations carried in the 2025 files | FUZ-1 (Fuzhou, 3 stations), JH-1 (Jinhua, 2 stations), CQ-3 (Chongqing, 3 to verify) | **Action.** Follow the Nantong 南通火车站 precedent: remove in repair, bridge the link, disclose as NOT\_OPEN. Affects station counts and therefore Table 1 |
| **(e) Exclusion register incomplete, or coded with the wrong reason** | A service correctly outside the sample with no trace in `registry.EXCLUDED`, or coded GAP where NOT\_OPEN is right, or coded T3 inside a rule in which T3 never excludes | BJ-01 (**the two Beijing trams, the most important of these**), SH-01 (the Shanghai Maglev, the one T3 code, see step 3 of section 2 and 7.5 below), CC-2, CHA-2, CHA-3, CD-5, CQ-2, WUH-01, XUZ-01, XIA-01, Y-01, BJ-04, BJ-05, NB-2 | **Action.** These are disclosure defects, not inclusion defects. BJ-01 matters most because memo 16's CPTOND reconciliation relies on the trace, and because the paper will claim the rule was applied |
| **(f) Exclusion register contradicts the sample** | A line listed as excluded while sitting in the same city's table as included | FS-01 (both Foshan additions still listed as GAP), NB-1 (Ningbo 7号线), SH-02 (Shanghai Airport Link), registry#F4 (five stale entries) | **Action, and urgent.** These are the findings a reviewer meets first, because one city section contradicts itself on the same page. Move them into an "Added in v2" block written in the past tense |
| **(g) T3 and scope coherence** | Tier B labels resting on a stale or wrong basis string | TAOYUAN-01 (**the one genuine open scope question**, see below), BJ-03, CD-1, CD-3, CHA-5, TZ-01, QD-01 and QD-03 | **Action, plus one decision for Hanyu.** QD-01 is the material one: Qingdao route 7 is not 3号线, it is 8号线南段, a designated 市域快轨 segment currently carried as an urban 地铁 line, so its reclassification moves it into Tier B and changes the Tier A Qingdao file |
| **(h) Link-level data defects** | Phantom chords, wrong run times, headway defaults | SH-03 (Shanghai Line 2, five phantom skip-stop chords, 40.6 km of inflation and four spurious degree-4 nodes, which corrupts exactly the topology indicators), SZ-1 (Shenzhen 晨曦特快 overlay), WUHU-01, XMN-02, HK-2, XIA-02, ZZ-2, SJZ-1, DAEGU-1, DAEGU-4 | **Action.** None changes a verdict. SH-03 and SJZ-1 change the topology indicators and therefore section 4.1 |
| **(i) Document number patches** | Stale counts in memos and the package | 07-02, 07-03, 07-04, 07-07, 07-08, 09-01, 09-03, 09-04, 09-05, 09-06, 06-02, 06-05, 06-06, DD-01, DD-02, F1, F2, F3 | **Mostly closed by this memo**, which states the numbers of record in 7.3. The three that still need file edits are `supplementary_network_sources.csv` (regenerate from the v2 annotated trees, currently 417 routes and 7,456 stations beside a 420-row inclusion table in the same package), `DATA_PACKAGE_README.md` lines 13 and 28, and `DATA_DICTIONARY_v2.md`, whose T1 gloss says the test "fails only for street running" in a file documenting a street-tram row that passes, whose `T3_scope` entry lists two values where the file carries three, and which with `09_VALIDATION_AND_TRANSPARENCY.md` line 12 still calls the inclusion table 28 columns where it carries 30 |
| **(j) Tier-semantics rewrites** | Whole passages built on the technology-tier scheme | 02-01 to 02-10, SYN-01 to SYN-07, RP-01 to RP-10, RM-04 | **Closed by supersession** (7.2) plus the replacement text in section 9. Do not rewrite the superseded files in place, banner them, because their reasoning is a record of how the decision was reached |
| **(k) Manuscript** | main.tex 3.4, the limitations paragraph, the title and keywords, the data-availability statement | TEX-01, TEX-02, TEX-03, tex-vs-rule F1 to F9 | **Replacement text in section 9.** F4 (the unsourced denominator 68) and F6 (the deposit promises 62 networks at a link containing 61) are the two that a reader can falsify in one click |
| **(l) Evidence and sourcing** | Quotations and figures with no primary on disk | C1-b (the UITP breakdown does not sum), C1-d (the fare flag misattributes UITP), C3-a (the MLIT quotation), C4-b (the Korean 40 km and 50 km/h test), D10 | **Action, listed as open questions.** Do not paste any of these into the tex until the download is on disk. Section 10 marks each source as safe or pending |

**The one genuine open scope question, TAOYUAN-01.** Taoyuan Airport MRT is labelled Tier B while its recorded proxy is 34.1 km/h, below the 60 km/h boundary, its `speed_proxy_reliable` is True, and its legal class is not 市域 or regional. The basis string rested on a claim about express patterns that the all-stop proxy contradicts, and it also quoted a 40 km/h proxy that appears nowhere in the file. Two coherent outcomes, and Hanyu must pick one. Either drop the scope override, in which case Taoyuan becomes urban, Tier B falls from 31 records to 30 and the sensitivity sample rises from 58 cities to 59. Or keep Tier B and rest the basis on the 51 km cross-municipality corridor rather than on a speed the file does not show. **Interim, 2 September:** the second reading is in the files, so that the row no longer contradicts itself on the page. The basis now names the corridor, quotes the recorded 34.1 km/h and marks the row as open for decision. The decision itself is still Hanyu's and the record count has not moved.

**The one misused code, SH-01.** `registry.EXCLUDED["Shanghai"]` holds the Shanghai Maglev 磁浮示范运营线 under the code T3, inside a rule in which T3 records scope and never removes anything, and `registry.py`'s own legend defines T3 as "metropolitan rather than urban scope (would be Tier B if present)". The line is absent from the 2025 file, so the code of record is GAP and the entry will be recoded. The alternative disposition, which the audit sets out, is to admit the line as a two-station Tier B row carrying the premium-fare flag. Either way no line that is in the data is kept out on scope grounds, which is what the rule promises. Note that Chengdu route 17 (57.2 km/h) and Guangzhou route 19 (51.4 km/h) look similar on the number but are covered by the stated "proxy unusable, assigned by designation" category, so Taoyuan is the only row where the label rests on nothing the file supports.

### 7.6 A structural warning about the evidence base

Two things the next writer needs before touching the tex.

`metro_definition_synthesis.md` states at its line 5 that "Every statutory or institutional claim below is sourced to a URL in the bibliography". The file has no bibliography and contains no URLs. It is nevertheless the only on-disk home of four load-bearing quotations, the MLIT sentence, the Korean 40 km and 50 km/h 광역철도 test, the Roth et al. sentence and the Derrible and Kennedy sentence. **Treat it as a draft, not as evidence.**

The CAMET annual report, the strongest Chinese primary after the GB standard, is on disk under the filename `china_metro/data calibration/metro_definition.pdf`, which hides it. Rename it before someone concludes we do not hold it.

---

## 8. The residue to state in the paper

A rule earns its authority by naming what it costs. Six items, all to appear in section 3.4 or the limitations paragraph.

**1. The Yamanote concession.** One sentence, and it must be there. The line passes every functional criterion and is excluded by T2 alone, on the same ground on which UITP excludes the RER and the S-Bahn.

**2. Lines the rule admits and the data lacks.** Recorded per city in `registry.EXCLUDED`, mostly under the code GAP: the **Rinkai Line** (8 stations) and the **Tama Toshi Monorail** in Tokyo, the **Minatomirai Line** (6 stations) and the **Kanazawa Seaside Line** (14 stations) in Yokohama, the **Port Liner and Rokko Liner** (12 and 6 stations) in Kobe, Shenzhen's **坪山云巴1号线**, Hangzhou's **杭海城际**, and a second Beijing 市域快轨 line and a second Shanghai 市域快轨 line that CAMET counts and we could not identify. Two of those carry a caveat. 杭海城际 is coded **SEP and not GAP**, because Amap rescoped the intercity line to Haining into the Hangzhou payload, so it is another city's line rather than a missing Hangzhou one. And the 坪山云巴1号线 entry is coded GAP while its reason string reads "opened after the reference date", which is a NOT\_OPEN reason and is wrong on the facts, since CPTOND-2025 has the line in service at the reference date. **Audit SZ-2 corrects the reason string, and the GAP disposition itself stands.** Say plainly that these lines are admitted by the rule and absent from the collection, and distinguish them in wording from services genuinely unavailable.

**3. Systems the rule predicts and the sample lacks, with the honest reason per city.** The current sentence at main.tex line 281 gives one reason, absence of data, for six cities, and it is false for five of them. Counted this session from the KTDB feed on disk: 대전1호선 has 22 stops, 광주1호선 has 20 stops and 김포도시철도 has 10 stops, all in the same file that produced Seoul, Busan, Daegu and Incheon, along with 의정부경전철 and 용인경전철. Only Pyongyang is genuinely absent. Osaka and Nagoya are recorded in `registry.MISSING_CITIES` and in `inclusion_table_v2.md` lines 81 to 82 as not collected, with the source named in each case, so they have no availability defence either. Daejeon, Gwangju, Gimpo, Osaka and Nagoya must all be described as a coverage limitation of this study rather than as a constraint of data availability.

**4. The Japan and Korea asymmetry.** In Japan and Korea the sample is the urban-transit layer only, while Chinese operators run essentially the whole rapid-transit layer of their cities. Accessibility in the Japanese and Korean cities is therefore understated relative to the Chinese ones, and the reported figures are a lower bound for cities with a large complementary suburban network. This is the single most important honest limitation in the paper and it belongs in the limitations paragraph, not buried in a footnote.

**5. Cross-city overlaps.** Guangzhou and Foshan share 21 stations through the 广佛线, Seoul and Incheon share 11, Hangzhou and Shaoxing share 1. The 62 networks are not independent observations, and any statistical statement across cities should say so.

**6. Frequency provenance.** Headways are line-specific in most cities and network-wide in a small number. After the band conversion and the Taiwan rebuild the state is one placeholder file (Ürümqi) and four single-value files (Dongguan, Kaohsiung, Taichung, Taizhou), and for Kaohsiung and Taichung the single value is an observed TDX figure. The supplementary table marks the basis per route, and no frequency-based claim should be made for the files still on a constant.

---

## 9. Paste-ready text

**Do not paste until the section 7.5 (b) route-identity repairs have been applied and the counts re-read.** The paragraphs below carry no route counts for exactly that reason, except where a count is unavoidable, and those are marked.

### 9.1 Section 3.4, the definition paragraphs, replacing main.tex lines 277 to 281 and the unsourced parenthesis at line 284

> **[Paragraph 1, the tests, replacing L277 and L278.]**
> The line is the unit of inclusion. A line is admitted if it meets the criteria of the International Association of Public Transport, that is a guided, electrically powered urban passenger service running on an exclusive right of way, with trains of at least two cars and a total capacity of at least 100 passengers \citep{UITP2025}. That definition is technology-neutral by its own wording, since it states that systems based on light rail vehicles, monorail or magnetic levitation are included where the other criteria hold, so straddle monorail, medium-low-speed maglev, automated guideway transit and fully segregated light rail are all admitted. The test is on the right of way and not on the vehicle class, so street running and shared lanes are excluded, and one line locally classed as a tram, Foshan Nanhai Tram Line 1, is admitted by a recorded exception because its right of way is exclusive and predominantly grade separated. A line is admitted only if it also belongs to the designated urban rail transit system of its city, as that system is defined by the jurisdiction itself, namely 城市轨道交通 under GB/T 44413-2024 in mainland China, 도시철도 under the Urban Railroad Act in Korea, 大眾捷運系統 under the Mass Rapid Transit Act in Taiwan, 都市高速鉄道 under the City Planning Act in Japan, the franchise under the Mass Transit Railway Ordinance in Hong Kong, and the 輕軌交通系統 of Law 18/2019 in Macau. National, regional and suburban railways are excluded as systems rather than line by line, following the exclusion of the Paris RER and the Berlin S-Bahn by \citet{UITP2025} and of the RER and NetworkRail by \citet{Roth2012}, so the JR Yamanote Line is outside the sample although it satisfies every functional criterion. Through-running services are truncated at the boundary of the designated system.

> **[Paragraph 2, scope and the fare flag, new.]**
> Service scope is recorded rather than used to filter. A line is urban where its commercial speed, computed as route length over summed in-vehicle time, is at or below 60 km/h, the boundary that GB/T 44413-2024 draws between urban and metropolitan rail transit, and metropolitan where the speed is higher or where the line is itself designated as a metropolitan or regional express service. Metropolitan lines are retained in the main sample and the results are reported again in a sensitivity sample from which they are removed. Where a route is too short for the speed to be meaningful, which is the case for two- and three-station branches, the scope is settled by the line's designation and the reason is recorded. A small number of lines charge a premium fare that is not integrated with the rest of the network. These are retained and flagged, so that a reader who prefers to remove them can identify them. Supplementary Table S1 gives, for every line, its technology, the instrument under which it is designated, its stations, its length, its headway and the source of that headway, its commercial speed, the outcome of each test and the resulting verdict.

> **[Paragraph 3, urban hierarchy, replacing L279.]**
> Because a designated urban rail transit system requires demand densities and fiscal capacity that only major metropolitan cores can sustain, the sample is drawn in effect from the upper tier of the regional urban hierarchy \citep{ChangPhang2017,YuCui2023}. The included systems serve the population-dense corridors of the Yangtze River Delta, the Pearl River Delta, Greater Tokyo, Keihanshin, the Seoul Capital Area and the Taiwanese west coast.

> **[Paragraph 4, the residue, replacing L281 and the "out of 68" clause at L284.]**
> Some systems that the rule admits are not in the sample. No accessible service data could be obtained for Pyongyang. Osaka and Nagoya publish open data through the Open Data Platform and the city catalogue respectively, and Daejeon Line 1, Gwangju Line 1 and the Gimpo Goldline are present in the national Korean feed used for the other Korean networks. These five absences are a coverage limitation of this study rather than a constraint of data availability. A small number of lines in sampled cities are likewise admitted by the rule and absent from the collection, principally the Rinkai and Minatomirai lines and the Kobe and Yokohama people movers, and these are listed with their reason in the supplementary material.

### 9.2 The limitations paragraph, replacing main.tex lines 712 to 713

> The analysis excludes national, regional and suburban railways as systems, which is the boundary that also excludes the Paris RER and the Berlin S-Bahn, and not because of any technical test applied to individual lines. Corridors such as the JR lines in Tokyo and the Korail lines in the Seoul Capital Area are therefore outside the sample although they complement the metro closely and would satisfy every functional criterion. Because Japanese and Korean operators run only the urban layer of their cities' rapid transit while Chinese operators run essentially all of it, the accessibility levels reported here are a lower bound for the Japanese and Korean cities in particular, and cross-country comparisons should be read with that asymmetry in mind.

### 9.3 Title, keywords and abstract sweep

Replace the title with "Accessibility comparison of **metro** networks of East Asia and beyond using access graphs". In the keyword list replace "Subway/metro" with "Metro". In the abstract replace "62 East Asian metro (subway) networks" with "62 East Asian metro networks". Retain "subway" only inside proper names such as Beijing Subway and Toei Subway. The reason is stated in section 1: 地下鉄 and 지하철 carry an underground connotation that the sample violates constantly, since much of the Chinese and all of the Chongqing and Wuhu network is elevated.

### 9.4 Response to R2-1, replacing the technology-tier draft

> We agree that the manuscript did not state its inclusion criterion, and we have replaced the definition passage entirely.
>
> The sample is now defined by a line-level rule with two tests and one recorded attribute. The first test is the criterion of the International Association of Public Transport, in UITP's terms: a high capacity urban guided transport system, mostly on rails, powered with electricity and running on an exclusive right of way, with trains of a minimum of two cars and a total capacity of at least 100 passengers per train. This test is technology-neutral, and deliberately so, because UITP states in the same paragraph that systems based on light rail vehicles, monorail or magnetic levitation are included where the other criteria hold, and because it counts monorails, people movers, light rails and maglev systems alongside metros and refers to all of them as metros. The test is applied to the right of way and not to the vehicle, so it excludes street running and shared lanes, and it admits one line that is locally classified as a tram, the Foshan Nanhai line, whose right of way is exclusive and predominantly grade separated. That exception is recorded in the supplementary table with its evidence rather than left implicit.
>
> The second test is membership of the city's designated urban rail transit system, as each jurisdiction defines that system for itself. We chose this because there is no shared legal category of "metro" across the six jurisdictions in the sample and no way to construct one. Mainland China defines 地铁 narrowly by technology, Korea's 도시철도 umbrella is broader and admits trams, Taiwan's 大眾捷運系統 is functional and omits technology, Hong Kong's boundary is a franchise, Macau's system is legally a light rail and technically a people mover, and Japan defines no category of subway at all, its transport ministry classifying undertakings and system types rather than defining the service. What all six do possess is a category meaning "the urban rail transit system of this city", and that is the category the rule uses. National, regional and suburban railways are excluded as systems and not line by line, which is the same basis on which UITP excludes the Paris RER and the Berlin S-Bahn and on which Roth et al. exclude the RER and NetworkRail. We state explicitly in the revised text that the JR Yamanote Line is excluded on this basis although it satisfies every functional criterion.
>
> A third attribute records service scope without filtering. A line is urban where its commercial speed is at or below 60 km/h, the boundary GB/T 44413-2024 draws between urban and metropolitan rail transit, and metropolitan otherwise or where it is itself designated as a regional express. Metropolitan lines are retained in the main sample and the results are reported again in a sensitivity sample from which they are removed. We publish the per-line assignment for the full dataset as Supplementary Table S1, with each line's technology, designating instrument, stations, length, headway and its source, commercial speed, the outcome of each test and the verdict, so that a reader who disagrees with any single call can identify it and recompute without it.

### 9.5 Response to R2-2, replacing the technology-tier draft

> The reviewer is right that the submitted sample mixed automated guideway systems, monorails and airport lines with conventional subways without saying so. We have not resolved this by narrowing the sample, because no published definition supports a narrow one, and we say so directly in the revised text: UITP's definition is technology-neutral in its own wording, Derrible and Kennedy define metros by exclusive right of way with no technology test, Taiwan's Mass Rapid Transit Act is functional and omits technology deliberately, and Japan has no statutory definition of a subway. Only the Chinese standard gives its metro term a narrow technical meaning, and the Chinese operators and the national statistics nevertheless report the Chongqing monorails inside the Chongqing network on a single fare.
>
> We have resolved it instead by stating the rule, applying it consistently and publishing the outcome line by line. The rule is technology-neutral on inclusion and bounded on service scope, which we regard as the correct division because the quantity this paper measures, generalised travel time, is composed of in-vehicle time, waiting time and transfer penalties. Every one of those is a property of the service and none is a property of the guideway. A passenger on Chongqing Line 2 experiences a frequent segregated line that interchanges with Line 1 on one fare, and their generalised travel time is unaffected by the fact that the vehicle straddles a beam.
>
> Concretely, the six categories the reviewer may have in mind are treated as follows. National, regional and suburban railways are excluded as systems, which is what the second test does. Straddle monorails, automated guideway transit and medium-low-speed maglev pass both tests and are in the main sample, so the Nippori-Toneri Liner and the Yurikamome, which the reviewer named, are included, and the supplementary table records their technology and the instrument that designates them. Fully segregated light rail is admitted, as UITP's own wording admits it, while street running and shared lanes are excluded, which is why the Hong Kong Light Rail and the two Beijing street trams are outside the sample. Chinese metropolitan and regional express lines that pass both tests are retained and recorded as metropolitan in scope, and the sensitivity sample removes them. Dedicated airport services that pass both tests are retained and flagged where their fare is premium and not integrated, four lines in all, and the flag and the scope label are independent attributes that only one line carries together.
>
> Two further points of transparency. Removing every metropolitan-scope line from the sample removes four networks, all of which consist only of such lines, and 4.7 percent of the stations, so the definitional question turns out to be a small and measurable robustness question rather than a decisive one. And the previous sentence excluding commuter rail where it was not "tightly coordinated" with the metro has been removed, since it stated an unmeasurable test that formed no part of our actual procedure.

---

## 10. Sources

Marked **on disk** where a primary is held in this repository and can be quoted today, and **pending** where a download is required before the claim may enter the tex.

| # | Source | Status | Path or note | Used for |
|---|---|---|---|---|
| 1 | UITP (2025). *Global Metro Figures 2024*, Statistics Brief. Union Internationale des Transports Publics, Brussels | **on disk** | `LR/01_regional_global_overviews/20250822_Global-Metro-Figures_Statistics-Brief_WEB.pdf` | T1 verbatim, the technology-neutrality clause, the RER, S-Bahn and KLIA exclusions, the suspended-systems exclusion, Japan 973 km and Korea 926 km on p. 4. **Do not restate the 237 breakdown as a sum** |
| 2 | GB/T 44413-2024, 城市轨道交通分类 (Classification of urban rail transit). 国家市场监督管理总局, issued 2024-08-23, in force 2024-12-01 | **on disk** | `August - revision/How each country defines the metro/China/GBT+44413-2024.pdf` | clause 5.1 the ten system types, clause 5.2.1 Table 1 the 60 km/h scope boundary, Table 4 the per-mode attributes |
| 3 | CAMET, 城市轨道交通2025年度统计和分析报告 | **on disk** | `china_metro/data calibration/metro_definition.pdf` (**rename this file**), parsed tables in the same folder | the separation of 市域快轨 from 地铁, 10,004.89 km against 1,706.00 km over 58 cities, per-city mode kilometres, commercial-speed validation |
| 4 | 日本地下鉄協会 (JAMETRO) operator roster | **on disk** | `August - revision/How each country defines the metro/JP/JP.txt` | the 851.5 km headline, the 765.9 km ten-operator subset and the 909.8 km printed roster, the Astram and Tsukuba Express inconsistencies |
| 5 | Roth, C., Kang, S. M., Batty, M. and Barthelemy, M. (2012). A long-time limit for world subway networks. *J. R. Soc. Interface* 9(75), 2540-2550 | **pending the quotation** | in `LR/04_network_science/`, but the exclusion sentence is quoted only from our own synthesis file | the exclusion of the RER and NetworkRail as systems, and the Tokyo N = 217 corroboration. Verify both against the paper before quoting |
| 6 | Derrible, S. and Kennedy, C. (2010). Characterizing metro networks: state, form, and structure. *Transportation* 37(2), 275-297 | **pending the quotation** | our files attribute the "underground, at grade or elevated" sentence to two different 2010 papers | the academic precedent for a technology-free definition. Settle which paper before citing |
| 7 | 도시철도법 제2조제2호 | **pending** | `SK/SK Law.txt` on disk is the construction standard, not the definition | the Korean designated category. Download from law.go.kr and save |
| 8 | 대도시권 광역교통 관리에 관한 특별법 시행령 제4조 (광역철도의 지정기준) | **pending** | not on disk | the 40 km radius and 50 km/h cross-check on the T3 boundary. **Do not paste the two numbers into the tex until this is downloaded.** T3 can rest on GB/T Table 1 plus the CAMET speed validation alone if it is not |
| 9 | 大眾捷運法 第3條 | **pending** | not on disk | the Taiwanese functional definition and the completely-independent right-of-way split |
| 10 | 都市計画法 第11条, and the absence of any statutory definition of 地下鉄 | **pending** | neither 都市計画法 nor 鉄道事業法 is on disk, so the flat negative about the two statutes is not yet supportable from anything held here. The MLIT sentence 「地下鉄についての明確な定義はない」 has **no URL and no access date** and is currently in 14 shipped JSON files | **Do not paste the negative about the two statutes into the tex until one of them is downloaded, the same marker as source 8.** Until then write the Japan finding on source 17, which is on disk |
| 17 | MLIT 鉄道統計年報, operator classification | **on disk** | the JR, 民鉄, 公営 and 第三セクター classes and the separate モノレール and 新交通システム system categories, cited at line 49 | the supportable form of the Japan finding, that the ministry counts by undertaking and by system type and never by a defined category called subway |
| 18 | Tokyo Monorail, route length and shareholding | **pending** | 17.8 km and the 79 percent JR East holding are hand-coded in `registry.py` and repeated from 06 and 07, with no primary on disk | the 4.1 worked case only. **Not for section 9 until a primary is held** |
| 11 | Mass Transit Railway Ordinance Cap. 556, Rail Merger Ordinance 2007 | **pending** | not on disk | the Hong Kong franchise boundary |
| 12 | Macau Law 18/2019, 輕軌交通系統 | **pending** | not on disk | the Macau designated system |
| 13 | Vijlbrief, T. et al. (2022), the European and North American comparison dataset | **on disk** | `L2/README.txt`, `L2/metadata.xlsx`, TU Delft repository record | the Kobe network, the comparison set, and the precedent for a reproducible data-driven inclusion rule. Note it publishes no inclusion criteria of its own, which is worth stating |
| 14 | Vuchic, V. R. (2007). *Urban Transit Systems and Technology*. Wiley | not held | | the right-of-way category backbone, ROW category A rapid transit against category B light rail, and the observation that "metro" is the international term for rail rapid transit |
| 15 | Wang et al. (2026), CPTOND-2025, *Scientific Data* | **on disk** | `dataset_v2/build/cptond_*.csv`, memo 16 | operators, along-route segment lengths, and the independent station cross-check |
| 16 | Our own inclusion table | **on disk** | `inclusion_table_v2.csv`, sha256 `235d2094…` | every count in this memo |

---

## Files

| File | What it is |
|---|---|
| `August - revision/analysis/20_LINE_LEVEL_INCLUSION_RULE.md` | **this memo, the document of record** |
| `August - revision/analysis/07_INCLUSION_RULE.md` | the 22 August rule statement. Superseded on its numbers, current on its rule |
| `August - revision/analysis/audit/INCLUSION_AUDIT_FINDINGS_2026-09-02.md` | the full audit register, 506 raw findings, 391 confirmed, 115 refuted. **Cite this for any individual finding** |
| `August - revision/analysis/inclusion_table_v2.csv` | 420 rows, 30 columns, sha256 `235d2094bcdd334926ed16d3a89f2ad3afc0a294b575aabcc301a869c9e7699f`. The numbers of record |
| `August - revision/analysis/inclusion_table_v2.md` | the same, one section per city, with excluded services and known defects |
| `August - revision/analysis/inclusion_summary_v2.csv` | one row per city, 62 rows |
| `August - revision/analysis/supplementary_line_inventory_v2.csv` | byte-identical to the inclusion table. Supplementary Table S1 |
| `August - revision/analysis/supplementary_network_sources.csv` | Supplementary Table S2. **Stale, still v1 at 417 routes and 7,456 stations** |
| `August - revision/analysis/09_VALIDATION_AND_TRANSPARENCY.md` | validation and transparency. Correct on the rule, stale on counts |
| `August - revision/analysis/06_SCOPE_DECISION.md` | the costed scope decision. Superseded in full, section 1 still worth reading |
| `August - revision/analysis/02_RESPONSE_DRAFTS.md` | superseded on scope, tiers, trams, airport expresses and Kobe |
| `August - revision/analysis/metro_definition_synthesis.md` | the jurisdiction synthesis. Sections 11 to 13 superseded. **No URLs despite its own claim** |
| `August - revision/How each country defines the metro/metro_terminology_decision.md` | sections 2 to 4 superseded, section 1 and section 5 current |
| `August - revision/analysis/revision_plan_definition_and_dataset.md` | D2 to D5 and sections 4 and 5 superseded |
| `August - revision/analysis/08_CAMET_CALIBRATION.md`, `16_CPTOND_CROSSCHECK.md` | the external calibrations behind T3 and the station cross-check |
| `dataset_v2/registry.py` | every hand-coded fact: jurisdictions, technology and legal-class constants, `EXCLUDED` (85 entries, 41 cities), `MISSING_CITIES` (5, Pyongyang added 2 September), `SCOPE_OVERRIDE`, `T1_OVERRIDE`, `TECH_OVERRIDE`, `PREMIUM_FARE`, `AMAP_OVERRIDES` |
| `dataset_v2/annotate.py` | the generator that writes the table and the annotated files. Holds the metric defect of 7.5 (a) |
| `dataset_v2/repair.py` | the repair pipeline, including the split and retime operations the route-identity fixes need |
| `asia/L2_v2`, `asia/P2_v2` | the main sample, 62 networks, 7,480 stations |
| `asia/L2_v2_tierA`, `asia/P2_v2_tierA` | the sensitivity sample, 58 networks, 7,126 stations |
| `asia/L2_v2_annotated`, `asia/P2_v2_annotated` | the deposit shape, carrying the same verdicts inside `graph.routes` |
| `August - revision/data_package_2026-09-01/` | the 1 September package. README lines 13 and 28 stale, dictionary glosses stale |
| `August - revision/submitted_version/main.tex` | the submitted manuscript. Lines 277 to 284, 712 to 713, 30, 63 and 86 to be replaced from section 9 |
| `LR/01_regional_global_overviews/20250822_Global-Metro-Figures_Statistics-Brief_WEB.pdf` | UITP, the primary behind T1 |
| `August - revision/How each country defines the metro/China/GBT+44413-2024.pdf` | GB/T 44413-2024, the primary behind T3 |
| `August - revision/How each country defines the metro/JP/JP.txt` | the JAMETRO roster |
| `August - revision/analysis/ktdb_subway_lines.json` | the Korean feed, holding Daejeon, Gwangju, Gimpo, Uijeongbu and Yongin |
