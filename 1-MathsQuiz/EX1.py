import random

def displayMenu():
    print("\n===============================")
    print("          DIFFICULTY LEVEL")
    print("===============================")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    print("===============================\n")

def randomInt(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (1000, 9999)}
    return random.randint(*ranges[level])

def decideOperation():
    return random.choice(['+', '-'])

def displayProblem(x, y, op):
    return int(input(f"\nSolve: {x} {op} {y}\nYour Answer: "))

def isCorrect(ans, correct):
    return ans == correct

def displayResults(score):
    print("\n===============================")
    print(f"Your final score is: {score}/100")
    if score >= 90:
        print("Grade: A+")
    elif score >= 80:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 60:
        print("Grade: C")
    else:
        print("Grade: F")
    print("===============================\n")

while True:
    displayMenu()
    level = int(input("Enter difficulty level (1, 2, or 3): "))
    total = 0

    for i in range(1, 11):
        x, y, op = randomInt(level), randomInt(level), decideOperation()
        correct = eval(f"{x}{op}{y}")

        print(f"\nQuestion {i}:")
        ans = displayProblem(x, y, op)

        if isCorrect(ans, correct):
            print("+ Correct!")
            total += 10
        else:
            print("- Incorrect, try again!")
            retry = int(input(f"Retry: {x} {op} {y} = "))
            if isCorrect(retry, correct):
                print("+ Correct on second attempt!")
                total += 5
            else:
                print(f"- Incorrect again! The correct answer was {correct}.")

    displayResults(total)

    if input("Play again? (yes/no): ").strip().lower() != "yes":
        print("\nThanks for playing! Goodbye!")
        break
