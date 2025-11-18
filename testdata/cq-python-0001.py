# ============================================
# cq-python-0001: No Pickle Loads
# This file contains both violating and compliant examples.
# ============================================

import pickle
import base64

# ------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Direct pickle.loads() on untrusted user input
# ------------------------------------------------
user_input = input("Paste serialized data: ")

try:
    data = pickle.loads(user_input.encode())  # VIOLATION: Unsafe deserialization
    print("Deserialized:", data)
except Exception:
    print("Deserialization failed")


# ------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Base64-decoded user data still fed into pickle.loads()
# ------------------------------------------------
encoded_input = input("Enter base64 encoded pickle string: ")

try:
    raw_bytes = base64.b64decode(encoded_input)
    data2 = pickle.loads(raw_bytes)  # VIOLATION
    print("Decoded:", data2)
except Exception:
    print("Unsafe input detected")


# ------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using json.loads() for safe data interchange
# ------------------------------------------------
import json

json_input = input("Enter JSON data (safe): ")

try:
    obj = json.loads(json_input)  # SAFE alternative to pickle
    print("JSON parsed:", obj)
except json.JSONDecodeError:
    print("Invalid JSON")


# ------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using safe, custom whitelist parser instead of pickle
# ------------------------------------------------
def safe_deserialize(data: str):
    """
    SAFE: Only accept integers or lists of integers.
    A realistic safe deserialization alternative.
    """
    try:
        parsed = json.loads(data)
        if isinstance(parsed, int):
            return parsed
        if isinstance(parsed, list) and all(isinstance(i, int) for i in parsed):
            return parsed
    except Exception:
        pass

    return None

safe_data = safe_deserialize("[1, 2, 3]")
print("Safely deserialized:", safe_data)
