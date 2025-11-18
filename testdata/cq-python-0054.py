# ===============================================================
# cq-python-0054: Structured Data
# This file contains both violating and compliant examples.
# ===============================================================

from collections import namedtuple
from dataclasses import dataclass

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using plain tuples for structured data
# --------------------------------------------------------------
person1 = ("Alice", 25, "Engineer")  # VIOLATION
person2 = ("Bob", 30, "Designer")    # VIOLATION

# Accessing by index (not readable)
print("Violation 1 - person1 name:", person1[0])
print("Violation 2 - person2 age:", person2[1])

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# List of tuples
# --------------------------------------------------------------
people = [("Charlie", 28, "Manager"), ("Diana", 35, "Architect")]  # VIOLATION
for p in people:
    print("Violation 3 - person role:", p[2])


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using namedtuple and dataclass for structured data
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using namedtuple
# --------------------------------------------------------------
Person = namedtuple("Person", ["name", "age", "role"])
person_named1 = Person("Alice", 25, "Engineer")
person_named2 = Person("Bob", 30, "Designer")

print("\nCompliant 1 - person_named1 name:", person_named1.name)
print("Compliant 2 - person_named2 role:", person_named2.role)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# List of namedtuples
# --------------------------------------------------------------
people_named = [
    Person("Charlie", 28, "Manager"),
    Person("Diana", 35, "Architect")
]
for p in people_named:
    print("Compliant 3 - person role:", p.role)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using dataclasses
# --------------------------------------------------------------
@dataclass
class PersonData:
    name: str
    age: int
    role: str

person_data1 = PersonData("Eve", 29, "Analyst")
person_data2 = PersonData("Frank", 32, "Consultant")

print("Compliant 4 - person_data1 age:", person_data1.age)
print("Compliant 5 - person_data2 name:", person_data2.name)
