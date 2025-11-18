# =========================================================
# cq-python-0019: No Shell Injection
# This file contains both violating and compliant examples.
# =========================================================

import os
import subprocess

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Directly passing user input to os.system() — injection risk
# ---------------------------------------------------------

user_input = input("Enter a file to list: ")

# Example exploit: ; rm -rf /
cmd = f"ls {user_input}"   # Untrusted input inside shell command
os.system(cmd)  # VIOLATION
print("Executed (VIOLATION):", cmd)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Building shell commands dynamically with string concatenation
# ---------------------------------------------------------

filename = input("Enter a backup filename: ")
os.system("cp data.txt " + filename)  # VIOLATION
print("Copy command executed (VIOLATION):", filename)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use subprocess.run() with argument list — safe, no shell
# ---------------------------------------------------------

safe_input = input("\nEnter a file to list safely: ")

try:
    subprocess.run(["ls", safe_input], check=True)  # SAFE
except subprocess.CalledProcessError:
    print("File not found or error occurred.")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Whitelisting + using subprocess without shell=True
# ---------------------------------------------------------

allowed_files = {"data.txt", "config.ini"}

file_choice = input("\nChoose a file (data.txt/config.ini): ")

if file_choice not in allowed_files:
    print("Invalid file selection.")
else:
    subprocess.run(["cat", file_choice], check=True)  # SAFE
