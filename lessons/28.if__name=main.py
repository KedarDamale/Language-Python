# ==========================================
# ✅ PURPOSE OF __name__ == "__main__"
# ==========================================

# Every Python file (.py) is either:
# 1. Run directly by the user (e.g., `python script.py`)
# 2. Imported as a module into another Python file (e.g., `import script`)

# In both cases, Python sets a built-in variable called __name__ in the file.

# ------------------------------
# Case 1: When run directly
#     __name__ == "__main__"
#
# Case 2: When imported
#     __name__ == "<module_name>"
# ------------------------------

# So, using the condition:
#     if __name__ == "__main__":
# lets us control what code should run **only when the file is executed directly**.
# It **prevents test/demo code from running** when the file is imported into another program.

# ==========================================
# ✅ MODULE-LIKE FUNCTIONS (TO BE REUSED)
# ==========================================

# These functions are meant to be used in other files too
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# ==========================================
# ✅ TEST OR DEMO CODE
# ==========================================

# This block will only run if this file is run directly,
# and will NOT run when imported into another script.
if __name__ == "__main__":
    # __name__ is "__main__" only if this script is run directly
    print("🔎 Running test code in this script...")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))

# ==========================================
# ✅ HOW TO TEST THIS
# ==========================================

# Save this file as `mathutils.py`
# Then run:
#   python mathutils.py
# Output will be:
#   🔎 Running test code in this script...
#   5 + 3 = 8
#   5 - 3 = 2

# But if you import it in another file:
#   import mathutils
#   print(mathutils.add(10, 5))
#
# The test code inside the `if __name__ == "__main__"` block will NOT execute.
