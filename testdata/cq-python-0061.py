# ===============================================================
# cq-python-0061: Thread Lock Context
# This file contains both violating and compliant examples.
# ===============================================================

import threading
import time

counter = 0
lock = threading.Lock()

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Acquiring and releasing lock manually
# --------------------------------------------------------------
def increment_violation():
    global counter
    for _ in range(1000):
        lock.acquire()  # VIOLATION: manual acquire
        try:
            counter += 1
        finally:
            lock.release()  # manual release

threads = [threading.Thread(target=increment_violation) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("Violation 1 - counter value with manual lock:", counter)


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Forgetting to release lock (can cause deadlock)
# --------------------------------------------------------------
def unsafe_increment():
    global counter
    for _ in range(10):
        lock.acquire()  # VIOLATION: no release in exception case
        counter += 1

t = threading.Thread(target=unsafe_increment)
t.start()
t.join()
print("Violation 2 - unsafe increment could cause deadlock")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using threading.Lock() as context manager
# ===============================================================

# Reset counter
counter_safe = 0
lock_safe = threading.Lock()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using 'with' statement for lock
# --------------------------------------------------------------
def increment_safe():
    global counter_safe
    for _ in range(1000):
        with lock_safe:  # SAFE: context manager handles acquire/release
            counter_safe += 1

threads_safe = [threading.Thread(target=increment_safe) for _ in range(5)]
for t in threads_safe:
    t.start()
for t in threads_safe:
    t.join()

print("\nCompliant 1 - counter value with lock context manager:", counter_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Thread-safe function with automatic release
# --------------------------------------------------------------
def safe_print(message):
    with lock_safe:
        print(message)

threads_print = [threading.Thread(target=safe_print, args=(f"Message {i}",)) for i in range(5)]
for t in threads_print:
    t.start()
for t in threads_print:
    t.join()

print("Compliant 2 - safe_print executed in multiple threads")
