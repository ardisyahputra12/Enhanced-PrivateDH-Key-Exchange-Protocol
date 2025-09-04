import common.state as state
from common.constants import yellow, reset

def replay_ciphertext():
    print("===== Replay attack =====")
    cipher = input(f"{yellow}[INPUT]{reset} Enter ciphertext: ")
    data = { "ciphertext": cipher }
    payload = {
        "from": "A",
        "type": "ecdhe",
        "to": "B",
        "data": data
    }
    state.sio.emit('send_message', payload)
    print(f"{yellow}[STEP 2]{reset}[SEND] Ciphertext has been sent to B")
