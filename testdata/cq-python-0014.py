# =========================================================
# cq-python-0014: Logging Over Print
# This file includes violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLES
# Using print() for application logging
# ---------------------------------------------------------

def process_data_violation(data):
    print("Processing data...")  # VIOLATION
    result = data * 2
    print("Result is:", result)  # VIOLATION
    return result


def handle_error_violation():
    try:
        1 / 0
    except Exception as e:
        print("An error occurred:", e)  # VIOLATION


# Running violation examples
process_data_violation(5)
handle_error_violation()


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLES
# Using logging instead of print
# ---------------------------------------------------------

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_data_compliant(data):
    logging.info("Processing data...")  # COMPLIANT
    result = data * 2
    logging.debug(f"Computed result: {result}")  # COMPLIANT
    return result


def handle_error_compliant():
    try:
        1 / 0
    except ZeroDivisionError as e:
        logging.error("Error encountered", exc_info=True)  # COMPLIANT


# Running compliant examples
process_data_compliant(10)
handle_error_compliant()
