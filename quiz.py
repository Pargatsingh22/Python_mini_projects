def main():
    questions = {
        "What is the capital of France?": "Paris",
        "What is the largest ocean?": "Pacific",
        "Which planet is known as the Red Planet?": "Mars",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
    }

    score = 0
    for question, correct_answer in questions.items():
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer.strip().lower() == correct_answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
    
    print(f"\nYou answered {score} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    main()
