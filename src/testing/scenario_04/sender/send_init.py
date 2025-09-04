import common.state as state
import time
import os
from crypts.crypt_rsa import rsa_encrypt, rsa_signature
from helpers.utils import get_public_key_rsa, runtime
from common.constants import yellow, cyan, reset

def kirim_secret_key():
    if state.user_id != "A": return

    state.step_3_start_time = time.perf_counter()
    secret_key = os.urandom(32)
    state.shared_secret_key = secret_key
    signature = rsa_signature(state.private_key_rsa, secret_key)

    pub_b_key = get_public_key_rsa("B")
    ciphertext = rsa_encrypt(pub_b_key, secret_key)

    data = {
        "ciphertext": ciphertext.hex(),
        "signature": signature.hex()
    }

    payload = {
        "from": "A",
        "type": "init",
        "to": "B",
        "data": data
    }

    state.sio.emit('send_message', payload)
    print(f"{yellow}[STEP 1]{reset}[KEY] {cyan}{state.shared_secret_key.hex()}{reset}")
    print(f"{yellow}[STEP 1]{reset}[DATA] {data}")
    print(f"{yellow}[STEP 1]{reset}[SEND] Initial secret key is sent to B")
    print()
