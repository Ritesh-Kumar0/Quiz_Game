questions = [
    {
        "question": "Which city is known as the City of Love?",
        "options": ["A) Rome", "B) Venice", "C) Paris", "D) New York"],
        "answer": "C) Paris"
    },
    {
        "question": "What is the longest-running animated TV show?",
        "options": ["A) Family Guy", "B) The Simpsons", "C) South Park", "D) SpongeBob SquarePants"],
        "answer": "B) The Simpsons"
    },
    {
        "question": "Which fast-food chain is famous for the Big Mac?",
        "options": ["A) Burger King", "B) KFC", "C) McDonald's", "D) Subway"],
        "answer": "C) McDonald's"
    },
    {
        "question": "Which festival is known as the 'Festival of Lights'?",
        "options": ["A) Holi", "B) Christmas", "C) Diwali", "D) Hanukkah"],
        "answer": "C) Diwali"
    },
    {
        "question": "What was the first social media platform to reach 1 billion users?",
        "options": ["A) Instagram", "B) Facebook", "C) Twitter", "D) YouTube"],
        "answer": "B) Facebook"
    },
    {
        "question": "What is the main ingredient in guacamole?",
        "options": ["A) Cucumber", "B) Avocado", "C) Tomato", "D) Lettuce"],
        "answer": "B) Avocado"
    },
    {
        "question": "Which famous landmark can be seen from space?",
        "options": ["A) Eiffel Tower", "B) Great Wall of China", "C) Statue of Liberty", "D) Mount Everest"],
        "answer": "B) Great Wall of China"
    },
    {
        "question": "Which planet in our solar system is known as the 'Red Planet'?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B) Mars"
    },
    {
        "question": "Which sport is known as the 'King of Sports'?",
        "options": ["A) Basketball", "B) Cricket", "C) Football (Soccer)", "D) Tennis"],
        "answer": "C) Football (Soccer)"
    },
    {
        "question": "Which country is home to the famous Machu Picchu ruins?",
        "options": ["A) Brazil", "B) Peru", "C) Mexico", "D) Argentina"],
        "answer": "B) Peru"
    }
]

def play_quiz(questions):
    score = 0
    for question in questions:
        print("-" * 50)
        print(question["question"])
        for option in question["options"]:
            print(option)
        
        while True:
            answer = input("Enter your option (A, B, C or D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            print("Invalid input! Please enter A, B, C, or D.")
        
        if answer == question["answer"][0]:  # Compare only the letter
            print("Correct, Awesome!!\n")
            score += 1
        else:
            print(f"Wrong answer!!! The correct answer was {question['answer']}\n")
    
    print("-" * 50)
    print(f"Quiz Over! You got {score} out of {len(questions)} questions correct. Great job! 🎉")

play_quiz(questions)
