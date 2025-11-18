# ==========================================================
# cq-python-0003: SSL Certificate Validation
# This file contains both violating and compliant examples.
# ==========================================================

import requests
import ssl
import urllib.request


# ----------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using requests with verify=False (disables SSL validation)
# ----------------------------------------------------------
url = "https://example.com"

try:
    response = requests.get(url, verify=False)  # VIOLATION
    print("Insecure request (verify=False):", response.status_code)
except Exception:
    print("Insecure request failed")


# ----------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Suppressing SSL warnings for insecure connections
# ----------------------------------------------------------
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # VIOLATION

try:
    response2 = requests.get(url, verify=False)  # still insecure
    print("Warning-suppressed insecure request:", response2.status_code)
except Exception:
    print("Failed insecure request")


# ----------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Creating an unverified SSL context
# ----------------------------------------------------------
insecure_context = ssl._create_unverified_context()  # VIOLATION

try:
    with urllib.request.urlopen(url, context=insecure_context) as res:
        print("Insecure urllib response:", res.status)
except Exception:
    print("Insecure urllib request failed")


# ==========================================================
# ✅ COMPLIANT EXAMPLES
# These demonstrate proper SSL certificate validation.
# ==========================================================

# ----------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Default SSL verification with requests
# ----------------------------------------------------------
try:
    secure_response = requests.get(url)  # SAFE: certificate verified
    print("Secure request status:", secure_response.status_code)
except Exception:
    print("Secure connection failed")


# ----------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using a properly created SSL context
# ----------------------------------------------------------
secure_context = ssl.create_default_context()  # SAFE

try:
    with urllib.request.urlopen(url, context=secure_context) as res2:
        print("Secure urllib response:", res2.status)
except Exception:
    print("Secure urllib request failed")


# ----------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Using requests with custom CA bundle (safe)
# ----------------------------------------------------------
try:
    secure_response2 = requests.get(url, verify="/etc/ssl/certs/ca-certificates.crt")  # SAFE
    print("Custom CA bundle request:", secure_response2.status_code)
except Exception:
    print("Secure CA-bundle request failed")
