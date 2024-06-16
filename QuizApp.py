import datetime
import re
from random import shuffle


def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, "%d.%m.%Y")


def updateStreak(filepath="QuizApp Files/Streak&Date"):
    global streak
    today = datetime.date.today()
    with open(filepath, "r") as file:
        for line in file:
            # Extract streak (digits after "Streak:")
            if "Streak:" in line:
                streak_match = re.search(r'\d+', line)
                streak = int(streak_match.group())

            if "LastEntry:" in line:
                date_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
                date = str_to_date(date_match.group())

    difference = today - date
    if difference > datetime.timedelta(hours=48):
        streak = 0
        updateFile(streak, date)
    elif difference > datetime.timedelta(hours=24):
        streak += 1
        updateFile(streak, date)


def updateFile(streak: int, lastEntry, filepath="QuizApp Files/Streak&Date"):
    with open(filepath, "w") as file:
        file.write("Streak:" + str(streak))
        file.write("\nLastEntry:" + str(lastEntry))


def read_questions(filepath="QuizApp Files/questions.txt"):
    questions = []
    with open(filepath, "r") as file:
        content = file.read().strip()
        q_and_a = content.split('---')
        for pair in q_and_a:
            if pair.strip():
                question = re.search(r'Question: (.*)', pair).group(1).strip()
                answer = re.search(r'Answer: (.*)', pair).group(1).strip()
                questions.append((question, answer))
    return questions


#START OF THE MAIN APPLICATION
updateStreak()

correctAnswers = 0
falseAnswers = 0
questionsAnswered = 0

print("***Welcome to Quiz App***")
print("Streak:", streak, "\n\n")

input("Press Enter to get your first question...")

questions = read_questions()
shuffle(questions)
for question, correct_answer in questions:
    print("Question:", question)
    user_answer = input("Your answer: ").strip()
    questionsAnswered += 1
    if user_answer.lower() == correct_answer.lower():
        correctAnswers += 1
        print("Correct!\n")
    else:
        falseAnswers += 1
        print(f"Incorrect! The correct answer is: {correct_answer}\n")

    quizEnd = input("Want to continue playing? Type 'no' if you wish to quit...")
    if quizEnd.lower() == "no":
        break


print("\nQuiz Finished!")
print(f"Questions Answered: {questionsAnswered}")
print(f"Correct Answers: {correctAnswers}")
print(f"Incorrect Answers: {falseAnswers}")