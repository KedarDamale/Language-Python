# -------------------------------------------------------
#      CONDITIONAL EXPRESSIONS / TERNARY OPERATOR
# -------------------------------------------------------

# 🧠 A conditional expression is a one-liner way to choose between two values based on a condition.
# 🧠 It’s also called a ternary operator because it has three parts: condition, true_value, false_value

# ✅ SYNTAX:
# result = true_value if condition else false_value

# -------------------------
# EXAMPLE 1: Check even or odd
# -------------------------

num = 21

# This line will print "Odd" because 21 % 2 != 0 → False → goes to the else part
print("Even" if num % 2 == 0 else "Odd")  # Output: Odd

# ✅ You can even wrap a print() call inside ternary, but it's not common practice
# Only one of these will execute — just like if/else
print("Even") if num % 2 == 0 else print("Odd")  # Output: Odd

# -------------------------
# EXAMPLE 2: Storing result in a variable
# -------------------------

# The result of the ternary expression is assigned to the variable `result`
result = "Even" if num % 2 == 0 else "Odd"
print(result)  # Output: Odd

# -------------------------
# EXAMPLE 3: Comparing two numbers
# -------------------------

a = 45
b = 18

# You can write multiple statements in one line using `;` (not recommended in production, but legal in Python)
# This will check: is a > b → 45 > 18 → True → print "a is bigger"
print("a is bigger" if a > b else "b is bigger")  # Output: a is bigger

# -------------------------
# WHEN TO USE TERNARY OPERATOR
# -------------------------
# ✅ Simple conditional assignments
# ✅ Inline quick conditions for print or small logic
# ❌ Don’t use ternary for complex decisions or nested conditions — it hurts readability

# Example of BAD USAGE (just for knowledge):
# print("Positive" if x > 0 else "Zero" if x == 0 else "Negative")
# Too hard to read — use if-elif-else instead

# -------------------------
# END OF PROGRAM
# -------------------------
