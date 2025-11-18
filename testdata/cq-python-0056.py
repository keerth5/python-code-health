# ===============================================================
# cq-python-0056: Slice Assignment
# This file contains both violating and compliant examples.
# ===============================================================

# Sample list
numbers = [1, 2, 3, 4, 5]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using del and insert to replace elements
# --------------------------------------------------------------
del numbers[1:3]  # remove elements 2 and 3
numbers.insert(1, 20)  # insert new element 20
numbers.insert(2, 30)  # insert new element 30
print("Violation 1 - modified list using del + insert:", numbers)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using loop with del/append for replacing multiple elements
# --------------------------------------------------------------
numbers2 = [10, 20, 30, 40, 50]
for i in range(1, 3):
    del numbers2[1]  # remove indices 1 and 2
numbers2.insert(1, 25)
numbers2.insert(2, 35)
print("Violation 2 - modified list with loop del + insert:", numbers2)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using slice assignment for list modifications
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Replacing multiple elements with slice assignment
# --------------------------------------------------------------
numbers3 = [1, 2, 3, 4, 5]
numbers3[1:3] = [20, 30]  # SAFE: replaces elements 2 and 3
print("\nCompliant 1 - modified list using slice assignment:", numbers3)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Deleting multiple elements using slice assignment
# --------------------------------------------------------------
numbers4 = [10, 20, 30, 40, 50]
numbers4[1:3] = []  # SAFE: removes elements at indices 1 and 2
print("Compliant 2 - deleted elements using slice assignment:", numbers4)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Inserting multiple elements using slice assignment
# --------------------------------------------------------------
numbers5 = [1, 4, 5]
numbers5[1:1] = [2, 3]  # SAFE: insert 2,3 at index 1
print("Compliant 3 - inserted elements using slice assignment:", numbers5)
