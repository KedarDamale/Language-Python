# -------------------------------------
# USER INPUT IN PYTHON - IN DETAIL
# -------------------------------------

# The input() function waits for the user to type something and press Enter.
# It always returns the input as a string — even if the user types a number.

# Basic example:
name = input("Enter your name: ")  # Prompts user and stores the input ,unlike input--scanf doesnt support anything other than format specifiers 
print(f"Hello, {name}!")  # f-string used to personalize greeting

# Check the data type:
print(f"Type of name: {type(name)}")  # Output: <class 'str'>


# --------------------------------------
# TYPE CASTING USER INPUT
# --------------------------------------

# Since input() always returns string, if you want numerical values:
age = int(input("Enter your age: "))  # Convert directly to integer
height = float(input("Enter your height in meters: "))  # Convert to float

print(f"Age: {age} (type: {type(age)})")
print(f"Height: {height} (type: {type(height)})")


# --------------------------------------
# CHAINING: TYPE CASTING + INPUT
# --------------------------------------

# Instead of:
# temp = input("Enter temperature: ")
# temp = float(temp)

# Do this (chaining):
temp = float(input("Enter temperature: "))
print(f"Temperature is {temp}°C")


# --------------------------------------
# HANDLING MULTIPLE INPUTS
# --------------------------------------

# Taking two values in one line separated by space
x, y = input("Enter two numbers separated by space: ").split()
print(f"x = {x}, y = {y}")

# By default these will be strings. Let's convert them:
x, y = map(int, input("Enter two integers separated by space: ").split())
print(f"Sum = {x + y}")


# --------------------------------------
# EDGE CASES & BEST PRACTICES
# --------------------------------------

# What if user enters wrong type?
# a = int(input("Enter number: "))  # Crashes if input is not numeric
# Instead, use try-except to make it robust:

try:
    num = int(input("Enter an integer: "))
    print(f"You entered: {num}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Note: This is essential for real-world applications


# --------------------------------------
# BOOL INPUT - manual conversion
# --------------------------------------

# Python doesn't have a built-in way to take boolean from user input directly.
# You must handle it manually:
val = input("Enter yes or no: ")

if val.lower() == "yes":
    flag = True
elif val.lower() == "no":
    flag = False
else:
    flag = None

print(f"Boolean flag is: {flag}")


# --------------------------------------
# ADVANCED EXAMPLE: SIMPLE CALCULATOR
# --------------------------------------

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(f"Result = {a + b}")
elif op == "-":
    print(f"Result = {a - b}")
elif op == "*":
    print(f"Result = {a * b}")
elif op == "/":
    if b != 0:
        print(f"Result = {a / b}")
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
