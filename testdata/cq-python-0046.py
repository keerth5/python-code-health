# ===============================================================
# cq-python-0046: Generator Expressions
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Creating a full list unnecessarily before iteration
# --------------------------------------------------------------
numbers = range(1, 1000000)

# Creates an intermediate list in memory (inefficient)
squares = [n * n for n in numbers]  # VIOLATION

total = 0
for sq in squares:
    total += sq
print("Violation 1 - sum of squares:", total)


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using map() to generate a list explicitly
# --------------------------------------------------------------
words = ["apple", "banana", "cherry", "date"]

# Wrap map() in list unnecessarily
uppercase_words = list(map(str.upper, words))  # VIOLATION
for w in uppercase_words:
    print("Violation 2 - uppercase word:", w)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use generator expressions or iterators to avoid intermediate lists
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using generator expression with sum()
# --------------------------------------------------------------
total_safe = sum(n * n for n in numbers)  # SAFE: no intermediate list
print("\nCompliant 1 - sum of squares (generator):", total_safe)


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using generator in a for loop
# --------------------------------------------------------------
for word in (w.upper() for w in words):  # SAFE: generator expression
    print("Compliant 2 - uppercase word (generator):", word)


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using map() as an iterator without converting to list
# --------------------------------------------------------------
for w in map(str.upper, words):  # SAFE
    print("Compliant 3 - uppercase word (map iterator):", w)
