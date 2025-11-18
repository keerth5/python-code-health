# =========================================================
# cq-python-0020: Secure Random Numbers
# This file contains both violating and compliant examples.
# =========================================================

import random
import secrets

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using random.randint() for security-sensitive token
# ---------------------------------------------------------

def generate_insecure_token():
    token = random.randint(100000, 999999)  # VIOLATION
    print("[Violation] Insecure token generated:", token)
    return token

generate_insecure_token()


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using random.choice() for password generation
# ---------------------------------------------------------

def insecure_password():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    pwd = "".join(random.choice(chars) for _ in range(8))  # VIOLATION
    print("[Violation] Insecure password:", pwd)
    return pwd

insecure_password()


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using secrets.token_hex()
# ---------------------------------------------------------

def secure_token():
    token = secrets.token_hex(16)  # SECURE
    print("[Compliant] Secure token:", token)
    return token

secure_token()


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using secrets.choice() for password generation
# ---------------------------------------------------------

def secure_password():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    pwd = "".join(secrets.choice(chars) for _ in range(12))  # SECURE
    print("[Compliant] Secure password:", pwd)
    return pwd

secure_password()
