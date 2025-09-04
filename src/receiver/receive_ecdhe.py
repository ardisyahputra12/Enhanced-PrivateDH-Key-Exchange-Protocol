import common.state as state
import time
from crypts.crypt_rsa import rsa_signature, rsa_verify
from crypts.crypt_aes import aes_encrypt_gcm, aes_decrypt_gcm
from crypts.crypt_dh import compute_shared_secret_ecdh, deserialize_public_key, derive_symmetric_key
from sender.send_ecdhe import kirim_public_key_ecdhe
from sender.send_msg import send_msg
from helpers.utils import get_public_key_rsa, runtime, exit_program
from common.constants import yellow, cyan, green, red, reset

def receive_ecdhe(data):
    ciphertext = bytes.fromhex(data["data"]["ciphertext"])
    sender_pubkey = get_public_key_rsa(data["from"])
    recipient = "A" if state.user_id == "B" else "B"
    print(f"{yellow}[STEP 2]{reset}[ECDHE] ECDHE public key from {recipient} is received by {state.user_id}")

    try:
        plaintext = aes_decrypt_gcm(state.shared_secret_key, ciphertext)
        peer_public_key = plaintext[:-256]
        peer_signature = plaintext[-256:]
        verify_signature = rsa_verify(sender_pubkey, peer_public_key, peer_signature)
        if not verify_signature:
            state.run_status = False
            print(f"{red}[PROGRAM]{reset} Key exchange failed. Exit.")
            return
        else:
            print(f"{yellow}[STEP 2]{reset}[KEY] ECDHE public key from {recipient} has been successfully verified: {cyan}{peer_public_key.hex()}{reset}")
            print()
            if state.user_id == "A": kirim_public_key_ecdhe()

        state.step_5_start_time = time.perf_counter()
        peer_key = deserialize_public_key(peer_public_key)
        shared_secret = compute_shared_secret_ecdh(state.ecdhe_private, peer_key)
        shared_secret_hkdf = derive_symmetric_key(shared_secret, state.shared_secret_key)
        state.shared_secret_key = shared_secret_hkdf
        print(f"{yellow}[STEP 3]{reset}[KEY] Final shared secret key successfully calculated: {cyan}{shared_secret.hex()}{reset}")
        print(f"{yellow}[STEP 3]{reset}[KEY][HKDF] {cyan}{shared_secret_hkdf.hex()}{reset}")

        # delete ecdhe private key
        del state.ecdhe_private

        print(f"{yellow}[STEP 3]{reset}[KEY] ECDHE private key is deleted")
        print()

        print(f"{green}[PROGRAM]{reset} Key exchange process completed.")
        exit_program()
        print()
        send_msg()

    except Exception as e:
        print(f"\n{yellow}[STEP 2]{reset}{red}[FAIL]{reset} Failure of the ECDHE exchange process:", e, "\n")
        exit_program()
