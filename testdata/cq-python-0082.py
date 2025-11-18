# ===============================================================
# cq-python-0082: Consistent Quotes
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Mixing single and double quotes
# --------------------------------------------------------------
message1 = "Hello World"   # ❌ uses double quotes
message2 = 'Hello Again'   # ❌ inconsistent quotes
print(message1, message2)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using double quotes unnecessarily
# --------------------------------------------------------------
def greet_violation(name):
    print("Hello, " + name + "!")  # ❌ uses double quotes

greet_violation("Alice")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using single quotes consistently
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Single quotes for variable strings
# --------------------------------------------------------------
message1_clean = 'Hello World'
message2_clean = 'Hello Again'
print(message1_clean, message2_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Single quotes in functions
# --------------------------------------------------------------
def greet_compliant(name):
    print('Hello, ' + name + '!')

greet_compliant('Alice')

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Single quotes in longer strings
# --------------------------------------------------------------
long_message = (
    'This is a longer message that uses single quotes consistently '
    'and adheres to PEP 8 style guidelines.'
)
print(long_message)
