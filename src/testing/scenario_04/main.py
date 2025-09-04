import time
import common.state as state
from crypts.crypt_rsa import generate_rsa_keys
from sender.send_init import kirim_secret_key
from receiver.receive_init import receive_init
from receiver.receive_ecdhe import receive_ecdhe
from receiver.receive_msg import receive_msg
from helpers.connect import connect
from helpers.utils import exit_program
from common.constants import socket, red, reset

state.user_id = input("Enter your name: ")
state.private_key_rsa, state.public_key_rsa, state.pem_public_key_rsa = generate_rsa_keys(state.user_id)
pem_public_key_rsa = state.pem_public_key_rsa.decode('utf-8')

@state.sio.on('connect')
def on_connect(): connect(pem_public_key_rsa)

@state.sio.on('receive_message')
def on_receive(data):
    msg_type = data.get("type", "init")
    if msg_type == "init": receive_init(data)
    elif msg_type == "ecdhe": receive_ecdhe(data)
    elif msg_type == "msg": receive_msg(data)
    else:
        print(f"\n{red}[ERROR]{reset} Unrecognized message type:", msg_type, "\n")
        exit_program()

def main():
    state.sio.connect(socket)
    kirim_secret_key()
    while state.run_status: time.sleep(1)

if __name__ == '__main__': main()
