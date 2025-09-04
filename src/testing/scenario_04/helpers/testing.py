import common.state as state
from crypts.crypt_rsa import generate_rsa_keys, rsa_encrypt, rsa_signature
from crypts.crypt_aes import aes_encrypt_gcm, aes_decrypt_gcm
from common.constants import cyan, yellow, reset

def kirim_public_key_ecdhe_mitm():
    shared_secret_key = bytes.fromhex(input(f"{yellow}[INPUT]{reset} Enter shared secret key: "))
    ciphertext = bytes.fromhex(input(f"{yellow}[INPUT]{reset} Enter ciphertext: "))
    plaintext = aes_decrypt_gcm(shared_secret_key, ciphertext)
    peer_public_key = plaintext[:-256]
    peer_signature = plaintext[-256:]
    print(f"\n{yellow}[READ][Peer Public Key]{reset} {peer_public_key.hex()}")
    print(f"{yellow}[READ][Peer Signature]{reset} {peer_signature.hex()}\n")

    # ========= START SCENARIO 04 =========
    fake_signature = rsa_signature(state.private_key_rsa, peer_public_key)
    print(f"{yellow}[CREATE]{reset}[Fake Signature] {cyan}{fake_signature.hex()}{reset}")
    # ========= END SCENARIO 04 =========

    tampered_plaintext = peer_public_key + fake_signature
    tampered_ciphertext = aes_encrypt_gcm(shared_secret_key, tampered_plaintext)
    print(f"{yellow}[CREATE]{reset}[Fake Ciphertext] {cyan}{tampered_ciphertext.hex()}{reset}\n")

    payload = {
        "from": "B",
        "type": "ecdhe",
        "to": "A",
        "data": { "ciphertext": tampered_ciphertext.hex() }
    }
    state.sio.emit('send_message', payload)

    print(f"{yellow}[STEP 2]{reset}[MITM] Attacker (C) modifies the signature and forwards it to A.")
    print()
