##Here is the updated, production-ready core layout for the system. It reorganizes the interface into a high-utility split-screen frame layout using CSS Grid, allowing you to load and manage multiple documents side by side in a single browser window.
##It also adds a functional Download & Export button that aggregates both the SOP structures and their corresponding historical change ledgers into a clean, formatted .txt report file.
## 1. Updated Python Interface Compiler Script (compile_workspace.py)
##This script bundles the unified data schema and automatically builds a complete, ready-to-run HTML file with side-by-side frames.

import json
# Setup standard system baseline config parameters
system_baseline = {
    "system_id": "ITOC-SYS-2026",
    "garrison_scope": ["ALPHA", "BRAVO"]
}
def generate_split_frame_dashboard():
    html_layout = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Integrated Multi-Frame Theater Logistical Console</title>
    <style>
        :root {
            --bg-deep: #090d16;
            --bg-panel: #111827;
            --bg-input: #1f2937;
            --border-glow: #1e293b;
            --text-main: #f3f4f6;
            --accent-cyan: #38bdf8;
            --accent-green: #10b981;
        }
        body {
            font-family: system-ui, -apple-system, sans-serif;
            background: var(--bg-deep);
            color: var(--text-main);
            margin: 0;
            padding: 15px;
            box-sizing: border-box;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        
        /* Layout Grid and Split Screen Frame Topography */
        .workspace-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: var(--bg-panel);
            padding: 12px 20px;
            border-radius: 6px;
            border: 1px solid var(--border-glow);
            margin-bottom: 12px;
        }
        .workspace-header h2 { margin: 0; font-size: 15px; text-transform: uppercase; color: #fff; letter-spacing: 0.5px; }
        
        .frame-grid-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            flex: 1;
            min-height: 0; /* Prevents container blowout */
        }
        
        .frame-panel {
            background: var(--bg-panel);
            border: 1px solid var(--border-glow);
            border-radius: 6px;
            display: flex;
            flex-direction: column;
            min-height: 0;
        }
        .frame-banner {
            background: #030712;
            padding: 10px 15px;
            font-size: 11px;
            font-weight: 700;
            color: #64748b;
            border-bottom: 1px solid var(--border-glow);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .frame-body {
            padding: 20px;
            overflow-y: auto;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        /* Input Controls & Structured Items */
        label { font-size: 10px; text-transform: uppercase; color: #94a3b8; font-weight: 700; }
        input, select, textarea {
            background: var(--bg-input);
            border: 1px solid #374151;
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 13px;
            font-family: inherit;
        }
        textarea { height: 60px; resize: none; }
        
        .btn-row { display: flex; gap: 10px; margin-top: auto; padding-top: 10px; }
        .primary-btn { background: var(--accent-green); color: white; border: none; padding: 10px 15px; font-weight: bold; border-radius: 4px; cursor: pointer; text-transform: uppercase; font-size: 11px; flex: 1; }
        .export-btn { background: transparent; border: 1px solid var(--accent-cyan); color: var(--accent-cyan); padding: 10px 15px; font-weight: bold; border-radius: 4px; cursor: pointer; text-transform: uppercase; font-size: 11px; display: flex; align-items: center; justify-content: center; gap: 6px; }
        .export-btn:hover { background: rgba(56, 189, 248, 0.1); }

        /* Document Display Matrix Components */
        .doc-list-node {
            background: var(--bg-deep);
            border: 1px solid #1e293b;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 13px;
        }
        .doc-list-node:hover { border-color: var(--accent-cyan); }
        .doc-list-node h5 { margin: 0 0 4px 0; color: #fff; }
        
        .timeline-card {
            background: #1f2937;
            border-left: 3px solid #64748b;
            padding: 10px;
            border-radius: 4px;
            font-size: 12px;
        }
        .timeline-card.critical { border-left-color: #ef4444; }
    </style>
</head>
<body>

    <!-- Global Operations Control Bar -->
    <div class="workspace-header">
        <h2>Theater Logistical Operations Command Board</h2>
        <button class="export-btn" onclick="triggerLocalDiskExport()">💾 Export Flat Ledger File</button>
    </div>

    <!-- Active Grid View Ports -->
    <div class="frame-grid-layout">
        
        <!-- FRAME LEFT: Active Document Generation Engine -->
        <div class="frame-panel">
            <div class="frame-banner">
                <span>[FRAME 01] Active Profile Editor Workspace</span>
                <span style="color: var(--accent-cyan);">MODE: INTERACTIVE</span>
            </div>
            <div class="frame-body">
                <label>SOP Code Identifier</label>
                <input type="text" id="sopCode" value="SOP-ORD-402">
                
                <label>Nomenclature Title Name</label>
                <input type="text" id="sopTitle" value="120mm Heavy Shell High-Explosive Transfer Sequence">
                
                <label>Execution Command Directives</label>
                <textarea id="sopSteps">1. Engage static discharge grounding wires.\n2. Deploy auxiliary battery rails before payload transport.</textarea>
                
                <div class="live-monitor-divider" style="height:1px; background:#1e293b; margin:10px 0;"></div>
                
                <label>Audit Release Notes</label>
                <textarea id="changeSummary" placeholder="Provide log detail notes explaining the reason for this version modification..."></textarea>
                
                <label>Log Impact Classification</label>
                <select id="impactGroup">
                    <option value="ROUTINE">ROUTINE MAINTENANCE PATCH</option>
                    <option value="CRITICAL">CRITICAL READINESS ALTERATION</option>
                </select>

                <div class="btn-row">
                    <button class="primary-btn" onclick="commitEntryData()">Commit Build Record</button>
                </div>
            </div>
        </div>
        
        <!-- FRAME RIGHT: Library Collections & Change Log Split view -->
        <div class="frame-panel">
            <div class="frame-banner">
                <span>[FRAME 02] Registry Repository & Timeline Trace</span>
                <span id="systemClock" style="font-family: monospace;">00:00:00Z</span>
            </div>
            <div class="frame-body">
                <label>Saved Library SOP Catalogs</label>
                <div id="catalogContainer" style="display:flex; flex-direction:column; gap:8px; max-height:160px; overflow-y:auto;">
                    <!-- Saved items loop dynamically here -->
                </div>
                
                <div style="height:1px; background:#1e293b; margin:5px 0;"></div>
                
                <label>Historical Release & Build Audits Timeline</label>
                <div id="timelineContainer" style="display:flex; flex-direction:column; gap:8px; flex:1; overflow-y:auto;">
                    <!-- Audit logs append here -->
                </div>
            </div>
        </div>

    </div>

    <!-- JavaScript Data Layer and Local Browser Storage Exporters -->
    <script>
        // Synchronized Data Storage Core Layers
        let loadedSops = {
            "SOP-ORD-402": {
                id: "SOP-ORD-402",
                title: "120mm Heavy Shell High-Explosive Transfer Sequence",
                steps: "1. Engage static discharge grounding wires.\\n2. Deploy auxiliary battery rails before payload transport.",
                version: "1.0",
                timestamp: "2026-06-03T01:30:00Z"
            }
        };

        let auditLogs = [
            { build_id: "BLD-X92A1B", sop_id: "SOP-ORD-402", version: "1.0", impact: "ROUTINE", notes: "Initial baseline creation framework setup.", time: "2026-06-03T01:30:00Z" }
        ];

        function commitEntryData() {
            const id = document.getElementById('sopCode').value.trim();
            const title = document.getElementById('sopTitle').value.trim();
            const steps = document.getElementById('sopSteps').value.trim();
            const notes = document.getElementById('changeSummary').value.trim() || "Routine operational patch maintenance.";
            const impact = document.getElementById('impactGroup').value;

            if(!id) return alert("System tracking indices require a valid identifier.");

            // Calculate version increments dynamically
            let currentVer = "1.0";
            if(loadedSops[id]) {
                let parts = loadedSops[id].version.split('.');
                currentVer = `1.${parseInt(parts[1]) + 1}`;
            }

            const zuluTime = new Date().toISOString().replace(/\\.\\d{3}/, '');
            const hexBuild = "BLD-" + Math.floor(Math.random()*16777215).toString(16).toUpperCase();

            // Store document properties 
            loadedSops[id] = { id: id, title: title, steps: steps, version: currentVer, timestamp: zuluTime };
            
            // Unshift prepends fresh audit elements to the top of the history timeline array
            auditLogs.unshift({ build_id: hexBuild, sop_id: id, version: currentVer, impact: impact, notes: notes, time: zuluTime });

            document.getElementById('changeSummary').value = "";
            renderInterfaceComponents();

alert(Record updated dynamically in tracking frame memory: ${id} (v${currentVer}));
}
// Flat Document Text Generator and Local File Exporter
function triggerLocalDiskExport() {
let fileContentOutput = "=====================================================\n";
fileContentOutput += " THEATER LOGISTICAL COMMAND OPERATIONAL LEDGER \n";
fileContentOutput += " TIMESTAMP EXPORTED: " + new Date().toISOString() + " \n";
fileContentOutput += "=====================================================\n\n";
fileContentOutput += "--- ACTIVE SOP LIBRARY INDEX ---\n";
Object.keys(loadedSops).forEach(key => {
let s = loadedSops[key];
fileContentOutput += [${s.id}] ${s.title}\\n;
fileContentOutput += Version Rank: v${s.version} | Last Modified: ${s.timestamp}\\n;
fileContentOutput += Directives Set:\\n${s.steps}\\n\\n;
});
fileContentOutput += "\n--- APPEND-ONLY BUILD AUDIT LOG TRACKS ---\n";
auditLogs.forEach(log => {
fileContentOutput += Build Trace: ${log.build_id} | Ref: ${log.sop_id} | Ver: ${log.version} [${log.impact}]\\n;
fileContentOutput += Change Record Summary: ${log.notes}\\n;
fileContentOutput += Publish Timestamp: ${log.time}\\n-----------------------------------------------------\\n;
});
// Create a virtual file object link to trigger browser download
const rawBlob = new Blob([fileContentOutput], { type: "text/plain;charset=utf-8" });
const linkElement = document.createElement("a");
linkElement.href = URL.createObjectURL(rawBlob);
linkElement.download = "COMMAND_LOGISTICAL_EXPORT_REPORT.txt";
document.body.appendChild(linkElement);
linkElement.click();
document.body.removeChild(linkElement);
}
function renderInterfaceComponents() {
// Build out inventory panel listings
const catalog = document.getElementById('catalogContainer');
catalog.innerHTML = "";
Object.keys(loadedSops).forEach(k => {
const doc = loadedSops[k];
catalog.innerHTML += <div class="doc-list-node" onclick="loadDocToInputs('${doc.id}')"> <h5>${doc.id}: ${doc.title}</h5> <div style="font-size:10px; color:#64748b;">Version v${doc.version} | Mod: ${doc.timestamp}</div> </div>;
});
// Build out reverse chronological build ledger listings
const timeline = document.getElementById('timelineContainer');
timeline.innerHTML = "";
auditLogs.forEach(l => {
const isCritical = l.impact === "CRITICAL" ? "critical" : "";
timeline.innerHTML += <div class="timeline-card ${isCritical}"> <div style="display:flex; justify-content:space-between; font-weight:bold; color:#94a3b8; font-family:monospace; font-size:10px;"> <span>${l.build_id} -> ${l.sop_id}</span> <span style="color:var(--accent-cyan)">v${l.version}</span> </div> <p style="margin:4px 0; color:#cbd5e1;">${l.notes}</p> <div style="font-size:9px; color:#4b5563; text-align:right;">${l.time}</div> </div>;
});
}
function loadDocToInputs(id) {
const item = loadedSops[id];
if(!item) return;
document.getElementById('sopCode').value = item.id;
document.getElementById('sopTitle').value = item.title;
document.getElementById('sopSteps').value = item.steps.replace(/\\n/g, '\n');
}
// Sync and format active system clock display logs
setInterval(() => {
document.getElementById('systemClock').innerText = new Date().toISOString().slice(11,19) + "Z";
}, 1000);
// Initial Framework Component Boot Load
renderInterfaceComponents();



"""
return html_layout
with open('theater_workspace.html', 'w') as f:
f.write(generate_split_frame_dashboard())
print("[COMPILE SUCCESS] Operational split-frame board built as 'theater_workspace.html'.")
