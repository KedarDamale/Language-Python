# ----------------------------------------------
#        STRING METHODS IN PYTHON (BUILT-IN)
# ----------------------------------------------

# Let's start with a string
name = "Kedar DaMale 123"

# ------------------------
# LENGTH
# ------------------------
# len() returns the number of characters in the string (including spaces and digits)
print(len(name))  # Output: 16

# ------------------------
# FIND
# ------------------------
# find() returns the index of the first occurrence of a character
# If not found, returns -1
print(name.find("a"))  # Output: 3 (first 'a')
print(name.find("z"))  # Output: -1 (not found)

# ------------------------
# RFIND
# ------------------------
# rfind() returns the index of the last occurrence of the character
print(name.rfind("a"))  # Output: 11 (last 'a')

# ------------------------
# CAPITALIZE
# ------------------------
# capitalize() → First letter uppercase, rest lowercase
name = name.capitalize()
print(name)  # Output: "Kedar damale 123"

# ------------------------
# UPPER & LOWER
# ------------------------
# upper() → Converts entire string to uppercase
print(name.upper())  # Output: "KEDAR DAMALE 123"

# lower() → Converts entire string to lowercase
print(name.lower())  # Output: "kedar damale 123"

# ------------------------
# ISDIGIT
# ------------------------
# isdigit() → Returns True if the string only contains digits (no letters or spaces)
print(name.isdigit())  # Output: False

# ------------------------
# ISALPHA
# ------------------------
# isalpha() → Returns True only if the string contains ONLY alphabet letters (no spaces, digits, or symbols)
print(name.isalpha())  # Output: False

# ------------------------
# COUNT
# ------------------------
# count() → Returns number of times a substring occurs
print(name.count("a"))  # Output: 2

# ------------------------
# REPLACE
# ------------------------
# replace("old", "new") → Replaces all occurrences of 'old' with 'new'
print(name.replace(" ", "_"))  # Output: "Kedar_damale_123"

# ------------------------
# EXPLORE MORE STRING METHODS
# ------------------------
# You can list all string methods using:
# print(dir(str)) or help(str)

# ----------------------------------------------
#         EXERCISE: VALIDATE USERNAME
# ----------------------------------------------

# Requirements:
# - Must be ≤ 12 characters
# - Must NOT contain spaces
# - Must NOT contain digits

username = input("Enter your username: ")

# Check 1: Length
if len(username) > 12:
    print("❌ Username must be 12 characters or less.")

# Check 2: Space check
elif " " in username:
    print("❌ Username must not contain spaces.")

# Check 3: Digit check (improved using any())
elif any(char.isdigit() for char in username):
    print("❌ Username must not contain digits.")

# Valid case
else:
    print("✅ Username is valid.")
