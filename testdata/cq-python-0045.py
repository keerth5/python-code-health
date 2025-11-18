# =========================================================
# cq-python-0045: Boolean Operations
# This file contains BOTH violating and compliant examples.
# =========================================================


numbers = [1, 2, 3, 4, 5]


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Manual loop to check if ANY number is even
# ---------------------------------------------------------

def has_even_violation(nums):
    for n in nums:          # VIOLATION
        if n % 2 == 0:
            return True
    return False

print("Violation ANY:", has_even_violation(numbers))


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Manual loop to check if ALL numbers are positive
# ---------------------------------------------------------

def all_positive_violation(nums):
    for n in nums:          # VIOLATION
        if n <= 0:
            return False
    return True

print("Violation ALL:", all_positive_violation(numbers))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using any() for even number check
# ---------------------------------------------------------

def has_even_compliant(nums):
    return any(n % 2 == 0 for n in nums)   # COMPLIANT

print("Compliant ANY:", has_even_compliant(numbers))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using all() for positive number check
# ---------------------------------------------------------

def all_positive_compliant(nums):
    return all(n > 0 for n in nums)        # COMPLIANT

print("Compliant ALL:", all_positive_compliant(numbers))
