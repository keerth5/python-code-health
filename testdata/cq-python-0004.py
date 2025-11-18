# ============================================================
# cq-python-0004: No Hardcoded Secrets
# This file contains both violating and compliant examples.
# ============================================================

import os


# ------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Hardcoded password in source code
# ------------------------------------------------------------
DB_PASSWORD = "SuperSecret123!"  # VIOLATION: Hardcoded credential

def connect_to_database():
    print("Connecting to database with password:", DB_PASSWORD)  # Unsafe use
connect_to_database()


# ------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Hardcoded API key for external service
# ------------------------------------------------------------
API_KEY = "AIzaSyD3fke93hfEXAMPLEKEY"  # VIOLATION

def call_service():
    print("Calling service using API key:", API_KEY)
call_service()


# ------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Inline hardcoded token inside a function
# ------------------------------------------------------------
def authenticate_user():
    token = "Bearer eyJhbGciO...ExampleToken..."  # VIOLATION
    print("Authenticating with token:", token)

authenticate_user()


# ============================================================
# ✅ COMPLIANT EXAMPLES
# Use environment variables, config files, or secret managers.
# ============================================================

# ------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Load secrets from environment variables
# ------------------------------------------------------------
safe_db_password = os.getenv("DB_PASSWORD")

if safe_db_password:
    print("Secure DB password loaded from environment.")
else:
    print("DB_PASSWORD not found in environment variables.")


# ------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Load secrets from a config file (not hardcoded)
# ------------------------------------------------------------
import json

def load_config():
    try:
        with open("config.json", "r") as f:  # SAFE (file not included in source)
            cfg = json.load(f)
            return cfg.get("api_key")
    except FileNotFoundError:
        return None

safe_api_key = load_config()
print("API key loaded from config file:", safe_api_key)


# ------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Simulated secret manager (e.g., AWS Secrets Manager)
# ------------------------------------------------------------
def fetch_secret_from_vault(name):
    # Simulation only — real secret vault use is SAFE
    fake_vault = {
        "service_token": "retrieved-at-runtime-not-hardcoded"
    }
    return fake_vault.get(name)

runtime_token = fetch_secret_from_vault("service_token")
print("Secret loaded at runtime:", runtime_token)
