# ===============================================================
# cq-python-0086: Docstring Documentation
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Public function without docstring
# --------------------------------------------------------------
def add_numbers(a, b):
    return a + b   # ❌ missing docstring

print("Violation - add_numbers:", add_numbers(2, 3))

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Public class without docstring
# --------------------------------------------------------------
class Calculator:
    def multiply(self, x, y):
        return x * y  # ❌ missing docstring

calc = Calculator()
print("Violation - multiply:", calc.multiply(2, 4))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Functions and classes with proper docstrings
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Function with docstring
# --------------------------------------------------------------
def add_numbers_compliant(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int or float): First number
    b (int or float): Second number

    Returns:
    int or float: Sum of a and b
    """
    return a + b

print("Compliant - add_numbers_compliant:", add_numbers_compliant(2, 3))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Class with docstring
# --------------------------------------------------------------
class CalculatorCompliant:
    """
    Simple calculator class for arithmetic operations.
    """

    def multiply(self, x, y):
        """
        Multiply two numbers and return the result.

        Parameters:
        x (int or float): First number
        y (int or float): Second number

        Returns:
        int or float: Product of x and y
        """
        return x * y

calc_compliant = CalculatorCompliant()
print("Compliant - multiply:", calc_compliant.multiply(2, 4))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Another function with docstring
# --------------------------------------------------------------
def divide_numbers(a, b):
    """
    Divide a by b and return the result.

    Raises:
    ZeroDivisionError: If b is zero
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

print("Compliant - divide_numbers:", divide_numbers(10, 2))
