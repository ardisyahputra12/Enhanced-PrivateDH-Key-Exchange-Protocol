# Scenario 4 - MITM Attack with Signature Modification


## 📌 Scenario

### Test Steps
1. Assume that the initial shared key between User A and User B has been compromised and is known to the attacker.
2. User B sends a ciphertext containing a ECDHE public key along with a valid digital signature to User A.
3. The attacker intercepts the data and replaces the original signature with a new signature generated using the attacker’s own private key.
4. The attacker forwards the modified ciphertext and forged signature to User A.
5. User A receives the data and proceeds with signature verification.

### Test Data
- Initial shared key
- Original ciphertext from User B
- Modified ciphertext from attacker
- Original signature from User B
- Forged signature from attacker

### Expected Result
Signature verification fails because the signature does not originate from the legitimate sender. The message is rejected.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_04/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---
