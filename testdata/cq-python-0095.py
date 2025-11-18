# ===============================================================
# cq-python-0095: No Return Parentheses
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using parentheses unnecessarily in return
# --------------------------------------------------------------
def get_number_violation():
    return (42)  # ❌ unnecessary parentheses
print("Violation - get_number_violation:", get_number_violation())

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using parentheses around string
# --------------------------------------------------------------
def get_greeting_violation():
    return ("Hello, World!")  # ❌ unnecessary parentheses
print("Violation - get_greeting_violation:", get_greeting_violation())


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Return values without unnecessary parentheses
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Returning a number directly
# --------------------------------------------------------------
def get_number_clean():
    return 42
print("Compliant - get_number_clean:", get_number_clean())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Returning a string directly
# --------------------------------------------------------------
def get_greeting_clean():
    return "Hello, World!"
print("Compliant - get_greeting_clean:", get_greeting_clean())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Returning a tuple only when needed
# --------------------------------------------------------------
def get_coordinates():
    return 10, 20  # tuple without unnecessary parentheses
print("Compliant - get_coordinates:", get_coordinates())
