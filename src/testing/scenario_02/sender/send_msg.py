import common.state as state
from crypts.crypt_rsa import rsa_signature
from crypts.crypt_aes import aes_encrypt_gcm
from common.constants import yellow, cyan, reset

def send_msg():
    message = input(f"{yellow}[MESSAGE]{reset}{cyan}[{state.user_id}]{reset} Enter Message: ")
    if message:
        message = message.encode()
        signature = rsa_signature(state.private_key_rsa, message)
        payload_plain = message + signature
        encrypt_data = aes_encrypt_gcm(state.shared_secret_key, payload_plain)

        recipient = "A" if state.user_id == "B" else "B"
        data = { "ciphertext": encrypt_data.hex() }
        payload = {
            "from": state.user_id,
            "type": "msg",
            "to": recipient,
            "data": data
        }
        state.sio.emit('send_message', payload)
        send_msg()
