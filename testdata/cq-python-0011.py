# =========================================================
# cq-python-0011: Context Managers for File Operations
# This file includes both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Opening a file without closing it
# ---------------------------------------------------------

def read_file_violation():
    f = open("data_violation.txt", "w")  # VIOLATION
    f.write("This file is never properly closed.")  # Resource leak
    # No f.close()


read_file_violation()


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Manual try–finally without using 'with'
# ---------------------------------------------------------

def manual_handling_violation():
    f = open("manual_violation.txt", "w")  # VIOLATION
    try:
        f.write("Using try/finally but missing context manager.")
    finally:
        f.close()  # Still discouraged; 'with' is preferred


manual_handling_violation()


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using 'with' for safe file writing
# ---------------------------------------------------------

def write_file_safe():
    with open("data_safe.txt", "w") as f:  # SAFE
        f.write("This file is safely handled using context manager.")


write_file_safe()


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using 'with' for reading
# ---------------------------------------------------------

def read_file_safe():
    with open("data_safe.txt", "r") as f:  # SAFE
        content = f.read()
        print("Compliant Read:", content)


read_file_safe()
