# ===============================================================
# cq-python-0101: Counter Usage
# This file contains both violating and compliant examples.
# ===============================================================

from collections import Counter

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Manual counting with loops
# --------------------------------------------------------------
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count_violation = {}
for word in words:
    if word in count_violation:
        count_violation[word] += 1
    else:
        count_violation[word] = 1

print("Violation - manual counting:", count_violation)

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Counting with get() method
# --------------------------------------------------------------
count_violation2 = {}
for word in words:
    count_violation2[word] = count_violation2.get(word, 0) + 1

print("Violation - counting with get():", count_violation2)


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Use collections.Counter for counting
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Simple Counter usage
# --------------------------------------------------------------
count_clean = Counter(words)
print("Compliant - Counter:", count_clean)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Counting characters in a string
# --------------------------------------------------------------
text = "abracadabra"
char_count = Counter(text)
print("Compliant - character Counter:", char_count)

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Counting with update method
# --------------------------------------------------------------
more_words = ["banana", "cherry", "banana"]
count_clean.update(more_words)
print("Compliant - updated Counter:", count_clean)
