# ===============================================================
# cq-python-0073: Batch Processing
# This file contains both violating and compliant examples.
# ===============================================================

import time

# Sample data
data = list(range(1, 21))

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Processing items one by one
# --------------------------------------------------------------
def process_violation(items):
    results = []
    for item in items:
        time.sleep(0.1)  # simulate expensive operation
        results.append(item * 2)
    return results

start = time.time()
violation_results = process_violation(data)
end = time.time()
print("Violation - results:", violation_results)
print("Violation - time taken:", end - start, "seconds")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using proper batch processing
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Process data in batches
# --------------------------------------------------------------
def batch_process_safe(items, batch_size=5):
    results = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        # simulate batch processing
        time.sleep(0.1)  # simulate expensive batch operation
        results.extend([x * 2 for x in batch])
    return results

start = time.time()
compliant_results = batch_process_safe(data)
end = time.time()
print("\nCompliant - results:", compliant_results)
print("Compliant - time taken:", end - start, "seconds")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using generator for streaming batch processing
# --------------------------------------------------------------
def batch_generator(items, batch_size=5):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

for batch in batch_generator(data):
    processed = [x * 2 for x in batch]
    print("Compliant 2 - processed batch:", processed)
