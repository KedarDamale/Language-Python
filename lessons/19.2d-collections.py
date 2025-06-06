# ================================
# ✅ 2D Collections in Python
# ================================
# - Built using nesting: List of Lists → most common (like matrix) or tuple of tuples or set of sets or even list of tuples, sets, lists and vice versa
# - Use two indices: n[row][col]
# - Use two loops to iterate: outer for rows, inner for cols
# - Very useful for matrix operations, grids, game boards, tables, etc.

# =================================================================================================
# 📌 2D COLLECTIONS IN PYTHON Normally to represent 2D collection in python NESTED LISTS are used) 
# =================================================================================================

# ✅ Nested list = A list containing multiple lists (like a matrix)
n = [
    [1, 2, 3],
    [2, 3, 6],
    [6, 8, 9],
    [2, 5, 7]
]

# 2D list visualized as matrix:
# Row 0 → [1, 2, 3]
# Row 1 → [2, 3, 6]
# Row 2 → [6, 8, 9]
# Row 3 → [2, 5, 7]

# ====================================
# 💡 ACCESSING ELEMENTS
# ====================================

print("Entire Matrix:")
print(n)  # Prints entire 2D list

print("\nRow at index 0:")
print(n[0])  # Prints first row → [1, 2, 3]

print("\nElement at row 0, column 1:")
print(n[0][1])  # Prints 2 → first row's second element

# Note:
# n[row][column]
# First index → row
# Second index → column

# ====================================
# 🔁 PRINTING EACH ROW
# ====================================
print("\nEach row separately:")
for row in n:
    print(row)

# OUTPUT:
# [1, 2, 3]
# [2, 3, 6]
# [6, 8, 9]
# [2, 5, 7]

# ====================================
# 🔁 PRINTING IN MATRIX FORM (Nested Loops)
# ====================================
print("\nMatrix format:")
for row in n:
    for col in row:
        print(col, end=" ")
    print()  # new line after each row

# OUTPUT:
# 1 2 3 
# 2 3 6 
# 6 8 9 
# 2 5 7

# ====================================
# 🔍 LOGIC EXPLANATION
# ====================================

# To iterate over 2D list, you need two loops:
# Outer loop → goes over each row (i.e., list inside list)
# Inner loop → goes over each element of that row (i.e., each column)

# Example:
# for row in matrix:
#     for col in row:
#         print(col)

# This prints each element in row-major order (left to right, top to bottom)

# ====================================
# 🧠 MEMORY MODEL
# ====================================

# n = [ [1,2,3], [2,3,6], ... ] ← n is a list of lists
# Each list (row) is a separate object in memory.
# You can access/modify any element directly using indexing.

# Example:
# n[1][2] = 99
# Changes the 3rd column of 2nd row to 99 → [2, 3, 99]

# ====================================
# ✅ Python 2D List Flexibility
# ====================================

# You can mix types too (though not recommended for matrix):
mix = [[1, 2], (3, 4), {5, 6}]
print("\nMixed 2D structure:")
for group in mix:
    print(group)

# You can even nest list inside tuple, tuple inside set (if hashable), etc.
