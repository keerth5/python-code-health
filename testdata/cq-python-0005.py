# ==============================================================
# cq-python-0005: Path Traversal Protection
# This file contains both violating and compliant examples.
# ==============================================================

import os


BASE_DIR = "/var/app/data"   # Allowed directory for file operations


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Directly using user input to access a file path (dangerous!)
# --------------------------------------------------------------
user_filename = input("Enter filename: ")

try:
    with open(user_filename, "r") as f:   # VIOLATION: Path traversal vulnerability
        print("File contents:", f.read())
except Exception as e:
    print("Unsafe file access failed:", e)


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# User input used in os.path.join without validation
# --------------------------------------------------------------
unsafe_path = os.path.join(BASE_DIR, user_filename)   # Still unsafe
try:
    with open(unsafe_path, "r") as f:
        print("Unsafe joined path read:", f.read())
except Exception as e:
    print("Unsafe joined path failed:", e)


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Allowing ../ traversal to escape directory boundaries
# --------------------------------------------------------------
relative_path = input("Enter relative path to read: ")

try:
    with open(os.path.join(BASE_DIR, relative_path), "r") as f:  # VIOLATION
        print("Read:", f.read())
except Exception:
    print("Path traversal attempt blocked (but insecure code tried!).")


# ==============================================================
# ✅ COMPLIANT EXAMPLES
# Proper validation and safe handling of file paths.
# ==============================================================

# --------------------------------------------------------------
# Helper: Resolve safe path and enforce directory constraints
# --------------------------------------------------------------
def get_safe_path(base_dir, user_path):
    """
    Ensures that the resolved absolute path stays inside base_dir.
    Prevents path traversal.
    """
    abs_base = os.path.abspath(base_dir)
    abs_target = os.path.abspath(os.path.join(abs_base, user_path))

    if not abs_target.startswith(abs_base):
        raise ValueError("Invalid path: Potential traversal detected")

    return abs_target


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using path validation before accessing a file
# --------------------------------------------------------------
safe_input = input("Enter safe filename: ")

try:
    safe_path = get_safe_path(BASE_DIR, safe_input)
    with open(safe_path, "r") as f:
        print("Safely accessed file:", f.read())
except Exception as e:
    print("Safe file read prevented:", e)


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Restricting to a whitelist of allowed filenames
# --------------------------------------------------------------
ALLOWED_FILES = {"config.json", "data.txt", "info.log"}

user_req = input("Enter allowed file to read (from whitelist): ")

if user_req in ALLOWED_FILES:
    try:
        with open(os.path.join(BASE_DIR, user_req), "r") as f:
            print("Whitelisted file accessed:", f.read())
    except Exception as e:
        print("Failed reading whitelisted file:", e)
else:
    print("File not allowed")


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using file open operations with sanitized filenames
# --------------------------------------------------------------
def sanitize_filename(name):
    """
    Accept only simple filenames (letters, digits, underscores, hyphens).
    No slashes allowed.
    """
    import re
    if not re.fullmatch(r"[A-Za-z0-9_\-\.]+", name):
        raise ValueError("Invalid filename format")
    return name

raw_input_name = input("Enter safe sanitized filename: ")

try:
    sanitized = sanitize_filename(raw_input_name)
    with open(os.path.join(BASE_DIR, sanitized), "r") as f:
        print("Sanitized file read:", f.read())
except Exception as e:
    print("Sanitized access failed:", e)
