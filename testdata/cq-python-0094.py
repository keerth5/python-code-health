# ===============================================================
# cq-python-0094: String Methods
# This file contains both violating and compliant examples.
# ===============================================================

import string

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using string.upper() function
# --------------------------------------------------------------
text = "hello world"
upper_text_violation = string.capwords(text)  # ❌ using string module function
print("Violation - upper_text_violation:", upper_text_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using string functions for common operations
# --------------------------------------------------------------
text2 = "   hello   "
stripped_text_violation = string.whitespace.strip(text2) if hasattr(string, 'whitespace') else text2.strip()  # artificial example
print("Violation - stripped_text_violation:", stripped_text_violation)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using string methods directly
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use str.upper() or str.lower()
# --------------------------------------------------------------
text_clean = "hello world"
upper_text_clean = text_clean.upper()
print("Compliant - upper_text_clean:", upper_text_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Use str.strip() for removing whitespace
# --------------------------------------------------------------
text2_clean = "   hello   "
stripped_text_clean = text2_clean.strip()
print("Compliant - stripped_text_clean:", stripped_text_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Use str.replace() instead of string module functions
# --------------------------------------------------------------
text3 = "hello world"
replaced_text_clean = text3.replace("world", "Python")
print("Compliant - replaced_text_clean:", replaced_text_clean)
