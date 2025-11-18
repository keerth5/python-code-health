# =========================================================
# cq-python-0013: No Assert Validation
# This file contains both violating and compliant examples.
# =========================================================


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using assert for validating user input
# ---------------------------------------------------------

def process_age_violation(age):
    assert age > 0, "Age must be positive"  # VIOLATION: assert used for validation
    return f"Age processed: {age}"

try:
    print(process_age_violation(-5))
except AssertionError as e:
    print("Violation 1 Triggered:", e)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Logical checks replaced by asserts (dangerous in production)
# ---------------------------------------------------------

def divide_violation(a, b):
    assert b != 0, "Division by zero!"  # VIOLATION
    return a / b

try:
    print(divide_violation(10, 0))
except AssertionError as e:
    print("Violation 2 Triggered:", e)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper validation using if/raise
# ---------------------------------------------------------

def process_age_safe(age):
    if age <= 0:
        raise ValueError("Age must be positive")  # SAFE
    return f"Age processed: {age}"

try:
    print(process_age_safe(25))
    print(process_age_safe(-5))
except ValueError as e:
    print("Compliant 1 Triggered:", e)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Proper exception for invalid operations
# ---------------------------------------------------------

def divide_safe(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # SAFE
    return a / b

try:
    print(divide_safe(10, 2))
    print(divide_safe(10, 0))
except ZeroDivisionError as e:
    print("Compliant 2 Triggered:", e)
