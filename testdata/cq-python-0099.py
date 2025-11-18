# ===============================================================
# cq-python-0099: Raw String Regex
# This file contains both violating and compliant examples.
# ===============================================================

import re

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using normal string with backslashes in regex
# --------------------------------------------------------------
pattern_violation = "\\d+\\w+"  # ❌ should use raw string
text = "123abc"
match_violation = re.match(pattern_violation, text)
print("Violation - match:", match_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using normal string with escape sequences
# --------------------------------------------------------------
pattern_violation2 = "\bword\b"  # ❌ backslashes interpreted incorrectly
text2 = "word boundary"
match_violation2 = re.search(pattern_violation2, text2)
print("Violation - search:", match_violation2)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use raw strings for regular expressions
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using raw string for regex
# --------------------------------------------------------------
pattern_clean = r"\d+\w+"
match_clean = re.match(pattern_clean, text)
print("Compliant - match:", match_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using raw string for word boundary regex
# --------------------------------------------------------------
pattern_clean2 = r"\bword\b"
match_clean2 = re.search(pattern_clean2, text2)
print("Compliant - search:", match_clean2)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using raw string for complex regex
# --------------------------------------------------------------
pattern_clean3 = r"^\w+@\w+\.\w+$"
email = "user@example.com"
match_clean3 = re.match(pattern_clean3, email)
print("Compliant - email match:", match_clean3)
