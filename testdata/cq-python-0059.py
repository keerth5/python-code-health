# ===============================================================
# cq-python-0059: Weak References
# This file contains both violating and compliant examples.
# ===============================================================

import weakref
import gc

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 1
# Circular reference without weakref
# --------------------------------------------------------------
class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.child = None

# Creating circular reference
node1 = Node("node1")
node2 = Node("node2")
node1.child = node2
node2.parent = node1  # VIOLATION: strong reference cycle

# Deleting references
del node1
del node2
gc.collect()  # The circular reference may prevent immediate garbage collection
print("Violation 1 - circular references may cause memory leak")

# --------------------------------------------------------------
# ❌ VIOLATION EXAMPLE 2
# Manual storage of circular objects in container without weakref
# --------------------------------------------------------------
container = []
class Person:
    def __init__(self, name):
        self.name = name
        self.friend = None

alice = Person("Alice")
bob = Person("Bob")
alice.friend = bob
bob.friend = alice  # VIOLATION: strong circular reference
container.append(alice)
container.append(bob)
del alice
del bob
gc.collect()
print("Violation 2 - circular references in container may leak memory")


# ===============================================================
# ✅ COMPLIANT EXAMPLES
# Using weak references to break cycles
# ===============================================================

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 1
# Weak reference for parent link
# --------------------------------------------------------------
class NodeSafe:
    def __init__(self, name):
        self.name = name
        self.child = None
        self._parent = None

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, value):
        self._parent = weakref.ref(value)

node_safe1 = NodeSafe("node_safe1")
node_safe2 = NodeSafe("node_safe2")
node_safe1.child = node_safe2
node_safe2.parent = node_safe1  # SAFE: weak reference prevents memory leak

del node_safe1
del node_safe2
gc.collect()
print("\nCompliant 1 - weakref breaks circular references safely")

# --------------------------------------------------------------
# ✅ COMPLIANT EXAMPLE 2
# WeakSet for storing circular objects in container
# --------------------------------------------------------------
class PersonSafe:
    def __init__(self, name):
        self.name = name
        self.friends = weakref.WeakSet()

alice_safe = PersonSafe("Alice")
bob_safe = PersonSafe("Bob")
alice_safe.friends.add(bob_safe)
bob_safe.friends.add(alice_safe)  # SAFE: weak references prevent memory leaks

del alice_safe
del bob_safe
gc.collect()
print("Compliant 2 - circular references using WeakSet handled safely")
