## A nested loop is a loop inside another loop.
#there can be n number of loops inside loops

# for i in range(outer_loop_count):
#     for j in range(inner_loop_count):
#         # Code block

# This structure means:

# The outer loop runs outer_loop_count times.

# For each iteration of the outer loop, the inner loop runs inner_loop_count times.

# This leads to a total number of iterations:> Total Iterations = outer_loop_count × inner_loop_count


#===================================
# NESTED LOOPS PATTERN EXAMPLES
# ===================================
# This program prints 20 different patterns (5 Easy, 10 Medium, 5 Hard)
# using nested loops in Python with explanations and OUTPUT shown.

# ==============================
# EASY PATTERNS (Level 1)
# ==============================

print("\n1. Square of stars (5x5):")
for i in range(5):
    print("* " * 5)
# OUTPUT:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

print("\n2. Right-angled triangle:")
for i in range(1, 6):
    print("* " * i)
# OUTPUT:
# *
# * *
# * * *
# * * * *
# * * * * *

print("\n3. Inverted triangle:")
for i in range(5, 0, -1):
    print("* " * i)
# OUTPUT:
# * * * * *
# * * * *
# * * *
# * *
# *

print("\n4. Number triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# OUTPUT:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

print("\n5. Alphabet triangle:")
for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()
# OUTPUT:
# A
# A B
# A B C
# A B C D
# A B C D E


# ==============================
# MEDIUM PATTERNS (Level 2)
# ==============================

print("\n6. Right-aligned triangle:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
# OUTPUT:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

print("\n7. Inverted right-aligned triangle:")
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
# OUTPUT:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

print("\n8. Pyramid:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
# OUTPUT:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

print("\n9. Inverted pyramid:")
for i in range(5, 0, -1):
    print(" " * (5 - i) + "* " * i)
# OUTPUT:
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

print("\n10. Diamond:")
for i in range(1, 6):
    print(" " * (5 - i) + "* " * i)
for i in range(4, 0, -1):
    print(" " * (5 - i) + "* " * i)
# OUTPUT:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

print("\n11. Hollow square:")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# OUTPUT:
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

print("\n12. Hollow triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
# OUTPUT:
# *
# * *
# *   *
# *     *
# * * * * *

print("\n13. Numeric right triangle:")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# OUTPUT:
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5

print("\n14. Centered number pyramid:")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
# OUTPUT:
#     1
#    121
#   12321
#  1234321
# 123454321

print("\n15. Star pyramid (centered):")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
# OUTPUT:
#     *
#    ***
#   *****
#  *******
# *********


# ==============================
# HARD PATTERNS (Level 3)
# ==============================

print("\n16. Floyd's triangle:")
n = 1
for i in range(1, 6):
    for j in range(i):
        print(n, end=" ")
        n += 1
    print()
# OUTPUT:
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

print("\n17. Pascal's triangle:")
def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f *= i
    return f

for i in range(6):
    for j in range(6 - i):
        print(" ", end="")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()
# OUTPUT:
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 1 5 10 10 5 1

print("\n18. Zig-zag pattern:")
rows = 3
cols = 15
for i in range(rows):
    for j in range(cols):
        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
# OUTPUT:
# *   *   *   *   *
#   *   *   *   *
# *   *   *   *   *

print("\n19. Alphabet hill pattern:")
for i in range(0, 5):
    for j in range(0, 5 - i - 1):
        print(" ", end="")
    ch = 65
    for j in range(0, i + 1):
        print(chr(ch), end="")
        ch += 1
    ch -= 2
    for j in range(0, i):
        print(chr(ch), end="")
        ch -= 1
    print()
# OUTPUT:
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

print("\n20. Butterfly pattern:")
n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
# OUTPUT:
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# **********
# ****  ****
# ***    ***
# **      **
# *        *