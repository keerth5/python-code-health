# ===============================================================
# cq-python-0049: No Len Boolean
# This file contains both violating and compliant examples.
# ===============================================================

# Sample data
items = [1, 2, 3]
empty_items = []

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using len() in boolean context
# --------------------------------------------------------------
if len(items):  # VIOLATION
    print("Violation 1 - items list is not empty")

if not len(empty_items):  # VIOLATION
    print("Violation 2 - empty_items list is empty")


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using len() in ternary / inline expressions
# --------------------------------------------------------------
status = "Has items" if len(items) else "Empty"  # VIOLATION
print("Violation 3 - status:", status)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use the object itself in boolean context
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Directly using list in if statement
# --------------------------------------------------------------
if items:  # SAFE
    print("Compliant 1 - items list is not empty")

if not empty_items:  # SAFE
    print("Compliant 2 - empty_items list is empty")


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using object in ternary / inline expression
# --------------------------------------------------------------
status_safe = "Has items" if items else "Empty"  # SAFE
print("Compliant 3 - status:", status_safe)


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using dictionaries or sets in boolean context
# --------------------------------------------------------------
user_data = {"name": "Alice"}
if user_data:  # SAFE
    print("Compliant 4 - user_data is not empty")

empty_dict = {}
if not empty_dict:  # SAFE
    print("Compliant 5 - empty_dict is empty")
