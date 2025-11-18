# ===============================================================
# cq-python-0104: Chain Flattening
# This file contains both violating and compliant examples.
# ===============================================================

from itertools import chain

# Sample nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Flattening with nested loops
# --------------------------------------------------------------
flattened_violation = []
for sublist in nested_list:
    for item in sublist:
        flattened_violation.append(item)

print("Violation - flattened with loops:", flattened_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using sum to flatten (less efficient)
# --------------------------------------------------------------
flattened_violation2 = sum(nested_list, [])
print("Violation - flattened with sum():", flattened_violation2)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use chain.from_iterable for flattening
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Flatten with chain.from_iterable
# --------------------------------------------------------------
flattened_clean = list(chain.from_iterable(nested_list))
print("Compliant - flattened with chain.from_iterable:", flattened_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Flatten and apply a function while flattening
# --------------------------------------------------------------
flattened_squared = [x**2 for x in chain.from_iterable(nested_list)]
print("Compliant - squared while flattening:", flattened_squared)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Flatten generator expression for memory efficiency
# --------------------------------------------------------------
flattened_generator = chain.from_iterable(nested_list)
for item in flattened_generator:
    print("Compliant - generator item:", item)
