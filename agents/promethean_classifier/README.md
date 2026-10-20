# Assignment 4 Promethean Technology Classification Agent

Lucy Shen | MASY1-GC 1800 | Candidate 0.3 | 20 October 2026

Read records/agent_record.md or the Word record for the conclusion and reflection. Read specialist_instructions.md and records/criteria_and_decision.md for criteria. records/source_register.json supplies dated evidence and limitations. records/revision_and_tests.md explains changes and test provenance. Earlier versions are preserved for comparison; 0.3 is the current candidate.

Scope: generative AI as evidenced by foundation language and code models. Preferred judgment: potentially Promethean, provisional, with demonstrated breakthrough as the evidentiary floor. The local content workflow remains untested. Broad significance supplies no adoption permission.

From the scaffold root:

```bash
python tools/build_prompt.py --agent agents/promethean_classifier --case agents/promethean_classifier/cases/v0_3/primary.json
```

Paste the resulting packet into ChatGPT. Save its returned JSON, then validate it using the supplied tools. No API key or programmatic model call is needed.

```bash
python tools/validate_response.py agents/promethean_classifier/responses/v0_3_primary.json
python agents/promethean_classifier/records/verify_contracts.py
python tools/check_frozen_core.py
```

Other current cases are safety, posture_only, hype_only, unknown and incremental_control under cases/v0_3. The last case is expressly synthetic. Saved outputs were composed in the same conversation and are not blind independent runs or proof of robustness. Original 0.1 and 0.2 examples remain preserved; their limits are explained rather than hidden.

Lucy selected the final higher classification, evidence-before-efficiency lesson and willingness to accept smaller reliable gains. AI assisted with code, analysis and wording. See records/student_input.json and the disclosure. Check any detailed lecture definition against the operational criteria before submission. No implemented Canva automation or time-saving result is claimed.
