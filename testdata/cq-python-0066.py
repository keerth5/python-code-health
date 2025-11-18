# ===============================================================
# cq-python-0066: Appropriate Data Structures
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using list for membership testing (O(n) lookup)
# --------------------------------------------------------------
fruits = ["apple", "banana", "cherry", "date"]
if "banana" in fruits:  # VIOLATION: list lookup is O(n)
    print("Violation 1 - banana found")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using list to count unique elements
# --------------------------------------------------------------
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:  # VIOLATION: O(n^2) operation
        unique_numbers.append(num)
print("Violation 2 - unique numbers:", unique_numbers)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using appropriate data structures
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using set for membership testing (O(1) lookup)
# --------------------------------------------------------------
fruit_set = {"apple", "banana", "cherry", "date"}
if "banana" in fruit_set:  # SAFE: set lookup is O(1)
    print("\nCompliant 1 - banana found in set")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using set to get unique elements efficiently
# --------------------------------------------------------------
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers_safe = set(numbers)  # O(n) operation
print("Compliant 2 - unique numbers using set:", unique_numbers_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using dict for key-value mapping instead of list of tuples
# --------------------------------------------------------------
students = [("Alice", 90), ("Bob", 85), ("Charlie", 92)]
student_scores = {name: score for name, score in students}  # O(1) lookup
print("Compliant 3 - Bob's score:", student_scores.get("Bob"))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 4
# Using deque for fast append/pop operations on both ends
# --------------------------------------------------------------
from collections import deque

queue = deque()
queue.append("task1")
queue.append("task2")
queue.appendleft("task0")  # Efficient prepend
print("Compliant 4 - queue state:", queue)
