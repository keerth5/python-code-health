# =========================================================
# cq-python-0016: Exception Chaining
# This file contains both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Raising a new exception without preserving the original
# ---------------------------------------------------------

def process_data_violation():
    try:
        int("abc")  # Causes ValueError
    except ValueError:
        # Losing original exception context
        raise RuntimeError("Failed to process data")  # VIOLATION


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using bare 'raise' incorrectly outside of except context
# ---------------------------------------------------------

def compute_value_violation():
    try:
        result = 1 / 0
    except Exception:
        raise Exception("Computation failed")  # VIOLATION – missing 'from e'


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper exception chaining using `raise ... from ...`
# ---------------------------------------------------------

def process_data_compliant():
    try:
        int("abc")
    except ValueError as e:
        raise RuntimeError("Failed to process data") from e  # COMPLIANT


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Wrapping lower-level errors with preserved context
# ---------------------------------------------------------

def compute_value_compliant():
    try:
        result = 1 / 0
    except ZeroDivisionError as err:
        raise ArithmeticError("Division error encountered") from err  # COMPLIANT


# ---------------------------------------------------------
# Execute examples (optional demonstration)
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Running compliant and violation examples...\n")

    try:
        process_data_violation()
    except Exception as ex:
        print("Violation 1 caught:", ex, "\n")

    try:
        compute_value_violation()
    except Exception as ex:
        print("Violation 2 caught:", ex, "\n")

    try:
        process_data_compliant()
    except Exception as ex:
        print("Compliant 1 caught (with chaining):", ex, "\n")

    try:
        compute_value_compliant()
    except Exception as ex:
        print("Compliant 2 caught (with chaining):", ex, "\n")
