# ===============================================================
# cq-python-0079: Upper Case Constants
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Constants using lowercase
# --------------------------------------------------------------
pi = 3.14159              # ❌ lowercase
max_value = 100            # ❌ lowercase
print("Violation - pi:", pi, "max_value:", max_value)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Constants using camelCase or mixed case
# --------------------------------------------------------------
DefaultTimeout = 30        # ❌ camelCase/mixed case
print("Violation - DefaultTimeout:", DefaultTimeout)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using UPPER_CASE for constants
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Standard uppercase constants
# --------------------------------------------------------------
PI = 3.14159
MAX_VALUE = 100
print("Compliant - PI:", PI, "MAX_VALUE:", MAX_VALUE)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Multi-word constants using underscores
# --------------------------------------------------------------
DEFAULT_TIMEOUT = 30
API_KEY = "ABC123XYZ"
print("Compliant - DEFAULT_TIMEOUT:", DEFAULT_TIMEOUT, "API_KEY:", API_KEY)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Constants for configuration values
# --------------------------------------------------------------
DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
print(
    "Compliant - DATABASE_HOST:", DATABASE_HOST,
    "DATABASE_PORT:", DATABASE_PORT
)
