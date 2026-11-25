from forenseal.core.hashing import hash_file
from forenseal.core.manifest import save_manifest
from forenseal.core.verification import verify_file

path = "sample_evidence/example.txt"
manifest_path = path + ".manifest.json"

try:

    case_id = input("Enter case id : ").strip()
    evidence_id = input("Enter evidence id : ").strip()
    collector = input("Enter collector name : ").strip()

    if case_id and evidence_id and collector:
        manifest_path = path + ".manifest.json"
        fingerprint = hash_file(path)
        print("ForenSeal - Evidence Fingerprint")
        print("File :", path)
        print("SHA-256 :", fingerprint)
        save_manifest(path, fingerprint, manifest_path, case_id, evidence_id, collector)
        print("Manifest saved :", manifest_path)
    else:
        print("Please enter case-id, evidence-id and collector name")

    result = verify_file(path, manifest_path)
    print(result)
    
except OSError as err:
    print(err)

