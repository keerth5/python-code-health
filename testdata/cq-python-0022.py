# =========================================================
# cq-python-0022: No Wildcard Imports
# This file includes both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using wildcard import pollutes namespace
# ---------------------------------------------------------

from math import *   # VIOLATION — Avoid wildcard imports

value1 = sqrt(16)    # Works, but unclear where sqrt came from
print("Violation sqrt:", value1)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Wildcard import from local module
# ---------------------------------------------------------

# Assuming helpers.py exists
# from helpers import *    # VIOLATION — Unclear symbol origins


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Explicit imports from module
# ---------------------------------------------------------

from math import sqrt, pi  # Safe and explicit

value2 = sqrt(25)
print("Compliant sqrt:", value2)
print("Pi value:", pi)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Import module and use qualified names
# ---------------------------------------------------------

import math  # Safe and clear

value3 = math.cos(0)
print("Compliant cos:", value3)
