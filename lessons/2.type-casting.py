# ------------------------------------------
# TYPE CASTING (a.k.a. Type Conversion) in PYTHON
# ------------------------------------------

# Type casting is used to **convert** one data type into another.
# This is often required when combining different types in operations (like str + int will cause error).

# EXPLICIT TYPE CASTING (you do it manually using functions like str(), int(), float(), bool())

name = "Kedar"     # <class 'str'>
age = 20           # <class 'int'>
age_str = "20"     # <class 'str'>
f = 98.345         # <class 'float'>

# Converting int -> str
print(f"Original age: {age}, Type: {type(age)}")  # Output: 20, <class 'int'>
converted = str(age)
print(f"After conversion: {converted}, Type: {type(converted)}")  # Output: "20", <class 'str'>


# Converting str -> int
# This will only work if the string contains a valid number
converted_age = int(age_str)  
print(converted_age, type(converted_age))  # Output: 20 <class 'int'>


# Invalid conversion will cause an error
invalid = "twenty"
# int(invalid)  # Uncommenting this line will raise: ValueError: invalid literal for int() with base 10: 'twenty'


# Converting float -> int (truncate, not round)
truncated = int(f)
print(f"Original float: {f}, After int conversion: {truncated}")  # Output: 98


# Converting int -> float
a = 15
a_float = float(a)
print(a_float, type(a_float))  # Output: 15.0 <class 'float'>


# ----------------------
# BOOLEAN CONVERSIONS
# ----------------------

# In Python, bool() is used to convert any value into True or False

print(bool(name))  # True → non-empty string
print(bool(""))    # False → empty string

print(bool(100))   # True → non-zero number
print(bool(0))     # False → zero

print(bool(0.00001))  # True → non-zero float
print(bool(0.0))      # False → zero float

print(bool("False"))  # True → string is non-empty, doesn't matter what it says inside
print(bool(None))     # False → None means absence of value


# -------------------------------
# IMPLICIT TYPE CASTING (done by Python)
# -------------------------------

# When you mix int and float in an expression, Python will implicitly cast int to float
x = 5       # int
y = 2.0     # float
z = x + y   # int + float → float
print(z, type(z))  # Output: 7.0 <class 'float'>


# -------------------------------
# SUMMARY TABLE: CASTING FUNCTIONS
# -------------------------------

# str(x)   → Convert to string
# int(x)   → Convert to integer (if possible)
# float(x) → Convert to float (if possible)
# bool(x)  → Convert to boolean (truthy/falsy evaluation)

# Some edge cases
print(int("10"))       # 10 → works
print(float("10.5"))   # 10.5 → works
# print(int("10.5"))   # ❌ Error! Cannot convert float string directly to int
print(int(float("10.5")))  # ✅ First convert to float then int → 10



