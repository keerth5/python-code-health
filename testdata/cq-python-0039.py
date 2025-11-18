# =========================================================
# cq-python-0039: Secure Cookies
# This file contains both violating and compliant examples.
# =========================================================

from flask import Flask, make_response

app = Flask(__name__)

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Insecure cookie without secure flags
# ---------------------------------------------------------

@app.route("/login-insecure")
def insecure_cookie():
    resp = make_response("Logged in (INSECURE)")
    
    # Missing secure=True, httponly=True, samesite settings → VIOLATION
    resp.set_cookie(
        "session_id",
        "ABC123", 
        secure=False,     # insecure
        httponly=False,   # insecure
        samesite=None     # insecure
    )
    
    return resp


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Completely missing flags (defaults insecure)
# ---------------------------------------------------------

@app.route("/login-insecure-default")
def insecure_cookie_default():
    resp = make_response("Logged in (INSECURE DEFAULTS)")
    
    resp.set_cookie("session_id", "XYZ987")  # VIOLATION
    
    return resp


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Secure cookie with all recommended flags
# ---------------------------------------------------------

@app.route("/login-secure")
def secure_cookie():
    resp = make_response("Logged in (SECURE)")
    
    resp.set_cookie(
        "session_id",
        "SECURE123",
        secure=True,         # cookie sent only over HTTPS
        httponly=True,       # prevents JavaScript access
        samesite="Strict"    # mitigates CSRF attacks
    )
    
    return resp


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Secure cookie with Safe defaults & consistent best practices
# ---------------------------------------------------------

@app.route("/login-secure-lax")
def secure_cookie_lax():
    resp = make_response("Logged in (SECURE LAX)")
    
    resp.set_cookie(
        "session_id",
        "SAFE456",
        secure=True,
        httponly=True,
        samesite="Lax"      # still secure and widely used
    )
    
    return resp


if __name__ == "__main__":
    app.run(debug=True)
