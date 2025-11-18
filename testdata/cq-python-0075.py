# ===============================================================
# cq-python-0075: Line Length Limit
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Line exceeds 79 characters
# --------------------------------------------------------------
long_line_violation = "This is a very long line that clearly exceeds the 79 characters " \
                      "limit which is not recommended according to PEP 8 style guide."
print(long_line_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Function definition with too many parameters on a single line
# --------------------------------------------------------------
def example_function_violation(param1, param2, param3, param4, param5, param6, param7, param8):
    print(param1, param2, param3, param4, param5, param6, param7, param8)

example_function_violation(1, 2, 3, 4, 5, 6, 7, 8)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Keeping lines under 79 characters
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Long string split across multiple lines
# --------------------------------------------------------------
long_line_compliant = (
    "This is a properly formatted long line that is split into multiple lines "
    "so that it does not exceed the recommended 79 character limit."
)
print(long_line_compliant)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Function parameters split across multiple lines
# --------------------------------------------------------------
def example_function_compliant(
    param1, param2, param3, param4, param5, param6, param7, param8
):
    print(param1, param2, param3, param4, param5, param6, param7, param8)

example_function_compliant(1, 2, 3, 4, 5, 6, 7, 8)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using implicit line continuation inside parentheses
# --------------------------------------------------------------
numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
]
print(numbers)
