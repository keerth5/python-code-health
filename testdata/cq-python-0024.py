# =========================================================
# cq-python-0024: Safe Subprocess Calls
# This file contains both violating and compliant examples.
# =========================================================

import subprocess

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using shell=True with user input → Command Injection risk
# ---------------------------------------------------------

user_input = input("Enter a command to run: ")

# Dangerous: Allows command injection (e.g., "ls; rm -rf /")
subprocess.call(user_input, shell=True)  # VIOLATION


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Unsafe string concatenation in subprocess + shell=True
# ---------------------------------------------------------

filename = input("Enter filename to list: ")

cmd = "ls " + filename   # Could inject: "; rm -rf /"
subprocess.run(cmd, shell=True)  # VIOLATION


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use list arguments (no shell=True) → SAFE
# ---------------------------------------------------------

safe_filename = input("Enter filename for safe listing: ")

# Using array prevents shell expansion & injection
subprocess.run(["ls", safe_filename])  # SAFE


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Explicitly disable shell usage
# ---------------------------------------------------------

safe_cmd = ["echo", "Hello World"]
subprocess.call(safe_cmd, shell=False)  # SAFE
