# ----------------------------------------------
#         LOGICAL OPERATORS IN PYTHON
# ----------------------------------------------

# 🧠 Logical operators allow us to evaluate **multiple conditions** in one statement.
# They are often used in `if`, `elif`, `while`, etc.

# Logical operators in Python:
# 1. and  → All conditions must be True
# 2. or   → At least one condition must be True
# 3. not  → Negates the condition (True becomes False, and vice versa)

# Let's define two variables
t, b = 45, 56  # t = 45, b = 56

# -----------------------------
# LOGICAL AND
# -----------------------------
# 'and' returns True only if both sides are True

if t == 45 and b == 56:
    print("✅ AND: Both conditions are true → Executes this block")  # This will run

# If even one side is False, the entire condition becomes False
if t == 45 and b == 90:
    print("❌ This won't print because b != 90")

# -----------------------------
# LOGICAL OR
# -----------------------------
# 'or' returns True if **any one** of the conditions is True

if t == 45 or b == 90:
    print("✅ OR: At least one condition is true → Executes this block")  # This will run

if t == 0 or b == 90:
    print("❌ This won't print because both are False")

# -----------------------------
# LOGICAL NOT
# -----------------------------
# 'not' is a unary operator → it negates (inverts) the condition

# Example: not True → False
#          not False → True

# Let's negate a condition
if not t == 90:  # t is 45, so t==90 is False → not False → True
    print("✅ NOT: t is NOT equal to 90 → Executes this block")

# Combine NOT with AND
if t == 45 and not b == 56:
    print("❌ Won't run because b == 56 → not b == 56 → False")

# Combine NOT with OR
if t == 45 or not b == 90:
    # t == 45 → True
    # b == 90 → False → not b == 90 → True
    # So True or True → True → this will run
    print("✅ OR+NOT: At least one condition is True → Executes this block")

# -----------------------------
# OPERATOR PRECEDENCE (IMPORTANT)
# -----------------------------
# not > and > or

# Example: not True or False and True
# → evaluates as: (not True) or (False and True)
# → False or False
# → False

# Always use brackets when mixing operators to avoid confusion

