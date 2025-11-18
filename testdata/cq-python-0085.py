# ===============================================================
# cq-python-0085: Parentheses Continuation
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using backslash for line continuation
# --------------------------------------------------------------
total = 1 + 2 + 3 + \
        4 + 5 + 6     # ❌ uses backslash
print("Violation - total:", total)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using backslash in function call
# --------------------------------------------------------------
def print_numbers():
    print(1, 2, 3, \
          4, 5, 6)       # ❌ uses backslash

print_numbers()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using parentheses for line continuation
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Parentheses for arithmetic continuation
# --------------------------------------------------------------
total_clean = (
    1 + 2 + 3 +
    4 + 5 + 6
)
print("Compliant - total_clean:", total_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Parentheses in function calls
# --------------------------------------------------------------
def print_numbers_compliant():
    print(
        1, 2, 3,
        4, 5, 6
    )

print_numbers_compliant()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Parentheses for long expressions
# --------------------------------------------------------------
result = (
    10 * 2 + 5 -
    3 / 1 + 8
)
print("Compliant - result:", result)
