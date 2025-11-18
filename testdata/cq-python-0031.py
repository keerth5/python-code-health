# =========================================================
# cq-python-0031: File Upload Validation
# This file contains both violating and compliant examples.
# =========================================================

import os
import mimetypes

# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Accepting uploaded file without validating extension
# ---------------------------------------------------------

def save_uploaded_file_violation(filename, data):
    # No validation — uploads ANY file, including .exe, .php, etc.
    upload_path = os.path.join("uploads", filename)   # VIOLATION
    with open(upload_path, "wb") as f:
        f.write(data)
    return upload_path

# Simulate user upload (unsafe)
unsafe_filename = "malicious.exe"
save_uploaded_file_violation(unsafe_filename, b"malicious content")


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Trusting MIME type sent by the client (spoofable)
# ---------------------------------------------------------

def unsafe_upload_with_mime(filename, content, mime_type):
    # Trusting client-provided MIME — attacker can send "image/png"
    print(f"Received MIME type: {mime_type}")  # VIOLATION
    with open(os.path.join("uploads", filename), "wb") as f:
        f.write(content)


unsafe_upload_with_mime("fake.png", b"script code", "image/png")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Validate file extension against a whitelist
# ---------------------------------------------------------

ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".pdf"}

def is_allowed_file(filename):
    _, ext = os.path.splitext(filename.lower())
    return ext in ALLOWED_EXTENSIONS

def save_uploaded_file_safe(filename, data):
    if not is_allowed_file(filename):
        raise ValueError("Invalid or unsupported file type")

    upload_path = os.path.join("uploads", filename)
    with open(upload_path, "wb") as f:
        f.write(data)
    return upload_path

# Safe upload
safe_filename = "document.pdf"
save_uploaded_file_safe(safe_filename, b"%PDF fake content")


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Server-side MIME detection using mimetypes or magic (safer)
# ---------------------------------------------------------

def save_file_with_mime_validation(filename, data):
    detected_type, _ = mimetypes.guess_type(filename)

    if detected_type not in ["image/png", "image/jpeg", "application/pdf"]:
        raise ValueError(f"Disallowed MIME type: {detected_type}")

    upload_path = os.path.join("uploads", filename)
    with open(upload_path, "wb") as f:
        f.write(data)

    return upload_path

# Safe usage
save_file_with_mime_validation("image.png", b"PNGDATA")
