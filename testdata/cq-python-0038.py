# ================================================================
# cq-python-0038: Email Validation
# This file contains both violating and compliant examples.
# ================================================================

import re

# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# No validation of user-supplied email
# ---------------------------------------------------------------

user_email = input("Enter your email (VIOLATION): ")

# Directly trusting user input → dangerous for auth systems
print("Processing email (VIOLATION):", user_email)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Using a naive or incorrect validation method
# ---------------------------------------------------------------

raw_email = input("Enter email (bad validation): ")

if "@" in raw_email:     # Very weak check → still allows injection or invalid formats
    print("Valid Email (INCORRECT):", raw_email)
else:
    print("Invalid Email (INCORRECT):", raw_email)


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Strong email validation with regex
# ---------------------------------------------------------------

email_regex = re.compile(
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

safe_email = input("Enter your email (SAFE): ")

if email_regex.match(safe_email):
    print("Valid Email (SAFE):", safe_email)
else:
    print("Invalid Email (SAFE):", safe_email)


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Sanitizing and validating email before processing
# ---------------------------------------------------------------

def sanitize_email(email: str) -> str:
    """Remove dangerous characters and trim spaces."""
    return email.strip().replace("\n", "").replace("\r", "").lower()

clean_email = sanitize_email(input("Enter email to sanitize & validate: "))

if email_regex.match(clean_email):
    print("Email sanitized & validated:", clean_email)
else:
    print("Invalid sanitized email:", clean_email)
