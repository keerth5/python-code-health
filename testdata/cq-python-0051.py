# ===============================================================
# cq-python-0051: Set Membership
# This file contains both violating and compliant examples.
# ===============================================================

# Sample data
large_list = list(range(1000000))
large_set = set(large_list)

element_to_check = 999999

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using list for membership testing
# --------------------------------------------------------------
if element_to_check in large_list:  # VIOLATION: O(n) lookup
    print("Violation 1 - element found in list")
else:
    print("Violation 2 - element not found in list")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using list in a loop membership test
# --------------------------------------------------------------
values_to_check = [10, 500000, 999999]

found_values = []
for v in values_to_check:
    if v in large_list:  # VIOLATION: O(n) lookup each time
        found_values.append(v)

print("Violation 3 - found values in list:", found_values)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using set for fast membership testing
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Single membership test
# --------------------------------------------------------------
if element_to_check in large_set:  # SAFE: O(1) lookup
    print("Compliant 1 - element found in set")
else:
    print("Compliant 2 - element not found in set")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Loop membership test
# --------------------------------------------------------------
found_values_safe = []
for v in values_to_check:
    if v in large_set:  # SAFE: O(1) lookup
        found_values_safe.append(v)

print("Compliant 3 - found values in set:", found_values_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using set operations (intersection)
# --------------------------------------------------------------
common_elements = set(values_to_check) & large_set  # SAFE
print("Compliant 4 - common elements using set intersection:", common_elements)
