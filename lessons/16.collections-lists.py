# ============================================
# ✅ PYTHON LISTS: Full In-Depth Explanation
# ============================================

# ✅ 1. What is a list?
# A list is an *ordered*, *mutable* collection that can hold elements of any data type.
# Syntax: my_list = [element1, element2, ...]

# Lists are stored in memory as objects containing a pointer to a dynamic array of object references.

# --------------------------------------------
# ✅ 2. List Creation and Access
# --------------------------------------------
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
print("First element (index 0):", fruits[0])         # Access by index
print("Last element (index -1):", fruits[-1])        # Negative index = from end
print("Sliced list (1:3):", fruits[1:3])             # Slicing: elements at index 1 and 2

# --------------------------------------------
# ✅ 3. Mutability and Memory Behavior
# --------------------------------------------
print(f"Before change: {fruits}, ID: {id(fruits)}")
fruits[1] = "Kedar"
print(f"After change: {fruits}, ID: {id(fruits)}")
# 🔍 Same ID ⇒ list is changed in-place, not recreated

# --------------------------------------------
# ✅ 4. Membership Testing
# --------------------------------------------
print("Is 'apple' in list?", "apple" in fruits)       # True
print("Is 'banana' not in list?", "banana" not in fruits) # True

# --------------------------------------------
# ✅ 5. List Methods
# --------------------------------------------
numbers = [10, 20, 30, 40, 30]
print("\nList:", numbers)

# 🔸 len() - count of elements
print("Length:", len(numbers))

# 🔸 append(x) - adds to end
numbers.append(50)
print("After append(50):", numbers)

# 🔸 extend(iterable) - adds multiple
numbers.extend([60, 70])
print("After extend([60, 70]):", numbers)

# 🔸 insert(index, value)
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# 🔸 pop([index]) - removes and returns item at index (last if omitted)
popped = numbers.pop()
print("After pop():", numbers, "Popped value:", popped)

# 🔸 remove(value) - removes first occurrence
numbers.remove(30)
print("After remove(30):", numbers)

# 🔸 index(value) - returns first index of value
print("Index of 40:", numbers.index(40))

# 🔸 count(value) - counts value
print("Count of 30:", numbers.count(30))

# 🔸 reverse() - reverses in-place
numbers.reverse()
print("After reverse():", numbers)

# 🔸 sort() - sorts in-place
numbers.sort()
print("After sort():", numbers)

# 🔸 copy() - shallow copy
copy_list = numbers.copy()
print("Copy of list:", copy_list)

# 🔸 clear() - removes all elements
copy_list.clear()
print("After clear():", copy_list)

# --------------------------------------------
# ✅ 6. List Comprehension
# --------------------------------------------
# Efficient way to create new lists from iterable
squares = [x**2 for x in range(5)]
print("\nSquares using list comprehension:", squares)

# --------------------------------------------
# ✅ 7. Identity vs Copy
# --------------------------------------------
a = [1, 2, 3]
b = a           # Reference copy - same object
c = a.copy()    # True copy - different object

a.append(4)
print("a:", a)  # Modified
print("b:", b)  # Also modified → same reference
print("c:", c)  # Unchanged → separate copy

# --------------------------------------------
# ✅ 8. Nested Lists (2D)
# --------------------------------------------
matrix = [[1, 2], [3, 4], [5, 6]]
print("\nMatrix:")
for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

# --------------------------------------------
# ✅ 9. Memory Address of Elements
# --------------------------------------------
sample = ["x", "y", "z"]
for i in range(len(sample)):
    print(f"sample[{i}] = {sample[i]}, ID: {id(sample[i])}")

# --------------------------------------------
# ✅ 10. dir() and help()
# --------------------------------------------
# Uncomment for interactive docs
# print(dir(list))
# help(list)
