import common.state as state
import requests
import time
from cryptography.hazmat.primitives import serialization
from common.constants import server, yellow, green, red, reset

def get_public_key_rsa(user_id):
    response = requests.get(f"{server}/get_key/{user_id}")
    if response.status_code != 200:
        print(f"\n{red}[ERROR]{reset} Public key retrieval failed {user_id}:", response.json(), "\n")
        exit_program()

    pub_data = response.json()
    pub_key = pub_data.get("public_key")
    if not pub_key:
        print(f"\n{red}[ERROR]{reset} The response is missing the 'public_key' field:", pub_data, "\n")
        exit_program()

    pub_key_rsa = serialization.load_pem_public_key(pub_key.encode())
    return pub_key_rsa

def get_time(elapsed):
    detik = int(elapsed)
    milidetik = int((elapsed - detik) * 1000)
    mikrodetik = int(((elapsed - detik) * 1_000_000) % 1000)
    return detik, milidetik, mikrodetik

def runtime(step, start, end):
    elapsed = end - start
    detik, milidetik, mikrodetik = get_time(elapsed)
    print(f"{green}[TIME]{reset}{yellow}[STEP {step}]{reset} Runtime: {green}{detik}s {milidetik}ms {mikrodetik}μs{reset}\n")

def exit_program():
    # Set status to "False" to stop program
    # state.run_status = False

    total_end_time = time.perf_counter()
    print("="*30)
    if state.user_id == "A": runtime("2-5", state.step_2_start_time, total_end_time)
    else: runtime("3-5", state.step_3_start_time, total_end_time)

    end_cpu = state.process.cpu_times()
    mem_used = state.process.memory_info().rss / (1024 * 1024)  # in MB
    cpu_percent = state.process.cpu_percent(interval=None)
    print(f"{green}[CPU]{reset} CPU usage percentage: {green}{cpu_percent:.2f}%{reset}")
    user_cpu = end_cpu.user - state.start_cpu.user
    us_detik, us_milidetik, us_mikrodetik = get_time(user_cpu)
    print(f"{green}[TIME]{reset}{yellow}[CPU]{reset} User: {green}{us_detik}s {us_milidetik}ms {us_mikrodetik}μs{reset}")
    system_cpu = end_cpu.system - state.start_cpu.system
    sy_detik, sy_milidetik, sy_mikrodetik = get_time(system_cpu)
    print(f"{green}[TIME]{reset}{yellow}[CPU]{reset} System: {green}{sy_detik}s {sy_milidetik}ms {sy_mikrodetik}μs{reset}")
    print(f"{green}[MEMORY]{reset} Memory usage: {green}{mem_used:.2f} MB{reset}")
    print("==============================")
