# ===============================================================
# cq-python-0052: Itertools Usage
# This file contains both violating and compliant examples.
# ===============================================================

import itertools

# Sample data
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Manually concatenating lists with loops
# --------------------------------------------------------------
combined = []
for x in list1:
    combined.append(x)
for y in list2:
    combined.append(y)  # VIOLATION
print("Violation 1 - combined list:", combined)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Flattening a list of lists manually
# --------------------------------------------------------------
nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []
for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)  # VIOLATION
print("Violation 2 - flattened list:", flat_list)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using itertools for efficient iteration
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Concatenating iterables using itertools.chain
# --------------------------------------------------------------
combined_safe = list(itertools.chain(list1, list2))  # SAFE
print("\nCompliant 1 - combined list with itertools.chain:", combined_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Flattening a list of lists using itertools.chain.from_iterable
# --------------------------------------------------------------
flat_list_safe = list(itertools.chain.from_iterable(nested_list))  # SAFE
print("Compliant 2 - flattened list with itertools:", flat_list_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using itertools.islice for partial iteration
# --------------------------------------------------------------
for val in itertools.islice(range(100), 0, 10):  # SAFE: efficient slicing without full list
    print("Compliant 3 - value from islice:", val, end=" ")
print()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 4
# Using itertools.cycle for repeated iteration
# --------------------------------------------------------------
cycle_iter = itertools.cycle(['A', 'B', 'C'])
for i, val in enumerate(cycle_iter):
    if i >= 6:
        break
    print("Compliant 4 - value from cycle:", val, end=" ")
print()
