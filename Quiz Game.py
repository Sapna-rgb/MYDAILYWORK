import random

# Define the quiz questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Pb", "D) Fe"],
        "answer": "A"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["A) Helium", "B) Hydrogen", "C) Lithium", "D) Oxygen"],
        "answer": "B"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
]

def display_welcome():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions.")
    print("Select the correct answer by typing the letter corresponding to your choice.")
    print("Let's see how many you can get right!\n")

def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
    user_answer = input("Your answer: ").strip().upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    return False

def play_quiz():
    score = 0
    random.shuffle(questions)  # Shuffle questions for variety

    for question in questions:
        user_answer = ask_question(question)
        if evaluate_answer(user_answer, question["answer"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {question['answer']}.\n")

    return score

def display_final_results(score):
    print(f"You scored {score} out of {len(questions)}.")
    if score == len(questions):
        print("Excellent! You got all the answers right!")
    elif score >= len(questions) / 2:
        print("Good job! You answered more than half correctly.")
    else:
        print("Keep trying! You can do better next time.")

def main():
    while True:
        display_welcome()
        score = play_quiz()
        display_final_results(score)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
