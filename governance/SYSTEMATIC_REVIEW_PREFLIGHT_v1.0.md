# Systematic Review Pre-Flight Protocol — v1.0

**Issued:** 18 March 2026
**Authority:** Julian Borges, MD — Lab Director
**Status:** ACTIVE
**Type:** Mandatory pre-execution governance standard
**Scope:** All systematic review and meta-analysis projects
**Derived from:** Pool 7 IronFF PROSPERO registration, Planning Protocol Standard v1.0, PROSPERO Registration Rubric v1.0
**Assigned executor:** Phase 2 Planning Agent (T3)

---

## Governance Rule

No database search may be executed until all 12 sections of this pre-flight are documented in a planning protocol file. PROSPERO/OSF registration is recommended but not mandatory; the planning document is the hard constraint.

## Pipeline Integration

| Phase | Gate | Pre-Flight Role |
|---|---|---|
| Phase 2 (Question Formulation) | G1 | Sections 1-3 completed |
| Phase 3 (Protocol Design) | G2 | Sections 4-12 completed |
| Phase 4 (Search Execution) | BLOCKED | Cannot begin without complete pre-flight |

## Agent Assignment

| Task | Agent | Tier |
|---|---|---|
| Draft planning protocol (Sections 1-12) | Phase 2 Planning Agent | T3 |
| Review and approve protocol | Master Orchestrator | T1 |
| Execute PROSPERO/OSF registration | Phase 2 Planning Agent | T3 |
| Confirm CRD/DOI received | Master Orchestrator | T1 |
| Insert CRD/DOI into manuscript | Phase 7 Manuscript Agent | T4 |

## G2 Gate Check (Orchestrator Directive)

Before authorizing Phase 4 search execution, the Master Orchestrator must verify:
1. File exists: `[PROJECT]-P[N]-PLANNING-PROTOCOL-v1.0-[YYYYMMDD].md` in project protocols directory
2. All 12 sections are populated (no empty sections)
3. PICO components are explicit and unambiguous
4. Primary outcome is singular
5. Synthesis method is pre-specified
6. RoB tool and GRADE criteria are named

If any condition fails, return to Phase 2 Planning Agent for completion. Do not proceed.

---

## 12-Section Checklist

### Section 1 — REVIEW TITLE AND BASIC DETAILS

| Field | Constraint | Guidance |
|---|---|---|
| Review title | ≤85 chars recommended | Include P, E, O, study design |
| Condition/domain | Free text | Map from PICO P + E |
| Rationale | Free text | State evidence gap; cite prior reviews |
| Objectives | Free text | Primary quantitative objective first |
| Keywords | Min 4; recommend 10-14 | MeSH + free text synonyms |
| Country | Free text | Country of corresponding author |

### Section 2 — ELIGIBILITY CRITERIA

| Field | Limit | Source |
|---|---|---|
| Population inclusion | Max 200 words | PICO P |
| Population exclusion | Max 200 words | Explicit rules |
| Intervention/exposure | Optional | PICO I/E |
| Comparator | Required | Comparative, non-comparative, or both |
| Study design | Required | Checkboxes |
| Study types included | Max 250 words | All eligible designs |
| Study types excluded | Max 250 words | All excluded designs |
| Context | Required | Geographic, language, date, setting |

Decision rule: Criteria must be specific enough that two independent reviewers would reach the same inclusion decision at least 90% of the time.

### Section 3 — SIMILAR REVIEWS

Search PROSPERO and Cochrane for existing registrations. Assess top 3 results. Write distinct/overlap statement for each.

Decision rule: If substantially overlapping Cochrane review exists and is recent (≤3 years), reframe as update or narrow scope. Document decision.

### Section 4 — TIMELINE

| Field | Guidance |
|---|---|
| Start date | Date of first database search |
| End date | Projected manuscript submission date |

For retrospective registrations: use 1st of search month. Disclose in Additional Information.

### Section 5 — PROTOCOL AVAILABILITY

| Option | When |
|---|---|
| No protocol written | Planning doc is internal only |
| Published with DOI | Deposited on OSF or journal |
| Upload | To PROSPERO directly |

Decision rule: If target journal Q1 (IF >3.0), deposit on OSF before search and cite DOI.

### Section 6 — SEARCHING AND SCREENING

| Field | Default |
|---|---|
| Databases | PubMed + min 1 additional |
| Language | No restriction |
| Date | No restriction unless justified |
| Supplementary | Reference list + forward citation (always) |
| Selection process | Document reviewer count; disclose sole-reviewer |

Minimum portfolio: PubMed + one additional (Scholar Gateway, WoS, or Embase-equivalent).

### Section 7 — DATA COLLECTION PROCESS

| Field | Default |
|---|---|
| RoB assessed | Always Yes |
| RoB tool | NIH QAT (observational); RoB-2 (RCTs); ROBINS-I (NRSI) |
| Certainty | Always Yes; GRADE |
| Reporting bias | Yes; Egger/funnel if k≥10; justify omission if k<10 |
| IPD sought | No (default) |
| Authors contacted | No (default for retrospective) |

Decision rule: RoB tool must be pre-specified before seeing data.

### Section 8 — OUTCOMES

| Field | Limit |
|---|---|
| Main outcomes | Max 250 words; include definition, instruments, time points, effect measure |
| Additional outcomes | Max 300 words; optional |

Decision rule: Primary outcome must be singular. If two equally important, designate co-primary and adjust for multiplicity.

### Section 9 — PLANNED SYNTHESIS

State: narrative vs quantitative. If quantitative: effect measure, model, heterogeneity estimator, transformation. List all pre-specified SA scenarios. List subgroups. State publication bias method or justify omission.

Decision rule: If k<5 anticipated, pre-specify narrative as primary with quantitative as exploratory.

### Section 10 — CURRENT REVIEW STAGE

| Registration timing | Selections |
|---|---|
| Prospective | All: Not started |
| Concurrent | Searching: Started/Completed; rest: Not started |
| Retrospective | All: Not started (PROSPERO requirement); disclose in Additional Information |

### Section 11 — AFFILIATION, FUNDING, PEER REVIEW

Min 2 team members (PROSPERO requirement). Guarantor and named contact designated. State affiliation, funding, conflicts.

### Section 12 — ADDITIONAL INFORMATION

Disclose all of: category mismatch (prevalence under intervention), retrospective registration, preprint status, protocol deviations. Over-disclosure always preferred.

---

## Output Format

Filename: `[PROJECT]-P[N]-PLANNING-PROTOCOL-v1.0-[YYYYMMDD].md`
Obsidian: `/OpenClaw/research/[project]/protocols/`
GitHub: `frontier-research-lab/research/[project]/protocols/`
Commit: `[PROTOCOL] [POOL-N] Planning protocol v1.0 pre-search`

## Post-Registration Checklist

| Action | Timing | Owner |
|---|---|---|
| Receive CRD/DOI | 24-72h (PROSPERO) / immediate (OSF) | Orchestrator monitors |
| Insert into manuscript Methods | Same day as receipt | Phase 7 Agent |
| Update PROSPERO at milestone | Each major stage change | Orchestrator |
| Final update on acceptance | Within 30 days | Orchestrator |

---

*Generated: 18 March 2026 | Frontier Translational AI Research Lab*
