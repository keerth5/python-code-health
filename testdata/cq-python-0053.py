# ===============================================================
# cq-python-0053: Exception Logging
# This file contains both violating and compliant examples.
# ===============================================================

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Catching exception and ignoring it
# --------------------------------------------------------------
try:
    x = 10 / 0  # This will raise ZeroDivisionError
except ZeroDivisionError:
    pass  # VIOLATION: exception ignored silently

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Catching general exception without logging
# --------------------------------------------------------------
try:
    int("abc")  # ValueError
except Exception:  # VIOLATION
    print("An error occurred")  # Not proper logging


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Catch exceptions and log them properly
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Catch specific exception and log
# --------------------------------------------------------------
try:
    x = 10 / 0
except ZeroDivisionError as e:
    logger.error("Division by zero occurred: %s", e)  # SAFE


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Catch general exception with logging
# --------------------------------------------------------------
try:
    int("abc")
except Exception as e:
    logger.exception("Exception occurred while converting string to int")  # SAFE: logs traceback


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Logging in a function
# --------------------------------------------------------------
def read_file(file_path):
    try:
        with open(file_path) as f:
            return f.read()
    except FileNotFoundError as e:
        logger.error("File not found: %s", file_path)  # SAFE
        return None
    except Exception as e:
        logger.exception("Unexpected error reading file: %s", file_path)
        return None
