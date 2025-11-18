# =========================================================
# cq-python-0026: JSON Error Handling
# This file includes both violating and compliant examples.
# =========================================================

import json

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Parsing JSON without any exception handling
# ---------------------------------------------------------

raw_data = input("Enter JSON: ")
data = json.loads(raw_data)  # VIOLATION: unhandled JSON errors
print("Parsed (VIOLATION):", data)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Dumping JSON without catching serialization errors
# ---------------------------------------------------------

obj = {"name": "Alice", "time": set([1, 2, 3])}  # sets are not JSON-serializable
json_string = json.dumps(obj)  # VIOLATION
print("Dumped JSON (VIOLATION):", json_string)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Handling json.loads() errors safely
# ---------------------------------------------------------

safe_raw = input("\nEnter JSON safely: ")

try:
    safe_data = json.loads(safe_raw)
    print("Parsed safely:", safe_data)
except json.JSONDecodeError:
    print("Invalid JSON provided!")
except Exception as e:
    print("Unexpected error:", e)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using safe serialization with error handling
# ---------------------------------------------------------

safe_obj = {"name": "Bob", "scores": [10, 20]}

try:
    safe_json_string = json.dumps(safe_obj)
    print("Serialized safely:", safe_json_string)
except (TypeError, ValueError) as e:
    print("Serialization error:", e)
