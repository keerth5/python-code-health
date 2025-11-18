# ===============================================================
# cq-python-0058: LRU Cache
# This file contains both violating and compliant examples.
# ===============================================================

import time
from functools import lru_cache

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Expensive recursive function without caching
# --------------------------------------------------------------
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)  # VIOLATION: recalculates repeatedly

start = time.time()
print("Violation 1 - fibonacci(20):", fibonacci(20))
print("Time taken (no cache):", time.time() - start, "seconds")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Function called repeatedly without memoization
# --------------------------------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # VIOLATION: recomputed every call
    return result

start = time.time()
for i in range(1, 21):
    factorial(i)
print("Violation 2 - factorial(20) repeated calls")
print("Time taken (no cache):", time.time() - start, "seconds")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using functools.lru_cache for caching expensive calls
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Memoized Fibonacci using lru_cache
# --------------------------------------------------------------
@lru_cache(maxsize=None)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

start = time.time()
print("\nCompliant 1 - fibonacci_cached(20):", fibonacci_cached(20))
print("Time taken (with lru_cache):", time.time() - start, "seconds")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Memoizing factorial using lru_cache
# --------------------------------------------------------------
@lru_cache(maxsize=None)
def factorial_cached(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

start = time.time()
for i in range(1, 21):
    factorial_cached(i)
print("Compliant 2 - factorial_cached(20) repeated calls")
print("Time taken (with lru_cache):", time.time() - start, "seconds")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using lru_cache with limited size
# --------------------------------------------------------------
@lru_cache(maxsize=5)
def square(n):
    return n * n

print("Compliant 3 - square(10):", square(10))
print("Compliant 4 - square(20):", square(20))
