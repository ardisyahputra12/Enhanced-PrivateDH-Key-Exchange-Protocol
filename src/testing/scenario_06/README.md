# Scenario 6 - Replay Attack


## 📌 Scenario

### Test Steps
1. User A completes a full handshake session with User B, resulting in the establishment of a valid shared session key.
2. The attacker captures all messages exchanged during this session, including the encrypted payloads that contain the exchanged ECDHE public keys.
3. The attacker replays User A’s previously sent ECDHE public key ciphertext to User B in a later session, unchanged.
4. User B receives the ciphertext and attempts to process it, assuming it is part of a valid handshake.

### Test Data
- User A’s ECDHE public key ciphertext from the previous session

### Expected Result
Replayed messages are rejected because the session key changes every time due to ephemeral ECDHE, making old encrypted data unusable.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_06/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---

## 📖 Documentations

### Session 1 shared secret key result

![Step 1](/src/testing/scenario_06/docs/s6_pic1.png)

### Session 2 shared secret key result

![Step 2](/src/testing/scenario_06/docs/s6_pic2.png)

### The attacker replays User A’s previously sent ECDHE public key ciphertext to User B in a later session, unchanged

![Step 3](/src/testing/scenario_06/docs/s6_pic3.png)

### Repeated message rejected, user B failed to decrypt

![Step 3](/src/testing/scenario_06/docs/s6_pic4.png)
