# =========================================================
# cq-python-0043: Zip Multiple Sequences
# This file includes both violating and compliant examples.
# =========================================================

# Two sample lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE
# Using range(len()) to loop over two lists simultaneously
# ---------------------------------------------------------

print("Violation Example:")
for i in range(len(names)):  # VIOLATION
    print(f"{names[i]} is {ages[i]} years old")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE
# Use zip() to iterate over multiple lists
# ---------------------------------------------------------

print("\nCompliant Example:")
for name, age in zip(names, ages):  # SAFE, readable, Pythonic
    print(f"{name} is {age} years old")


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Manual index tracking instead of zip()
# ---------------------------------------------------------

print("\nViolation Example 2:")
i = 0
for n in names:  # VIOLATION
    print(f"{n} -> {ages[i]}")
    i += 1


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using zip() with unpacking
# ---------------------------------------------------------

print("\nCompliant Example 2:")
for name, age in zip(names, ages):
    print(f"{name} -> {age}")
