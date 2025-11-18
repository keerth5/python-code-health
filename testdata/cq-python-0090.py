# ===============================================================
# cq-python-0090: Empty List Type
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using empty list literal []
# --------------------------------------------------------------
my_list = []  # ❌ using [] instead of list()
print("Violation - my_list type:", type(my_list))

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Function returning empty list literal
# --------------------------------------------------------------
def get_items():
    return []  # ❌ using [] instead of list()

items = get_items()
print("Violation - items type:", type(items))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using list() for empty lists
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Assigning empty list with list()
# --------------------------------------------------------------
my_list_clean = list()
print("Compliant - my_list_clean type:", type(my_list_clean))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Function returning empty list using list()
# --------------------------------------------------------------
def get_items_clean():
    """
    Return an empty list using list() for clarity and type consistency.
    """
    return list()

items_clean = get_items_clean()
print("Compliant - items_clean type:", type(items_clean))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Explicitly showing type with list()
# --------------------------------------------------------------
numbers: list[int] = list()
print("Compliant - numbers type:", type(numbers))
