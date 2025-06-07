# =========================================================
# ✅ PYTHON MATCH-CASE STATEMENT (Pattern Matching)
# =========================================================

# 🔹 Introduced in Python 3.10
# 🔹 Works like switch-case from C, but more powerful (structural pattern matching)
# 🔹 Cleaner alternative to multiple if-elif-else statements

# 📌 Basic Syntax:
# match variable:
#     case value1:
#         # code
#     case value2:
#         # code
#     case _:
#         # default case (underscore = wildcard)

# ========================
# ✅ Basic Example
# ========================

day = "Sunday"

match day:
    case "Monday":
        print("Start of work week")
    case "Friday":
        print("End of work week")
    case "Sunday":
        print("Time to rest")
    case _:
        print("Just another day")

# Output: Time to rest

# ========================
# ✅ Integer Match Example
# ========================

x = 2

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Unknown")

# Output: Two

# ==========================================
# ✅ Multiple Values in One Case (Tuple match)
# ==========================================

color = "green"

match color:
    case "red" | "blue":
        print("Primary color")
    case "green" | "yellow":
        print("Secondary color")
    case _:
        print("Unknown color")

# Output: Secondary color

# ===================================
# ✅ Matching with Variables (Binding)
# ===================================

person = ("Kedar", 22)

match person:
    case (name, age):
        print(f"Name: {name}, Age: {age}")

# Output: Name: Kedar, Age: 22

# 🔸 Variables can be extracted directly from tuples/lists — very powerful!

# ===================================
# ✅ Dictionary Matching
# ===================================

user = {"type": "admin", "id": 101}

match user:
    case {"type": "admin", "id": user_id}:
        print(f"Admin with ID {user_id}")
    case {"type": "guest"}:
        print("Guest User")
    case _:
        print("Unknown")

# Output: Admin with ID 101

# ===================================
# ✅ Using Conditions (Guards)
# ===================================

score = 87

match score:
    case s if s >= 90:
        print("Grade: A")
    case s if s >= 80:
        print("Grade: B")
    case s if s >= 70:
        print("Grade: C")
    case _:
        print("Fail")

# Output: Grade: B

# ================================
# ✅ The Default Case: `case _`
# ================================
# The underscore (`_`) is the default or fallback case, like `default:` in C

# ======================================
# ✅ Important: No Fall-through Behavior
# ======================================

# 🚫 Unlike C/C++ switch, Python's match-case does NOT fall through
# ✅ No need for break statements — only the first matching case runs

# Example:

x = 3

match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")

# Output: Three
# ✅ ONLY "Three" is printed — no fall-through like C

# ========================================
# ✅ Comparison: Python match vs C/C++ switch
# ========================================

'''
+----------------------------+-------------------------------+
| Feature                    | C/C++ switch-case             |
+----------------------------+-------------------------------+
| Introduced in              | C since early versions        |
|                            | Python 3.10 (match-case)      |
+----------------------------+-------------------------------+
| Syntax                     | switch(x) { case ... }        |
|                            | match x: case ...             |
+----------------------------+-------------------------------+
| Pattern matching           | ❌ only compares values        |
|                            | ✅ supports structure, tuples |
+----------------------------+-------------------------------+
| Fall-through by default    | ✅ requires break             |
|                            | ❌ No fall-through in Python  |
+----------------------------+-------------------------------+
| Multiple values per case   | Needs multiple cases          |
|                            | Use `case a | b | c`          |
+----------------------------+-------------------------------+
| Works with dict/list       | ❌ No                         |
|                            | ✅ Yes                        |
+----------------------------+-------------------------------+
| Default Case               | case default:                 |
|                            | case _:                       |
+----------------------------+-------------------------------+
| Can destructure values     | ❌                            |
|                            | ✅ match (a, b), match dict   |
+----------------------------+-------------------------------+
'''

# ========================================
# ✅ Summary
# ========================================

'''
🔹 Python's match-case is a modern, powerful replacement for if-elif chains.
🔹 Cleaner than if-else, more flexible than C-style switch.
🔹 No need for `break` — no fall-through behavior.
🔹 Supports:
    • Simple value matches
    • OR (|) conditions in a single case
    • Tuple/list unpacking
    • Dict matching
    • Guards (if condition after case)
🔹 Use `case _:` as default
🔹 Python's match-case is pattern-matching, not just value checking — this makes it significantly more powerful.
'''

# ✅ End of Program
