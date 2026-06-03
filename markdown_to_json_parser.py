import re
import json

def parse_markdown_sop(md_content):
    """
    Parses a tactical Markdown file and flattens it into structured data.
    """
    sop_data = {
        "metadata": {},
        "sections": {},
        "steps": []
    }
    
    # Extract IDs and Header Info
    header_match = re.search(r'#\s*(SOP-[A-Z]{3}-\d{3}):\s*(.*)', md_content)
    if header_match:
        sop_data["metadata"]["sop_id"] = header_match.group(1).strip()
        sop_data["metadata"]["title"] = header_match.group(2).strip()

    # Parse metadata block attributes
    metadata_fields = re.findall(r'\*\s*\*\*([A-Za-z\s]+):\*\*\s*(.*)', md_content)
    for field, value in metadata_fields:
        key = field.lower().replace(" ", "_")
        sop_data["metadata"][key] = value.strip()

    # Parse numbered execution lists
    steps = re.findall(r'\d+\.\s*(.*)', md_content)
    sop_data["steps"] = [step.strip() for step in steps]

    # Parse key-value specifications from bullet lists
    bullets = re.findall(r'\*\s*\*\*([A-Za-z\s]+):\*\*\s*(.*)', md_content)
    for key, val in bullets:
        clean_key = key.lower().replace(" ", "_")
        if clean_key not in sop_data["metadata"]:
            sop_data["sections"][clean_key] = val.strip()

    return sop_data

# Example Execution
markdown_input = """
# SOP-LOG-001: Cold-Chain Medical Kit Storage
* **Classification:** CONFIDENTIAL  
* **Effective Date:** 2026-06-03  
* **Version:** 1.2  

## 1. Storage Environmental Constraints
* **Target Temperature:** 2°C to 8°C
* **Max Humidity:** 60%

## 2. Sequence of Handling Steps
1. Verify seal integrity at point of entry.
2. Transfer payload immediately to refrigerated Zone C units.
"""

structured_json = parse_markdown_sop(markdown_input)
print(json.dumps(structured_json, indent=2))
