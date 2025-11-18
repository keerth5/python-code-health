# ===============================================================
# cq-python-0081: No Trailing Whitespace
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Trailing spaces at the end of lines
# --------------------------------------------------------------
x = 10     # ❌ trailing spaces
y = 20\t  # ❌ trailing tab character
print(x + y)   

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Trailing whitespace in function
# --------------------------------------------------------------
def function_violation():
    a = 5     
    b = 10\t
    print(a + b)    

function_violation()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# No trailing whitespace
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Clean variable assignments
# --------------------------------------------------------------
x_clean = 10
y_clean = 20
print(x_clean + y_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Clean function body
# --------------------------------------------------------------
def function_compliant():
    a = 5
    b = 10
    print(a + b)

function_compliant()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Proper spacing in loops
# --------------------------------------------------------------
for i in range(3):
    print("Iteration:", i)
