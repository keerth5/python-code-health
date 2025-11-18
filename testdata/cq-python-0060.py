# ===============================================================
# cq-python-0060: Class Slots
# This file contains both violating and compliant examples.
# ===============================================================

import sys

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Regular class without __slots__
# --------------------------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print("Violation 1 - memory size of instance p1:", sys.getsizeof(p1))

# Adding dynamic attributes increases memory
p1.address = "123 Main St"
p2.phone = "555-1234"
print("Violation 2 - dynamic attributes allowed without __slots__")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using __slots__ to reduce memory usage
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Class with __slots__ defined
# --------------------------------------------------------------
class PersonSlots:
    __slots__ = ("name", "age")  # Only these attributes are allowed

    def __init__(self, name, age):
        self.name = name
        self.age = age

p_slots1 = PersonSlots("Charlie", 28)
p_slots2 = PersonSlots("Diana", 32)

print("\nCompliant 1 - memory size of instance p_slots1:", sys.getsizeof(p_slots1))

# Attempting to add dynamic attribute raises AttributeError
try:
    p_slots1.address = "456 Elm St"  # SAFE: will raise error
except AttributeError as e:
    print("Compliant 2 - cannot add dynamic attribute:", e)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using __slots__ with inheritance
# --------------------------------------------------------------
class Employee(PersonSlots):
    __slots__ = ("role",)

    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role

e1 = Employee("Eve", 29, "Analyst")
print("Compliant 3 - Employee role:", e1.role)
