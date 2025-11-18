# =========================================================
# cq-python-0015: Safe List Iteration
# This file includes both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Removing items from a list while iterating over it
# ---------------------------------------------------------

numbers_violation = [1, 2, 3, 4, 5]

print("Violation Example 1:")
for n in numbers_violation:          # VIOLATION
    if n % 2 == 0:
        numbers_violation.remove(n)  # Modifying during iteration

print(numbers_violation)  # Produces unexpected output (skips items)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Appending elements while iterating
# ---------------------------------------------------------

values_violation = ["a", "b", "c"]

print("\nViolation Example 2:")
for v in values_violation:           # VIOLATION
    values_violation.append(v.upper())

print(values_violation)  # Infinite loop risk or unexpected growth


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Iterate over a copy when modifying the original
# ---------------------------------------------------------

numbers_safe = [1, 2, 3, 4, 5]

print("\nCompliant Example 1:")
for n in numbers_safe[:]:  # Safe: iterate over a copy
    if n % 2 == 0:
        numbers_safe.remove(n)

print(numbers_safe)  # Expected behavior


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Use list comprehension instead of modifying during iteration
# ---------------------------------------------------------

values_safe = ["a", "b", "c"]

print("\nCompliant Example 2:")
filtered_values = [v for v in values_safe if v != "b"]  # Safe alternative

print(filtered_values)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Build a new list instead of modifying the existing one
# ---------------------------------------------------------

items = [1, 2, 3, 4, 5]

print("\nCompliant Example 3:")
new_items = []
for item in items:
    if item < 4:
        new_items.append(item)

print(new_items)
