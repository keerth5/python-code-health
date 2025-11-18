# =========================================================
# cq-python-0036: Cryptographic Random
# This file includes both violating and compliant examples.
# =========================================================

import random
import secrets
import os


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using random.randint() for security-sensitive token generation
# ---------------------------------------------------------

def generate_insecure_token():
    # VIOLATION: random is not cryptographically secure
    token = str(random.randint(100000, 999999))
    return token

print("Insecure Token (VIOLATION):", generate_insecure_token())


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using random.choice() for password generation
# ---------------------------------------------------------

def generate_insecure_password():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    # VIOLATION: predictable random
    pwd = ''.join(random.choice(chars) for _ in range(10))
    return pwd

print("Insecure Password (VIOLATION):", generate_insecure_password())


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using secrets.token_hex() for cryptographic-safe tokens
# ---------------------------------------------------------

def generate_secure_token():
    return secrets.token_hex(16)  # Secure

print("Secure Token:", generate_secure_token())


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using os.urandom() for cryptographically safe random bytes
# ---------------------------------------------------------

def generate_secure_password():
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    pwd = ''.join(chars[b % len(chars)] for b in os.urandom(12))
    return pwd

print("Secure Password:", generate_secure_password())
