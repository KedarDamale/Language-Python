# ================================
# PYTHON SETS - COMPLETE EXPLANATION
# ================================

# Sets are:
# - Unordered: No guaranteed order
# - Mutable: You can add/remove items
# - Unique: No duplicates allowed
# - Hashable: Elements must be immutable

# 1️⃣ Creating Sets
s1 = {1, 2, 3, 4, 5}
print("Set s1:", s1)

# From list (removes duplicates)
s2 = set([1, 2, 2, 3])
print("Set from list:", s2)

# Empty set (MUST use set(), not {})
s3 = set()
print("Empty set s3:", s3)

# Mixed types (must be hashable)
s4 = {10, "apple", 3.14}
print("Mixed set:", s4)

# 2️⃣ No Duplicates
dup = {1, 1, 2, 2}
print("After removing duplicates:", dup)

# 3️⃣ No Indexing
for item in s1:
    print("Iterating set s1 →", item)
# ❌ s1[0] will throw TypeError

# 4️⃣ Set Methods
a = {1, 2, 3}
b = {3, 4, 5}

a.add(10)              # Adds 10
a.update([20, 30])     # Adds multiple
a.discard(100)         # No error even if not found
a.remove(20)           # ❌ Error if not found
val = a.pop()          # Removes a random item
print("a after operations:", a)
print("Popped value:", val)

# 5️⃣ Set Operations
x = {1, 2, 3, 4}
y = {3, 4, 5, 6}

print("x | y (union):", x | y)
print("x & y (intersection):", x & y)
print("x - y (difference):", x - y)
print("x ^ y (symmetric diff):", x ^ y)

print("x is subset of y:", x.issubset(y))
print("x is superset of y:", x.issuperset(y))
print("x and y disjoint:", x.isdisjoint({7, 8}))

# 6️⃣ Copy vs Reference
original = {1, 2, 3}
reference = original         # Same memory
copyset = original.copy()    # Different memory

original.add(999)

print("original:", original)
print("reference:", reference)  # Also affected
print("copyset:", copyset)      # Unaffected

print("id(original):", id(original))
print("id(reference):", id(reference))
print("id(copyset):", id(copyset))

# 7️⃣ Set Comprehension
squares = {x**2 for x in range(5)}
print("Set comprehension (x²):", squares)

# 8️⃣ Common Errors
# s5 = {[1, 2]}  # ❌ TypeError: list is unhashable
# Only hashable (immutable) elements like int, str, tuple can be in sets

# 9️⃣ List of Set Methods
print("Set methods:", dir(set))
# Use help(set) in terminal for documentation
