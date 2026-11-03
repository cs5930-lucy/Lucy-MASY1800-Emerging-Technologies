From the scaffold root, build a fresh packet:
python tools/build_prompt.py --agent agents/adoption_agent --case agents/adoption_agent/cases/primary.json
Paste the resulting work/adoption_agent_primary_prompt.txt into ChatGPT. Save its JSON and run python tools/validate_response.py PATH_TO_JSON. Use python tools/check_frozen_core.py to check the scaffold. Repeat with contrast_1 and contrast_2. The archived initial prompt and response use v01_primary in their filenames. Packet construction uses no API key.
