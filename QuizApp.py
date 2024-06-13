import datetime
import re

def str_to_date(date_str):
    return datetime.strptime(date_str, "%d.%m.%Y")

def updateStreak(filepath="Experiments/QuizApp Files/Streak&Date"):
    today = datetime.date.today()
    with open(filepath, "r") as file:
        for line in file:
            # Extract streak (digits after "Streak:")
            if "Streak:" in line:
                streak_match = re.search(r'\d+', line)
                streak = int(streak_match.group())

            if "Date:" in line:
                date_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
                date = str_to_date(date_match.group())

            if "LastEntry:" in line:
                last_entry_match = re.search(r'\d{4}-\d{2}-\d{2}', line)
                lastEntry = str_to_date(last_entry_match.group())

    difference = today - date
    if difference > datetime.timedelta(hours=24):
        streak = 0
        # TODO: update streak in the file
        # TODO: update last entry and date in the file
    elif lastEntry - date > datetime.timedelta(hours=24):
        streak += 1
        # TODO: update streak in the file
        # TODO: update last entry and date in the file



correctAnswers = 0
falseAnswers = 0
questionAnswered = 0



print("***Welcome to Quiz App***")
print("Streak:", streak)


