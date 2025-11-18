# ===============================================================
# cq-python-0072: Async Context Managers
# This file contains both violating and compliant examples.
# ===============================================================

import asyncio

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Async resource without context manager
# --------------------------------------------------------------
class AsyncResourceViolation:
    async def connect(self):
        print("Violation - resource connected")
    async def close(self):
        print("Violation - resource closed")

async def use_resource_violation():
    resource = AsyncResourceViolation()
    await resource.connect()
    # ❌ forgot to ensure close() is called if exception occurs
    print("Violation - using resource")
    # await resource.close()  # could be skipped if exception occurs

asyncio.run(use_resource_violation())


# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Multiple async resources without proper context management
# --------------------------------------------------------------
async def multiple_resources_violation():
    res1 = AsyncResourceViolation()
    res2 = AsyncResourceViolation()
    await res1.connect()
    await res2.connect()
    # ❌ exception here would leave resources open
    raise RuntimeError("Simulated error")
    await res1.close()
    await res2.close()

# asyncio.run(multiple_resources_violation())  # uncommenting raises unhandled exception


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using proper async context managers
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Async context manager with __aenter__ and __aexit__
# --------------------------------------------------------------
class AsyncResourceSafe:
    async def __aenter__(self):
        print("Compliant 1 - resource connected")
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Compliant 1 - resource closed")
        if exc_val:
            print(f"Compliant 1 - caught exception: {exc_val}")

async def use_resource_safe():
    async with AsyncResourceSafe() as resource:
        print("Compliant 1 - using resource")

asyncio.run(use_resource_safe())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# Multiple async resources safely managed
# --------------------------------------------------------------
class AsyncResourceSafe2:
    async def __aenter__(self):
        print("Compliant 2 - resource connected")
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Compliant 2 - resource closed")
        if exc_val:
            print(f"Compliant 2 - caught exception: {exc_val}")

async def multiple_resources_safe():
    async with AsyncResourceSafe2() as res1, AsyncResourceSafe2() as res2:
        print("Compliant 2 - using multiple resources")
        # raise RuntimeError("Simulated error")  # safely handled

asyncio.run(multiple_resources_safe())

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 3
# Async file operation using aiofiles (example)
# --------------------------------------------------------------
# import aiofiles
# async def read_file_async(path):
#     async with aiofiles.open(path, 'r') as f:
#         contents = await f.read()
#         return contents
