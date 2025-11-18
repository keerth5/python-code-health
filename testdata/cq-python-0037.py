# =========================================================
# cq-python-0037: Access Control Checks
# This file contains both violating and compliant examples.
# =========================================================

# Mock user database
USERS = {
    "admin": {"role": "admin"},
    "bob": {"role": "user"},
    "guest": {"role": "guest"},
}

# Mock resource requiring admin privileges
def delete_record(record_id):
    print(f"Record {record_id} deleted!")


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Missing access control check before sensitive action
# ---------------------------------------------------------

def delete_record_violation(username, record_id):
    # Performs sensitive operation without checking user role
    print(f"[VIOLATION] User '{username}' is deleting record without checks!")
    delete_record(record_id)

# Try deleting without access validation
delete_record_violation("guest", 101)


# ---------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Weak or fake access control (always returns True)
# ---------------------------------------------------------

def is_authorized_weak(user):
    return True  # VIOLATION — no real check

def delete_record_weak(username, record_id):
    if is_authorized_weak(username):
        delete_record(record_id)

print("\n[VIOLATION] Weak auth check allows anyone:")
delete_record_weak("bob", 202)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Proper role-based access control
# ---------------------------------------------------------

def is_authorized(user, required_role="admin"):
    user_info = USERS.get(user)
    return user_info and user_info.get("role") == required_role

def delete_record_safe(username, record_id):
    if not is_authorized(username, "admin"):
        print(f"[DENIED] User '{username}' does not have permission.")
        return
    print(f"[ALLOWED] User '{username}' deleted the record.")
    delete_record(record_id)

print("\n[COMPLIANT] Proper access control:")
delete_record_safe("admin", 303)
delete_record_safe("guest", 404)


# ---------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using decorators for access control enforcement
# ---------------------------------------------------------

def require_role(role):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if not is_authorized(user, role):
                print(f"[DENIED] User '{user}' lacks required role: {role}")
                return
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def modify_config(user, config_key, value):
    print(f"[ALLOWED] '{user}' modified config '{config_key}' to '{value}'")

print("\n[COMPLIANT] Decorator-based RBAC:")
modify_config("admin", "timeout", 500)
modify_config("guest", "mode", "debug")
