# ===============================================================
# cq-python-0078: Camel Case Classes
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using snake_case for class name
# --------------------------------------------------------------
class my_class_violation:
    def __init__(self):
        print("Violation - class name uses snake_case")

obj1 = my_class_violation()

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using lowercase or all caps for class name
# --------------------------------------------------------------
class anotherclass:
    def __init__(self):
        print("Violation - class name uses all lowercase")

obj2 = anotherclass()

class CLASSNAME:
    def __init__(self):
        print("Violation - class name uses all caps")

obj3 = CLASSNAME()


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using CamelCase for class names
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Standard CamelCase class
# --------------------------------------------------------------
class MyClass:
    def __init__(self):
        print("Compliant - class name uses CamelCase")

obj4 = MyClass()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# CamelCase class with multiple words
# --------------------------------------------------------------
class CustomerAccountManager:
    def __init__(self):
        print("Compliant - multi-word CamelCase class")

obj5 = CustomerAccountManager()

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# CamelCase class with inheritance
# --------------------------------------------------------------
class BaseClass:
    def __init__(self):
        print("Compliant - BaseClass initialized")

class DerivedClass(BaseClass):
    def __init__(self):
        super().__init__()
        print("Compliant - DerivedClass initialized")

obj6 = DerivedClass()
