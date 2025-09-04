from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

rsa_keys = {}
connected_clients = {}

# ========== ANSI color codes ==========
YELLOW = "\033[93m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

@app.route('/register_key', methods=['POST'])
def register_key():
    data = request.get_json()
    rsa_keys[data['user_id']] = data['public_key']
    print(f'{YELLOW}[STEP 2]{RESET}[RSA KEYS] {rsa_keys}\n')
    return jsonify({'status': 'success', 'message': 'RSA public key is stored'})

@app.route('/get_key/<user_id>', methods=['GET'])
def get_key(user_id):
    if user_id not in rsa_keys:
        return jsonify({'status': 'error', 'message': 'Public key not found'}), 404
    return jsonify({'status': 'success', 'public_key': rsa_keys[user_id]})

@socketio.on('register')
def handle_register(data):
    user_id = data.get('user_id')
    if user_id:
        connected_clients[user_id] = request.sid
        join_room(user_id)
        print(f"\n{YELLOW}[STEP 2]{RESET} {user_id} connected with SID {request.sid}")
        print(f"{YELLOW}[STEP 2]{RESET}[CLIENTS] {connected_clients}")

@socketio.on('send_message')
def handle_send_message(data):
    recipient = data.get('to')
    if recipient in connected_clients:
        emit('receive_message', data, room=recipient)
        print(f"\n{GREEN}[SERVER]{RESET} Message from {data.get('from')} to {recipient} has been sent.\n")
    else:
        print(f"\n{RED}[SERVER]{RESET} Recipient {recipient} is not connected.\n")

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
