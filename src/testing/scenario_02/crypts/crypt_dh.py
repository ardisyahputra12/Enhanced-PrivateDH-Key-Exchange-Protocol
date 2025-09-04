from cryptography.hazmat.primitives.asymmetric.x25519 import (
    X25519PrivateKey, X25519PublicKey
)
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization, hashes


def generate_ecdh_keypair():
    private_key = X25519PrivateKey.generate()
    public_key = private_key.public_key()
    return private_key, public_key

def compute_shared_secret_ecdh(
        private_key: X25519PrivateKey,
        peer_public_key: X25519PublicKey
    ) -> bytes:
    return private_key.exchange(peer_public_key)

def derive_symmetric_key(
        shared_secret: bytes,
        salt: bytes,
        length: int = 32
    ) -> bytes:
    return HKDF(
        algorithm=hashes.SHA256(),
        length=length,
        salt=salt,
        info=b"Session Key for PrivateDH",
    ).derive(shared_secret)

def serialize_public_key(public_key: X25519PublicKey) -> bytes:
    return public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw
    )

def deserialize_public_key(raw_bytes: bytes) -> X25519PublicKey:
    return X25519PublicKey.from_public_bytes(raw_bytes)
