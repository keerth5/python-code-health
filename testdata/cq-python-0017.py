# =========================================================
# cq-python-0017: Global Declaration
# This file includes violating and compliant examples.
# =========================================================

counter = 0  # Global variable


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Modifying a global variable without declaring 'global'
# ---------------------------------------------------------
def increment_violation():
    # This attempts to modify global 'counter'
    # but without 'global counter', Python treats 'counter'
    # as a local variable → UnboundLocalError
    counter = counter + 1  # VIOLATION
    return counter


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Assigning to a global without declaring it
# ---------------------------------------------------------
message = "Hello"

def update_message_violation():
    message = "Updated"  # VIOLATION — shadows global unintentionally
    return message


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper use of global declaration
# ---------------------------------------------------------
def increment_safe():
    global counter        # Correct global declaration
    counter += 1
    return counter


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Safely updating global message with 'global'
# ---------------------------------------------------------
def update_message_safe():
    global message        # Correct global declaration
    message = "Updated Safely"
    return message


# ---------------------------------------------------------
# Test Execution (Optional)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== Compliant Outputs ===")
    print(increment_safe())       # Works
    print(update_message_safe())  # Works

    print("\n=== Violation Examples (will error or misbehave) ===")
    # Uncomment these to see violations:
    # print(increment_violation())
    # print(update_message_violation())
