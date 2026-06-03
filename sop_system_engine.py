import datetime
import json
import re

class SOPLibraryManager:
    def __init__(self):
        # Simulation storage of active records library
        self.library = {}

    def save_sop_record(self, raw_payload):
        """
        Saves or increments a document structure within the system directory.
        Applies live ISO timestamps and handles version string changes.
        """
        sop_id = raw_payload.get("sop_id", "SOP-GEN-000")
        current_time = datetime.datetime.utcnow().isoformat() + "Z"
        
        if sop_id in self.library:
            # Document exists: Extract old configuration numbers to bump patch version
            old_version = self.library[sop_id]["metadata"]["version"]
            major, minor = map(int, old_version.split('.'))
            new_version = f"{major}.{minor + 1}"
        else:
            # Brand new file initialization template parameters
            new_version = "1.0"

        finalized_node = {
            "sop_id": sop_id,
            "title": raw_payload.get("title", "Untitled Document Blueprint"),
            "metadata": {
                "version": new_version,
                "last_modified": current_time,
                "security_classification": raw_payload.get("classification", "UNCLASSIFIED")
            },
            "steps": raw_payload.get("steps", []),
            "directory": raw_payload.get("directory", [])
        }
        
        self.library[sop_id] = finalized_node
        return finalized_node

    def duplicate_sop_record(self, source_id, new_target_id):
        """
        Duplicates an existing record to create a new standalone template draft.
        """
        if source_id not in self.library:
            raise KeyError(f"Source file register code '{source_id}' not found.")
            
        source_data = json.loads(json.dumps(self.library[source_id])) # Deep copy
        source_data["sop_id"] = new_target_id
        source_data["title"] = f"Copy of {source_data['title']}"
        source_data["metadata"]["version"] = "1.0"
        source_data["metadata"]["last_modified"] = datetime.datetime.utcnow().isoformat() + "Z"
        
        self.library[new_target_id] = source_data
        return source_data

# Verification Runtime execution test check
mgr = SOPLibraryManager()
initial_payload = {
    "sop_id": "SOP-MNT-104",
    "title": "Abrams Hull Sensor Tuning",
    "classification": "SECRET",
    "steps": ["De-energize chassis batteries.", "Verify interface bus links."]
}

# Save first version (v1.0)
v1 = mgr.save_sop_record(initial_payload)
print(f"Saved: {v1['sop_id']} Version: {v1['metadata']['version']} Timestamp: {v1['metadata']['last_modified']}")

# Save update to trigger automatic version bump (v1.1)
v2 = mgr.save_sop_record(initial_payload)
print(f"Updated: {v2['sop_id']} Version: {v2['metadata']['version']} Timestamp: {v2['metadata']['last_modified']}")

