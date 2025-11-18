# ======================================================
# cq-python-0002: SQL Injection Prevention
# This file contains both violating and compliant examples.
# ======================================================

import sqlite3

# Setup in-memory DB for demo
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER, name TEXT);")
cursor.executemany("INSERT INTO users VALUES (?, ?);", [(1, "Alice"), (2, "Bob")])
conn.commit()


# --------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Direct SQL concatenation with user input
# --------------------------------------------------
user_input = input("Enter user name: ")

query = "SELECT * FROM users WHERE name = '" + user_input + "'"  # VIOLATION: SQL Injection
try:
    cursor.execute(query)
    print("Query result:", cursor.fetchall())
except Exception as e:
    print("Error executing unsafe query:", e)


# --------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using f-strings for dynamic SQL with user data
# --------------------------------------------------
user_id = input("Enter user id: ")

query2 = f"SELECT * FROM users WHERE id = {user_id}"  # VIOLATION
try:
    cursor.execute(query2)
    print("Query result:", cursor.fetchall())
except Exception:
    print("Unsafe dynamic query failed")


# --------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Using format() for dynamic SQL
# --------------------------------------------------
table = input("Enter table name: ")

query3 = "SELECT * FROM {}".format(table)  # VIOLATION: User controls table name
try:
    cursor.execute(query3)
    print("Query result:", cursor.fetchall())
except Exception:
    print("Unsafe table query failed")


# --------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using parameterized queries
# --------------------------------------------------
safe_name = input("Enter user name (safe query): ")

cursor.execute("SELECT * FROM users WHERE name = ?", (safe_name,))  # SAFE
print("Safe query result:", cursor.fetchall())


# --------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using named parameters
# --------------------------------------------------
safe_id = input("Enter user id (safe): ")

cursor.execute("SELECT * FROM users WHERE id = :id", {"id": safe_id})  # SAFE
print("Safe named-param result:", cursor.fetchall())


# --------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Safe table access using whitelisted allowed tables
# --------------------------------------------------
allowed_tables = {"users"}

requested_table = input("Request table (users only): ")

if requested_table in allowed_tables:
    cursor.execute(f"SELECT * FROM {requested_table}")  # SAFE due to whitelist
    print("Whitelisted query result:", cursor.fetchall())
else:
    print("Table not allowed")
