questions = [
    {
        "prompt": "What is the capital of France?",
        "options":["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in Brazil?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "B"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote the 'Percy Jackson' Book Series?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. Rick Riordan", "D. J.K. Rowling"],
        "answer": "C"
    },
]

def run_quiz(questions):
    score = 0
    for question in questions: # Iterate over each question in the list of questions
        print(question["prompt"])
        for option in question["options"]:  # Display each possible answer (option) for the question
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper() # .upper is used in case the user inputs the letters in lowercase
        if answer == question["answer"]: # Check if the user's answer matches the correct answer for the questio
            print("Correct!\n")
            score += 1 # Increment the score if the answer is correct
        else:
            print("Incorrect! The correct answer was", question["answer"], "\n") # If the answer is wrong, display the correct answer

    print(f"You got {score} correct out of {len(questions)} questions.") #Display the total number of correct answers out of total questions



run_quiz(questions)