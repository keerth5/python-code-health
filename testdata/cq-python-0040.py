# =========================================================
# cq-python-0040: List Comprehensions
# This file includes both violating and compliant examples.
# =========================================================


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using map() instead of a clear list comprehension
# ---------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Less readable for simple transformation
squared_numbers_violation = list(map(lambda x: x * x, numbers))  # VIOLATION
print("Violation 1:", squared_numbers_violation)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using filter() instead of a clear list comprehension
# ---------------------------------------------------------

# Less clear filtering logic
even_numbers_violation = list(filter(lambda x: x % 2 == 0, numbers))  # VIOLATION
print("Violation 2:", even_numbers_violation)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using list comprehension for transformation
# ---------------------------------------------------------

squared_numbers_compliant = [x * x for x in numbers]  # COMPLIANT
print("Compliant 1:", squared_numbers_compliant)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using list comprehension for filtering
# ---------------------------------------------------------

even_numbers_compliant = [x for x in numbers if x % 2 == 0]  # COMPLIANT
print("Compliant 2:", even_numbers_compliant)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# More complex map+filter replaced with a single comprehension
# ---------------------------------------------------------

complex_compliant = [x * 2 for x in numbers if x > 2]  # COMPLIANT
print("Compliant 3:", complex_compliant)
