# ============================================
# ✅ ITERABLES, LOOPS, AND REVERSING IN PYTHON
# ============================================

# 🔸 An **iterable** is any object capable of returning its elements one at a time.
# These can be used in loops like `for` and are commonly lists, tuples, strings, dicts, and sets.

# --------------------------------------------
# ✅ Iterating over a list
# --------------------------------------------
l = [2, 3, 4, 5, 6]
for i in l:
    print(i)  # Prints each element one per line

# --------------------------------------------
# ✅ Nested Loop with `end` Argument in Print
# --------------------------------------------

# List of names (strings are also iterable)
s = ["Kedar", "Kanchan", "Pravin", "Priya"]

# Outer loop over strings, inner loop over characters in string
for name in s:
    for ch in name:
        print(ch, end=" ")  # print letters with a space, on same line
    print()  # move to new line after each name

# Output:
# K e d a r
# K a n c h a n
# P r a v i n
# P r i y a


# --------------------------------------------
# ✅ Reversing Iteration using `reversed()`
# --------------------------------------------

# reversed() works on sequences: list, tuple, string. Not on sets or dicts directly.
for name in reversed(s):
    for ch in name:
        print(ch, end=" ")
    print()

# --------------------------------------------
# ✅ Reversing using Indexing (alternative)
# --------------------------------------------

# Reversing using range (index method)
for i in range(len(s)-1, -1, -1):  # from last index to 0
    for ch in s[i]:
        print(ch, end=" ")
    print()

# --------------------------------------------
# ❌ Wrong usage to correct
# The below code was incorrect: s[i]-1 tries to subtract 1 from a string!
# for i in range(0,len(s)):
#     for j in range(0,len(s[i]-1)):
#         print(s[j],end=" ")

# Corrected (printing letters again)
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end=" ")
    print()


# --------------------------------------------
# ✅ Iterating over Tuples (same as lists)
# --------------------------------------------
t = ("apple", "banana", "cherry")
for item in t:
    print(item)

# --------------------------------------------
# ✅ Iterating over Sets (unordered)
# --------------------------------------------

# NOTE: Sets are unordered, so output order is not guaranteed.
set_example = {"red", "green", "blue"}
for color in set_example:
    print(color)

# ❌ reversed(set_example) will raise TypeError
# reversed() does not work on sets directly:
# TypeError: 'set' object is not reversible

# --------------------------------------------
# ✅ Iterating over Dictionaries
# --------------------------------------------

info = {
    "Name": "Kedar",
    "Age": 20,
    "Grade": "Last year",
    "Degree": "BE"
}

# 🔹 Iterating over keys (default behavior of for loop on dict)
for key in info:
    print(key)

# 🔹 Using .keys() explicitly (same result)
for key in info.keys():
    print(key)

# 🔹 Using .values() to iterate over values
for value in info.values():
    print(value)

# 🔹 Using .items() to get both keys and values
for key, value in info.items():
    print(f"{key}: {value}")

# Output:
# Name: Kedar
# Age: 20
# Grade: Last year
# Degree: BE

# --------------------------------------------
# ✅ Summary
# --------------------------------------------

'''
🔸 All the following are iterable: list, tuple, string, dict, set
🔸 `for element in iterable` is the standard loop form
🔸 `end=" "` in `print()` lets you control line breaks and spacing
🔸 `reversed()` only works on sequences like list/tuple/string
🔸 Set and dict are unordered — no guaranteed order of elements
🔸 Use `.keys()`, `.values()`, and `.items()` with dicts
🔸 Avoid using reversed() on set/dict directly
'''

# ✅ End of Iterable Concepts
