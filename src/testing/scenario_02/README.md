# Scenario 2 - MITM Attack with Random Secret Key Modification


## 📌 Scenario

### Test Steps
1. Assume that the RSA public key of User B has been leaked and is known to the attacker.
2. User A sends a ciphertext containing a random secret key to User B, along with a digital signature.
3. The attacker intercepts the data and modifies the originalrandom secret key with a new one.
4. The attacker forwards the modified ciphertext and the original signature (unchanged) to User B.
5. User B receives the data and proceeds with the protocol steps, including signature verification.

### Test Data
- User B’s RSA public key
- Original random secret key
- Modified random secret key
- Original ciphertext
- Modified ciphertext
- User A’s original signature
- Attacker’s (unchanged) signature

### Expected Result
Signature verification fails due to data modification, resulting in an invalid signature.
The data is rejected.

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/testing/scenario_02/main.py

Input client username: 
- Client A as **initiator**
- Client B as **responder**
- Client C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

---

## 📖 Documentations

### User A is sending the encrypted initial secret key

![Step 1](/src/testing/scenario_02/docs/s2_pic1.png)

### The attacker modifies the random secret key

![Step 2](/src/testing/scenario_02/docs/s2_pic2.png)

### Signature Verification Failed by User B

![Step 3](/src/testing/scenario_02/docs/s2_pic3.png)
