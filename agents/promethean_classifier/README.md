# Assignment 4 Promethean Technology Classification Agent

Candidate version 0.2 for Lucy Shen, MASY1-GC 1800, 19 October 2026.

Read specialist_instructions.md for the proposed significance criteria. See records/source_register.json for checked sources, records/revision_and_tests.md for the first-draft weakness and context comparison, and responses/ for representative JSON outputs. records/prompts/ preserves assembled prompt packets, including version 0.1.

From the scaffold root, build a new prompt with:

```bash
python tools/build_prompt.py --agent agents/promethean_classifier --case agents/promethean_classifier/cases/primary.json
```

Paste the generated packet into ChatGPT and save its JSON response. This is the interactive runtime, with no API key. Do not treat a packet as an automatically executed model call.

```bash
python tools/validate_response.py agents/promethean_classifier/responses/v0_2_primary.json
python agents/promethean_classifier/records/verify_contracts.py
python tools/check_frozen_core.py
```

Independent judgment for student review: breakthrough is currently supported; potentially Promethean remains a qualified possibility. Broader significance justifies monitoring and learning. The local decision still requires approved product evidence, acceptable quality, measured total effort and accountable approval. The 80% efficiency target is untested and its metric needs agreement.

The four criteria are an operational proposal based on the assignment categories. Detailed lecture criteria were not provided and should be checked before submission. Organizational resources, posture and the four-week evaluation horizon are case assumptions. Lucy supplied the workflow, desired brief and mockup, willingness to retouch and efficiency goal. AI drafted the implementation, tests and analytical judgment. Lucy has not yet independently confirmed this Assignment 4 judgment.
