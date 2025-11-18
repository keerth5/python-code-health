# =========================================================
# cq-python-0010: No Mutable Defaults
# This file includes both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Mutable list as default argument
# ---------------------------------------------------------

def add_item_violation(item, my_list=[]):  # VIOLATION: mutable default
    my_list.append(item)
    return my_list

print("Violation 1 Output:")
print(add_item_violation("apple"))
print(add_item_violation("banana"))  # Unexpectedly retains previous state


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Mutable dict used in default args
# ---------------------------------------------------------

def register_user_violation(name, flags={"active": True}):  # VIOLATION
    flags["last_user"] = name
    return flags

print("\nViolation 2 Output:")
print(register_user_violation("user1"))
print(register_user_violation("user2"))  # Uses shared dict


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use None as default and initialize inside function
# ---------------------------------------------------------

def add_item_safe(item, my_list=None):
    if my_list is None:
        my_list = []  # Fresh list each call
    my_list.append(item)
    return my_list

print("\nCompliant 1 Output:")
print(add_item_safe("apple"))
print(add_item_safe("banana"))  # No shared state


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Correct handling of dict defaults
# ---------------------------------------------------------

def register_user_safe(name, flags=None):
    if flags is None:
        flags = {"active": True}
    flags["last_user"] = name
    return flags

print("\nCompliant 2 Output:")
print(register_user_safe("user1"))
print(register_user_safe("user2"))  # No shared state
