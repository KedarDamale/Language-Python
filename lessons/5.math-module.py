# ----------------------------------------
# DEMO OF PYTHON MATH MODULE (IN DEPTH)
# ----------------------------------------

import math  # The built-in math module provides advanced mathematical functions

# ----------------------------------------
# BASIC MATH FUNCTIONS
# ----------------------------------------

a = 16
b = 5

# √16 = 4.0 — returns square root of a number
print(f"Square root of {a}: {math.sqrt(a)}")              # Returns float

# 16^5 = 1048576.0 — raises a to the power b
print(f"{a} raised to {b}: {math.pow(a, b)}")             # Returns float, even if result is whole

# Ceil: smallest integer >= number
print(f"Ceil of 5.2: {math.ceil(5.2)}")                   # 6

# Floor: largest integer <= number
print(f"Floor of 5.8: {math.floor(5.8)}")                 # 5

# Trunc: remove decimal part (doesn't round, just chops off)
print(f"Truncate 7.999 to integer: {math.trunc(7.999)}")  # 7

# fabs(): float version of abs(), always returns positive float
print(f"Absolute of -7.5: {math.fabs(-7.5)}")             # 7.5

print("-" * 50) #This is string multiplication in python 

# ----------------------------------------
# LOGARITHMIC FUNCTIONS
# ----------------------------------------

# Natural log: base e (2.71828)
print(f"Natural log of 10 (ln(10)): {math.log(10)}")      # ~2.302

# Base 10 log
print(f"Log base 10 of 1000: {math.log10(1000)}")         # 3.0

# Base 2 log — useful in binary operations and CS problems
print(f"Log base 2 of 8: {math.log2(8)}")                 # 3.0

# Log with custom base
print(f"Log base 3 of 81: {math.log(81, 3)}")             # 4.0

print("-" * 50)

# ----------------------------------------
# EXPONENTIAL FUNCTION
# ----------------------------------------

# e^2 — used in exponential growth problems
print(f"e^2: {math.exp(2)}")  # ~7.389

print("-" * 50)

# ----------------------------------------
# TRIGONOMETRIC FUNCTIONS
# ----------------------------------------

angle_deg = 90
angle_rad = math.radians(angle_deg)  # Convert 90 degrees → π/2 radians

# sin(90°) = 1
print(f"sin({angle_deg}°): {math.sin(angle_rad)}")

# cos(90°) = 0
print(f"cos({angle_deg}°): {math.cos(angle_rad)}")

# tan(45°) = 1
print(f"tan(45°): {math.tan(math.radians(45))}")

# Inverse functions (arc = angle in radians)
print(f"asin(1): {math.degrees(math.asin(1))}°")  # sin⁻¹(1) = 90°
print(f"acos(0): {math.degrees(math.acos(0))}°")  # cos⁻¹(0) = 90°
print(f"atan(1): {math.degrees(math.atan(1))}°")  # tan⁻¹(1) = 45°

# radians() converts degrees → radians
# degrees() converts radians → degrees

print("-" * 50)

# ----------------------------------------
# CONSTANTS
# ----------------------------------------

print(f"Value of pi: {math.pi}")     # 3.14159
print(f"Value of e: {math.e}")       # 2.71828
print(f"Value of tau (2π): {math.tau}") # ~6.28318

# Used in physics, geometry, data science

print("-" * 50)

# ----------------------------------------
# SPECIAL NUMERIC FUNCTIONS
# ----------------------------------------

print(f"Is 5 finite? {math.isfinite(5)}")           # True
print(f"Is infinity infinite? {math.isinf(math.inf)}")  # True
print(f"Is NaN not a number? {math.isnan(math.nan)}")   # True

# Notes:
# - NaN (Not a Number) is used for undefined results (0/0, etc.)
# - inf (infinity) is used for overflows, divisions by 0

print("-" * 50)

# ----------------------------------------
# GCD, LCM, and DIVMOD
# ----------------------------------------

x, y = 48, 18

# GCD → Greatest Common Divisor
print(f"GCD of {x} and {y}: {math.gcd(x, y)}")  # 6

# LCM → Least Common Multiple (Python 3.9+)
print(f"LCM of {x} and {y}: {math.lcm(x, y)}")  # 144

# divmod() → Returns (quotient, remainder)
q, r = divmod(17, 4)
print(f"divmod(17, 4): Quotient = {q}, Remainder = {r}")

print("-" * 50)

# ----------------------------------------
# MINI PROJECT: CIRCLE METRICS
# ----------------------------------------

radius = float(input("Enter the radius of a circle: "))  # User input for radius

# Area = π * r^2
area = math.pi * math.pow(radius, 2)

# Circumference = 2 * π * r
circumference = 2 * math.pi * radius

# round() is used here to format output
print(f"Area of circle: {round(area, 2)}")             # Rounded to 2 decimal places
print(f"Circumference of circle: {round(circumference, 2)}")
