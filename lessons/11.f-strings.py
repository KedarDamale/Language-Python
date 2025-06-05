# ---------------------------------------------------
#        FORMAT SPECIFIERS USING f-STRINGS IN PYTHON
# ---------------------------------------------------

# FORMAT: {value:flags}
# Flags control the output format: decimal places, alignment, padding, signs, etc.

price = 3.14568734

# -----------------------------
# ROUNDING DECIMALS
# -----------------------------

print(f"{price:.2f}")  # Output: 3.15
# Explanation:
#   .2f → rounds float to 2 decimal places (f = fixed-point number)

print(f"{price:.2}")   # Output: 3.1
# Explanation:
#   .2  → rounds to 2 significant digits (not necessarily decimals)

# -----------------------------
# FIELD WIDTH AND ALIGNMENT
# -----------------------------

print(f"{price:20}")   # Output: (spaces + value, total 20 chars wide)
# Default alignment is right-aligned

print(f"{price:<20}")  # Output: 3.14568734 followed by spaces (left-aligned)
print(f"{price:>20}")  # Output: spaces followed by 3.14568734 (right-aligned)

print(f"{price:^20}")  # Output: value centered within 20-width field

# -----------------------------
# ZERO PADDING
# -----------------------------

print(f"{price:020}")  # Output: 00000000003.14568734
# 20 total width with zeros used as padding

# -----------------------------
# SIGN DISPLAY
# -----------------------------

print(f"{price:+}")    # Output: +3.14568734
# Always shows + or - in front of the number

# -----------------------------
# THOUSANDS SEPARATOR
# -----------------------------

a = 394758363427865873673

print(f"{a:,}")        # Output: 394,758,363,427,865,873,673
# Adds comma as thousand separator

print(f"{a:_}")        # Output: 394_758_363_427_865_873_673
# Uses underscore instead of comma

# -----------------------------
# MULTIPLE COMBINATIONS
# -----------------------------

print(f"{a:+20,}")     # Output: formatted with sign, width=20, comma-separated
# Example: +394,758,363,427,865,873,673 (if fits in 20 width; otherwise, expands)

# -----------------------------
# SPECIAL NOTE ON NUMERIC LITERALS WITH SEPARATORS
# -----------------------------

# Python allows underscores in numeric literals for readability
big_number = 1_000_000_000
print(big_number)      # Output: 1000000000 (underscores are just for readability)

# But if you use commas while assigning:
b = 3,000
print(b)               # Output: (3, 0)
# It's a tuple of two values, not an integer!

# To store 3000 properly, use:
c = 3_000
print(c)               # Output: 3000

# -----------------------------
# ADDITIONAL FORMATTING OPTIONS (SHORT)
# -----------------------------
# :d  → Integer
# :f  → Fixed-point float
# :.2f → Round to 2 decimals
# :<   → Left align
# :>   → Right align
# :^   → Center align
# :0   → Zero padding
# :+   → Show + or -
# :,   → Comma separator
# :_   → Underscore separator

# Full combination example:
print(f"{price:+020,.2f}")
# Explanation:
# + → show sign
# 0 → pad with zeros
# 20 → total width
# , → thousands separator
# .2f → round to 2 decimals

# -------------------------------
# print() FUNCTION IN DETAIL
# -------------------------------

# The print() function outputs text to the console.
# Syntax: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# 🔸 sep (separator) – controls what goes between multiple values
print("Kedar", "Damale", sep="🚀")  # Output: Kedar🚀Damale

# 🔸 end – what to print at the end instead of default newline
print("This is printed...", end=" 😎 ")
print("on the same line because end was custom.")

# 🔸 flush – forces the output to be flushed to screen (usually used for buffering control)
# Used rarely unless you're doing real-time output display
print("This is immediate", flush=True)

print("\n" + "-" * 50)


# Example: Fancy progress bar simulation
import time

i = 0
while i <= 10:
    print(f"\rLoading {i * 10}%", end="")  # \r brings cursor to start of line; end="" avoids newline
    time.sleep(0.2)
    i += 1

print("\n✅ Loading Complete!")


