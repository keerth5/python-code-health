# ===============================================================
# cq-python-0092: Comprehension Over Map
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using map() for simple operation
# --------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))  # ❌ map used instead of comprehension
print("Violation - squared:", squared)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using filter() for simple condition
# --------------------------------------------------------------
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # ❌ filter used instead of comprehension
print("Violation - even_numbers:", even_numbers)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using list comprehensions
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Squaring numbers with list comprehension
# --------------------------------------------------------------
squared_clean = [x**2 for x in numbers]
print("Compliant - squared_clean:", squared_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Filtering even numbers with list comprehension
# --------------------------------------------------------------
even_numbers_clean = [x for x in numbers if x % 2 == 0]
print("Compliant - even_numbers_clean:", even_numbers_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Combined operation using comprehension
# --------------------------------------------------------------
squared_even_numbers = [x**2 for x in numbers if x % 2 == 0]
print("Compliant - squared_even_numbers:", squared_even_numbers)
