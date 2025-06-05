# ----------------------------
# WHILE LOOP + print() Explained
# ----------------------------

# 1️⃣ Basic While Loop Example:
# The while loop keeps running as long as the condition is True.

name = input("Enter your name: ")

# This loop checks if the input is empty, and keeps asking until user enters something.
while name == "":
    print("❌ Name can't be empty. Please enter again.")
    name = input("Enter your name: ")

print(f"✅ Hello {name}!")  # this executes after loop ends

print("-" * 50)  # prints a horizontal line using string multiplication


# 2️⃣ Counting Example using While Loop
# We print numbers from 1 to 5

counter = 1  # start from 1
while counter <= 5:
    print(f"Counter: {counter}")
    counter += 1  # increment to eventually end loop

print("-" * 50)


# 3️⃣ Password Retry Example using While Loop

correct_password = "python123"
password = input("Enter your password: ")

# Keep asking until correct password is given
while password != correct_password:
    print("❌ Incorrect password. Try again.")
    password = input("Enter your password: ")

print("🔓 Access granted!")

print("-" * 50)


# 4️⃣ Infinite Loop Example (with break)
# Use `break` to exit even when the loop condition is always True

while True:
    command = input("Type 'exit' to stop: ")
    if command == "exit":
        print("👋 Exiting loop now...")
        break  # breaks the loop
    print(f"You typed: {command}")

print("-" * 50)


# 5️⃣ Using while loop to validate numeric input

age = input("Enter your age: ")

# Keep asking if the input is not a digit
while not age.isdigit():
    print("❌ Age must be a number.")
    age = input("Enter your age: ")

print(f"🎉 You entered age: {age}")

print("-" * 50)


