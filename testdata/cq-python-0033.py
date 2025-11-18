# ================================================================
# cq-python-0033: API Rate Limiting
# This file contains both violating and compliant examples.
# ================================================================

from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# ----------------------------------------------------------------
# ❌ VIOLATION EXAMPLE
# No rate limiting -> API can be spammed causing DoS
# ----------------------------------------------------------------

@app.route("/no_rate_limit")
def no_rate_limit():
    # VIOLATION: endpoint performs heavy work without any rate limit
    time.sleep(0.5)  # Simulate expensive computation
    return jsonify({"status": "OK", "note": "This endpoint has NO rate limiting"})


# ----------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE
# Simple in-memory rate limiting using timestamps
# ----------------------------------------------------------------

RATE_LIMIT_WINDOW = 5      # seconds
RATE_LIMIT_MAX_CALLS = 3   # max requests allowed in window
user_access_log = {}       # user_ip -> [timestamps]

@app.route("/safe_endpoint")
def safe_endpoint():
    user_ip = request.remote_addr
    now = time.time()

    # Initialize log entry
    if user_ip not in user_access_log:
        user_access_log[user_ip] = []

    # Filter timestamps within the window
    user_access_log[user_ip] = [
        t for t in user_access_log[user_ip] if now - t < RATE_LIMIT_WINDOW
    ]

    # Check limit
    if len(user_access_log[user_ip]) >= RATE_LIMIT_MAX_CALLS:
        return jsonify({"error": "Rate limit exceeded"}), 429

    # Log request
    user_access_log[user_ip].append(now)

    return jsonify({
        "status": "OK",
        "note": "Rate limit applied correctly",
        "remaining_calls": RATE_LIMIT_MAX_CALLS - len(user_access_log[user_ip])
    })


# Run only if executed directly
if __name__ == "__main__":
    app.run(debug=True)
