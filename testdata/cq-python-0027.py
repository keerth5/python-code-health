# =========================================================
# cq-python-0027: Input Validation
# This file contains both violating and compliant code.
# =========================================================


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Function accepting user input but performing no validation
# ---------------------------------------------------------

def calculate_discount_violation(price, discount):
    # No type checks, no range checks → VIOLATION
    return price - (price * discount)


try:
    print("Violation 1:", calculate_discount_violation("100", 0.1))  # Causes runtime error
except Exception as e:
    print("Violation 1 Error:", e)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# No validation on API-like function
# ---------------------------------------------------------

def fetch_user_violation(user_id):
    # Missing validation → allows invalid/negative IDs
    return {"id": user_id, "name": "Test User"}

print("Violation 2:", fetch_user_violation(-10))  # Should be validated


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper type and range validation
# ---------------------------------------------------------

def calculate_discount_safe(price, discount):
    if not isinstance(price, (int, float)):
        raise TypeError("price must be a number")

    if not isinstance(discount, (int, float)):
        raise TypeError("discount must be numeric")

    if price < 0:
        raise ValueError("price cannot be negative")

    if not (0 <= discount <= 1):
        raise ValueError("discount must be between 0 and 1")

    return price - (price * discount)

print("\nCompliant 1:", calculate_discount_safe(100, 0.2))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Validating function parameters explicitly
# ---------------------------------------------------------

def fetch_user_safe(user_id):
    if not isinstance(user_id, int):
        raise TypeError("user_id must be an integer")

    if user_id <= 0:
        raise ValueError("user_id must be a positive number")

    return {"id": user_id, "name": "Safe User"}

print("Compliant 2:", fetch_user_safe(10))
