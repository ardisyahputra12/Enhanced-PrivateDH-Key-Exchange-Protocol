# Scenario 5 - MITM Attack with Modification of the ECDHE Public Key


## 📌 Scenario

### Test Steps
1. Assume that the initial shared key has been compromised and is known to the attacker.
2. User B sends a ciphertext containing their ECDHE public key along with a digital signature to User A.
3. The attacker intercepts the message and replaces User B’s ECDHE public key with their own ECDHE public key.
4. The attacker forwards the modified ciphertext, still containing User B’s original signature, to User A.
5. User A receives the data and performs signature verification.

### Test Data
- Initial shared key
- User B’s original ECDHE public key
- Attacker’s ECDHE public key
- Originalciphertext
- Modified ciphertext
- User B’s original signature

### Expected Result
Signature verification fails due to data modification causing signature mismatch. The data is rejected.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_05/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---
