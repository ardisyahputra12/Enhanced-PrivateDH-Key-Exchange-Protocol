import common.state as state
import requests
import time
from helpers.testing import replay_ciphertext
from common.constants import server

def connect(pem_public_key_rsa):
    state.step_2_start_time = time.perf_counter()
    state.start_cpu = state.process.cpu_times()
    state.process.cpu_percent(interval=None)
    time.sleep(0.2)

    state.sio.emit('register', {'user_id': state.user_id})
    print(f"\nConnected to server as {state.user_id}\n")

    requests.post(
        f"{server}/register_key",
        json={
            "user_id": state.user_id,
            "public_key": pem_public_key_rsa
        }
    )

    # ======== START - Scenario 06 (Replay) ========
    if state.user_id == "C": replay_ciphertext()
    # ======== END - Scenario 06 (Replay) ========
