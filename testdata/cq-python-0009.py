# =========================================================
# cq-python-0009: NoSQL Injection Prevention
# This file contains both violating and compliant examples.
# =========================================================

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sample_db"]
users_collection = db["users"]

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Directly injecting user-controlled query fields
# ---------------------------------------------------------

user_input = input("Enter username: ")

# Dangerous: attacker can supply {"$gt": ""} to dump all records
query = {"username": user_input}   # When used directly, it becomes injection-prone

result = users_collection.find(query)  # VIOLATION
print("User Records (VIOLATION):")
for r in result:
    print(r)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Dynamically building NoSQL query strings
# ---------------------------------------------------------

field = input("Field to search: ")      # e.g., "username"
value = input("Value to search: ")      # e.g., {"$ne": null}

# Direct dictionary concatenation from user input → injection
dangerous_query = {field: value}        # VIOLATION
print("Executing Dangerous Query:", dangerous_query)
unsafe_results = users_collection.find(dangerous_query)

for r in unsafe_results:
    print(r)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Validate & whitelist allowed fields
# ---------------------------------------------------------

allowed_fields = ["username", "email"]

safe_field = input("Search by (username/email): ").strip()
safe_value = input("Enter value: ").strip()

if safe_field not in allowed_fields:
    raise ValueError("Invalid field")

safe_query = {safe_field: safe_value}   # Safe because field is validated
print("\nExecuting Safe Query:", safe_query)

safe_results = users_collection.find(safe_query)
for r in safe_results:
    print(r)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using parameterized / structured filters only
# ---------------------------------------------------------

search_username = input("Enter username to lookup safely: ").strip()

# Structured and limited → safe
safe_param_query = {"username": {"$eq": search_username}}

print("\nExecuting Parameterized Safe Query:", safe_param_query)

safe_param_results = users_collection.find(safe_param_query)
for r in safe_param_results:
    print(r)
