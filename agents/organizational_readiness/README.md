# Organizational readiness specialist
From the scaffold root run:
python tools/build_prompt.py --agent agents/organizational_readiness --case agents/organizational_readiness/cases/primary.json
Paste the work/organizational_readiness_primary_prompt.txt packet into ChatGPT. Save its JSON to a new file and run python tools/validate_response.py PATH. Repeat with contrast_1 and contrast_2; compare with responses/. Use python tools/check_frozen_core.py to check integrity.
