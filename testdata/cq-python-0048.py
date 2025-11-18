# ===============================================================
# cq-python-0048: Context Management
# This file contains both violating and compliant examples.
# ===============================================================

import threading
import sqlite3

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using lock without context manager
# --------------------------------------------------------------
lock = threading.Lock()

lock.acquire()  # VIOLATION: manual acquire/release
try:
    print("Critical section without context manager")
finally:
    lock.release()


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Database connection without context manager
# --------------------------------------------------------------
conn = sqlite3.connect(":memory:")  # VIOLATION: manual open/close
cursor = conn.cursor()
cursor.execute("CREATE TABLE test (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO test VALUES (?, ?)", (1, "Alice"))
conn.commit()
cursor.close()
conn.close()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using context managers for proper resource cleanup
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using lock as context manager
# --------------------------------------------------------------
lock2 = threading.Lock()
with lock2:
    print("Critical section with context manager")


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using database connection and cursor as context managers
# --------------------------------------------------------------
with sqlite3.connect(":memory:") as conn2:
    with conn2:
        with conn2.cursor() as cur:
            cur.execute("CREATE TABLE test2 (id INTEGER, name TEXT)")
            cur.execute("INSERT INTO test2 VALUES (?, ?)", (2, "Bob"))
            print("Database operations safely executed with context manager")


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Generic context manager with custom resource
# --------------------------------------------------------------
from contextlib import contextmanager

@contextmanager
def custom_resource(name):
    print(f"Acquiring resource {name}")
    try:
        yield name
    finally:
        print(f"Releasing resource {name}")


with custom_resource("Resource1") as res:
    print(f"Using {res} safely")
