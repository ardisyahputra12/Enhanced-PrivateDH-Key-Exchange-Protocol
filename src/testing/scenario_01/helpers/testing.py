from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)
from crypts.crypt_dh import compute_shared_secret_ecdh
from common.constants import cyan, yellow, reset

def ecdhe_attack():
    print("\n===== ECDHE primary private key compromise scenario =====")
    ecdhe_private = X25519PrivateKey.from_private_bytes(bytes.fromhex(input(f"{yellow}[INPUT]{reset} Enter ECDHE private (A): ")))
    peer_public_key = X25519PublicKey.from_public_bytes(bytes.fromhex(input(f"{yellow}[INPUT]{reset} Enter peer's public key (B): ")))
    shared_secret = compute_shared_secret_ecdh(ecdhe_private, peer_public_key)
    print(f"Shared secret: {cyan}{shared_secret.hex()}{reset}")
