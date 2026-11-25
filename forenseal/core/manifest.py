# for creating manifest file

import json
from pathlib import Path
from datetime import datetime, timezone

def save_manifest(evidence_path, fingerprint, manifest_path, evidence_id, case_id, collector):

    evidence = Path(evidence_path)
    record = {
        "case_id" : case_id,
        "evidence_id" : evidence_id,
        "collector" : collector,
        "path" : evidence.name,
        "sha-256" : fingerprint,
        "size_bytes" : evidence.stat().st_size,
        "record_utc" : datetime.now(timezone.utc).isoformat(timespec="seconds")
    }

    with open(manifest_path, "x") as file:
        # indent make the file easier to read 4 space infront of every field
        json.dump(record, file, indent=4)