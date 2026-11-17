# Running SubAgent 7
From the scaffold root:

    python tools/check_frozen_core.py
    python tools/build_prompt.py --agent agents/landscape --case agents/landscape/cases/primary.json --out work/landscape_primary.txt

Paste the packet in ChatGPT, save the JSON output, then run python tools/validate_response.py against that file. Repeat with contrast.json and hype.json. The suggested operating thresholds are illustrative. To analyze a new technology, replace all case fields and the dated evidence in additional_context. The register is a snapshot, not an automated feed.
