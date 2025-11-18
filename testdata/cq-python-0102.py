# ===============================================================
# cq-python-0102: No Range Len
# This file contains both violating and compliant examples.
# ===============================================================

# Sample list
fruits = ["apple", "banana", "cherry"]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using range(len(...)) to iterate
# --------------------------------------------------------------
for i in range(len(fruits)):
    print("Violation - fruit:", fruits[i])

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using range(len(...)) with index for modification
# --------------------------------------------------------------
for i in range(len(fruits)):
    fruits[i] = fruits[i].upper()
print("Violation - modified fruits:", fruits)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Iterate directly over items
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Direct iteration over list
# --------------------------------------------------------------
for fruit in fruits:
    print("Compliant - fruit:", fruit)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using enumerate() when index is needed
# --------------------------------------------------------------
for index, fruit in enumerate(fruits):
    fruits[index] = fruit.upper()
print("Compliant - modified fruits with enumerate():", fruits)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Iterating over dictionary directly
# --------------------------------------------------------------
fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
for fruit, color in fruit_colors.items():
    print("Compliant -", fruit, "is", color)
