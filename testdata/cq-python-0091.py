# ===============================================================
# cq-python-0091: Handle Empty Except
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Empty except block
# --------------------------------------------------------------
try:
    result = 10 / 0
except:  # ❌ empty except block, silently ignores error
    pass

print("Violation - empty except block ignored an error")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Catching exception without handling
# --------------------------------------------------------------
try:
    open("non_existent_file.txt", "r")
except Exception:  # ❌ exception caught but nothing done
    pass


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Properly handle exceptions
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Catch specific exception and log it
# --------------------------------------------------------------
try:
    result_clean = 10 / 0
except ZeroDivisionError as e:
    print("Compliant - Caught ZeroDivisionError:", e)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Catch exception and take action
# --------------------------------------------------------------
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print("Compliant - file not found:", e)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Re-raise exception after logging
# --------------------------------------------------------------
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Compliant - Error occurred:", e)
        raise  # re-raise after logging

try:
    divide_numbers(5, 0)
except ZeroDivisionError:
    print("Handled re-raised ZeroDivisionError")
