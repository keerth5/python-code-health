# ===============================================================
# cq-python-0069: Error Boundaries
# This file contains both violating and compliant examples.
# ===============================================================

import asyncio

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Async function without error handling
# --------------------------------------------------------------
async def fetch_data_violation():
    print("Violation 1 - start")
    # This will raise ZeroDivisionError
    result = 10 / 0  # ❌ no error boundary
    print("Violation 1 - result:", result)

# asyncio.run(fetch_data_violation())  # Uncommenting will raise exception


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple async tasks without error handling
# --------------------------------------------------------------
async def task_violation(task_id):
    if task_id == 2:
        raise ValueError("Simulated error")  # ❌ unhandled exception
    return task_id * 2

async def run_tasks_violation():
    tasks = [task_violation(i) for i in range(3)]
    results = await asyncio.gather(*tasks)  # ❌ exceptions propagate, no handling
    print("Violation 2 - results:", results)

# asyncio.run(run_tasks_violation())  # Uncommenting will raise exception


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Async functions with proper error boundaries
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Using try/except inside async function
# --------------------------------------------------------------
async def fetch_data_safe():
    print("\nCompliant 1 - start")
    try:
        result = 10 / 0  # will raise ZeroDivisionError
    except ZeroDivisionError as e:
        print("Compliant 1 - caught exception:", e)
        result = None
    print("Compliant 1 - result:", result)
    return result

asyncio.run(fetch_data_safe())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Using asyncio.gather with return_exceptions=True
# --------------------------------------------------------------
async def task_safe(task_id):
    if task_id == 2:
        raise ValueError("Simulated error")
    return task_id * 2

async def run_tasks_safe():
    tasks = [task_safe(i) for i in range(3)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    for i, res in enumerate(results):
        if isinstance(res, Exception):
            print(f"Compliant 2 - task {i} raised exception: {res}")
        else:
            print(f"Compliant 2 - task {i} result: {res}")

asyncio.run(run_tasks_safe())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Catch exceptions with context manager for async code
# --------------------------------------------------------------
class AsyncContext:
    async def __aenter__(self):
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            print(f"Compliant 3 - caught exception in context manager: {exc_val}")
        return True  # suppress exception

async def async_task_with_context():
    async with AsyncContext():
        1 / 0  # raises ZeroDivisionError, handled by context manager

asyncio.run(async_task_with_context())
