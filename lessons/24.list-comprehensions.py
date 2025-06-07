# ====================================================
# ✅ LIST COMPREHENSION IN PYTHON — DETAILED EXAMPLES
# ====================================================

# 🔸 List comprehension is a concise way to create lists.
# 🔸 It is compact, faster, and more readable than traditional loops.
# 🔸 General Syntax:
#     [expression for item in iterable if condition]

# -------------------------
# ✅ Traditional Method
# -------------------------

# Given list
s = [2, 4, 7, 4, 2, 1]

# Square every element using traditional for loop
s_squared = []
for i in s:
    s_squared.append(i ** 2)

print(s_squared)  # Output: [4, 16, 49, 16, 4, 1]

# -------------------------
# ✅ Equivalent using List Comprehension
# -------------------------
s_squared = [i ** 2 for i in s]
print(s_squared)  # Output: [4, 16, 49, 16, 4, 1]

# ---------------------------------------------
# ✅ Add a condition inside list comprehension
# ---------------------------------------------

# Square only the even numbers
s_squared_even = [i ** 2 for i in s if i % 2 == 0]
print(s_squared_even)  # Output: [4, 16, 16, 4]

# ---------------------------------------------
# ✅ Using range() in List Comprehension
# ---------------------------------------------

# Create a list of even numbers from 0 to 49
even_nums = [x for x in range(0, 50) if x % 2 == 0]
print(even_nums)
# Output: [0, 2, 4, 6, ..., 48]

# Create a list of squares of even numbers from 0 to 49
even_squares = [x ** 2 for x in range(0, 50) if x % 2 == 0]
print(even_squares)
# Output: [0, 4, 16, 36, ..., 2304]

# -----------------------------------------------------
# ✅ Nested List Comprehension (2D list flattening)
# -----------------------------------------------------

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten the matrix into a single list
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# -----------------------------------------------------
# ✅ Conditional Expressions (if-else) inside List Comp
# -----------------------------------------------------

# Categorize numbers as "even" or "odd"
labels = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(labels)  # Output: ['even', 'odd', 'even', ..., 'odd']

# -----------------------------------------------------
# ✅ Filtering Strings using List Comprehension
# -----------------------------------------------------

words = ["apple", "banana", "cherry", "apricot", "blueberry"]

# Select only words that start with 'a'
a_words = [w for w in words if w.startswith('a')]
print(a_words)  # Output: ['apple', 'apricot']

# -----------------------------------------------------
# ✅ Advanced: Cartesian Product using List Comprehension
# -----------------------------------------------------

colors = ["red", "green"]
objects = ["apple", "leaf"]

combinations = [(c, o) for c in colors for o in objects]
print(combinations)
# Output: [('red', 'apple'), ('red', 'leaf'), ('green', 'apple'), ('green', 'leaf')]

# ======================================================
# ✅ Summary of List Comprehension Features:
# ======================================================

'''
🔹 Basic Syntax:
    [expression for item in iterable]

🔹 With condition:
    [expression for item in iterable if condition]

🔹 With if-else inside:
    [true_val if condition else false_val for item in iterable]

🔹 Nested:
    [expression for outer in outer_iterable for inner in inner_iterable]

🔹 Equivalent of:
    result = []
    for item in iterable:
        if condition:
            result.append(expression)

🔹 Faster and shorter but use only when readability is preserved.
'''

# ✅ End of List Comprehension Examples
