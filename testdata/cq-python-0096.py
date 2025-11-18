# ===============================================================
# cq-python-0096: None Comparisons
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using '==' to compare with None
# --------------------------------------------------------------
value = None
if value == None:  # ❌ should use 'is None'
    print("Violation - value is None using '=='")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using '!=' to compare with None
# --------------------------------------------------------------
value2 = 42
if value2 != None:  # ❌ should use 'is not None'
    print("Violation - value2 is not None using '!='")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use 'is' and 'is not' for None comparisons
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Check for None using 'is'
# --------------------------------------------------------------
if value is None:
    print("Compliant - value is None using 'is'")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Check for not None using 'is not'
# --------------------------------------------------------------
if value2 is not None:
    print("Compliant - value2 is not None using 'is not'")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Function returning None with proper check
# --------------------------------------------------------------
def find_item(lst, target):
    for item in lst:
        if item == target:
            return item
    return None

result = find_item([1, 2, 3], 4)
if result is None:
    print("Compliant - result is None")
