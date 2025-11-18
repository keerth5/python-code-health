# ===============================================================
# cq-python-0097: Avoid Nested Functions
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Nested function inside another function unnecessarily
# --------------------------------------------------------------
def outer_function_violation(x):
    def inner_function(y):  # ❌ nested function not needed
        return y * 2
    return inner_function(x)

print("Violation - nested function result:", outer_function_violation(5))

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple nested functions
# --------------------------------------------------------------
def process_list_violation(lst):
    def double_items(sublist):
        return [i * 2 for i in sublist]

    def sum_items(sublist):
        return sum(sublist)

    doubled = double_items(lst)
    return sum_items(doubled)

print("Violation - nested functions sum result:", process_list_violation([1, 2, 3]))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Avoid unnecessary nested functions
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Define functions separately
# --------------------------------------------------------------
def double_number(x):
    return x * 2

def process_number(x):
    return double_number(x)

print("Compliant - processed number:", process_number(5))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Separate processing functions for lists
# --------------------------------------------------------------
def double_items(lst):
    return [i * 2 for i in lst]

def sum_items(lst):
    return sum(lst)

def process_list(lst):
    doubled = double_items(lst)
    return sum_items(doubled)

print("Compliant - processed list sum:", process_list([1, 2, 3]))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Use higher-order functions if necessary
# --------------------------------------------------------------
numbers = [1, 2, 3, 4]
doubled_numbers = list(map(lambda x: x * 2, numbers))  # acceptable for small anonymous logic
print("Compliant - doubled numbers with map:", doubled_numbers)
