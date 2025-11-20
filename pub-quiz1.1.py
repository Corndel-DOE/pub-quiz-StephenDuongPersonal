# Welcome message
print("Welcome to the Pub Quiz!")
print("Try your best to answer the following questions!\n")

# List of quiz questions
quiz_questions = [
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Tokyo", "B) Kyoto", "C) Osaka", "D) Hiroshima"],
        "answer": "A"
    },
    {
        "question": "Solve this math problem: 15 * 3 = ?",
        "options": ["A) 30", "B) 45", "C) 50", "D) 35"],
        "answer": "B"
    },
    {
        "question": "What programming language is this quiz written in?",
        "options": None,  # Free-text question
        "answer": "python"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "In which year did the first moon landing occur?",
        "options": ["A) 1965", "B) 1969", "C) 1972", "D) 1975"],
        "answer": "B"
    }
]

# Initialize score
score = 0

# Loop through each question
for question in quiz_questions:
    print(question["question"])
    
    # If multiple choice, show options
    if question["options"]:
        for option in question["options"]:
            print(option)
        valid_options = ["A", "B", "C", "D"]
        while True:
            user_answer = input("Your answer (A, B, C, D): ").strip().upper()
            if user_answer in valid_options:
                break
            else:
                print("Please enter a valid option: A, B, C, or D.")
    else:
        user_answer = input("Your answer: ").strip().lower()
    
    # Check the answer
    if question["options"]:  # Multiple choice
        if user_answer == question["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.\n")
    else:  # Free-text
        if user_answer == question["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer'].capitalize()}.\n")

# Final score and fun message
print(f"Your final score is {score} out of {len(quiz_questions)}.\n")

# Fun messages based on score
if score == len(quiz_questions):
    print("🏆 Amazing! You're a Pub Quiz Master!")
elif score >= len(quiz_questions) * 0.8:
    print("🎉 Great job! Almost perfect!")
elif score >= len(quiz_questions) * 0.5:
    print("🙂 Not bad! Keep practicing!")
else:
    print("😅 Better luck next time! Study up and try again!")
a