import json

# 1. Mock JSON Logistics Data
garrisons = [
    {
        "zone_id": "ZONE-ALPHA", "location": "Sector 4-North",
        "personnel": {"active_duty": 1250, "medical_staff": 45, "commanding_officer": "Col. J. Vance"},
        "supplies": {"rations_days": 45, "medical_kits": 850, "fuel_liters": 120000},
        "ordnance": {"5.56mm_rounds": 500000, "120mm_shells": 320, "anti_tank_missiles": 45},
        "equipment": {"m1a2_tanks": 12, "m2_bradleys": 24, "unmanned_aerial_vehicles": 8}
    },
    {
        "zone_id": "ZONE-BRAVO", "location": "Sector 9-Delta",
        "personnel": {"active_duty": 850, "medical_staff": 30, "commanding_officer": "Lt. Col. A. Reyes"},
        "supplies": {"rations_days": 30, "medical_kits": 400, "fuel_liters": 75000},
        "ordnance": {"5.56mm_rounds": 350000, "120mm_shells": 150, "anti_tank_missiles": 20},
        "equipment": {"m1a2_tanks": 6, "m2_bradleys": 16, "unmanned_aerial_vehicles": 4}
    }
]

# 2. Knowledge Base Data Library
kb_articles = [
    {
        "id": "SOP-001", "category": "supplies", "title": "Cold-Chain Medical Kit Storage",
        "summary": "Standard procedures for maintaining thermal integrity of Class VIII medical supplies in field conditions.",
        "steps": ["Ensure main containment units stay between 2°C and 8°C.", "Log temperature variance reports every 0400 and 1600 hours.", "Deploy auxiliary generator if primary power drops below 15%."]
    },
    {
        "id": "SOP-002", "category": "ordnance", "title": "120mm Munitions Transfer Protocols",
        "summary": "Safety mechanisms and transport rules for heavy armor payload replenishment cycles.",
        "steps": ["Verify grounding strap engagement prior to unboxing hulls.", "Utilize dual-operator mechanical lifts for all Sabot rounds.", "Maintain 50-meter separation distance between unvetted transport assets."]
    },
    {
        "id": "SOP-003", "category": "equipment", "title": "UAV Pre-Flight Log Checklist",
        "summary": "Mandatory systems operational verification sequence for mid-range surveillance assets.",
        "steps": ["Audit link encryption keys against current HQ cipher blocks.", "Inspect composite wing-root assemblies for micro-fractures.", "Calibrate optical payload arrays across infrared spectrum bands."]
    },
    {
        "id": "SOP-004", "category": "personnel", "title": "Rotational Decompression Schedules",
        "summary": "Mandatory stand-down cycles to preserve theater deployment readiness indicators.",
        "steps": ["Enforce 72-hour operational restriction post 14-day field watches.", "Execute mandatory medical triage reviews at designated zone collection centers.", "Update active personnel status ledgers within 60 minutes of shifts."]
    }
]

# Calculate High Level Aggregates
total_troops = sum(g['personnel']['active_duty'] for g in garrisons)
total_tanks = sum(g['equipment']['m1a2_tanks'] for g in garrisons)

# Build HTML Table Rows
table_rows = ""
for g in garrisons:
    table_rows += f"""
    <tr>
        <td class="bold">{g['zone_id']}</td>
        <td>{g['location']}</td>
        <td>{g['personnel']['commanding_officer']}</td>
        <td>{g['personnel']['active_duty']:,}</td>
        <td>{g['supplies']['fuel_liters']:,} L</td>
        <td>{g['ordnance']['5.56mm_rounds']:,}</td>
        <td>{g['equipment']['m1a2_tanks']}</td>
    </tr>"""

# Build Knowledge Base Grid Cards
kb_cards = ""
for art in kb_articles:
    steps_list = "".join([f"<li>{step}</li>" for step in art['steps']])
    kb_cards += f"""
    <div class="kb-card" data-category="{art['category']}">
        <div class="kb-meta">
            <span class="kb-id">{art['id']}</span>
            <span class="tag tag-{art['category']}">{art['category']}</span>
        </div>
        <h4 class="kb-title">{art['title']}</h4>
        <p class="kb-desc">{art['summary']}</p>
        <ul class="kb-steps">{steps_list}</ul>
    </div>"""

# 3. Compile Master HTML Layout String
html_layout = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Integrated Tactical Operations Center</title>
    <style>
        :root {{ --bg: #0f172a; --panel: #1e293b; --border: #334155; --text: #e2e8f0; --accent: #38bdf8; }}
        body {{ font-family: system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--text); margin: 30px; line-height: 1.5; }}
        h2, h3 {{ text-transform: uppercase; letter-spacing: 1px; color: #f8fafc; margin-bottom: 15px; border-left: 4px solid var(--accent); padding-left: 10px; }}
        .metrics {{ display: flex; gap: 20px; margin-bottom: 35px; }}
        .card {{ background: var(--panel); padding: 20px; border-radius: 6px; flex: 1; border: 1px solid var(--border); }}
        .card div {{ font-size: 11px; color: #94a3b8; text-transform: uppercase; font-weight: 600; }}
        .card p {{ font-size: 28px; font-weight: 700; margin: 5px 0 0 0; color: #fff; }}
        table {{ width: 100%; border-collapse: collapse; background: var(--panel); border-radius: 6px; overflow: hidden; margin-bottom: 45px; border: 1px solid var(--border); }}
        th, td {{ padding: 12px 16px; text-align: left; border-bottom: 1px solid var(--border); }}
        th {{ background: #0b0f19; color: var(--accent); font-size: 12px; text-transform: uppercase; }}
        .bold {{ font-weight: 600; color: var(--accent); }}
        
        /* Knowledge Base Section Styles */
        .kb-controls {{ display: flex; gap: 15px; margin-bottom: 20px; align-items: center; background: var(--panel); padding: 15px; border-radius: 6px; border: 1px solid var(--border); }}
        .search-bar {{ flex: 1; background: #0f172a; border: 1px solid var(--border); padding: 10px 15px; border-radius: 4px; color: #fff; font-size: 14px; }}
        .search-bar:focus {{ outline: 1px solid var(--accent); }}
        .filter-btn {{ background: #0b0f19; border: 1px solid var(--border); padding: 8px 16px; border-radius: 4px; color: #94a3b8; cursor: pointer; text-transform: uppercase; font-size: 12px; font-weight: 600; }}
        .filter-btn.active, .filter-btn:hover {{ background: var(--accent); color: #000; border-color: var(--accent); }}
        .kb-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 20px; }}
        .kb-card {{ background: var(--panel); border: 1px solid var(--border); border-radius: 6px; padding: 20px; display: flex; flex-direction: column; transition: transform 0.2s; }}
        .kb-card:hover {{ transform: translateY(-2px); border-color: #475569; }}
        .kb-meta {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
        .kb-id {{ font-family: monospace; color: #64748b; font-size: 13px; font-weight: 700; }}
        .tag {{ font-size: 10px; padding: 3px 8px; border-radius: 4px; text-transform: uppercase; font-weight: 700; }}
        .tag-supplies {{ background: #1e3a8a; color: #93c5fd; }}
        .tag-ordnance {{ background: #7c2d12; color: #fdba74; }}
        .tag-equipment {{ background: #581c87; color: #d8b4fe; }}
        .tag-personnel {{ background: #064e3b; color: #6ee7b7; }}
        .kb-title {{ margin: 0 0 8px 0; font-size: 17px; color: #f1f5f9; }}
        .kb-desc {{ margin: 0 0 15px 0; font-size: 13px; color: #94a3b8; flex-grow: 1; }}
        .kb-steps {{ margin: 0; padding-left: 20px; font-size: 12px; color: #cbd5e1; border-top: 1px solid var(--border); padding-top: 12px; }}
        .kb-steps li {{ margin-bottom: 6px; }}
    </style>
</head>
<body>

    <h2>Theater Fleet & Logistical Summary</h2>
    <div class="metrics">
        <div class="card"><div>Active Theater Troops</div><p>{total_troops:,}</p></div>
        <div class="card"><div>Tracked Armor Assets</div><p>{total_tanks}</p></div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Zone ID</th><th>Location Sector</th><th>Commanding Officer</th><th>Personnel</th><th>Fuel Reserves</th><th>Ordnance (5.56mm)</th><th>Equipment (Armor)</th>
            </tr>
        </thead>
        <tbody>{table_rows}</tbody>
    </table>

    <h2>Tactical Knowledge Base (SOP Library)</h2>
    <div class="kb-controls">
        <input type="text" id="kbSearch" class="search-bar" placeholder="Search standard operating procedures by keywords, IDs, or details...">
        <button class="filter-btn active" onclick="filterCategory('all', this)">All SOPs</button>
        <button class="filter-btn" onclick="filterCategory('supplies', this)">Supplies</button>
        <button class="filter-btn" onclick="filterCategory('ordnance', this)">Ordnance</button>
        <button class="filter-btn" onclick="filterCategory('equipment', this)">Equipment</button>
        <button class="filter-btn" onclick="filterCategory('personnel', this)">Personnel</button>
    </div>

    <div class="kb-grid" id="kbGrid">{kb_cards}</div>

    <script>
        function filterCategory(cat, btn) {{
            // Update Active Tab Button Highlights
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            // Execute Filter Matrix
            const query = document.getElementById('kbSearch').value.toLowerCase();
            applyFilterAndSearch(cat, query);
        }}

        document.getElementById('kbSearch').addEventListener('input', function(e) {{
            const query = e.target.value.toLowerCase();
            const activeCatBtn = document.querySelector('.filter-btn.active');
            const activeCat = activeCatBtn.innerText.toLowerCase().replace(' all sops', 'all').replace(' sops', '');
            applyFilterAndSearch(activeCat, query);
        }});

        function applyFilterAndSearch(category, query) {{
            const cards = document.querySelectorAll('.kb-card');
            cards.forEach(card => {{
                const cardCat = card.getAttribute('data-category');
                const cardText = card.innerText.toLowerCase();
                const matchCat = (category === 'all' || category === cardCat);
                const matchSearch = cardText.includes(query);
                if (matchCat && matchSearch) {{card.style.display = 'flex';}} 
                else {{card.style.display = 'none';}}}});}}"""with open('index.html', 'w') as f:f.write(html_layout)
                print("[INFO] Production interface 'index.html' written cleanly with real-time UI knowledge base filters.")
