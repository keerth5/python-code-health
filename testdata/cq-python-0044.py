# =========================================================
# cq-python-0044: Dict Get Method
# This file contains both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Manual key existence check
# ---------------------------------------------------------

data = {"name": "Alice", "age": 30}

if "age" in data:  # VIOLATION
    age_value = data["age"]
else:
    age_value = 0

print("Violation 1 Age:", age_value)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using try/except KeyError instead of default
# ---------------------------------------------------------

try:
    city = data["city"]  # VIOLATION
except KeyError:
    city = "Unknown"

print("Violation 2 City:", city)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using dict.get() with a default value
# ---------------------------------------------------------

age_safe = data.get("age", 0)
print("Compliant 1 Age:", age_safe)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using dict.get() with missing key
# ---------------------------------------------------------

city_safe = data.get("city", "Unknown")
print("Compliant 2 City:", city_safe)
