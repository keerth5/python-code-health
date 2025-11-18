# ===============================================================
# cq-python-0088: Import Cleanup
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Unused imports
# --------------------------------------------------------------
import os       # ❌ imported but not used
import sys      # ❌ imported but not used
import math     # ❌ imported but not used
from datetime import datetime   # ❌ imported but not used

print("Violation - this code has unused imports")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Some used, some unused imports
# --------------------------------------------------------------
import random   # ❌ imported but not used
import json     # ✅ used
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print("Violation - random import is unused:", json_str)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Only used imports remain
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Only imports that are used
# --------------------------------------------------------------
import json
data_clean = {"name": "Bob", "age": 25}
json_string = json.dumps(data_clean)
print("Compliant - json_string:", json_string)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using datetime import
# --------------------------------------------------------------
from datetime import datetime
current_time = datetime.now()
print("Compliant - current_time:", current_time)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using math import
# --------------------------------------------------------------
import math
circle_radius = 5
circle_area = math.pi * (circle_radius ** 2)
print("Compliant - circle_area:", circle_area)
