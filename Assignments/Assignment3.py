# Python Quiz Program

def quiz():
    questions = {
        "Which keyword is used to define a function in Python?": {
            "options": ["A. func", "B. function", "C. def", "D. define"],
            "answer": "C"
        },
        "What is the output of: print(type([])) ?": {
            "options": ["A. <class 'tuple'>", "B. <class 'list'>", "C. <class 'dict'>", "D. <class 'set'>"],
            "answer": "B"
        },
        "Which of the following is immutable in Python?": {
            "options": ["A. List", "B. Dictionary", "C. Tuple", "D. Set"],
            "answer": "C"
        },
        "Which library is commonly used for numerical computations in Python?": {
            "options": ["A. Matplotlib", "B. NumPy", "C. Pandas", "D. Scikit-learn"],
            "answer": "B"
        },
        "What does the 'len()' function do in Python?": {
            "options": ["A. Returns the length of an object", "B. Returns the type of an object", "C. Converts to list", "D. None of the above"],
            "answer": "A"
        },
        "Which symbol is used for comments in Python?": {
            "options": ["A. //", "B. <!-- -->", "C. #", "D. %"],
            "answer": "C"
        },
        "What is the output of: bool(0)?": {
            "options": ["A. True", "B. False", "C. 0", "D. None"],
            "answer": "B"
        },
        "Which data type is used to store key-value pairs in Python?": {
            "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
            "answer": "D"
        },
        "What will be the output of: print('Python'[::-1]) ?": {
            "options": ["A. nohtyP", "B. Python", "C. Error", "D. None"],
            "answer": "A"
        }
    }

    score = 0
    print("----- Welcome to the Python Quiz -----\n")

    for q, details in questions.items():
        print(q)
        for option in details["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        
        if answer == details["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {details['answer']}\n")

    print(f"Your final score is {score}/{len(questions)} 🎉")

# Run the quiz
quiz()
