# ========================================
# QUIZ APPLICATION USING ENUMERATE()
# ========================================

questions = [
    "What is the capital of Canada?",
    "Which element has the chemical symbol ‘O’?",
    "Who wrote the play 'Romeo and Juliet'?",
    "Which planet is known as the Red Planet?",
    "In which year did World War II end?",
    "What is the largest organ in the human body?",
    "Who is known as the Father of Computers?",
    "Which gas is most abundant in Earth's atmosphere?",
    "What is the currency of Japan?",
    "Who discovered the law of gravity?"
]

options = [
    ["Toronto", "Vancouver", "Ottawa", "Montreal"],
    ["Gold", "Oxygen", "Osmium", "Ozone"],
    ["Charles Dickens", "William Shakespeare", "Jane Austen", "Leo Tolstoy"],
    ["Earth", "Venus", "Mars", "Jupiter"],
    ["1942", "1945", "1939", "1950"],
    ["Liver", "Brain", "Heart", "Skin"],
    ["Alan Turing", "Charles Babbage", "Bill Gates", "Steve Jobs"],
    ["Oxygen", "Hydrogen", "Nitrogen", "Carbon Dioxide"],
    ["Yen", "Won", "Ringgit", "Baht"],
    ["Albert Einstein", "Galileo Galilei", "Isaac Newton", "Nikola Tesla"]
]

answers = ['3', '2', '2', '3', '2', '4', '2', '3', '1', '3']

correct_ans = 0
wrong_ans = 0

# ========================================
# ✅ Using enumerate() to get both index (idx) and value (question)
# ========================================
for idx, question in enumerate(questions):  
    # idx: index of the question (starts from 0)
    # question: actual question string

    print(f"\nQ{idx + 1}: {question}")  # Adding 1 to index to show Q1, Q2, etc.
    
    # Nested enumerate for options (start from 1 to match choice numbers)
    for opt_idx, opt in enumerate(options[idx], start=1):
        print(f"  {opt_idx}. {opt}")
    
    user_input = input("Your answer (1-4): ").strip()

    if user_input == answers[idx]:
        print("✅ Correct")
        correct_ans += 1
    else:
        correct_option = options[idx][int(answers[idx]) - 1]
        print(f"❌ Wrong (Correct answer: {answers[idx]}. {correct_option})")
        wrong_ans += 1

# ========================================
# 🔚 Final Score Summary
# ========================================
print("\nQuiz Completed!")
print(f"✔️ Correct Answers: {correct_ans}")
print(f"❌ Wrong Answers: {wrong_ans}")
print(f"🏆 Your Score: {correct_ans} / {len(questions)}")

# ========================================
# 🧠 LOGIC OF enumerate()
# ========================================
# In: for idx, val in enumerate(iterable):
# → You get both:
#     idx → index (0,1,2,...)
#     val → element at that index
# Much cleaner than maintaining a counter manually.
# In Python, enumerate() is a built-in function used to loop over an iterable (like a list) and get both the index and the value at the same time.
#Syntax: enumerate(iterable, start=0)

# iterable: A sequence (like a list, string, tuple).
# start: The index to start from (default is 0).


# Without enumerate():
# i = 0
# for item in mylist:
#     print(i, item)
#     i += 1

# With enumerate():
# for i, item in enumerate(mylist):
#     print(i, item)

# - Built-in function for iteration.
# - Gives both index and element at once.
# - Prevents need for manually increasing counter.
# - Cleaner and more Pythonic.
# - Especially useful in loops where you need index + value.


# ✔ Bonus Tip:
# Use ➤ tuple  → when you only need to **search / read** (immutability helps performance)
# Use ➤ list   → when you need to **modify** (Create, Read, Update, Delete — CRUD)

# Tuples are faster than lists because they are immutable, meaning Python can optimize them better internally:

# Less memory usage
# No dynamic resizing
# No modification tracking
# Better CPU caching



