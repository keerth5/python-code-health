# ===============================================================
# cq-python-0062: No Sleep in Async
# This file contains both violating and compliant examples.
# ===============================================================

import time
import asyncio

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Using time.sleep() in async function
# --------------------------------------------------------------
async def async_task_violation():
    print("Violation 1 - start")
    time.sleep(2)  # VIOLATION: blocks the event loop
    print("Violation 1 - end")

# Running violating async task
asyncio.run(async_task_violation())


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Blocking multiple async tasks
# --------------------------------------------------------------
async def multiple_tasks_violation():
    for i in range(3):
        print(f"Violation 2 - task {i} start")
        time.sleep(1)  # VIOLATION: blocks other async tasks
        print(f"Violation 2 - task {i} end")

# asyncio.run(multiple_tasks_violation())  # Uncommenting blocks event loop


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using asyncio.sleep() instead of time.sleep()
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Non-blocking async sleep
# --------------------------------------------------------------
async def async_task_safe():
    print("\nCompliant 1 - start")
    await asyncio.sleep(2)  # SAFE: does not block event loop
    print("Compliant 1 - end")

asyncio.run(async_task_safe())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Multiple async tasks running concurrently
# --------------------------------------------------------------
async def async_worker(task_id):
    print(f"Compliant 2 - task {task_id} start")
    await asyncio.sleep(1)  # SAFE non-blocking
    print(f"Compliant 2 - task {task_id} end")

async def main():
    tasks = [async_worker(i) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
