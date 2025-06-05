#Memory management is python:https://chatgpt.com/c/68411af3-17e0-800a-906f-019174e0c941
# 
# -----------------------------------
# VARIABLES IN PYTHON (Detailed View)
# -----------------------------------

# A variable is simply a **name** that points to a **value** in memory.
# Think of it as a label you stick on some data so you can use it later.

# SYNTAX: variable_name = value

# Python is a **dynamically typed** language:
# You don't need to specify the type of a variable. Python figures it out at runtime.

# -------------------------
# 1. STRING TYPE VARIABLES
# -------------------------

name = "Kedar"  # This is a string — sequence of characters surrounded by quotes (single or double).
print(name)  # Output: Kedar
print("Kedar")  # Also prints Kedar, but directly as a string literal
print("Kedar " * 3)   # Output: Kedar Kedar Kedar #This is called string multiplication in python

# f-string (formatted string literal)
print(f"Hello {name}!")  
# The `f` before the string allows you to embed variables using curly braces.

# Checking the data type of the variable
print(type(name))  # Output: <class 'str'>


# --------------------------
# 2. NUMBER TYPES: int, float
# --------------------------

a = 45          # Integer (whole number)
b = 56.78       # Float (decimal number)

print(f"Integer is {a}\nFloat is {b}")
# \n is a newline character — used to print on a new line

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>


# --------------------------
# 3. BOOLEAN TYPE
# --------------------------

is_student = True
is_employed = False

# Boolean values can only be: True or False (capital T and F are mandatory)

print(f"Are you a student? {is_student}")
print(f"Are you employed? {is_employed}")
print(type(is_student))  # Output: <class 'bool'>


# ----------------------------------
# 4. VARIABLE NAMING RULES & TIPS
# ----------------------------------

# Rules:
# 1. Must start with a letter (a-z, A-Z) or underscore (_)
# 2. Can contain letters, numbers, underscores
# 3. Cannot be a Python keyword (like if, else, for, True, etc.)
# 4. Case-sensitive (age and Age are two different variables)

# Good Examples:
first_name = "John"
last_name = "Doe"
age = 22
_is_valid = True
roll_no_10 = 501

# Bad Examples (will give error):
# 2name = "error"     # Starts with a number
# first-name = "bad"  # Hyphens not allowed
# class = "illegal"   # 'class' is a keyword


# -------------------------------------
# 5. MULTIPLE VARIABLE ASSIGNMENTS
# -------------------------------------

x, y, z = 1, 2.5, "Hello"
print(x, y, z)  # Output: 1 2.5 Hello

# Assigning the same value to multiple variables:
a = b = c = 100
print(a, b, c)  # Output: 100 100 100


# --------------------------------
# 6. SPECIAL CASE: None (null value)
# --------------------------------

result = None  # Means 'nothing' or 'no value yet'
print(result)  # Output: None ,meaning it will print "None" on the screen
print(type(result))  # Output: <class 'NoneType'>
