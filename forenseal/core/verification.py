# function for comparing the hash in the evidence file with the manifest file

import json

from forenseal.core.hashing import hash_file

def verify_file(evidence_path, manifest_path):
    with open(manifest_path, "r") as file:
        record = json.load(file)

    save_hash = record["sha-256"]
    hash = hash_file(evidence_path)

    return hash == save_hash