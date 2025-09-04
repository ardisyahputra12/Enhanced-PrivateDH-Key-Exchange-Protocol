# Enhanced PrivateDH Key Exchange Protocol


## 📌 Overview
This project is a Python-based implementation of a **secure key exchange protocol**.  
It extends the baseline **Private Diffie–Hellman (PrivateDH)** scheme by integrating:
- **ECDHE Curve25519** for efficient forward secrecy,
- **RSASSA-PSS (RSA-2048)** for endpoint authentication,
- **AES-256** for symmetric encryption.

The protocol is designed to provide stronger security guarantees and better performance in modern deployment scenarios, while keeping both endpoints (Client A and Client B) lightweight. The server acts only as a relay for exchanging RSA public keys.

---

## 🚀 Features
- Mutual authentication using **RSASSA-PSS**  
- Ephemeral key agreement with **ECDHE Curve25519**  
- Secure message exchange using **AES-256**  
- Resistance to **MITM** and replay attacks  
- Measurements for **runtime, CPU, and memory usage**

---

## 🔧 Installation
1. Clone this repository:
    ```
    git clone https://github.com/ardisyahputra12/Enhanced-PrivateDH-Key-Exchange-Protocol.git
    cd Enhanced-PrivateDH-Key-Exchange-Protocol
    ```
2. Create a virtual environment and install dependencies:
    ```
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    
    pip install -r requirements.txt
    ```

---

## ▶️ Usage
Run the relay server:

    python src/server.py

Start Client:

    python src/main.py

Input client username: 
- A as **initiator**
- B as **responder**
- C as **attacker**

Execution order:

`Server` > `Attacker` > `Responder` > `Initiator`

Both clients (Client A and B) will perform a secure handshake and establish a shared secret key for further communication.

***execute `Attacker` if you want to perform a test**

---

## 🛡️ Security Testing
Attack simulations are included to verify resilience against common threats:

- [Compromise of the Main ECDHE Private Key](/src/testing/scenario_01)

- [MITM Attack with Random Secret Key Modification](/src/testing/scenario_02)
- [MITM Attack Without Authentication](/src/testing/scenario_03)
- [MITM Attack with Signature Modification](/src/testing/scenario_04)
- [MITM Attack with Modification of the ECDHE Public Key](/src/testing/scenario_05)
- [Replay Attack](/src/testing/scenario_06)

---

## 📖 Documentations

### Step 1. Generating the Initial Shared Secret Key

![Step 1](/docs/step-1.png)

### Step 2. Exchanging ECDHE Public Keys

![Step 2](/docs/step-2.png)

### Step 3. Generating the Final Shared Secret Key

![Step 3](/docs/step-3.png)

### Step 4. Shared Secret Key

![Step 4](/docs/step-4.png)
