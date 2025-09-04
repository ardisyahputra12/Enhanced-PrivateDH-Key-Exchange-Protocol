import socketio
import psutil
import os

# ========== MAIN ==========
sio = socketio.Client()
process = psutil.Process(os.getpid())
user_id = None
run_status = True
shared_secret_key = None
ecdhe_private = None

# ========== RSA ==========
private_key_rsa = None
public_key_rsa = None
pem_public_key_rsa = None

# ========== COUNTER ==========
start_cpu = None
total_start_time = None
step_2_start_time = None
step_3_start_time = None
step_4_start_time = None
step_5_start_time = None
