# ===============================================================
# cq-python-0055: String Over Regex
# This file contains both violating and compliant examples.
# ===============================================================

import re

text = "Hello World! Welcome to Python 3.11."

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using regex to check prefix
# --------------------------------------------------------------
if re.match(r"Hello", text):  # VIOLATION
    print("Violation 1 - text starts with 'Hello' (using regex)")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using regex to check suffix
# --------------------------------------------------------------
if re.search(r"3\.11\.$", text):  # VIOLATION
    print("Violation 2 - text ends with '3.11.' (using regex)")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Using regex to replace simple substring
# --------------------------------------------------------------
text2 = re.sub(r"World", "Universe", text)  # VIOLATION
print("Violation 3 - replaced text (regex):", text2)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using string methods instead of regex
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using str.startswith()
# --------------------------------------------------------------
if text.startswith("Hello"):  # SAFE
    print("\nCompliant 1 - text starts with 'Hello' (string method)")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using str.endswith()
# --------------------------------------------------------------
if text.endswith("3.11."):  # SAFE
    print("Compliant 2 - text ends with '3.11.' (string method)")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using str.replace() for simple substring replacement
# --------------------------------------------------------------
text_safe = text.replace("World", "Universe")  # SAFE
print("Compliant 3 - replaced text (string method):", text_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 4
# Using str.find() or 'in' for containment checks
# --------------------------------------------------------------
if "Python" in text:  # SAFE
    print("Compliant 4 - text contains 'Python'")
