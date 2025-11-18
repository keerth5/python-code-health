# =========================================================
# cq-python-0023: Network Timeouts
# This file includes both violating and compliant examples.
# =========================================================

import requests
import socket

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# requests.get() without timeout → hangs indefinitely
# ---------------------------------------------------------

def fetch_data_violation(url):
    response = requests.get(url)  # VIOLATION: No timeout
    return response.text

# Uncomment to test (Warning: may hang!)
# print(fetch_data_violation("https://example.com"))


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Raw socket without timeout
# ---------------------------------------------------------

def socket_violation():
    s = socket.socket()
    s.connect(("example.com", 80))  # VIOLATION: No timeout
    s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    return s.recv(1024)

# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper timeout in requests
# ---------------------------------------------------------

def fetch_data_safe(url):
    response = requests.get(url, timeout=5)  # SAFE: timeout added
    return response.text

# Example:
# print(fetch_data_safe("https://example.com"))


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Socket with timeout
# ---------------------------------------------------------

def socket_safe():
    s = socket.socket()
    s.settimeout(5)  # SAFE: timeout added
    s.connect(("example.com", 80))
    s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    return s.recv(1024)

# ---------------------------------------------------------
# End of file
# ---------------------------------------------------------
