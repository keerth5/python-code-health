# ===============================================================
# cq-python-0093: No Redundant Else
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Redundant else after return
# --------------------------------------------------------------
def check_positive_violation(x):
    if x > 0:
        return "Positive"
    else:  # ❌ redundant else
        return "Non-positive"

print("Violation:", check_positive_violation(5))
print("Violation:", check_positive_violation(-2))


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple redundant else
# --------------------------------------------------------------
def check_number_violation(n):
    if n == 0:
        return "Zero"
    elif n > 0:
        return "Positive"
    else:  # ❌ redundant else
        return "Negative"

print("Violation:", check_number_violation(0))
print("Violation:", check_number_violation(3))
print("Violation:", check_number_violation(-1))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Remove redundant else after return
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using direct return after if
# --------------------------------------------------------------
def check_positive_clean(x):
    if x > 0:
        return "Positive"
    return "Non-positive"  # no else needed

print("Compliant:", check_positive_clean(5))
print("Compliant:", check_positive_clean(-2))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Multiple conditions without redundant else
# --------------------------------------------------------------
def check_number_clean(n):
    if n == 0:
        return "Zero"
    if n > 0:
        return "Positive"
    return "Negative"  # no else needed

print("Compliant:", check_number_clean(0))
print("Compliant:", check_number_clean(3))
print("Compliant:", check_number_clean(-1))
