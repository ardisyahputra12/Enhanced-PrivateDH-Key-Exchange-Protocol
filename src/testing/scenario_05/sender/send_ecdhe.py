import common.state as state
import time
from cryptography.hazmat.primitives import serialization
from crypts.crypt_rsa import generate_rsa_keys, rsa_signature
from crypts.crypt_aes import aes_encrypt_gcm, aes_decrypt_gcm
from crypts.crypt_dh import generate_ecdh_keypair, serialize_public_key
from common.constants import yellow, cyan, reset

def kirim_public_key_ecdhe():
    state.step_4_start_time = time.perf_counter()
    state.ecdhe_private, public_key = generate_ecdh_keypair()
    raw_public_key = serialize_public_key(public_key)

    raw_ecdhe_private = state.ecdhe_private.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    print(f"{yellow}[STEP 2]{reset}[KEY] ECDHE Public key: {cyan}{raw_public_key.hex()}{reset}")
    print(f"{yellow}[STEP 2]{reset}[KEY] ECDHE Private key: {cyan}{raw_ecdhe_private.hex()}{reset}")

    signature = rsa_signature(state.private_key_rsa, raw_public_key)
    payload_plain = raw_public_key + signature
    encrypt_data = aes_encrypt_gcm(state.shared_secret_key, payload_plain)

    recipient = "A" if state.user_id == "B" else "B"
    data = { "ciphertext": encrypt_data.hex() }

    # ======== START - Scenario 05 (MITM) ========
    to = "C" if state.user_id == "B" else "B"
    payload = {
        "from": state.user_id,
        "type": "ecdhe",
        "to": to,
        "data": data
    }
    state.sio.emit('send_message', payload)
    # ======== END - Scenario 05 (MITM) ========

    print(f"{yellow}[STEP 2]{reset}[DATA] {data}")
    print(f"{yellow}[STEP 2]{reset}[SEND] ECDHE public key is sent to {recipient}")
    print()
