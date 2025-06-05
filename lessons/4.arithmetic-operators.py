# ---------------------------------------------------------
# ARITHMETIC OPERATORS IN PYTHON (With Detailed Explanation)
# ---------------------------------------------------------

# These are basic operators used for mathematical calculations.

a = 15
b = 4

# 1. Addition (+)
print(a + b)  # Output: 19

# 2. Subtraction (-)
print(a - b)  # Output: 11

# 3. Multiplication (*)
print(a * b)  # Output: 60

# 4. Division (/) → Returns float
print(a / b)  # Output: 3.75

# 5. Floor Division (//) → Discards decimal part, returns int result
print(a // b)  # Output: 3

# 6. Modulus (%) → Gives the remainder
print(a % b)  # Output: 3

# 7. Exponentiation (**) → a raised to the power b
print(a ** b)  # Output: 15^4 = 50625


# --------------------------------------------------
# AUGMENTED ASSIGNMENT OPERATORS (Shorthand Notation)
# --------------------------------------------------

# These are used to **update** the value of a variable using an operation and assignment.

x = 10

x += 5     # Equivalent to: x = x + 5
print(x)   # Output: 15

x -= 3     # x = x - 3 → 15 - 3 = 12
print(x)   # Output: 12

x *= 2     # x = x * 2 → 12 * 2 = 24
print(x)   # Output: 24

x /= 4     # x = x / 4 → 24 / 4 = 6.0
print(x)   # Output: 6.0 (Notice: becomes float)

x //= 2    # Floor divide and assign → 6.0 // 2 = 3.0
print(x)   # Output: 3.0

x %= 2     # Modulus and assign → 3.0 % 2 = 1.0
print(x)   # Output: 1.0

x **= 3    # Raise to power and assign → 1.0 ** 3 = 1.0
print(x)   # Output: 1.0


# --------------------------------------------
# BUILT-IN MATH FUNCTIONS (No math module yet)
# --------------------------------------------

# These functions work **without importing anything**

# 1. abs() → Absolute value
print(abs(-10))    # Output: 10
print(abs(5))      # Output: 5

# 2. round() → Rounds a number to nearest integer by default
print(round(3.2))  # Output: 3
print(round(3.8))  # Output: 4

# round() with second argument → number of decimal places
print(round(3.14159, 2))  # Output: 3.14

# 3. max() → Returns the largest value
print(max(3, 5, 1, 100, -2))  # Output: 100

# 4. min() → Returns the smallest value
print(min(3, 5, 1, 100, -2))  # Output: -2

# 5. pow() → Same as exponentiation (**), but is a function
print(pow(2, 3))  # Output: 8 (2^3)

# 6. sum() → Sums elements of an iterable (like a list)
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Output: 10

# 7. divmod() → Returns quotient and remainder as a tuple
print(divmod(17, 4))  # Output: (4, 1) → 17 // 4 = 4 and 17 % 4 = 1

# You can unpack it too:
q, r = divmod(17, 4)
print(f"Quotient = {q}, Remainder = {r}")  # Output: Quotient = 4, Remainder = 1
