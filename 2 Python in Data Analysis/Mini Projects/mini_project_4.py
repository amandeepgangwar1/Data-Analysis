print("__________Quiz Game__________")

def run_quiz():
    questions =[
        {
            "question": "What is the correct file extension for Python files?",
            "options": ["A) .pyth", "B) .pt", "C) .py", "D) .p"],
            "answer": "C) .py"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A) function", "B) def", "C) fun", "D) define"],
            "answer": "B) def"
        },
        {
            "question": "Which of the following is used to take input from the user?",
            "options": ["A) input()", "B) scan()", "C) get()", "D) read()"],
            "answer": "A) input()"
        },
        {
            "question": "What will print(2 ** 3) output?",
            "options": ["A) 6", "B) 8", "C) 9", "D) 5"],
            "answer": "B) 8"
        },
        {
            "question": "Which data type is immutable in Python?",
            "options": ["A) list", "B) dictionary", "C) set", "D) tuple"],
            "answer": "D) tuple"
        },
        {
            "question": "What is the output of len(\"Python\")?",
            "options": ["A) 5", "B) 6", "C) 7", "D) Error"],
            "answer": "B) 6"
        },
        {
            "question": "Which of the following is used for exception handling?",
            "options": ["A) try-except", "B) if-else", "C) for loop", "D) def"],
            "answer": "A) try-except"
        },
        {
            "question": "What will this code output? x = [1, 2, 3]; print(x[1])",
            "options": ["A) 1", "B) 2", "C) 3", "D) Error"],
            "answer": "B) 2"
        },
        {
            "question": "Which function is used to open a file in Python?",
            "options": ["A) open()", "B) file()", "C) read()", "D) fopen()"],
            "answer": "A) open()"
        },
        {
            "question": "What is Python mainly known for?",
            "options": ["A) Complex syntax", "B) Easy readability", "C) Only web development", "D) Only gaming"],
            "answer": "B) Easy readability"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        # print(index, q)
        print(f"Q{index + 1}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer(A/B/C/D): ")
        # print(user_answer.strip().upper(), q['answer'][0])
        if user_answer.strip().upper() == q['answer'][0]:
            print("Correct!\n")
            score += 1

    print(f"Your final score is {score}/{len(questions)}")

run_quiz()
