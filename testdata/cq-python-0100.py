# ===============================================================
# cq-python-0100: Remove Lambda
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Redundant lambda that wraps a function
# --------------------------------------------------------------
numbers = [1, 2, 3, 4]
squared_violation = list(map(lambda x: x**2, numbers))  # ❌ lambda not needed
print("Violation - squared with lambda:", squared_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Lambda that calls an existing function unnecessarily
# --------------------------------------------------------------
def double(x):
    return x * 2

doubled_violation = list(map(lambda x: double(x), numbers))  # ❌ redundant lambda
print("Violation - doubled with lambda:", doubled_violation)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use direct function reference or comprehension instead of lambda
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use list comprehension instead of lambda
# --------------------------------------------------------------
squared_clean = [x**2 for x in numbers]
print("Compliant - squared with comprehension:", squared_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Use function reference directly in map
# --------------------------------------------------------------
doubled_clean = list(map(double, numbers))
print("Compliant - doubled with function reference:", doubled_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using built-in functions directly
# --------------------------------------------------------------
words = ["apple", "banana", "cherry"]
upper_clean = list(map(str.upper, words))
print("Compliant - upper with function reference:", upper_clean)
