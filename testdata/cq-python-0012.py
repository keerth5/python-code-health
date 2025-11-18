# =========================================================
# cq-python-0012: Specific Exceptions
# This file contains both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Bare except — catches ALL exceptions
# ---------------------------------------------------------

def read_number_violation():
    try:
        value = int(input("Enter a number: "))
        print("Value:", value)
    except:  # VIOLATION: Bare except
        print("An error occurred")  # Hides the root cause


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Catching top-level Exception
# ---------------------------------------------------------

def divide_violation(a, b):
    try:
        return a / b
    except Exception:  # VIOLATION: Too broad
        return "Something went wrong"


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Catch specific known exceptions
# ---------------------------------------------------------

def read_number_safe():
    try:
        value = int(input("Enter a number: "))
        print("Value:", value)
    except ValueError:
        print("Please enter a valid integer")
    except EOFError:
        print("No input provided")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Multiple specific exception handlers
# ---------------------------------------------------------

def divide_safe(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Inputs must be numbers"


# Driver calls for demonstration
if __name__ == "__main__":
    print("Violation Example 1:")
    read_number_violation()

    print("\nViolation Example 2:")
    print(divide_violation(10, 0))

    print("\nCompliant Example 1:")
    read_number_safe()

    print("\nCompliant Example 2:")
    print(divide_safe(10, 0))
