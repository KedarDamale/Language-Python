# ============================================
# ✅ PYTHON FUNCTIONS: COMPLETE EXPLANATION
# ============================================

# 🔹 FUNCTIONS are reusable blocks of code
# Syntax:
#     def function_name(arguments):
#         # code block
#     function_name(arguments)

# ----------------------------
# 📌 BASIC FUNCTION (No args)
# ----------------------------
def greet():
    print("Hello, world!")  # Simple function with no arguments

greet()  # Calling the function


# ----------------------------
# 📌 FUNCTION WITH ARGUMENTS
# ----------------------------
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Kedar")
greet_person("Damale")

# Arguments (in def) vs Parameters (at call):
# - Arguments: Variables used in the function definition.
# - Parameters: Actual values passed during function call.


# ----------------------------
# 📌 MULTIPLE ARGUMENTS
# ----------------------------
def greet_full(a, b, c, d, e):
    print(f"Hello {a}, {b}, {c}, {d}, {e}")

greet_full("k", "e", "d", "a", "r")  # Order matters! Positional


# ----------------------------
# 📌 RETURN STATEMENT
# ----------------------------
def add(x, y):
    return x + y  # return ends the function and returns a value

result = add(10, 20)
print("Addition:", result)


# ----------------------------
# 📌 CAPITALIZED FULL NAME
# ----------------------------
def full_name(fname, lname):
    return f"{fname.capitalize()} {lname.capitalize()}"

print(full_name("kedar", "damale"))


# ============================================
# ✅ TYPES OF ARGUMENTS
# ============================================

# --------------------------------
# 1️⃣ POSITIONAL ARGUMENTS
# --------------------------------
def describe_pet(animal, name):
    print(f"{name} is a {animal}.")

describe_pet("dog", "Buddy")
describe_pet("Buddy", "dog")  # Wrong meaning but still valid


# --------------------------------
# 2️⃣ DEFAULT ARGUMENTS
# --------------------------------
def net_price(price, tax=0.05, discount=0):
    return price * (1 - discount) * (1 + tax)

print(net_price(500))            # Uses default tax and discount
print(net_price(500, 0.1))       # tax = 0.1, discount = 0
print(net_price(500, 0.1, 0.1))  # tax = 0.1, discount = 0.1


# --------------------------------
# 3️⃣ KEYWORD ARGUMENTS
# --------------------------------
def student_info(name, age):
    print(f"{name} is {age} years old.")

student_info(name="Kedar", age=21)
student_info(age=21, name="Kedar")  # Order doesn't matter

# Invalid:
# student_info("Kedar", age=21, name="Kedar") → multiple values for 'name'
# student_info(age=21, "Kedar") → positional after keyword ❌


# --------------------------------
# 4️⃣ ARBITRARY ARGUMENTS (*args)
# --------------------------------
# *args = Arbitrary Positional Arguments (stored as tuple)
def add_all(*args):
    print(f"Type of args: {type(args)}")
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3, 4, 5))  # 15


# --------------------------------
# 5️⃣ ARBITRARY KEYWORD ARGUMENTS (**kwargs)
# --------------------------------
# **kwargs = Arbitrary Keyword Arguments (stored as dict)
def user_profile(**kwargs):
    return f'''
    Name: {kwargs.get("name")}
    Age: {kwargs.get("age")}
    Country: {kwargs.get("country")}
    '''

print(user_profile(name="Kedar", age=21, country="India"))


# --------------------------------
# 6️⃣ COMBINED: *args and **kwargs
# --------------------------------
def calc_sum(*args, **kwargs):
    total = sum(args)
    sign = kwargs.get("sign", "+")
    return f"{sign}{total}"

print(calc_sum(1, 2, 3, 4, 5, sign="+"))
print(calc_sum(10, 20, 30, sign="-"))


# ============================================
# ✅ EXTRA: FUNCTION NESTING & INLINE
# ============================================

# Functions can call other functions
def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)

print("Sum of Squares:", sum_of_squares(3, 4))  # 25


# ============================================
# ✅ SUMMARY
# ============================================

'''
🔹 Function = Reusable block with def keyword
🔹 Arguments:
    1. Positional: Based on order.
    2. Default: Values used when not supplied.
    3. Keyword: key=value style, order doesn't matter.
    4. *args: Tuple of extra unnamed values.
    5. **kwargs: Dict of extra named values.
🔹 Return = Exit function and return data
🔹 Use functions to reduce redundancy and modularize logic
'''

