import common.state as state
import time
from crypts.crypt_rsa import rsa_decrypt, rsa_verify
from helpers.testing import kirim_init_secret_key_mitm
from sender.send_ecdhe import kirim_public_key_ecdhe
from helpers.utils import get_public_key_rsa, runtime, exit_program
from common.constants import yellow, cyan, red, reset

def receive_init(data):
    ciphertext = bytes.fromhex(data["data"]["ciphertext"])
    recipient = "A" if state.user_id == "B" else "B"

    # ======== START - Scenario 02 (MITM) ========
    if state.user_id == "C":
        print(f"{yellow}[STEP 1]{reset}[KEY] Secret key awal dari A diterima oleh C")
        kirim_init_secret_key_mitm()
    else:
    # ======== END - Scenario 02 (MITM) ========

        print(f"{yellow}[STEP 1]{reset}[KEY] Initial secret key from {recipient} is received by {state.user_id}")
        state.step_3_start_time = time.perf_counter()
        try:
            # ======== START - Scenario 03 (MITM) ========
            secret_key = rsa_decrypt(state.private_key_rsa, ciphertext)
            state.shared_secret_key = secret_key
            print(f"{yellow}[STEP 1]{reset}[KEY] {cyan}{state.shared_secret_key.hex()}{reset}")
            print(f"{yellow}[STEP 1]{reset}[KEY] Initial shared secret key successfully stored")
            print()
            # ======== END - Scenario 03 (MITM) ========
            
            if state.user_id == "B": kirim_public_key_ecdhe()
        except Exception as e:
            print(f"\n{yellow}[STEP 1]{reset}{red}[FAIL]{reset} Failure occurred:", e, "\n")
            exit_program()
