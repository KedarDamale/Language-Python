# =============================================================
# 🔧 Python File Handling: Detection, Creation, Update, Deletion
# =============================================================

import os  # Used for file detection, deletion, path operations

# -------------------------------------------------------------
# ✅ 1. Detect if file exists before operating on it
# -------------------------------------------------------------
file_path = "demo_file.txt"

if os.path.exists(file_path):
    print(f"📁 File '{file_path}' exists.")
else:
    print(f"📁 File '{file_path}' does not exist. Will be created.")

# -------------------------------------------------------------
# ✅ 2. Create a file and write initial data to it
# -------------------------------------------------------------
# 'w' mode creates file if it doesn't exist, or overwrites if it does
with open(file_path, 'w') as f:
    f.write("First Line\n")
    f.write("Second Line\n")
    print("✅ File created and initial content written.")

# -------------------------------------------------------------
# ✅ 3. Append more data without erasing old data
# -------------------------------------------------------------
# 'a' mode appends to the file instead of overwriting it
with open(file_path, 'a') as f:
    f.write("Third Line (appended)\n")
    print("📝 Additional content appended to the file.")

# -------------------------------------------------------------
# ✅ 4. Read full content of the file
# -------------------------------------------------------------
with open(file_path, 'r') as f:
    content = f.read()
    print("📄 Reading full file content:")
    print(content)

# -------------------------------------------------------------
# ✅ 5. Read file line by line (memory-efficient for large files)
# -------------------------------------------------------------
print("📑 Reading line by line:")
with open(file_path, 'r') as f:
    for line in f:
        print(f"→ {line.strip()}")

# -------------------------------------------------------------
# ✅ 6. File pointer operations using tell() and seek()
# -------------------------------------------------------------
with open(file_path, 'r') as f:
    print(f"📍 Current pointer position: {f.tell()}")  # → 0
    data = f.read(5)  # Reads first 5 characters
    print(f"📖 First 5 characters: {data}")
    print(f"📍 New pointer position: {f.tell()}")  # After reading
    f.seek(0)  # Moves pointer back to beginning
    print(f"📍 Pointer reset to: {f.tell()}")
    print(f"📖 File again from start: {f.readline().strip()}")

# -------------------------------------------------------------
# ✅ 7. Error handling with files
# -------------------------------------------------------------
try:
    with open("non_existing_file.txt", 'r') as f:
        data = f.read()
except FileNotFoundError:
    print("🚫 FileNotFoundError: File doesn't exist.")

# -------------------------------------------------------------
# ✅ 8. File Deletion
# -------------------------------------------------------------
# Always check before deleting
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"🗑️ File '{file_path}' has been deleted.")
else:
    print(f"⚠️ File '{file_path}' doesn't exist. Cannot delete.")

# -------------------------------------------------------------
# ✅ 9. Create a directory (if needed)
# -------------------------------------------------------------
folder_name = "new_folder"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"📁 Directory '{folder_name}' created.")
else:
    print(f"📁 Directory '{folder_name}' already exists.")

# -------------------------------------------------------------
# ✅ 10. Binary file writing (image/audio/etc.)
# -------------------------------------------------------------
binary_file = "binary_data.bin"
with open(binary_file, 'wb') as bf:
    bf.write(b"\x42\x43\x44")  # Writing raw bytes
    print("📦 Binary file written.")

# ✅ Read binary file
with open(binary_file, 'rb') as bf:
    data = bf.read()
    print(f"📦 Binary content: {data}")

# Delete binary file after use
os.remove(binary_file)


# With operator in python 