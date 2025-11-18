# ===============================================================
# cq-python-0080: Blank Line Separation
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# No blank lines around functions
# --------------------------------------------------------------
def function_violation1():
    print("Violation - no blank line before function")
def function_violation2():
    print("Violation - no blank line between functions")

function_violation1()
function_violation2()

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# No blank lines around class definition
# --------------------------------------------------------------
class MyClassViolation:
    def method(self):
        print("Violation - class definition not separated by blank lines")

obj1 = MyClassViolation()
obj1.method()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Blank lines around functions and classes
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Blank line before and after function definitions
# --------------------------------------------------------------

def function_compliant1():
    print("Compliant - blank line before function")

def function_compliant2():
    print("Compliant - blank line between functions")

function_compliant1()
function_compliant2()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Blank line before and after class definitions
# --------------------------------------------------------------

class MyClassCompliant:
    def method(self):
        print("Compliant - blank line before class definition")

obj2 = MyClassCompliant()
obj2.method()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Multiple functions and classes separated by blank lines
# --------------------------------------------------------------

class AnotherClass:
    def __init__(self):
        print("Compliant - another class with blank lines")

def another_function():
    print("Compliant - another function with blank lines")

another_obj = AnotherClass()
another_obj.__init__()
another_function()
