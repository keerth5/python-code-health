# ===============================================================
# cq-python-0057: String Join
# This file contains both violating and compliant examples.
# ===============================================================

# Sample list of words
words = ["Hello", "world", "from", "Python"]

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using string concatenation in a loop
# --------------------------------------------------------------
result = ""
for word in words:
    result += word + " "  # VIOLATION: inefficient concatenation
print("Violation 1 - concatenated string:", result.strip())

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Concatenating multiple strings in loop with format
# --------------------------------------------------------------
phrases = ["I", "love", "Python"]
sentence = ""
for phrase in phrases:
    sentence = "{} {}".format(sentence, phrase)  # VIOLATION
print("Violation 2 - formatted string in loop:", sentence.strip())


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using str.join() instead of concatenation
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Joining list of strings efficiently
# --------------------------------------------------------------
result_safe = " ".join(words)  # SAFE
print("\nCompliant 1 - joined string using join():", result_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Joining with different separator
# --------------------------------------------------------------
phrases_safe = "-".join(phrases)  # SAFE
print("Compliant 2 - joined string with dash:", phrases_safe)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Joining dynamically created list
# --------------------------------------------------------------
numbers = [str(i) for i in range(5)]
numbers_str = ", ".join(numbers)  # SAFE
print("Compliant 3 - joined numbers:", numbers_str)
