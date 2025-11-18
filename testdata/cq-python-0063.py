# ===============================================================
# cq-python-0063: Type Hints
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Function without type hints
# --------------------------------------------------------------
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Violation 1 - add_numbers result:", result)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Function with ambiguous return type
# --------------------------------------------------------------
def greet(name):
    return "Hello " + name

print("Violation 2 - greet result:", greet("Alice"))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using type hints for function parameters and return type
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Type hints for simple function
# --------------------------------------------------------------
def add_numbers_safe(a: int, b: int) -> int:
    return a + b

result_safe = add_numbers_safe(5, 10)
print("\nCompliant 1 - add_numbers_safe result:", result_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Type hints for string function
# --------------------------------------------------------------
def greet_safe(name: str) -> str:
    return "Hello " + name

print("Compliant 2 - greet_safe result:", greet_safe("Alice"))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Type hints with optional and complex types
# --------------------------------------------------------------
from typing import List, Optional

def sum_list(numbers: List[int], start: Optional[int] = 0) -> int:
    total = start
    for num in numbers:
        total += num
    return total

print("Compliant 3 - sum_list result:", sum_list([1, 2, 3], start=5))
