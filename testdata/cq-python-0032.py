# =========================================================
# cq-python-0032: Secure Sessions
# This file contains both violating and compliant examples.
# =========================================================

from flask import Flask, session

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Insecure cookie settings for Flask session
# ---------------------------------------------------------

app_violation = Flask(__name__)
app_violation.secret_key = "weak_dev_key"  # Hardcoded, also weak

@app_violation.route("/login_violation")
def login_violation():
    session["user"] = "admin"
    # VIOLATION: Session cookie uses insecure defaults (no secure, httponly, samesite)
    return "Logged in with insecure session"


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Explicitly disabling security flags
# ---------------------------------------------------------

app_violation.config.update(
    SESSION_COOKIE_SECURE=False,     # VIOLATION
    SESSION_COOKIE_HTTPONLY=False,   # VIOLATION
    SESSION_COOKIE_SAMESITE=None     # VIOLATION
)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Secure session configuration
# ---------------------------------------------------------

app_secure = Flask(__name__)
app_secure.secret_key = "CHANGE_ME_IN_PRODUCTION"

app_secure.config.update(
    SESSION_COOKIE_SECURE=True,       # Only sent via HTTPS
    SESSION_COOKIE_HTTPONLY=True,     # Prevents JavaScript access
    SESSION_COOKIE_SAMESITE="Strict"  # Prevents CSRF-style attacks
)

@app_secure.route("/login_safe")
def login_safe():
    session["user"] = "admin"
    return "Logged in with secure session"


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using per-cookie secure flags in response
# ---------------------------------------------------------

from flask import make_response

@app_secure.route("/set_cookie_secure")
def set_cookie_secure():
    response = make_response("Setting secure cookie")
    # Properly configured secure cookie
    response.set_cookie(
        "token",
        "secure-value",
        secure=True,
        httponly=True,
        samesite="Strict"
    )
    return response
