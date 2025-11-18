# ===============================================================
# cq-python-0083: Operator Spacing
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# No spaces around arithmetic operators
# --------------------------------------------------------------
a=5+3*2      # ❌ no spaces around + or *
b=a-1/2      # ❌ no spaces around - or /
print(a,b)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# No spaces around comparison or assignment operators
# --------------------------------------------------------------
x=10
y=20
if x>y:
    print("Violation - x>y")
z=x==y       # ❌ no spaces around ==
print(z)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Proper spacing around operators
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Spaces around arithmetic operators
# --------------------------------------------------------------
a_clean = 5 + 3 * 2
b_clean = a_clean - 1 / 2
print(a_clean, b_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Spaces around comparison and assignment operators
# --------------------------------------------------------------
x_clean = 10
y_clean = 20
if x_clean > y_clean:
    print("Compliant - x_clean > y_clean")
z_clean = x_clean == y_clean
print(z_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Spaces in complex expressions
# --------------------------------------------------------------
result = (a_clean + b_clean) * (x_clean - y_clean) / 2
print("Compliant - result:", result)
