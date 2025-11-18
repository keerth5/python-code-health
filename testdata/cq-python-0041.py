# =========================================================
# cq-python-0041: F-String Formatting
# This file contains both violating and compliant examples.
# =========================================================

name = "Alice"
age = 28

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using percent (%) formatting
# ---------------------------------------------------------
msg_violation_1 = "User %s is %d years old." % (name, age)
print(msg_violation_1)  # VIOLATION


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using str.format()
# ---------------------------------------------------------
msg_violation_2 = "User {} is {} years old.".format(name, age)
print(msg_violation_2)  # VIOLATION


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using f-strings (recommended)
# ---------------------------------------------------------
msg_safe_1 = f"User {name} is {age} years old."
print(msg_safe_1)  # COMPLIANT


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# f-strings with expressions
# ---------------------------------------------------------
msg_safe_2 = f"Next year, {name} will be {age + 1}."
print(msg_safe_2)  # COMPLIANT
