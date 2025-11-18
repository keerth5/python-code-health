# ===============================================================
# cq-python-0067: Logging Configuration
# This file contains both violating and compliant examples.
# ===============================================================

import logging

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using print statements for logging
# --------------------------------------------------------------
def process_data_violation(data):
    print("Violation - processing data:", data)  # VIOLATION: using print
    # ... processing ...

process_data_violation({"id": 1, "value": "test"})

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using logging without proper configuration
# --------------------------------------------------------------
logging.warning("Violation - something might be wrong")  # default config
logging.info("Violation - info message")  # may not show up depending on default level


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Proper logging configuration with levels
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Configure logging with basicConfig
# --------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,  # Set minimum log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("MyAppLogger")

logger.debug("Compliant 1 - debug message")  # Will not appear (level INFO)
logger.info("Compliant 1 - info message")
logger.warning("Compliant 1 - warning message")
logger.error("Compliant 1 - error message")
logger.critical("Compliant 1 - critical message")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using function-specific logging
# --------------------------------------------------------------
def process_data_safe(data):
    logger.info("Compliant 2 - processing data: %s", data)
    try:
        result = data["value"].upper()
        logger.debug("Compliant 2 - processed result: %s", result)
    except KeyError as e:
        logger.error("Compliant 2 - missing key in data: %s", e)
    return result if "value" in data else None

process_data_safe({"id": 2, "value": "hello"})
process_data_safe({"id": 3})
