# ===============================================================
# cq-python-0076: Four Space Indentation
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using tabs instead of 4 spaces
# --------------------------------------------------------------
def tab_indented_function():
\tprint("Violation - This line is indented with a tab")  # ❌ tab used
\tif True:
\t\tprint("Violation - Nested tab indentation")         # ❌ tab used

tab_indented_function()

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Mixing tabs and spaces
# --------------------------------------------------------------
def mixed_indentation():
    print("This line uses spaces")  # ✅ spaces
\tprint("Violation - This line uses a tab")  # ❌ tab mixed

mixed_indentation()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using 4 spaces per indentation level
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Standard 4-space indentation
# --------------------------------------------------------------
def space_indented_function():
    print("Compliant - 4 spaces for indentation")
    if True:
        print("Compliant - Nested block with 4 spaces")

space_indented_function()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Proper indentation in loops
# --------------------------------------------------------------
for i in range(3):
    print("Compliant - loop iteration", i)
    for j in range(2):
        print("Compliant - nested loop iteration", j)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Proper indentation in class methods
# --------------------------------------------------------------
class ExampleClass:
    def method(self):
        print("Compliant - method indented with 4 spaces")
        if True:
            print("Compliant - nested block with 4 spaces")

obj = ExampleClass()
obj.method()
