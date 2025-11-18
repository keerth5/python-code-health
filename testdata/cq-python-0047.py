# ===============================================================
# cq-python-0047: Default Dict Usage
# This file contains both violating and compliant examples.
# ===============================================================

from collections import defaultdict

# Sample data
data = [("apple", 1), ("banana", 2), ("apple", 3), ("banana", 4), ("cherry", 5)]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using dict with setdefault repeatedly
# --------------------------------------------------------------
freq_dict = {}
for key, value in data:
    freq_dict.setdefault(key, []).append(value)  # VIOLATION

print("Violation 1 - dict with setdefault:", freq_dict)


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# More complex nested setdefault
# --------------------------------------------------------------
nested_dict = {}
for key, value in data:
    nested_dict.setdefault(key, {}).setdefault("values", []).append(value)  # VIOLATION

print("Violation 2 - nested dict with setdefault:", nested_dict)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use defaultdict for cleaner, faster code
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Simple list aggregation
# --------------------------------------------------------------
dd_list = defaultdict(list)
for key, value in data:
    dd_list[key].append(value)  # SAFE

print("\nCompliant 1 - defaultdict(list):", dict(dd_list))


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Nested defaultdict usage
# --------------------------------------------------------------
dd_nested = defaultdict(lambda: defaultdict(list))
for key, value in data:
    dd_nested[key]["values"].append(value)  # SAFE

print("Compliant 2 - nested defaultdict:", {k: dict(v) for k, v in dd_nested.items()})


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using defaultdict with integer counts
# --------------------------------------------------------------
dd_count = defaultdict(int)
for _, value in data:
    dd_count[value] += 1  # SAFE: counting occurrences

print("Compliant 3 - defaultdict(int):", dict(dd_count))
