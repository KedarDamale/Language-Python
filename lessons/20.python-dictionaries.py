# ============================================
# 📘 PYTHON DICTIONARIES - COMPLETE EXPLANATION
# ============================================

# A dictionary is a collection of **key-value** pairs
# Syntax: dictionary = {key1: value1, key2: value2, ...}
# Keys must be unique and immutable (string, int, tuple)
# Values can be any data type

# Creating a dictionary
person = {
    "name": "Kedar",
    "age": 21,
    "is_student": True,
    "skills": ["Python", "C", "SQL"]
}

# --------------------------------------------
# ✅ ACCESSING VALUES
# --------------------------------------------

print(person["name"])       # Accessing using key (throws error if key doesn't exist)
print(person.get("age"))    # Safer way to access (returns None if key doesn't exist)
print(person.get("address", "Not Available"))  # Get with default value

# --------------------------------------------
# ✅ MUTABILITY & UPDATES
# --------------------------------------------

# Dictionaries are mutable → we can modify them after creation

# Adding new key-value pair
person["city"] = "Pune"

# Updating existing key
person["age"] = 22

# Updating multiple values at once
person.update({"name": "Kedar Damale", "graduated": False})

print(person)

# --------------------------------------------
# ✅ DELETION METHODS
# --------------------------------------------

# Remove a specific key
person.pop("is_student")

# Remove last inserted key-value pair (Python 3.7+)
person.popitem()

# Clear all entries but keeps dictionary object
person.clear()

print("After clear:", person)

# --------------------------------------------
# ✅ DICTIONARY CREATION METHODS
# --------------------------------------------

# Using dict() constructor
student = dict(name="Ravi", age=20, branch="IT")

# Nested dictionary
students = {
    "T-001": {"name": "Amit", "age": 21},
    "T-002": {"name": "Sneha", "age": 22}
}

print(students["T-001"]["name"])  # Access nested dictionary

# --------------------------------------------
# ✅ DICTIONARY METHODS
# --------------------------------------------

sample = {
    "a": 1,
    "b": 2,
    "c": 3
}

# Get all keys
print(sample.keys())

# Get all values
print(sample.values())

# Get all items (key-value pairs)
print(sample.items())

# Loop through keys
for k in sample.keys():
    print(f"Key: {k}")

# Loop through values
for v in sample.values():
    print(f"Value: {v}")

# Loop through both keys and values
for k, v in sample.items():
    print(f"Key: {k}, Value: {v}")

# --------------------------------------------
# ✅ MEMBERSHIP CHECK
# --------------------------------------------

print("a" in sample)   # True
print("z" in sample)   # False

# --------------------------------------------
# ✅ DICTIONARY COMPREHENSION
# --------------------------------------------

# Squaring numbers using dict comprehension
squares = {x: x**2 for x in range(5)}
print("Dict Comprehension:", squares)

# --------------------------------------------
# ✅ DICTIONARY VS LIST VS SET
# --------------------------------------------

# DICTIONARY:
# - Key-value pairs
# - Mutable
# - No duplicate keys
# - Ordered (as of Python 3.7+)
# - Very fast lookup via hash table

# LIST:
# - Ordered sequence of items
# - Mutable
# - Allows duplicates
# - Uses index-based access
# - Slower lookup than dictionary (O(n) vs O(1))

# SET:
# - Unordered collection of unique elements
# - Mutable (but only stores immutable types)
# - No duplicates
# - Faster membership checks than list
# - No indexing (non-subscriptable)

# --------------------------------------------
# ✅ REAL-WORLD EXAMPLE: CAPITAL LOOKUP
# --------------------------------------------

capitals = {
    "maharashtra": "mumbai",
    "delhi": "new delhi",
    "goa": "panaji",
    "karnataka": "bengaluru",
    "gujarat": "gandhinagar",
    "uttar pradesh": "lucknow"
}

state = input("Enter a state to get its capital: ").lower()

if state in capitals:
    print(f"The capital of {state.title()} is {capitals[state]}")
else:
    print("We don't have a record of that state.")

# ============================================
# ⚙ INTERNALS: HOW DICTIONARIES WORK
# ============================================

# Python uses a **hash table** under the hood for dictionaries:
# - Each key is hashed (using hash(key))
# - Hash maps to a memory index (bucket)
# - Fast lookup (avg time complexity O(1))
# - If a key has same hash as another (collision), Python handles it internally

# Mutable objects like lists can't be used as keys
# because their hash can change → leads to inconsistencies

# Example (invalid key):
# my_dict = {[1,2,3]: "invalid"} → ❌ TypeError: unhashable type: 'list'

# Valid keys → str, int, float, bool, tuple (if tuple contains only hashable types)

# ============================================
# ✅ SUMMARY
# ============================================
# - Use dictionaries when you need fast lookup using a unique key
# - Ideal for representing structured data
# - Avoid using unhashable types as keys
# - Supports nesting, comprehensions, updates, deletions
# - Very memory-efficient and optimized in CPython
