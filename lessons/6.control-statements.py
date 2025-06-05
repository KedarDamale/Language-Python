# --------------------------------------
#        IF STATEMENTS IN PYTHON
# --------------------------------------

# ✅ if is used to execute a block of code only when a condition is True.
# ✅ Syntax:
# if condition:
#     code_block (indented)

# 🧠 No need for parentheses like in C or Java, but you can use them optionally.

age = 20

# Version with parentheses (optional in Python)
if (age > 20):
    print("You are an adult")  # This won't execute since 20 is not greater than 20

# Recommended Pythonic way (no parentheses)
if age > 20:
    print("You are an adult")

# 🧠 The above if statement does nothing because the condition is False.
# If we want something to happen when the condition is False, we use an else block.

if age > 20:
    print("Adult")
else:
    print("Not adult")  # This will print because age is not > 20

# -------------------------
# ELIF → Else If
# -------------------------
# Used to check multiple conditions
# Python will evaluate each from top to bottom and execute only the FIRST match

if age == 10:
    print("Age is 10")
elif age == 11:
    print("Age is 11")
else:
    print("Age is neither 10 nor 11")  # This will execute

# 🧠 Even if multiple conditions are technically True, only the first one is executed.

# -------------------------
# COMPARISON OPERATORS
# -------------------------
# These return True/False based on comparison

# ==  → Equal to
# !=  → Not equal to
# >   → Greater than
# <   → Less than
# >=  → Greater than or equal to
# <=  → Less than or equal to

# Example:
if age != 25:
    print("Age is not 25")  # Output: Age is not 25

# -------------------------
# TRUTHY AND FALSY VALUES
# -------------------------
# The following values are considered Falsy in Python:
# False, None, 0, 0.0, "", [], {}, (), set()

user_input = ""

if user_input:
    print("You entered something.")
else:
    print("Input was empty.")  # This executes because "" is falsy

# This is useful for checking whether a value is "non-empty" or "non-zero" without explicitly comparing.

# -------------------------
# COMMON MISTAKES
# -------------------------

# ❌ Using = instead of ==
# if x = 5:  # This is a syntax error in Python. Use == for comparison.

# ✅ Correct usage
x = 5
if x == 5:
    print("x is 5")

# 🧠 In C, writing if(x = 5) works because = returns 5, which is truthy
# ⚠️ In Python, assignment (=) is not allowed inside conditions. Use == only.

