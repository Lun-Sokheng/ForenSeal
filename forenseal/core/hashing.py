# function to hash the file to sha-256

import hashlib

def hash_file(path):
    sha256_hash = hashlib.sha256()

    with open(path, "rb") as file:
        while True:
            chunk = file.read(64*1024)

            # if no more byte then break from function
            if not chunk:
                break
            sha256_hash.update(chunk)

    return sha256_hash.hexdigest()