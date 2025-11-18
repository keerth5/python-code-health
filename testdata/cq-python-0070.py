# ===============================================================
# cq-python-0070: Connection Pooling
# This file contains both violating and compliant examples.
# ===============================================================

import sqlite3

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Creating a new database connection for every query
# --------------------------------------------------------------
def get_user_violation(user_id):
    conn = sqlite3.connect("example.db")  # ❌ new connection each time
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result

print("Violation - user 1:", get_user_violation(1))
print("Violation - user 2:", get_user_violation(2))  # ❌ inefficient repeated connections


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using connection pooling
# ===============================================================

# For demonstration, using sqlite3 + connection pool simulation
# In real apps, use libraries like psycopg2.pool (PostgreSQL), SQLAlchemy, or mysql.connector.pooling

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Reusing single connection (simple pool simulation)
# --------------------------------------------------------------
class SimpleConnectionPool:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)

    def get_connection(self):
        return self._conn  # reuse the same connection

pool = SimpleConnectionPool("example.db")

def get_user_safe(user_id):
    conn = pool.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE id=?", (user_id,))
    return cursor.fetchone()

print("\nCompliant - user 1:", get_user_safe(1))
print("Compliant - user 2:", get_user_safe(2))  # ✅ reuses connection

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using context manager with connection pool
# --------------------------------------------------------------
class ContextConnectionPool:
    def __init__(self, db_path):
        self._conn = sqlite3.connect(db_path)

    def __enter__(self):
        return self._conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Connection remains open for reuse
        pass

pool_ctx = ContextConnectionPool("example.db")

with pool_ctx as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    print("Compliant - user count:", cursor.fetchone()[0])
