import common.state as state
import os
from cryptography.hazmat.primitives import serialization
from crypts.crypt_rsa import generate_rsa_keys, rsa_encrypt, rsa_signature
from common.constants import cyan, yellow, reset
from helpers.utils import get_public_key_rsa

def kirim_init_secret_key_mitm():
    pub_b_key = get_public_key_rsa("B")
    pem_string = pub_b_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()
    print(f"{yellow}[INPUT]{reset} User B's public key:\n {pem_string}")

    signature = bytes.fromhex(input(f"{yellow}[INPUT]{reset} Enter signature: "))

    fake_secret_key = os.urandom(32)
    state.shared_secret_key = fake_secret_key
    print(f"\n{yellow}[CREATE]{reset}[Fake Secret Key] {cyan}{fake_secret_key.hex()}{reset}")

    fake_ciphertext = rsa_encrypt(pub_b_key, fake_secret_key)
    print(f"{yellow}[CREATE]{reset}[Fake Ciphertext] {cyan}{fake_ciphertext.hex()}{reset}\n")

    data = {
        "ciphertext": fake_ciphertext.hex(),
        "signature": signature.hex()
    }
    payload = {
        "from": "A",
        "type": "init",
        "to": "B",
        "data": data
    }
    state.sio.emit('send_message', payload)

    print(f"{yellow}[STEP 1]{reset}[MITM] Attacker (C) modifies the initial secret key and forwards it to B.")
    print()
