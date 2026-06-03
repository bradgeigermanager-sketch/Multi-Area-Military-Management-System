import re
import json

def parse_advanced_markdown_sop(md_content):
    """
    Parses a tactical Markdown document containing cross-reference hyperlinks,
    Table of Contents links, and equipment/checklist tracking tables.
    """
    sop_data = {
        "metadata": {},
        "table_of_contents": [],
        "tracking_tables": [],
        "steps": []
    }
    
    # 1. Parse Title and Identifier
    header_match = re.search(r'#\s*(SOP-[A-Z]{3}-\d{3}):\s*(.*)', md_content)
    if header_match:
        sop_data["metadata"]["sop_id"] = header_match.group(1).strip()
        sop_data["metadata"]["title"] = header_match.group(2).strip()

    # 2. Extract Table of Contents Hyperlinks [Text](#Anchor)
    toc_matches = re.findall(r'\*\s*\[([^\]]+)\]\((#[^\)]+)\)', md_content)
    for text, anchor in toc_matches:
        sop_data["table_of_contents"].append({"label": text, "target_anchor": anchor})

    # 3. Parse Standard Execution Sequences
    steps = re.findall(r'\d+\.\s*(.*)', md_content)
    sop_data["steps"] = [step.strip() for step in steps]

    # 4. Extract and Structure Markdown Data Tables
    # Locates rows bounded by '|' characters and segments the columns
    table_rows = re.findall(r'^\|(.*)\|', md_content, re.MULTILINE)
    active_table = []
    
    for row in table_rows:
        # Filter out layout dividing separating lines (e.g., |---|---|)
        if re.match(r'^\s*[:-]+\s*\|', row) or '---' in row:
            continue
        cells = [cell.strip() for cell in row.split('|')]
        active_table.append(cells)
        
    if active_table:
        sop_data["tracking_tables"].append({
            "headers": active_table[0],
            "rows": active_table[1:]
        })

    return sop_data

# Operational Demonstration Input
markdown_payload = """
# SOP-MNT-104: Main Battle Tank Armor Check
* **Classification:** SECRET

## Directory Table of Contents
* [Operational Checklist](#checklist)
* [Reference External Manual](https://garrison.mil)

## Inventory Matrix Tracking Table

| Item Code | Equipment Nomenclature | Check Frequency | Reference Link |
| :--- | :--- | :--- | :--- |
| TM-901 | [M1A2 Reactive Armor Hull](#step1) | Pre-Op | [System Link](https://sec.mil) |
| TM-905 | Track Assembly Pivot Pins | Weekly | [Parts Log](https://inventory.mil) |

## 1. Sequence Instructions
1. Inspect composite front-facing wedge sections for visible impacts.
2. Cross-reference diagnostic numbers against global registry keys.
"""

parsed_output = parse_advanced_markdown_sop(markdown_payload)
print(json.dumps(parsed_output, indent=2))
