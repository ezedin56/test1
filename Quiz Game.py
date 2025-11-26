def quiz_game():
    # Quiz questions stored as a list of dictionaries
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "correct_answer": "B",
            "explanation": "Paris is the capital and most populous city of France."
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "correct_answer": "B",
            "explanation": "Mars appears red due to iron oxide (rust) on its surface."
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Polar Bear"],
            "correct_answer": "B",
            "explanation": "The Blue Whale can reach up to 100 feet long and 200 tons."
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"],
            "correct_answer": "B",
            "explanation": "World War II ended in 1945 with the surrender of Germany and Japan."
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "correct_answer": "C",
            "explanation": "Au comes from the Latin word 'aurum' meaning gold."
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["A) Picasso", "B) Van Gogh", "C) Leonardo da Vinci", "D) Michelangelo"],
            "correct_answer": "C",
            "explanation": "Leonardo da Vinci painted the Mona Lisa in the early 16th century."
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
            "correct_answer": "C",
            "explanation": "Diamond is the hardest known natural material on the Mohs scale."
        },
        {
            "question": "How many bones are in the human body?",
            "options": ["A) 196", "B) 206", "C) 216", "D) 226"],
            "correct_answer": "B",
            "explanation": "Adults have 206 bones, while babies are born with about 300 bones."
        }
    ]
    
    print("=" * 60)
    print("            🎯 WELCOME TO THE QUIZ GAME")
    print("=" * 60)
    print("Answer the following questions by entering A, B, C, or D")
    print("Good luck! 🍀")
    print("-" * 60)
    
    # Track user's answers and score
    user_answers = []
    score = 0
    
    # Ask each question
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}/{len(questions)}:")
        print(f"💡 {q['question']}")
        
        # Display options
        for option in q['options']:
            print(f"   {option}")
        
        # Get user's answer with validation
        while True:
            answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                user_answers.append({
                    'question': q['question'],
                    'user_answer': answer,
                    'correct_answer': q['correct_answer'],
                    'explanation': q['explanation']
                })
                break
            else:
                print("❌ Invalid input! Please enter A, B, C, or D.")
        
        # Check if answer is correct
        if answer == q['correct_answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The correct answer is {q['correct_answer']}")
    
    # Display final results
    print("\n" + "=" * 60)
    print("                 QUIZ RESULTS")
    print("=" * 60)
    
    # Calculate percentage
    percentage = (score / len(questions)) * 100
    
    print(f"🎯 Your Score: {score}/{len(questions)} ({percentage:.1f}%)")
    
    # Display performance message
    if percentage == 100:
        print("🏆 Perfect score! You're a genius! 🌟")
    elif percentage >= 80:
        print("👍 Excellent job! You know your stuff!")
    elif percentage >= 60:
        print("😊 Good effort! Keep learning!")
    else:
        print("📚 Keep studying! You'll do better next time!")
    
    # Show incorrect answers with explanations
    incorrect_answers = [ans for ans in user_answers if ans['user_answer'] != ans['correct_answer']]
    
    if incorrect_answers:
        print(f"\n📖 Review your incorrect answers ({len(incorrect_answers)}):")
        print("-" * 60)
        
        for i, wrong in enumerate(incorrect_answers, 1):
            print(f"\n{i}. {wrong['question']}")
            print(f"   Your answer: {wrong['user_answer']}")
            print(f"   Correct answer: {wrong['correct_answer']}")
            print(f"   💡 {wrong['explanation']}")
    
    print(f"\n🎉 Thanks for playing! 🎉")

# Run the quiz game
if __name__ == "__main__":
    quiz_game()