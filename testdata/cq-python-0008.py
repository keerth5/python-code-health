# ======================================================================
# cq-python-0008: CSRF Protection
# This file contains both violating and compliant examples using Flask.
# ======================================================================

from flask import Flask, request, render_template_string, session
import secrets

app = Flask(__name__)
app.secret_key = "development-key"  # For demo only


# ======================================================================
# ❌ VIOLATION SECTION
# Missing or improper CSRF protection.
# ======================================================================

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Form without CSRF token
# --------------------------------------------------------------
@app.route("/unsafe-form", methods=["GET"])
def unsafe_form():
    # No CSRF token in form → vulnerable
    return render_template_string("""
        <form action="/unsafe-submit" method="POST">
            <input type="text" name="comment">
            <button type="submit">Submit</button>
        </form>
    """)


@app.route("/unsafe-submit", methods=["POST"])
def unsafe_submit():
    # No CSRF validation → dangerous
    comment = request.form.get("comment")
    return f"Unsafe submission received: {comment}"


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# CSRF token generated but NOT verified
# --------------------------------------------------------------
@app.route("/half-safe-form", methods=["GET"])
def half_safe_form():
    session["csrf_token"] = secrets.token_hex(16)
    # Token added in form but missing verification
    return render_template_string("""
        <form action="/half-safe-submit" method="POST">
            <input type="hidden" name="csrf" value="{{ csrf_token }}">
            <input type="text" name="message">
            <button>Submit</button>
        </form>
    """, csrf_token=session["csrf_token"])


@app.route("/half-safe-submit", methods=["POST"])
def half_safe_submit():
    # Forgot to VERIFY token → still vulnerable
    msg = request.form.get("message")
    return f"Half-safe received (still unsafe): {msg}"


# ======================================================================
# ✅ COMPLIANT SECTION
# Proper CSRF token generation and validation.
# ======================================================================

# --------------------------------------------------------------
# Helper function: Validate CSRF token
# --------------------------------------------------------------
def verify_csrf():
    form_token = request.form.get("csrf")
    session_token = session.get("csrf_token")

    if not form_token or not session_token or form_token != session_token:
        return False
    return True


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Form with correct CSRF token handling
# --------------------------------------------------------------
@app.route("/safe-form", methods=["GET"])
def safe_form():
    # Generate CSRF token
    session["csrf_token"] = secrets.token_hex(32)

    return render_template_string("""
        <form action="/safe-submit" method="POST">
            <input type="hidden" name="csrf" value="{{ csrf_token }}">
            <input type="text" name="content">
            <button type="submit">Submit Safely</button>
        </form>
    """, csrf_token=session["csrf_token"])


@app.route("/safe-submit", methods=["POST"])
def safe_submit():
    # Validate token
    if not verify_csrf():
        return "CSRF validation failed!", 403

    content = request.form.get("content")
    return f"Safely submitted: {content}"


# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using framework-provided CSRF libraries (Flask-WTF)
# --------------------------------------------------------------
# (This is a simplified demo; requires Flask-WTF installed)
try:
    from flask_wtf import CSRFProtect
    csrf = CSRFProtect(app)
    print("Flask-WTF CSRF protection enabled")
except Exception:
    print("Flask-WTF not installed; skipping framework-based CSRF example")


# --------------------------------------------------------------
# App runner
# --------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
