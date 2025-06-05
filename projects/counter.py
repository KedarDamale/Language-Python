import time  # Import time module to use time.sleep()

# ===========================
# COUNTDOWN TIMER APPLICATION
# ===========================

# Ask the user for input in seconds
t = int(input("Enter the timer in seconds: "))

# We will now display a countdown in HH:MM:SS format from t to 1
# Using range(start, stop, step) with step -1 to count backwards
for i in range(t, 0, -1):  # from t down to 1 (0 excluded)
    
    # Convert current seconds to hours, minutes and seconds
    hr = i // 3600              # 1 hour = 3600 seconds
    min = (i % 3600) // 60      # remainder seconds into minutes
    sec = i % 60                # remainder seconds into seconds

    # Format the output with 2 digits using format specifier :02
    print(f"{hr:02}:{min:02}:{sec:02}")

    # Delay execution by 1 second
    time.sleep(1)

# When countdown ends
print("⏰ Times up!")



# ============================================
# reversed() FUNCTION EXPLANATION & COMPARISON
# ============================================

# reversed() returns a reverse iterator over any iterable (does NOT modify original)
# reverse() is a LIST METHOD that reverses the list IN-PLACE and returns None

# Demonstration of reversed()
print("\nDemonstrating reversed():")
r = range(5)                # range object from 0 to 4
rev = reversed(r)           # reversed iterator from 4 to 0
print(list(rev))            # convert to list and print → Output: [4, 3, 2, 1, 0]

# Demonstration of .reverse()
print("\nDemonstrating .reverse():")
mylist = [10, 20, 30, 40]
print("Original list:", mylist)
mylist.reverse()            # reverse in place
print("Reversed list:", mylist)  # Output: [40, 30, 20, 10]

# Difference Summary:
# reversed() → does NOT change the original object, returns new iterator
# .reverse() → modifies the original list directly, returns None

# You could use reversed(range()) for countdown like this:
print("\nUsing reversed(range()):")
for i in reversed(range(1, 6)):
    print(i, end=" ")  # Output: 5 4 3 2 1

# But range(t, 0, -1) is more explicit and better suited for countdowns
