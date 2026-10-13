# Lucy Shen Assignment 3

Innovation and Disruption Agent for MASY1-GC 1800 Emerging Technologies. Version 0.2-student. The agent distinguishes general technology classification from application and organizational impact. The three organizational cases are hypothetical.

## Start here

Read records/agent_record.md for the submission record and records/business_model_analysis.md for the concise analytical handoff. The Word version is records/Lucy_Shen_Assignment3_Agent_Record.docx. Read records/test_record.md and records/revision_log.md for evidence of evaluation and revision. Source URLs and limitations are in evidence/source_register.md.

## Run the course workflow

From the repository root, use Python 3. The course workflow requires no API key or additional Python packages.

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/innovation_disruption --case agents/innovation_disruption/cases/primary.json
```

Open the printed prompt file, paste its complete contents into ChatGPT and request JSON only. Save the returned object to agents/innovation_disruption/responses/primary_response.json. Then run:

```bash
python3 tools/validate_response.py agents/innovation_disruption/responses/primary_response.json
```

Repeat with contrast_1.json, contrast_2.json and insufficient_context.json. If replacing saved outputs, also update the run manifest rather than presenting old hashes as proof of a new run. The preserved outputs were generated in the development conversation; running the Python tools alone does not invoke an AI model.

## Verify this saved submission

```bash
python3 agents/innovation_disruption/verify_submission.py
```

The additional student script checks the supplied input/output schemas, frozen hashes, prompt reproducibility, controlled context inputs and saved run hashes. It does not score truth or prove repeatability of an LLM response. No shared course file was modified.

## Reading the results

| Case | Final judgment | Main reason |
| --- | --- | --- |
| Linden and Row | High conditional exposure | Assumed content advantage may become imitable; economics remain unverified |
| B2B uniforms | Low under stated scope | Supporting content does not establish disruption of contract value |
| Luxury heritage | Firm rating withheld; Moderate or High conditionally | Use boundary and authenticity response determine severity |
| Insufficient context | Withheld | Missing business model and source of advantage |

General classification stays a qualified commercialized breakthrough across these same-scope examples. This is a reasoned interpretation, not a forced answer for every emerging technology. Application implementation is not established.

## Published repository

Repository: https://github.com/cs5930-lucy/Lucy-MASY1800-Emerging-Technologies

Assignment branch: https://github.com/cs5930-lucy/Lucy-MASY1800-Emerging-Technologies/tree/assignment-3-innovation-disruption

Analyzed candidate: https://github.com/cs5930-lucy/Lucy-MASY1800-Emerging-Technologies/commit/866b6997bc55707b1f2052f9c442a6bd25188377

The private course repository preserves the original scaffold on main and the development stages on the assignment branch. The local archive retains its original Git history; commit metadata changed during GitHub publication, so use the remote commit in the Agent Record for the submitted reference. GitHub publication is complete. Brightspace submission and instructor access remain the student's responsibility.
