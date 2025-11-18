# =========================================================
# cq-python-0029: No Exec Execution
# This file contains both violating and compliant examples.
# =========================================================

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Direct exec() on user input (remote code execution risk)
# ---------------------------------------------------------

user_code = input("Enter Python code: ")
exec(user_code)  # VIOLATION: Dangerous use of exec()


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# exec used inside a function with user-controlled string
# ---------------------------------------------------------

def run_custom_logic(code_str):
    exec(code_str)  # VIOLATION

run_custom_logic("print('Executed!')")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Avoid exec completely — use safe dispatch or mapping
# ---------------------------------------------------------

def safe_operation(name):
    operations = {
        "greet": lambda: print("Hello!"),
        "bye": lambda: print("Goodbye!"),
    }

    if name in operations:
        operations[name]()  # SAFE: controlled behavior
    else:
        print("Unknown operation")

safe_operation("greet")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Use ast.literal_eval when parsing user input safely
# ---------------------------------------------------------

import ast

user_input_data = input("Enter a list (e.g., [1, 2]): ")

try:
    parsed_value = ast.literal_eval(user_input_data)  # SAFE
    print("Parsed Value:", parsed_value)
except Exception:
    print("Invalid input — cannot parse safely.")
