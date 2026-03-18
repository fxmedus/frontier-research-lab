# Research Planning Protocol — v1.0

**Issued:** 18 March 2026
**Authority:** Julian Borges, MD — Lab Director
**Status:** ACTIVE
**Type:** Mandatory pre-execution governance standard
**Scope:** ALL research projects in the Frontier Translational Research Lab
**Principle:** Plan first, execute second — no exceptions

---

## Governing Rule

No research execution of any kind may begin without a completed planning protocol document saved to Obsidian and GitHub. This applies to every project type the lab produces.

## Why This Exists

Without structured planning:
- Analytical drift occurs (outcomes change after seeing data)
- Reporting bias creeps in (only favorable results survive)
- Methods sections become post-hoc rationalizations rather than pre-specified designs
- Peer reviewers and journal editors detect this and reject
- Reproducibility is impossible because the original intent is undocumented

---

## Project Type Templates

Each project type has a tailored planning template. All share the same core structure adapted to the specific methodology.

### Template A — Systematic Review / Meta-Analysis

See `SYSTEMATIC_REVIEW_PREFLIGHT_v1.0.md` for the full 12-section checklist. This is the most detailed template because PROSPERO registration demands it.

### Template B — Mendelian Randomization Study

| Section | Content Required |
|---|---|
| 1. Study title and design | Two-sample MR; instrument source; outcome source |
| 2. Research question | Exposure, outcome, causal hypothesis |
| 3. Instrument selection criteria | GWS threshold, F-statistic minimum, LD clumping parameters |
| 4. Data sources | Exposure GWAS (ID, sample size, ancestry); outcome GWAS (ID, sample size, ancestry) |
| 5. Primary analysis | IVW method specification |
| 6. Sensitivity analyses | MR-Egger, weighted median, MR-PRESSO, Steiger directionality |
| 7. Colocalization | Method (coloc, eCAVIAR), priors, threshold |
| 8. Power and sample overlap | Sample overlap assessment; F-statistic distribution |
| 9. Quality assurance | InSIDE assumption, NOME assumption, horizontal pleiotropy tests |
| 10. Registration | OSF pre-registration recommended; include Methods section |
| 11. Timeline | Start and projected submission |
| 12. Funding and conflicts | Standard disclosure |

### Template C — Drug Discovery / Computational Pipeline (DrugSynth AI)

| Section | Content Required |
|---|---|
| 1. Pipeline identity | Disease, target class, pipeline version |
| 2. Target selection criteria | Evidence grade, druggability threshold, complex membership |
| 3. Data sources | UniProt, ChEMBL, PDB, OMIM; version and access date |
| 4. Computational methods | Docking software, scoring function, ADMET filters |
| 5. Validation criteria | Pass/fail thresholds for each filter stage |
| 6. Output registries | YAML schema, field definitions, ID format |
| 7. Manuscript plan | Chapter structure, IMRAD per chapter |
| 8. Quality assurance | Cross-validation, literature benchmarking |
| 9. Timeline | Per-chapter milestones |
| 10. Funding and conflicts | Standard disclosure |

### Template D — Case Report / Case Series

| Section | Content Required |
|---|---|
| 1. Case identity | Patient demographics (de-identified), presenting condition |
| 2. Clinical question | What this case demonstrates or challenges |
| 3. CARE checklist mapping | Pre-map all 13 CARE items to planned manuscript sections |
| 4. Literature context | Prior case reports on same condition; what is novel |
| 5. Ethical considerations | IRB status, informed consent, de-identification plan |
| 6. Target journal | Journal specs (word limit, figure limit, APC) |
| 7. Timeline | Draft to submission |
| 8. Funding and conflicts | Standard disclosure |

### Template E — Cohort Analysis / Secondary Data Analysis

| Section | Content Required |
|---|---|
| 1. Study title and design | Cohort source, analysis type (cross-sectional, longitudinal) |
| 2. Research question | Exposure, outcome, covariates |
| 3. Data source | Cohort name, access mechanism, sample size, variables available |
| 4. Inclusion/exclusion criteria | Population definition, missing data handling |
| 5. Statistical plan | Primary model, covariates, interaction terms, sensitivity analyses |
| 6. Multiple comparisons | Bonferroni, FDR, or other correction if applicable |
| 7. Quality assurance | Assumption checks, residual diagnostics, DAG for confounding |
| 8. Registration | OSF or ClinicalTrials.gov if prospective |
| 9. Timeline | Analysis to submission |
| 10. Funding and conflicts | Standard disclosure |

---

## Retroactive Application to Existing Projects

For projects already in execution without a planning protocol, create one retroactively and disclose it.

| Project | Status | Action |
|---|---|---|
| IronFF Pool 7 | Complete; PROSPERO submitted | Protocol documented via PROSPERO registration |
| IronFF Pool 6 | Complete; manuscript accepted | Create retroactive protocol before journal submission |
| CYP19A1-ASD MR | Complete; submitted to Frontiers | Create retroactive protocol; add to OSF |
| DrugSynth AI MitoCorex | 7 chapters complete | Create retroactive pipeline protocol |
| IronFF Pools 2-5, 8-10 | Phase 4 or pending | Create prospective protocol BEFORE resuming searches |

---

## Pipeline Integration

| Phase | Gate | Planning Role |
|---|---|---|
| Phase 2 (Question Formulation) | G1 | Core sections completed (question, design, data sources) |
| Phase 3 (Protocol Design) | G2 | All sections completed; protocol file saved |
| Phase 4+ (Execution) | BLOCKED | Cannot begin without G2 pass |

## Agent Assignment

| Task | Agent | Tier |
|---|---|---|
| Draft planning protocol | Phase 2 Planning Agent | T3 |
| Review and approve | Master Orchestrator | T1 |
| Execute registration (PROSPERO/OSF) | Phase 2 Planning Agent | T3 |
| Insert registration ID into manuscript | Phase 7 Manuscript Agent | T4 |

## Output Format

Filename: `[PROJECT]-PLANNING-PROTOCOL-v1.0-[YYYYMMDD].md`
Obsidian: `/OpenClaw/research/[project]/protocols/`
GitHub: `frontier-research-lab/research/[project]/protocols/`
Commit: `[PROTOCOL] Planning protocol v1.0 pre-execution`

---

*Generated: 18 March 2026 | Frontier Translational Research Lab*
