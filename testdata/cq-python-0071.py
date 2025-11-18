# ===============================================================
# cq-python-0071: Caching Strategies
# This file contains both violating and compliant examples.
# ===============================================================

import time
from functools import lru_cache

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Recomputing expensive function every call
# --------------------------------------------------------------
def expensive_computation_violation(n):
    time.sleep(1)  # Simulate expensive computation
    return n * n

start = time.time()
print("Violation - result 1:", expensive_computation_violation(5))
print("Violation - result 2:", expensive_computation_violation(5))  # ❌ recomputed
end = time.time()
print("Violation - total time:", end - start, "seconds")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using caching for expensive operations
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using functools.lru_cache for caching
# --------------------------------------------------------------
@lru_cache(maxsize=None)
def expensive_computation_safe(n):
    time.sleep(1)  # Simulate expensive computation
    return n * n

start = time.time()
print("\nCompliant - result 1:", expensive_computation_safe(5))
print("Compliant - result 2:", expensive_computation_safe(5))  # ✅ cached
end = time.time()
print("Compliant - total time with caching:", end - start, "seconds")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Manual caching using dictionary
# --------------------------------------------------------------
cache = {}

def expensive_computation_manual(n):
    if n in cache:
        return cache[n]
    time.sleep(1)
    result = n * n
    cache[n] = result
    return result

print("Compliant - manual cache result 1:", expensive_computation_manual(6))
print("Compliant - manual cache result 2:", expensive_computation_manual(6))  # ✅ cached

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Caching results for I/O-bound operations
# --------------------------------------------------------------
file_content_cache = {}

def read_file_cached(file_path):
    if file_path in file_content_cache:
        return file_content_cache[file_path]
    with open(file_path, "r") as f:
        content = f.read()
        file_content_cache[file_path] = content
        return content

# Example usage (file not actually required)
# print("Compliant - file content:", read_file_cached("example.txt"))
