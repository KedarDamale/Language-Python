import random

# List of valid choices
choice = ['rock', 'paper', 'scissors']

# Scores
computer_count = 0
user_count = 0

# Show user available options with indices (for user reference)
print("Welcome to Rock-Paper-Scissors!")
print("Options:")
for id, i in enumerate(choice,start=1):
    print(f"{id}: {i}")

# Start the game loop
while True:
    user_choice = input("\nType in your choice (press 'q' to exit): ").lower()

    if user_choice == 'q':
        # End the game and display results
        print(f"\nYour score: {user_count}")
        print(f"Computer's score: {computer_count}")
        if computer_count > user_count:
            print("💻 Computer won! Better luck next time.")
        elif user_count > computer_count:
            print("🎉 You won!!! Congratulations!")
        else:
            print("😐 It's a tie!")
        break

    elif user_choice not in choice:
        print("❌ Invalid choice! Please type rock, paper, or scissors.")
        continue

    # Computer randomly chooses
    computer_choice = random.choice(choice)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie! No points awarded.")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("✅ You win this round!")
        user_count += 1
    else:
        print("❌ You lost this round!")
        computer_count += 1
