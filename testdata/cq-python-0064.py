# ===============================================================
# cq-python-0064: Constants Over Magic
# This file contains both violating and compliant examples.
# ===============================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using magic numbers directly
# --------------------------------------------------------------
def calculate_area_circle(radius):
    return 3.14159 * radius * radius  # VIOLATION: magic number for pi

print("Violation 1 - area of circle with radius 5:", calculate_area_circle(5))

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using literal values in code
# --------------------------------------------------------------
def total_cost(price, tax_rate):
    return price + price * 0.08  # VIOLATION: magic number 0.08

print("Violation 2 - total cost for 100:", total_cost(100, 0.08))


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using constants instead of magic numbers
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Define constant for pi
# --------------------------------------------------------------
PI = 3.14159

def calculate_area_circle_safe(radius: float) -> float:
    return PI * radius * radius

print("\nCompliant 1 - area of circle with radius 5:", calculate_area_circle_safe(5))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Define constant for tax rate
# --------------------------------------------------------------
TAX_RATE = 0.08

def total_cost_safe(price: float) -> float:
    return price + price * TAX_RATE

print("Compliant 2 - total cost for 100:", total_cost_safe(100))

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using multiple constants for readability
# --------------------------------------------------------------
MAX_RETRIES = 5
TIMEOUT_SECONDS = 30

def perform_request():
    for i in range(MAX_RETRIES):
        print(f"Attempt {i+1}/{MAX_RETRIES} with timeout {TIMEOUT_SECONDS} seconds")

perform_request()
