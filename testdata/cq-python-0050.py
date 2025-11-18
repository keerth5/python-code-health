# ===============================================================
# cq-python-0050: Pathlib Usage
# This file contains both violating and compliant examples.
# ===============================================================

import os
from pathlib import Path

# Sample file paths
file_name = "example.txt"
dir_name = "sample_dir"

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using os.path.join and os.path.exists
# --------------------------------------------------------------
full_path = os.path.join(dir_name, file_name)  # VIOLATION
print("Violation 1 - full_path:", full_path)

if os.path.exists(full_path):  # VIOLATION
    print("Violation 2 - file exists")
else:
    print("Violation 3 - file does not exist")


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using os.path functions for file manipulation
# --------------------------------------------------------------
base_name = os.path.basename(full_path)  # VIOLATION
extension = os.path.splitext(full_path)[1]  # VIOLATION
print("Violation 4 - basename:", base_name, "extension:", extension)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using pathlib for modern path operations
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Joining paths
# --------------------------------------------------------------
p = Path(dir_name) / file_name  # SAFE
print("\nCompliant 1 - Pathlib path:", p)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Checking if file exists
# --------------------------------------------------------------
if p.exists():  # SAFE
    print("Compliant 2 - file exists")
else:
    print("Compliant 3 - file does not exist")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Extracting filename and extension
# --------------------------------------------------------------
print("Compliant 4 - filename:", p.name)       # SAFE
print("Compliant 5 - extension:", p.suffix)    # SAFE

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 4
# Creating directories safely
# --------------------------------------------------------------
new_dir = Path("new_folder")
new_dir.mkdir(exist_ok=True)  # SAFE: avoids manual os.mkdir checks
print("Compliant 6 - directory created:", new_dir)
