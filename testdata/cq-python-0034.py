# =========================================================
# cq-python-0034: XSS Prevention
# This file contains both violating and compliant examples.
# =========================================================

from flask import Flask, request, escape
app = Flask(__name__)

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Directly embedding user-controlled HTML in output
# ---------------------------------------------------------

@app.route("/greet_violation")
def greet_violation():
    name = request.args.get("name", "")
    # UNSAFE: user input is rendered directly --> XSS
    return f"<h1>Hello {name}</h1>"   # VIOLATION


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Unsafe HTML concatenation for rendering
# ---------------------------------------------------------

@app.route("/comment_violation")
def comment_violation():
    comment = request.args.get("comment", "")
    html = "<div>Your comment: " + comment + "</div>"  # VIOLATION
    return html


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Use Flask escape() to sanitize HTML
# ---------------------------------------------------------

@app.route("/greet_safe")
def greet_safe():
    name = request.args.get("name", "")
    safe_name = escape(name)  # Sanitizes <script>, etc.
    return f"<h1>Hello {safe_name}</h1>"


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Whitelisting safe HTML if needed
# ---------------------------------------------------------

from markupsafe import Markup

@app.route("/comment_safe")
def comment_safe():
    comment = request.args.get("comment", "")
    sanitized = escape(comment)
    html = Markup("<div>Your comment: ") + sanitized + Markup("</div>")
    return html


if __name__ == "__main__":
    app.run(debug=True)
