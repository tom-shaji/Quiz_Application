import sys

# Define the questions using a list of dictionaries
questions = [
    {
        "question": "What is the capital of France?",
        "options": {"A": "London", "B": "Berlin", "C": "Paris", "D": "Madrid"},
        "answer": "C"
    },
    {
        "question": "Which programming language is known as the snake?",
        "options": {"A": "Java", "B": "Python", "C": "C++", "D": "Ruby"},
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": {"A": "10", "B": "11", "C": "12", "D": "13"},
        "answer": "C"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Mark Twain", "D": "Jane Austen"},
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our Solar System?",
        "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Saturn"},
        "answer": "C"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": {"A": "Gold", "B": "Oxygen", "C": "Osmium", "D": "Hydrogen"},
        "answer": "B"
    },
    {
        "question": "In what year did the Titanic sink?",
        "options": {"A": "1912", "B": "1905", "C": "1898", "D": "1923"},
        "answer": "A"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": {"A": "Gold", "B": "Iron", "C": "Diamond", "D": "Quartz"},
        "answer": "C"
    },
    {
        "question": "Which ocean is the largest?",
        "options": {"A": "Atlantic", "B": "Indian", "C": "Arctic", "D": "Pacific"},
        "answer": "D"
    },
    {
        "question": "What is the speed of light?",
        "options": {"A": "300,000 km/s", "B": "150,000 km/s", "C": "1,000,000 km/s", "D": "3,000 km/s"},
        "answer": "A"
    }
]

def run_quiz():
    while True:
        score = 0
        total_questions = len(questions)
        
        print("\n--- Welcome to the Quiz Application! ---")
        
        for i, q in enumerate(questions, 1):
            print(f"\nQuestion {i}: {q['question']}")
            for key, value in q['options'].items():
                print(f"  {key}) {value}")
            
            # Input validation loop
            while True:
                answer = input("Your answer (A/B/C/D): ").strip().upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input. Please enter A, B, C, or D.")
            
            if answer == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")
                
        # Calculate results
        wrong_answers = total_questions - score
        percentage = (score / total_questions) * 100
        
        print("\n--- Quiz Results ---")
        print(f"Total questions: {total_questions}")
        print(f"Correct answers: {score}")
        print(f"Wrong answers: {wrong_answers}")
        print(f"Final score: {score}/{total_questions}")
        print(f"Percentage: {percentage:.2f}%")
        
        # Performance message
        if percentage == 100:
            print("Performance: Excellent! Perfect score!")
        elif percentage >= 80:
            print("Performance: Great job!")
        elif percentage >= 50:
            print("Performance: Good effort, but room for improvement.")
        else:
            print("Performance: Better luck next time!")
            
        # Restart prompt
        while True:
            restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if restart in ['yes', 'y']:
                break
            elif restart in ['no', 'n']:
                print("Thank you for playing. Goodbye!")
                sys.exit()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")
        sys.exit()
