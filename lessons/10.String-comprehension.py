# --------------------------------------------------
#        STRING INDEXING, SLICING, COMPREHENSION
# --------------------------------------------------

# Strings in Python are sequences of characters.
# You can access parts of the string using indexing and slicing.

# SYNTAX:
#   string[start:end:step]
#   - start → index where slice begins (inclusive)
#   - end   → index where slice ends (exclusive, NOT included)
#   - step  → jump/stride between elements (default is 1)

name = "Kedar"

# --------------------------
# INDEXING
# --------------------------

print(name[0])  # Output: K  → 0th index
print(name[4])  # Output: r  → 4th index (5th character)
print(name[-2]) # Output: a  → -2 means second last character

# --------------------------
# SLICING
# --------------------------

# Basic forward slicing
print(name[0:3])  # Output: Ked → indices 0, 1, 2 (3 is excluded)

# If start is omitted, defaults to 0
print(name[:5])   # Output: Kedar → 0 to 4

# If both start and end are omitted, gets full string
print(name[:])    # Output: Kedar

# Step size of 1 (default)
print(name[::1])  # Output: Kedar

# Step size of 2 → skips every other character
print(name[::2])  # Output: Kdr → takes 0, 2, 4

# --------------------------
# NEGATIVE STEP (REVERSE)
# --------------------------

# Reverses the string
print(name[::-1])  # Output: radeK

# --------------------------
# SYNTAX ERROR EXAMPLE
# --------------------------
# You must include at least one `:` in slicing.
# print(name[])  # ❌ This is a SyntaxError

# --------------------------
# PRACTICAL EXAMPLE: Extract digits
# --------------------------

n = "6991-7804-7212"

# Extract last 4 digits
print(n[-4::])     # Output: 7212
# Here:
# -4 means 4th from last = index 11 (value: '7')
# Since step is positive (default), flow is left-to-right

# Extract last 4 digits in reverse
print(n[-1:-5:-1]) # Output: 2127 → starts from end, goes back 4 positions

# --------------------------
# NOTES:
# --------------------------
# Indexing is 0-based in Python
# Negative indices count from end: -1 is last, -2 is second last, etc.
# Slicing is powerful for working with substrings, reversing, or skipping elements
