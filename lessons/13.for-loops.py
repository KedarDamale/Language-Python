# -----------------------------------------------------------
# FOR LOOP, RANGE(), MEMBERSHIP OPERATORS, CONTROL STATEMENTS
# -----------------------------------------------------------

# 🔹 FOR LOOP with RANGE()

# range(start, stop, step)
# start → starting number (inclusive)
# stop → stopping number (exclusive, i.e., not included)
# step → increment/decrement value

print("🔸 Printing even numbers from 0 to 98 using range():")
for i in range(0, 100, 2):  # start=0, stop=100, step=2
    print(i, end=" ")
print("\n" + "-" * 50)

# range(n) is same as range(0, n)
print("🔸 Print numbers 0 to 4:")
for i in range(5):  # same as range(0, 5)
    print(i, end=" ")
print("\n" + "-" * 50)

# range with negative step (counting backwards)
print("🔸 Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n" + "-" * 50)


# 🔹 FOR LOOP over an iterable (like string)

print("🔸 Looping over characters of string (ignoring spaces):")

a = "Kedar Pravin Damale"
for ch in a:
    if ch == " ":
        pass  # do nothing, skip this iteration (used as placeholder)
    else:
        print(f"{ch}-", end="")
print("\n" + "-" * 50)

# 🔹 MEMBERSHIP OPERATORS
# Used to check if a value exists in a sequence

# in → returns True if found
# not in → returns True if not found

word = "damale"
if "d" in word:
    print("✅ Letter 'd' found in the word.")
if "z" not in word:
    print("✅ Letter 'z' is NOT in the word.")
print("-" * 50)


# 🔹 BREAK Statement
# Used to exit the loop prematurely

print("🔸 Using break: Stop printing at 5")

for i in range(10):
    if i == 5:
        print("Reached 5, breaking loop.")
        break  # exits the loop
    print(i)

print("-" * 50)


# 🔹 CONTINUE Statement
# Used to skip the current iteration and move to next one

print("🔸 Using continue: Skip even numbers")

for i in range(1, 10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i, end=" ")
print("\n" + "-" * 50)


# 🔹 PASS Statement
# Used as a placeholder when a statement is syntactically required but no code is needed

print("🔸 Using pass in loop:")
for letter in "Kedar":
    if letter == "e":
        pass  # no operation; can be used while planning code
    else:
        print(letter, end=" ")
print("\n" + "-" * 50)

# 🔹 Nested for-loop example (extra)

print("🔸 Multiplication Table (1 to 3)")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}×{j}={i*j}", end="\t")
    print()  # newline after each row
print("-" * 50)
