# =========================================================
# cq-python-0042: Enumerate Usage
# This file includes both violating and compliant examples.
# =========================================================

items = ["apple", "banana", "cherry"]

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE
# Using range(len()) instead of enumerate()
# ---------------------------------------------------------

print("Violation Output:")
for i in range(len(items)):  # VIOLATION
    print(f"Index: {i}, Value: {items[i]}")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE
# Using enumerate() for cleaner, safer iteration
# ---------------------------------------------------------

print("\nCompliant Output:")
for index, value in enumerate(items):  # COMPLIANT
    print(f"Index: {index}, Value: {value}")
