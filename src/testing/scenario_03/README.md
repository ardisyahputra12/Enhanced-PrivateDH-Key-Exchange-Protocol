# Scenario 3 - MITM Attack Without Authentication


## 📌 Scenario

### Test Steps
1. Assume that the RSA public key of User B has been leaked and is known to the attacker.
2. Temporarily disable the digital signature scheme (RSASSAPSS).
3. Re-execute the MITM attack scenario by modifying the random secret key within the ciphertext sent from User A to User B.
4. Evaluate whether the communication continues without detection.

### Test Data
- User B’s RSA public key
- Original random secret key
- Modified random secret key
- Original ciphertext
- Modified ciphertext

### Expected Result
The attacker successfully inserts themselves into the communication flow, and the session proceeds without detection.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_03/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---
