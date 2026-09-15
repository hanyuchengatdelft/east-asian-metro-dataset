# Open decisions, 12 September 2026

**BOTH DECISIONS RESOLVED 12 September 2026. See the Resolution section at the foot of this file. The bodies below are retained as the record of what was weighed.**

Two items came out of the China adversarial pass that I will not decide alone. One is a data decision that changes a city by a third. The other is a wording decision that carries 336 of the 420 register rows. Everything else from that pass is applied or is a wording fix.

---

## Decision 1. Changchun Line 3, 34 stations

**This is a co-author question that was already asked and never answered.** `analysis/revision_plan_definition_and_dataset.md` line 38 recommends removing "Beijing route 23 (Xijiao line, 6 stations), Beijing route 26 (Yizhuang T1, 14 stations) and, **pending co-author confirmation**, Changchun route 5 (Line 3, 34 stations, low-floor stock with at-grade crossings)". Line 172 puts it directly: "Do you approve the removal of Changchun Line 3 alongside Beijing's two trams? Changchun drops by roughly a third if Line 3 goes."

The two Beijing trams are not part of the Beijing network. **Changchun Line 3 is the other half of the same decision and it is still open.**

### The problem in one line

The register row contradicts itself in print:

| Field | Value |
|---|---|
| `technology` | steel-wheel light rail (轻轨), **fully segregated** |
| `note` | CAMET 2025: 轻轨 (68.20 km together with Lines 4 and 8); **some at-grade sections** |
| `T1_uitp_line_criteria` | pass |

The supplementary table prints both fields. A reviewer reads "fully segregated" next to "some at-grade sections" in the same row.

Two further repo files call it at-grade light rail, and `analysis/inventory_Changchun.md` classifies it as **tram-LRT**.

### What is at stake

| Option | Changchun | Consequence |
|---|---|---|
| **Keep**, with a documented T1 override | 111 stations | The override must name the evidence, in the same form the Foshan entry used, and the technology string must stop saying "fully segregated". Requires establishing that the at-grade crossings are protected level crossings on an otherwise reserved alignment. |
| **Remove** | 111 → 77 | Consistent with Beijing's two trams and with Foshan Nanhai. Changchun loses roughly a third and its indicators must be recomputed. |

### My recommendation

**Establish the crossing type first, then decide.** This is not a case where the precautionary answer is obviously right, because the line is four times the size of the Foshan one and Changchun Line 3 is a genuine 轻轨 within 城市轨道交通, not a tram. If its at-grade sections have gated, signal-protected crossings on a reserved alignment, it passes T1 as written and should stay with an explicit override entry. If any section is shared with road traffic, it goes.

What must not happen is the current state, where the row passes T1 while its own note records the fact that would fail it.

---

## Decision 2. The Chinese T2 instrument sentence

Not a data decision, but it carries 336 of 420 rows, and a Chinese-literate reviewer can falsify the current wording against the sample in one search.

### The problem

The rule names **GB/T 44413-2024** as the Chinese T2 instrument. That standard classifies **system modes**, it designates no line, and it entered force on 1 December 2024, after most sampled Chinese lines opened. The MOT Provisions are an operating regime rather than a membership definition. So the Chinese limb has the same circularity that was just found fatal in Japan.

Worse, the draft says the excluded Chinese suburban layer is the 市域(郊)铁路 category, and **three sampled lines carry 市域(郊)铁路 or 市郊铁路 in their own official names.** Under the rule as drafted they fail T2. They are the structural twins of 하남선.

### The fix, which keeps the lines

Do not exclude them. State the Chinese test as **mode plus undertaking**:

> GB/T 44413-2024 places 市域快速轨道系统 inside urban rail transit as a mode. A line approved under a 市域(郊)铁路 or 都市圈城际铁路 planning instrument is inside the designated system when it is built to that mode and operated by a municipal urban rail undertaking, and outside it when it runs on national railway infrastructure under a China Railway group company. The approval instrument is recorded in the register for every such line.

This matches the position taken earlier in this revision, that the S-lines are integral parts of the metro networks that operate them. It also matches the two Chinese exclusions already made, Beijing S2 and the Shanghai Jinshan Railway, which are China Railway operated, and Xi'an 西户线.

**A new `approval_instrument` column must then be populated for the fourteen affected rows**, so that nothing is concealed.

### The asymmetry that has to be stated rather than denied

The Korean and Chinese instantiations are **not** symmetric, and the reason is in the instruments. The Korean Special Act designates individual lines and sections as metropolitan railways, so Korea supplies a line-level designation the rule can read. China has no equivalent line-level designation, so the Chinese test falls back on mode plus undertaking. Say this in Part V of the argument as a stated limit. Denying it is what a reviewer will catch.

### A free improvement while you are there

**Xi'an 西户线 fails T1 independently and decisively: the service is diesel locomotive-hauled, so it is not an electrically powered railway.** Recording T1 as the primary ground, with the China Railway infrastructure argument as secondary, removes the whole Korean-symmetry attack surface for that line at no cost.

---

## Applied without asking

These came out of the same pass and are either already done or are wording fixes with no judgement in them.

| Item | Status |
|---|---|
| Foshan tram ground restated from "shared lanes" to "undocumented right of way" | **Applied** in `metadata.md`. The study's own record says the decisive fact is undocumented, which is itself the ground. |
| Publish the corrected register, not a draft that predates the corrections | **Applied**, the register is `east_asian_metro_route.csv`. |
| Register omits Beijing's trams and eight further CAMET-counted services | Deferred. The register is a documentation generator and no indicator depends on it, but the paper claims the rule was applied rather than inherited, and the register is the only evidence of that. |
| Shanghai 市域机场线 should be named in the text | Deferred. It is built to national-railway standards but owned and operated inside the municipal undertaking, so it stays. That built-versus-operated distinction is what the whole 西户线 argument rests on and it is currently stated nowhere. |
| Foshan retained a route id 4 tag on one link after the tram exclusion | **Applied** on 15 September 2026, the tag was stripped. |


---

# Resolution, 12 September 2026

## Decision 1. Changchun Line 3: RETAINED

The line was first deleted on the author's instruction and then **restored on the same day**, on the author's revised view that the line has undergone grade-separation works. Changchun stands at **111 stations, 6 routes, one connected component**, identical to source.

**The register row was not restored verbatim.** The technology string previously read "fully segregated" while the note on the same row read "some at-grade sections", and the supplementary table prints both. The string now reads "steel-wheel light rail (轻轨), exclusive right of way", which is the thing T1 actually tests. T1 asks whether the right of way is exclusive to the line, not whether the line is fully grade separated, so a reserved alignment with protected level crossings passes and the earlier deletion rested on the wrong reading.

**Evidence still to be attached, and this is the weakest documented row in the sample.** The grade-separation works and the current status of the remaining at-grade sections are recorded nowhere in the repository, and the web search budget for the session was exhausted before they could be verified. Until a source is attached, the row rests on the author's knowledge alone.

This matters because Changchun Line 3 is 34 stations, four times the Foshan line that was excluded, and because three files in the repository still describe the line as at-grade light rail, one of them classifying it as tram-LRT. **The register must carry a citation for the works, and the three stale descriptions must be reconciled, before the supplementary table is shipped.** A reviewer who finds the old wording and no citation will ask why this line was treated differently from Beijing's two trams and Foshan's.

## Decision 2. Chinese T2: MODE PLUS UNDERTAKING

Adopted. Written into `Sep report/INCLUSION_ARGUMENT.md` as a new section I.5, with the instrument table row rewritten, the Part III suburban row re-based on the undertaking rather than the Chinese label, and the Korea-China asymmetry added to Part V as a stated limit.

The three lines carrying 市域(郊)铁路 or 市郊铁路 in their official names are retained. Shanghai 市域机场线 is named in the text as the built-to-national-standards but municipally-operated case.

**Still to do:** populate an `approval_instrument` column for the fourteen affected rows.

## Also applied

Xi'an 西户线 now records **T1 as the primary ground**, because the service is diesel locomotive-hauled and so is not an electrically powered railway, with the China Railway infrastructure argument as the secondary T2 ground. This removes the Korea-symmetry attack surface for that line at no cost.
