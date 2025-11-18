# ===============================================================
# cq-python-0089: Import Sorting
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Imports not alphabetically sorted
# --------------------------------------------------------------
import sys
import os
import datetime
print("Violation - imports not sorted")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Third-party imports not sorted
# --------------------------------------------------------------
import requests
import numpy
import pandas
print("Violation - third-party imports not sorted")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Alphabetically sorted imports within groups
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Standard library imports sorted
# --------------------------------------------------------------
import datetime
import os
import sys
print("Compliant - standard library imports sorted")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Third-party imports sorted alphabetically
# --------------------------------------------------------------
import numpy
import pandas
import requests
print("Compliant - third-party imports sorted")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Mixed imports grouped and sorted
# --------------------------------------------------------------
# Standard library
import datetime
import os
import sys

# Third-party
import numpy
import pandas
import requests

# Local modules
# from mymodule import helper   # Example local module

print("Compliant - all imports grouped and sorted")
