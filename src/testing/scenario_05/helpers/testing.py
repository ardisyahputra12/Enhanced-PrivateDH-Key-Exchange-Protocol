import common.state as state
from cryptography.hazmat.primitives import serialization
from crypts.crypt_dh import compute_shared_secret_ecdh, generate_ecdh_keypair, serialize_public_key
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

    # ========= START Scenario 05 =========
    state.ecdhe_private, public_key = generate_ecdh_keypair()
    fake_public_key = serialize_public_key(public_key)
    fake_ecdhe_private = state.ecdhe_private.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption()
    )
    print(f"{yellow}[CREATE]{reset}[Fake ECDHE Public key] {cyan}{fake_public_key.hex()}{reset}")
    print(f"{yellow}[CREATE]{reset}[Fake ECDHE Private key] {cyan}{fake_ecdhe_private.hex()}{reset}")
    # ========= END Scenario 05 =========

    tampered_plaintext = fake_public_key + peer_signature
    tampered_ciphertext = aes_encrypt_gcm(shared_secret_key, tampered_plaintext)
    print(f"{yellow}[CREATE]{reset}[Fake Ciphertext] {cyan}{tampered_ciphertext.hex()}{reset}\n")

    payload = {
        "from": "B",
        "type": "ecdhe",
        "to": "A",
        "data": { "ciphertext": tampered_ciphertext.hex() }
    }
    state.sio.emit('send_message', payload)

    print(f"{yellow}[STEP 2]{reset}[MITM] Attacker (C) modifies the ECDHE public key and forwards it to A.")
    print()
