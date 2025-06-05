# --------------------------------------------
# Program: Demonstrating 'is', 'is not', '==' and '!=' in Python
# Author: Kedar Damale
# --------------------------------------------

print("-" * 50)
print("1️⃣ IMMUTABLE TYPE (int):")
print("-" * 50)

a = 100
b = 100

# '==' checks if values are equal
print(f"a == b: {a == b}")   # True, because both hold value 100

# 'is' checks if both refer to the same memory location
print(f"a is b: {a is b}")   # True, because integers from -5 to 256 are cached in Python

# Check memory addresses using id()
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")

print("-" * 50)
print("2️⃣ MUTABLE TYPE (list):")
print("-" * 50)

x = [1, 2, 3]
y = [1, 2, 3]

print(f"x == y: {x == y}")   # True → values are same
print(f"x is y: {x is y}")   # False → different memory locations

print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")

# Let's assign x to z
z = x

print(f"x == z: {x == z}")   # True → same values
print(f"x is z: {x is z}")   # True → both refer to same list

print(f"id(x): {id(x)}")
print(f"id(z): {id(z)}")

print("-" * 50)
print("3️⃣ COMPARISON WITH None:")
print("-" * 50)

none_var = None

# Best practice is to use 'is' to compare with None
if none_var is None:
    print("none_var is None ✅")
else:
    print("none_var is NOT None ❌")

# Avoid using '== None'
if none_var == None:
    print("Still works but not recommended (== None)")

print("-" * 50)
print("4️⃣ 'is not' Operator:")
print("-" * 50)

a = "Python"
b = "Java"

# Check if two variables refer to different objects
print(f"a is not b: {a is not b}")  # True → different objects

# Even though they are different strings, you can also check values
print(f"a != b: {a != b}")  # True → different values

print("-" * 50)
print("5️⃣ STRINGS with same values (interned):")
print("-" * 50)

s1 = "hello"
s2 = "hello"

print(f"s1 == s2: {s1 == s2}")   # True → Same value
print(f"s1 is s2: {s1 is s2}")   # True → Python interns short strings for optimization

print(f"id(s1): {id(s1)}")
print(f"id(s2): {id(s2)}")

print("-" * 50)
print("6️⃣ FORCE DIFFERENT OBJECTS WITH str():")
print("-" * 50)

s3 = str("hello")
s4 = str("hello")

print(f"s3 == s4: {s3 == s4}")   # True → Same content
print(f"s3 is s4: {s3 is s4}")   # May be False → new objects created

print(f"id(s3): {id(s3)}")
print(f"id(s4): {id(s4)}")

print("-" * 50)
print("📌 SUMMARY:")
print("-" * 50)

print("""
==     → Compares values (equality)
!=     → Compares values (inequality)

is     → Compares memory identity (object location)
is not → Checks if two objects are different in memory

Use 'is' when:
  - Comparing with None
  - You need to verify object identity (not value)

Use '==' when:
  - You want to compare values or contents

Caution:
  - Don't use 'is' to compare strings, lists, or numbers for equality
  - Always use '==' unless you're specifically checking memory identity
""")
