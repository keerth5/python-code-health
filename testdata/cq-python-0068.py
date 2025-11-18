# ===============================================================
# cq-python-0068: Generator Memory
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Creating large list in memory
# --------------------------------------------------------------
def process_numbers_violation():
    numbers = [i for i in range(1_000_000)]  # VIOLATION: loads all numbers into memory
    total = sum(numbers)
    print("Violation 1 - total sum:", total)

process_numbers_violation()

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Returning entire list from function
# --------------------------------------------------------------
def get_squares_violation(n):
    return [i*i for i in range(n)]  # VIOLATION: list stored entirely in memory

squares = get_squares_violation(1_000_000)
print("Violation 2 - first 5 squares:", squares[:5])


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using generators for memory-efficient processing
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Generator expression for lazy evaluation
# --------------------------------------------------------------
def process_numbers_safe():
    numbers = (i for i in range(1_000_000))  # generator, does not load all in memory
    total = sum(numbers)
    print("\nCompliant 1 - total sum using generator:", total)

process_numbers_safe()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Generator function for producing data on the fly
# --------------------------------------------------------------
def get_squares_safe(n):
    for i in range(n):
        yield i*i  # yields one value at a time

squares_gen = get_squares_safe(1_000_000)
# Use next() or iterate without storing all in memory
print("Compliant 2 - first 5 squares using generator:", [next(squares_gen) for _ in range(5)])

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Streaming processing of large dataset
# --------------------------------------------------------------
def process_large_file(file_path):
    with open(file_path, "r") as f:
        for line in f:  # generator over file lines
            yield line.strip()

# Example usage (commented since no actual file)
# for line in process_large_file("large_file.txt"):
#     print(line)
