# =========================================================
# cq-python-0028: Proper Cleanup
# This file contains both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Missing cleanup for opened file
# ---------------------------------------------------------

def read_file_violation(path):
    f = open(path, "r")      # Resource opened
    data = f.read()          # No cleanup, no close()
    return data              # VIOLATION: leaked file handle


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Missing finally block for risky operation
# ---------------------------------------------------------

def process_file_violation(path):
    f = open(path, "r")
    data = f.read()
    risky = 10 / 0           # Exception thrown → file remains open
    f.close()                # Not reached → VIOLATION
    return data


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use try/finally to ensure cleanup
# ---------------------------------------------------------

def read_file_safe(path):
    f = open(path, "r")
    try:
        return f.read()
    finally:
        f.close()            # Guaranteed cleanup


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Use context manager (best practice)
# ---------------------------------------------------------

def read_file_best(path):
    with open(path, "r") as f:
        return f.read()      # Auto cleanup on exit


# ---------------------------------------------------------
# Test Calls (ignored by scanners)
# ---------------------------------------------------------

if __name__ == "__main__":
    try:
        print(read_file_violation("test.txt"))
    except Exception as e:
        print("Violation 1 error:", e)

    try:
        print(process_file_violation("test.txt"))
    except Exception as e:
        print("Violation 2 error:", e)

    print(read_file_safe("test.txt"))
    print(read_file_best("test.txt"))
