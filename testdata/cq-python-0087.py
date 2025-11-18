# ===============================================================
# cq-python-0087: Meaningful Names
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Single-letter variable names
# --------------------------------------------------------------
a = 5
b = 10
c = a + b
print("Violation - c:", c)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Single-letter loop variables with unclear purpose
# --------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]
s = 0
for n in numbers:
    s += n
print("Violation - sum:", s)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Meaningful variable names
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Variables with meaningful names
# --------------------------------------------------------------
first_number = 5
second_number = 10
sum_result = first_number + second_number
print("Compliant - sum_result:", sum_result)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Meaningful loop variables
# --------------------------------------------------------------
numbers_list = [1, 2, 3, 4, 5]
total_sum = 0
for number in numbers_list:
    total_sum += number
print("Compliant - total_sum:", total_sum)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Meaningful names in functions
# --------------------------------------------------------------
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    area = length * width
    return area

rect_area = calculate_area(5, 10)
print("Compliant - rect_area:", rect_area)
