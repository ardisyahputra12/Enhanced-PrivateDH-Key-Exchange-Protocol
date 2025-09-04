# Scenario 1 - Compromise of the Main ECDHE Private Key


## 📌 Scenario

### Test Steps
1. User A and User B perform a full key exchange using the protocol.
2. Simulate a key compromise by exposing the long-term ECDHE private key of User A.
3. Attempt to regenerate the original shared key using only the public key of User B from the new session and the compromised private key of User A, assuming the context of a previous session.
4. Compare the newly computed shared key with the original shared key.

### Test Data
- User A’s private key
- User B’s public key
- Original session shared key
- Newly computed shared key

### Expected Result
It is not possible to reconstruct the original shared key without the ephemeral private key used during the actual session. Forward secrecy is verified.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_01/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---
