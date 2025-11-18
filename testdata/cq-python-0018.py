# =========================================================
# cq-python-0018: Type Checking
# This file includes violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using type() for direct comparison
# ---------------------------------------------------------

def process_value_violation(value):
    if type(value) == int:  # VIOLATION
        print("Integer detected (VIOLATION)")
    else:
        print("Not an integer (VIOLATION)")


process_value_violation(10)
process_value_violation(True)  # bool is subclass of int, but type() breaks this


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using type() to check for list instead of isinstance()
# ---------------------------------------------------------

def handle_collection_violation(collection):
    if type(collection) == list:  # VIOLATION
        print("Processing list (VIOLATION)")
    else:
        print("Not a list (VIOLATION)")


handle_collection_violation([1, 2, 3])
handle_collection_violation((1, 2, 3))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using isinstance() correctly (supports inheritance)
# ---------------------------------------------------------

def process_value_safe(value):
    if isinstance(value, int):  # COMPLIANT
        print("Integer detected (SAFE)")
    else:
        print("Not an integer (SAFE)")


process_value_safe(10)
process_value_safe(True)  # bool is subclass of int → handled correctly


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using isinstance() for collections
# ---------------------------------------------------------

def handle_collection_safe(collection):
    if isinstance(collection, (list, tuple)):  # COMPLIANT
        print("Processing collection (SAFE)")
    else:
        print("Not a supported collection (SAFE)")


handle_collection_safe([1, 2, 3])
handle_collection_safe((1, 2, 3))
