# =========================================================
# cq-python-0035: File Path Validation
# This file contains both violating and compliant examples.
# =========================================================

import os

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Directly trusting user input for file paths
# ---------------------------------------------------------

user_path = input("Enter file name to read: ")  
# Example attack input: ../../etc/passwd

try:
    # No validation → Directory Traversal Possible (VIOLATION)
    with open(user_path, "r") as f:        # VIOLATION
        print("File Contents (VIOLATION):")
        print(f.read())
except Exception as e:
    print("Error:", e)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Joining paths with unvalidated user input
# ---------------------------------------------------------

base_dir = "/var/app/uploads/"

file_name = input("Enter uploaded file: ")
full_path = os.path.join(base_dir, file_name)   # Still vulnerable without validation

try:
    with open(full_path, "r") as f:             # VIOLATION
        print("Read from:", full_path)
except Exception as e:
    print("Error:", e)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Validating file path using os.path.normpath and restricting base directory
# ---------------------------------------------------------

safe_base_dir = "/var/app/uploads/"

file_name_safe = input("Enter safe file name: ")

normalized = os.path.normpath(file_name_safe)

# Ensure the path does not escape the base directory
safe_path = os.path.join(safe_base_dir, normalized)

if not safe_path.startswith(safe_base_dir):
    raise ValueError("Invalid file path — path traversal attempt blocked!")

try:
    with open(safe_path, "r") as f:
        print("Safe File Contents:")
        print(f.read())
except Exception as e:
    print("Error:", e)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Allow only whitelisted extensions
# ---------------------------------------------------------

allowed_extensions = {".txt", ".log"}

file_name_check = input("Enter file to read (.txt/.log only): ")
_, ext = os.path.splitext(file_name_check)

if ext not in allowed_extensions:
    raise ValueError("File type not allowed")

safe_whitelist_path = os.path.join(safe_base_dir, os.path.basename(file_name_check))

try:
    with open(safe_whitelist_path, "r") as f:
        print("Whitelisted File Contents:")
        print(f.read())
except Exception as e:
    print("Error:", e)
