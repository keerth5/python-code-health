# =========================================================
# cq-python-0021: Database Connection Cleanup
# This file contains both violating and compliant examples.
# =========================================================

import sqlite3

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Cursor and connection never closed
# ---------------------------------------------------------

def fetch_users_violation():
    conn = sqlite3.connect("sample.db")  # Open connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")   # VIOLATION: no cleanup
    return cursor.fetchall()                # Both cursor and conn leak


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Closing only cursor but not connection
# ---------------------------------------------------------

def add_user_violation(name):
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users(name) VALUES (?)", (name,))
    cursor.close()     # Only cursor closed
    conn.commit()      # VIOLATION: connection never closed


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper cleanup using try-finally
# ---------------------------------------------------------

def fetch_users_safe():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()   # Proper cleanup


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using context manager for automatic cleanup
# ---------------------------------------------------------

def add_user_safe(name):
    # sqlite3 supports context managers for connection
    with sqlite3.connect("sample.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(name) VALUES (?)", (name,))
        # cursor is cleaned by connection context manager
    # conn closes automatically here


# ---------------------------------------------------------
# Execution for demonstration (optional)
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Violation output:", fetch_users_violation())
    print("Safe output:", fetch_users_safe())
