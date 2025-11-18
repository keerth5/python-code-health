# ===============================================================
# cq-python-0103: Default Dict
# This file contains both violating and compliant examples.
# ===============================================================

from collections import defaultdict

# Sample data
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using dict.setdefault() to count elements
# --------------------------------------------------------------
count_violation = {}
for word in words:
    count_violation.setdefault(word, 0)
    count_violation[word] += 1

print("Violation - counting with setdefault():", count_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using dict.setdefault() for grouping
# --------------------------------------------------------------
groups_violation = {}
for word in words:
    key = word[0]
    groups_violation.setdefault(key, []).append(word)

print("Violation - grouping with setdefault():", groups_violation)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use defaultdict for default values
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Counting elements with defaultdict
# --------------------------------------------------------------
count_clean = defaultdict(int)
for word in words:
    count_clean[word] += 1

print("Compliant - counting with defaultdict:", dict(count_clean))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Grouping elements with defaultdict(list)
# --------------------------------------------------------------
groups_clean = defaultdict(list)
for word in words:
    key = word[0]
    groups_clean[key].append(word)

print("Compliant - grouping with defaultdict:", dict(groups_clean))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using defaultdict with custom default factory
# --------------------------------------------------------------
length_map = defaultdict(lambda: "unknown")
length_map["apple"] = 5
length_map["banana"] = 6
print("Compliant - custom defaultdict:", dict(length_map))
