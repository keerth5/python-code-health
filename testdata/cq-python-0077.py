# ===============================================================
# cq-python-0077: Snake Case Variables
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using camelCase for variable names
# --------------------------------------------------------------
myVariable = 10            # ❌ camelCase
AnotherVar = 20            # ❌ capitalized variable
print("Violation - myVariable:", myVariable, "AnotherVar:", AnotherVar)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using PascalCase for function names
# --------------------------------------------------------------
def MyFunction():
    print("Violation - function name uses PascalCase")

MyFunction()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using snake_case for variables and functions
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Variable names in snake_case
# --------------------------------------------------------------
my_variable = 10
another_var = 20
print("Compliant - my_variable:", my_variable, "another_var:", another_var)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Function names in snake_case
# --------------------------------------------------------------
def my_function():
    print("Compliant - function name uses snake_case")

my_function()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Multiple variables in snake_case
# --------------------------------------------------------------
first_value = 5
second_value = 15
total_sum = first_value + second_value
print("Compliant - total_sum:", total_sum)
