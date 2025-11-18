# ===============================================================
# cq-python-0084: One Statement Per Line
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Multiple statements on one line using semicolon
# --------------------------------------------------------------
a = 5; b = 10; c = a + b     # ❌ multiple statements on one line
print(a, b, c)               

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple statements on one line in a loop
# --------------------------------------------------------------
for i in range(3): print(i); print(i*2)   # ❌ multiple statements on one line


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# One statement per line
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Separate variable assignments
# --------------------------------------------------------------
a_clean = 5
b_clean = 10
c_clean = a_clean + b_clean
print(a_clean, b_clean, c_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Separate statements in loops
# --------------------------------------------------------------
for i in range(3):
    print(i)
    print(i * 2)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Functions with one statement per line
# --------------------------------------------------------------
def add_numbers(x, y):
    result = x + y
    return result

sum_result = add_numbers(2, 3)
print("Compliant - sum_result:", sum_result)
