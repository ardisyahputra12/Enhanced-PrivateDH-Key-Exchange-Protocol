import common.state as state
from crypts.crypt_rsa import rsa_verify
from crypts.crypt_aes import aes_decrypt_gcm
from sender.send_msg import send_msg
from helpers.utils import get_public_key_rsa, exit_program
from common.constants import yellow, cyan, red, reset

def receive_msg(data):
    ciphertext = bytes.fromhex(data["data"]["ciphertext"])
    sender_pubkey = get_public_key_rsa(data["from"])
    recipient = "A" if state.user_id == "B" else "B"

    try:
        plaintext = aes_decrypt_gcm(state.shared_secret_key, ciphertext)
        message = plaintext[:-256]
        peer_signature = plaintext[-256:]
        verify_signature = rsa_verify(sender_pubkey, message, peer_signature, True)
        if not verify_signature:
            state.run_status = False
            print(f"{red}[PROGRAM]{reset} Key exchange process failed. Exit.")
            return
        else:
            print()
            print(f"{yellow}[MESSAGE]{reset}{cyan}[{recipient}]{reset} {message.decode()}")
            print(">>> Press Enter.")
        send_msg()
    except Exception as e:
        print(f"\n{yellow}[STEP 4]{reset}{cyan}[MESSAGE]{reset}{red}[FAIL]{reset} Message failed to load:", e, "\n")
        exit_program()
