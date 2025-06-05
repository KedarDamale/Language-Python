# ============================================
# PYTHON TUPLES – COMPLETE DETAILED EXPLANATION
# ============================================

# ✅ What is a Tuple?
# A tuple is an immutable, ordered collection of items. Once created, it cannot be changed.
# Tuples are faster than lists and can be used as keys in dictionaries or elements in sets (if hashable).

# 1️⃣ Tuple Creation
t1 = (1, 2, 3)                 # Normal tuple
t2 = 4, 5, 6                   # Without parentheses (still a tuple)
t3 = (42,)                    # Single-element tuple MUST use trailing comma
t4 = ()                       # Empty tuple
t5 = (1, "hello", 3.14, True) # Mixed data types

print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("t4:", t4)
print("t5:", t5)

# 2️⃣ Accessing Elements
print("First element of t1:", t1[0])
print("Last element of t1:", t1[-1])

# 3️⃣ Iterating Over a Tuple
print("Items in t5:")
for item in t5:
    print(item)

# 4️⃣ Tuple Packing and Unpacking
person = ("Kedar", 22, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# 5️⃣ Immutability
# t1[0] = 100  # ❌ Error! Tuples can't be modified

# 6️⃣ Tuple Methods (only 2 because tuples are immutable)
print("Count of 2 in (1,2,2,3,2):", (1,2,2,3,2).count(2))  # → 3
print("Index of 3 in (1,2,2,3,2):", (1,2,2,3,2).index(3))  # → 3

# 7️⃣ Tuple with mutable object inside
t6 = (1, [10, 20])
print("Before:", t6)
t6[1].append(30)  # Allowed! We're not modifying tuple structure, just the list inside
print("After:", t6)

# 8️⃣ Memory and ID
import sys
l1 = [1, 2, 3]
t1 = (1, 2, 3)
print("List size:", sys.getsizeof(l1))  # 88 bytes
print("Tuple size:", sys.getsizeof(t1)) # 64 bytes → smaller

# 9️⃣ Tuples Are Hashable (if all elements inside are hashable)
d = {}
key = (10, 20)
d[key] = "Location A"
print("Dict with tuple key:", d)

# 1️⃣0️⃣ Mutable list vs Immutable tuple – ID change
l1 = [1, 2, 3]
print("List ID before append:", id(l1))
l1.append(4)
print("List ID after append:", id(l1))  # same ID (mutable)

t1 = (1, 2, 3)
print("Tuple ID before change:", id(t1))
t1 = t1 + (4,)  # creates new tuple
print("Tuple ID after change:", id(t1))  # different ID (immutable)

# 1️⃣1️⃣ Tuple comprehension? ❌ No → Use generator expressions
gen = (x**2 for x in range(5))  # generator, not tuple
print("Generator squares:", list(gen))  # → [0, 1, 4, 9, 16]

# 1️⃣2️⃣ Tuple IndexError
# print(t1[10])  # ❌ will raise IndexError

# 1️⃣3️⃣ dir() & help()
print("Tuple methods:", dir(t1))  # Only useful methods are count() and index()
# help(tuple)  # Uncomment to read full docs in terminal

# ✅ Summary:
# - Tuples are immutable → once created, can't be changed
# - Ordered → you can access items using index
# - Allow duplicates
# - Faster and more memory-efficient than lists
# - Useful for data that shouldn't change
# - Can be used as keys in dicts if fully immutable (no lists inside)




# ======================================================
# 📌 DIFFERENCE BETWEEN LIST, TUPLE, AND SET IN PYTHON
# ======================================================

# ┌────────────┬──────────────┬──────────────┬───────────────┐
# │ Feature    │ List         │ Tuple        │ Set           │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Syntax     │ [1, 2, 3]     │ (1, 2, 3)     │ {1, 2, 3}      │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Ordered?   │ ✅ Yes        │ ✅ Yes        │ ❌ No          │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Duplicates │ ✅ Allowed    │ ✅ Allowed    │ ❌ Not allowed │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Mutable?   │ ✅ Yes        │ ❌ No         │ ✅ Yes         │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Indexing   │ ✅ Supported  │ ✅ Supported  │ ❌ Not supported│
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Methods    │ Many (e.g.,   │ Few (only    │ Set-specific  │
# │            │ append, pop) │ count/index) │ (union, etc.) │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Performance│ 🐢 Slower     │ ⚡ Faster     │ ⚡ Faster      │
# ├────────────┼──────────────┼──────────────┼───────────────┤
# │ Use Cases  │ Dynamic,     │ Fixed,       │ Membership,   │
# │            │ changeable   │ constant     │ unique data   │
# └────────────┴──────────────┴──────────────┴───────────────┘

# ====================================
# ✅ LIST – Ordered, Mutable, Allows Duplicates
# ====================================
fruits = ["apple", "banana", "mango"]
fruits.append("orange")     # adds item
fruits[1] = "grape"         # can modify
print("List:", fruits)      # Output: ['apple', 'grape', 'mango', 'orange']

# ====================================
# ✅ TUPLE – Ordered, Immutable, Allows Duplicates
# ====================================
person = ("Kedar", 22, "Engineer")
# person[0] = "KD"  ❌ Error: tuples are immutable
print("Tuple:", person)     # Output: ('Kedar', 22, 'Engineer')

# ====================================
# ✅ SET – Unordered, Mutable, No Duplicates Allowed
# ====================================
numbers = {1, 2, 3, 3, 4}
numbers.add(5)
numbers.add(2)              # Duplicate won't be added
print("Set:", numbers)      # Output: {1, 2, 3, 4, 5} – No order, no duplicates

# ====================================
# 🔎 Real-World Use Cases:
# ====================================
# 📦 Use LIST when:
#     - You want to store and modify data dynamically
#     - You care about the order of insertion
#     - You allow duplicates
#
# 📦 Use TUPLE when:
#     - You want to store a fixed collection of values (like coordinates, config)
#     - You want immutability (e.g., for dictionary keys)
#     - You want better performance over lists
#
# 📦 Use SET when:
#     - You need to store only unique items
#     - You want to do mathematical operations like union, intersection, etc.
#     - You don't care about order or indexing

# ====================================
# 🚀 Performance Summary:
# ====================================
# - Tuples use less memory than lists (they're static, so Python optimizes them)
# - Sets are optimized for fast lookup (like checking if an item exists)
# - Lists are flexible but a bit slower due to dynamic resizing and rich functionality

