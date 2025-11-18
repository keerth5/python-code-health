# =========================================================
# cq-python-0030: Secure Password Hashing
# This file contains both violating and compliant examples.
# =========================================================

import hashlib
from werkzeug.security import generate_password_hash, check_password_hash

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Storing passwords in plain text
# ---------------------------------------------------------

def store_password_plain(password):  # VIOLATION
    print("Storing password (PLAIN TEXT):", password)  # Not secure
    return password

store_password_plain("mySecret123")


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using weak hashing algorithms like MD5 or SHA1
# ---------------------------------------------------------

def store_password_md5(password):  # VIOLATION
    hashed = hashlib.md5(password.encode()).hexdigest()
    print("MD5 Hashed Password (VIOLATION):", hashed)
    return hashed

store_password_md5("mySecret123")


def store_password_sha1(password):  # VIOLATION
    hashed = hashlib.sha1(password.encode()).hexdigest()
    print("SHA1 Hashed Password (VIOLATION):", hashed)
    return hashed

store_password_sha1("mySecret123")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using PBKDF2 with Werkzeug (recommended)
# ---------------------------------------------------------

def store_password_secure(password):
    hashed = generate_password_hash(password, method="pbkdf2:sha256", salt_length=16)
    print("\nSecure PBKDF2 Hashed Password (COMPLIANT):", hashed)
    return hashed

secure_hash = store_password_secure("mySecret123")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Verifying passwords securely
# ---------------------------------------------------------

def verify_password(stored_hash, password):
    if check_password_hash(stored_hash, password):
        print("Password verified successfully.")
    else:
        print("Password verification failed.")

verify_password(secure_hash, "mySecret123")
