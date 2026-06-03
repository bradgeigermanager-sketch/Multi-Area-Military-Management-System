import json

# Sample data database matching the Logistics schema rules
sop_database = [
    {
        "template_type": "logistics_template",
        "title": "Cold-Chain Medical Kit Storage",
        "summary": "Environmental control rules for medical assets.",
        "data": {
            "metadata": {
                "sop_id": "SOP-LOG-001", "version": "1.2",
                "security_classification": "CONFIDENTIAL",
                "effective_date": "2026-06-03", "author_signoff": "Capt. E. Miller"
            },
            "storage_constraints": { "temperature_celsius": "2C to 8C", "humidity_max_percent": 60, "hazmat_class": "Class 6.2" },
            "inventory_thresholds": { "minimum_reserve": 200, "reorder_trigger_point": 350 },
            "handling_steps": ["Verify containment seals.", "Log temperature every 4 hours.", "Check reserve count thresholds."]
        }
    }
]

# Generate interface modules to inject into the web view
def generate_sop_html_components():
    injected_html = ""
    for sop in sop_database:
        m = sop['data']['metadata']
        steps = "".join([f"<li>{s}</li>" for s in sop['data']['handling_steps']])
        
        injected_html += f"""
        <div class="sop-card" data-template="{sop['template_type']}">
            <div class="sop-badge">{m['security_classification']}</div>
            <h3>{m['sop_id']}: {sop['title']}</h3>
            <p><strong>Effective:</strong> {m['effective_date']} | <strong>Ver:</strong> {m['version']}</p>
            <p class="summary-txt">{sop['summary']}</p>
            <div class="sop-details">
                <strong>Mandatory Steps:</strong>
                <ol>{steps}</ol>
            </div>
        </div>
        """
    return injected_html

print("[SUCCESS] SOP compilation complete. Nodes processed ready for dashboard integration.")
