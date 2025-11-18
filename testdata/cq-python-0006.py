# ===============================================================
# cq-python-0006: LDAP Injection Prevention
# This file contains both violating and compliant examples.
# ===============================================================

from ldap3 import Server, Connection, ALL, SAFE_FILTERS


# Dummy LDAP setup (placeholder)
server = Server("ldap://example.com", get_info=ALL)
conn = Connection(server, auto_bind=False)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Direct string concatenation into LDAP filter
# ---------------------------------------------------------------
username = input("Enter username (unsafe): ")

unsafe_filter = f"(uid={username})"  # VIOLATION
print("Using unsafe LDAP filter:", unsafe_filter)

# (Not executing for safety, just demonstrating)
# conn.search("dc=example,dc=com", unsafe_filter)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Building LDAP query with unvalidated user input
# ---------------------------------------------------------------
dept = input("Enter department: ")

unsafe_filter2 = "(&(objectClass=person)(department=" + dept + "))"  # VIOLATION
print("Unsafe department filter:", unsafe_filter2)


# ---------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 3
# Allowing wildcard injection in LDAP queries
# ---------------------------------------------------------------
user_filter = input("Search filter: ")  # User might input: *) (|(uid=*)) (

unsafe_filter3 = f"(cn={user_filter})"  # VIOLATION
print("Unsafe wildcard filter:", unsafe_filter3)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Proper escaping, safe filters, and whitelisting.
# ===============================================================

# ---------------------------------------------------------------
# Helper: Safe LDAP escaping function
# ---------------------------------------------------------------
def ldap_escape(value: str) -> str:
    """Escape special characters per RFC 4515."""
    replacements = {
        "\\": r"\5c",
        "*": r"\2a",
        "(": r"\28",
        ")": r"\29",
        "\x00": r"\00",
    }
    escaped = ""
    for ch in value:
        escaped += replacements.get(ch, ch)
    return escaped


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Escape user input before injecting into LDAP filter
# ---------------------------------------------------------------
safe_username = input("Enter username (safe): ")
escaped_username = ldap_escape(safe_username)

safe_filter = f"(uid={escaped_username})"  # SAFE
print("Safe escaped LDAP filter:", safe_filter)


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using ldap3 SAFE_FILTERS to sanitize input
# ---------------------------------------------------------------
safe_dept = input("Enter department (safe): ")

# SAFE_FILTERS automatically escapes input safely
safe_filter2 = f"(&(objectClass=person)(department={SAFE_FILTERS.escape_filter_chars(safe_dept)}))"
print("Safe filter using SAFE_FILTERS:", safe_filter2)


# ---------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Whitelisting allowed search attributes
# ---------------------------------------------------------------
allowed_attrs = {"cn", "uid", "mail"}

attr = input("Enter attribute to search (cn, uid, mail): ")

if attr not in allowed_attrs:
    print("Attribute not allowed")
else:
    value = input("Enter search value: ")
    escaped_value = ldap_escape(value)
    safe_filter3 = f"({attr}={escaped_value})"
    print("Safe whitelisted filter:", safe_filter3)
