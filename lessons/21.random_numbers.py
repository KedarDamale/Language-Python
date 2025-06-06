import random  # Import the random module for generating random values

# -------------------------------
# 🎲 1. Random whole number (integer)
# -------------------------------

number = random.randint(1, 30)  # Returns a random integer between 1 and 30 (inclusive)
print(number)

# Example output: 17

# -------------------------------
# 🎲 2. Random float number from 0.0 to 1.0
# -------------------------------

number = random.random()  # Returns a float between 0.0 and 1.0 (not including 1.0)
print(number)

# Example output: 0.72619184

# -------------------------------
# ✂️ 3. Random choice from a list
# -------------------------------

l = ["rock", "paper", "scissors"]
print(random.choice(l))  # Picks one element randomly from the list

# Example output: "scissors"

# -------------------------------
# ♠️ 4. Randomly shuffling a list
# -------------------------------

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# ❌ Mistake:
# print(random.shuffle(cards))
# `random.shuffle()` does **not return** a new list. It shuffles the list **in place** and returns None.

# ✅ Correct usage:
print("Before shuffling:", cards)
random.shuffle(cards)  # Shuffles the original list in-place
print("After shuffling:", cards)

# Example output:
# Before shuffling: ['1', '2', '3', ..., '10']
# After shuffling: ['6', '3', '10', ..., '1']

#If you want to get a shuffled version of a list without modifying the original, use:
shuffled_cards = cards[:]
random.shuffle(shuffled_cards)
print("Original:", cards)
print("Shuffled Copy:", shuffled_cards)
