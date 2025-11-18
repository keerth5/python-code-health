# ===============================================================
# cq-python-0074: Configuration Management
# This file contains both violating and compliant examples.
# ===============================================================

import os
import json

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Hardcoded values in code
# --------------------------------------------------------------
def connect_database_violation():
    host = "localhost"       # ❌ hardcoded
    port = 5432              # ❌ hardcoded
    user = "admin"           # ❌ hardcoded
    password = "password123" # ❌ hardcoded
    print(f"Violation - connecting to DB at {host}:{port} with user {user}")
    # connection logic here

connect_database_violation()


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Hardcoded API endpoint
# --------------------------------------------------------------
def call_api_violation():
    api_url = "https://api.example.com/data"  # ❌ hardcoded
    api_key = "ABC123XYZ"                      # ❌ hardcoded
    print(f"Violation - calling API: {api_url} with key {api_key}")
    # API call logic here

call_api_violation()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using proper configuration management
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using environment variables
# --------------------------------------------------------------
def connect_database_safe():
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", 5432))
    user = os.getenv("DB_USER", "admin")
    password = os.getenv("DB_PASSWORD", "password123")
    print(f"Compliant - connecting to DB at {host}:{port} with user {user}")
    # connection logic here

connect_database_safe()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using a configuration file (JSON)
# --------------------------------------------------------------
def load_config():
    # Example JSON config: {"api_url": "https://api.example.com/data", "api_key": "ABC123XYZ"}
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

config = load_config()

def call_api_safe():
    api_url = config.get("api_url", "https://api.example.com/data")
    api_key = config.get("api_key", "")
    print(f"Compliant - calling API: {api_url} with key {api_key}")
    # API call logic here

call_api_safe()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using a Python config module
# --------------------------------------------------------------
# config_module.py
# DB_HOST = "localhost"
# DB_PORT = 5432
# DB_USER = "admin"
# DB_PASSWORD = "password123"

# from config_module import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD
# print(f"Compliant - connecting to DB at {DB_HOST}:{DB_PORT} with user {DB_USER}")
