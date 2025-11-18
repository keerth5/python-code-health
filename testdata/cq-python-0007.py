# ================================================================
# cq-python-0007: Safe YAML Loading
# This file contains both violating and compliant examples.
# ================================================================

import yaml


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using yaml.load() directly on untrusted user input
# ---------------------------------------------------------------
user_yaml_input = input("Enter YAML (unsafe): ")

try:
    data = yaml.load(user_yaml_input, Loader=yaml.Loader)  # VIOLATION
    print("Unsafe loaded data:", data)
except Exception as e:
    print("Unsafe YAML load failed:", e)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using yaml.load() without specifying safe loader
# (defaults to unsafe FullLoader in old versions)
# ---------------------------------------------------------------
file_content = """
!!python/object/apply:os.system ['echo Hacked!']
"""

try:
    data2 = yaml.load(file_content)  # VIOLATION
    print("Loaded unsafe file content:", data2)
except Exception as e:
    print("YAML exploit attempt blocked:", e)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Using FullLoader on untrusted data
# ---------------------------------------------------------------
malicious_yaml = input("Enter YAML (malicious possible): ")

try:
    data3 = yaml.load(malicious_yaml, Loader=yaml.FullLoader)  # VIOLATION
    print("Dangerous load:", data3)
except Exception:
    print("Dangerous YAML load failed")


# ================================================================
# ✅ COMPLIANT EXAMPLES
# Safe loaders and safer YAML handling
# ================================================================

# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using yaml.safe_load() on user input
# ---------------------------------------------------------------
safe_input = input("Enter safe YAML: ")

try:
    safe_data = yaml.safe_load(safe_input)  # SAFE
    print("Safely loaded YAML:", safe_data)
except Exception as e:
    print("Failed safe load:", e)


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Safe loading from a file
# ---------------------------------------------------------------
try:
    with open("config.yml", "r") as f:
        config_data = yaml.safe_load(f)  # SAFE
        print("Safely loaded config.yml:", config_data)
except FileNotFoundError:
    print("config.yml not found")


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using SafeLoader explicitly
# ---------------------------------------------------------------
trusted_yaml = """
app:
  version: 1
  name: sample-app
"""

try:
    parsed = yaml.load(trusted_yaml, Loader=yaml.SafeLoader)  # SAFE
    print("Loaded using SafeLoader:", parsed)
except Exception as e:
    print("SafeLoader failed:", e)
