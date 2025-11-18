# ================================
# cq-python-0000: No Eval Execution
# This file contains both violating and compliant examples.
# ================================

# -------------------------
# ❌ VIOLATION EXAMPLE 1
# Direct eval() on user input
# -------------------------
user_input = input("Enter a Python expression: ")
result = eval(user_input)  # VIOLATION: Dangerous use of eval()
print("Result:", result)


# -------------------------
# ❌ VIOLATION EXAMPLE 2
# eval() used inside a vulnerable API wrapper
# -------------------------
def compute_expression(expr):
    return eval(expr)  # VIOLATION

print(compute_expression("2 + 3"))


# -------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using safe parsing via ast.literal_eval
# -------------------------
import ast

user_data = input("Enter a list (e.g., [1,2,3]): ")

try:
    parsed_data = ast.literal_eval(user_data)  # SAFE
    print("Parsed safely:", parsed_data)
except Exception:
    print("Invalid input")


# -------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using safer alternatives (e.g., int conversion)
# -------------------------
user_number = input("Enter a number: ")

try:
    num = int(user_number)  # SAFE, avoids eval entirely
    print("Valid number:", num)
except ValueError:
    print("Not a valid number")
