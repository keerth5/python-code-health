# ===============================================================
# cq-python-0098: Tuple Unpacking
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Assigning multiple variables separately
# --------------------------------------------------------------
a_violation = 1
b_violation = 2
c_violation = 3
print("Violation - separate assignments:", a_violation, b_violation, c_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Assigning from a tuple without unpacking
# --------------------------------------------------------------
my_tuple = (4, 5, 6)
x_violation = my_tuple[0]
y_violation = my_tuple[1]
z_violation = my_tuple[2]
print("Violation - tuple indexing:", x_violation, y_violation, z_violation)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use tuple unpacking
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Multiple assignment with tuple unpacking
# --------------------------------------------------------------
a, b, c = 1, 2, 3
print("Compliant - tuple unpacking:", a, b, c)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Unpacking from a tuple directly
# --------------------------------------------------------------
my_tuple = (4, 5, 6)
x, y, z = my_tuple
print("Compliant - unpacked tuple:", x, y, z)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Swapping variables with tuple unpacking
# --------------------------------------------------------------
m, n = 10, 20
m, n = n, m
print("Compliant - swapped with tuple unpacking:", m, n)
