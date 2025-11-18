# =========================================================
# cq-python-0025: Thread Synchronization
# Contains both violating and compliant code examples.
# =========================================================

import threading
import time

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Shared mutable variable modified by multiple threads
# without any locking → Race Condition
# ---------------------------------------------------------

counter = 0  # shared resource

def increment_violation():
    global counter
    for _ in range(10000):
        counter += 1  # VIOLATION: no lock used

threads = []
for _ in range(5):
    t = threading.Thread(target=increment_violation)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Violation Counter Result (race condition likely):", counter)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple threads appending to a list unsafely
# ---------------------------------------------------------

shared_list = []

def append_violation(value):
    for _ in range(5000):
        shared_list.append(value)  # VIOLATION: not synchronized

threads = [threading.Thread(target=append_violation, args=(i,)) for i in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Violation List Length (inconsistent):", len(shared_list))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using threading.Lock() to protect critical section
# ---------------------------------------------------------

counter_safe = 0
lock = threading.Lock()

def increment_safe():
    global counter_safe
    for _ in range(10000):
        with lock:
            counter_safe += 1  # SAFE: protected by lock

threads = []
for _ in range(5):
    t = threading.Thread(target=increment_safe)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Compliant Counter Result:", counter_safe)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using Lock for list operations
# ---------------------------------------------------------

safe_list = []
list_lock = threading.Lock()

def append_safe(value):
    for _ in range(5000):
        with list_lock:
            safe_list.append(value)  # SAFE

threads = [threading.Thread(target=append_safe, args=(i,)) for i in range(3)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Compliant List Length:", len(safe_list))
