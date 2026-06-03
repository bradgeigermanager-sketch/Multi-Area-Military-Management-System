import json
import csv

# 1. Load the core dataset
with open('military_data.json', 'r') as f:
    data = json.load(f)

garrisons = data['garrisons']

# 2. Export and flatten data to CSV format
csv_headers = [
    "zone_id", "location", "commanding_officer", "active_duty", "medical_staff",
    "rations_days", "medical_kits", "fuel_liters", "rounds_556mm", "shells_120mm",
    "anti_tank_missiles", "m1a2_tanks", "m2_bradleys", "uavs"
]

with open('military_inventory.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    
    for g in garrisons:
        writer.writerow([
            g['zone_id'], g['location'], g['personnel']['commanding_officer'],
            g['personnel']['active_duty'], g['personnel']['medical_staff'],
            g['supplies']['rations_days'], g['supplies']['medical_kits'], g['supplies']['fuel_liters'],
            g['ordnance']['5.56mm_rounds'], g['ordnance']['120mm_shells'], g['ordnance']['anti_tank_missiles'],
            g['equipment']['m1a2_tanks'], g['equipment']['m2_bradleys'], g['equipment']['unmanned_aerial_vehicles']
        ])

# 3. Compute structural totals for Command Summary
total_troops = sum(g['personnel']['active_duty'] for g in garrisons)
total_tanks = sum(g['equipment']['m1a2_tanks'] for g in garrisons)
total_rounds = sum(g['ordnance']['5.56mm_rounds'] for g in garrisons)

# 4. Generate the Dynamic HTML Control Panel Dashboard
html_rows = ""
for g in garrisons:
    html_rows += f"""
    <tr>
        <td class="bold">{g['zone_id']}</td>
        <td>{g['location']}</td>
        <td>{g['personnel']['commanding_officer']}</td>
        <td>{g['personnel']['active_duty']:,}</td>
        <td>{g['supplies']['fuel_liters']:,} L</td>
        <td>{g['ordnance']['5.56mm_rounds']:,}</td>
        <td>{g['equipment']['m1a2_tanks']}</td>
    </tr>
    """

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Command & Logistics Management Board</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #121824; color: #e2e8f0; margin: 40px; }}
        h1 {{ color: #f8fafc; border-bottom: 2px solid #1e293b; padding-bottom: 10px; font-size: 24px; text-transform: uppercase; tracking: 1px; }}
        .summary-container {{ display: flex; gap: 20px; margin-bottom: 30px; }}
        .card {{ background: #1e293b; padding: 20px; border-radius: 6px; flex: 1; border-left: 4px solid #38bdf8; }}
        .card h3 {{ margin: 0 0 10px 0; font-size: 12px; color: #94a3b8; text-transform: uppercase; }}
        .card .value {{ font-size: 28px; font-weight: bold; color: #f1f5f9; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: #1e293b; border-radius: 6px; overflow: hidden; }}
        th, td {{ padding: 14px 18px; text-align: left; border-bottom: 1px solid #334155; }}
        th {{ background-color: #0f172a; color: #38bdf8; font-size: 13px; text-transform: uppercase; }}
        tr:hover {{ background-color: #243249; }}
        .bold {{ font-weight: bold; color: #38bdf8; }}
    </style>
</head>
<body>

    <h1>Theater Logistical Command Dashboard</h1>
    
    <div class="summary-container">
        <div class="card">
            <h3>Total Troops</h3>
            <div class="value">{total_troops:,}</div>
        </div>
        <div class="card" style="border-left-color: #a78bfa;">
            <h3>Total Armor (M1A2)</h3>
            <div class="value">{total_tanks}</div>
        </div>
        <div class="card" style="border-left-color: #34d399;">
            <h3>Munitions Stockpile (5.56mm)</h3>
            <div class="value">{total_rounds:,}</div>
        </div>
    </div>

    <table>
        <thead>
            <tr>
                <th>Zone ID</th>
                <th>Location Sector</th>
                <th>Commanding Officer</th>
                <th>Personnel Units</th>
                <th>Fuel Supplies</th>
                <th>Ordnance (5.56mm)</th>
                <th>Equipment (Tanks)</th>
            </tr>
        </thead>
        <tbody>
            {html_rows}
        </tbody>
    </table>

</body>
</html>
"""

with open('dashboard.html', 'w') as f:
    f.write(html_content)

print("[SUCCESS] Export matrices generated: 'military_inventory.csv' and 'dashboard.html' successfully written.")

