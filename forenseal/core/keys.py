from getpass import getpass
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

password = getpass("Create password for your private key :")
if not password:
    raise SystemExit("Please enter a password to protect your private key.")

def generate_keys():

    # create private & public key
    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    # format to store and load key to use for later
    private_key_data = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.BestAvailableEncryption(password.encode("utf-8")))
    public_key_data = public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

    key_folder = Path("keys")/"collector"
    key_folder.mkdir(parents=True, exist_ok=False)

    (key_folder/"private_key.pem").write_bytes(private_key_data)
    (key_folder/"public_key.pem").write_bytes(public_key_data)

    print("Keys pair generated successfully")