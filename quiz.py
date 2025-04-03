import mysql.connector
import json
import os

class Question:
    def __init__(self, prompt, answers):
        self.prompt = prompt
        self.answers = answers

    def is_correct(self, user_answer):

        return user_answer.lower() in [answer.lower() for answer in self.answers]


class Quiz:
    def __init__(self, name, correct_score=4, incorrect_penalty=1):
        self.name = name
        self.score = 0
        self.questions = []
        self.question_count = 0
        self.correct_score = correct_score
        self.incorrect_penalty = incorrect_penalty

    def add_question(self, question):
        self.questions.append(question)

    def load_questions(self, category):
        if not os.path.exists('questions.json'):
            print("Questions file not found.")
            return

        with open('questions.json') as f:
            data = json.load(f)
            if category in data:
                for item in data[category]:
                    if isinstance(item, dict) and 'prompt' in item and 'answer' in item:
                        self.add_question(Question(item['prompt'], item['answer']))
                    else:
                        print(f"Invalid question format for item: {item}")
            else:
                print(f"No questions found for category: {category}")

    def ask_questions(self):
        for question in self.questions:
            user_answer = input(question.prompt)
            if question.is_correct(user_answer):
                print('Correct!')
                self.score += self.correct_score
                self.question_count += 1
            else:
                print(f'Incorrect! The correct answers were: {", ".join(question.answers)}')
                self.score -= self.incorrect_penalty

    def show_results(self):
        print("------------------------")

        print(f"You answered {self.question_count} questions correctly, earning a score of {self.score}.")

    def save_score(self):
        try:
            with mysql.connector.connect(host='localhost', password='1234', user='root', database='quiz_game') as db:
                with db.cursor() as cursor:
                    cursor.execute("INSERT INTO scores (name, score) VALUES (%s, %s)", (self.name, self.score))
                    db.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


def main():
    print("Welcome to my Quiz Game!")
    print("------------------------")

    while True:
        ask = input("Would you like to play? (yes/no) ")
        if ask.lower() != "yes":
            break
        print("------------------------")

        name = input("What should we call you? ")
        print("------------------------")

        quiz = Quiz(name)
        print(f"Let's begin with the quiz {name.upper()}")
        print("------------------------")

        category = input(
            "Please choose a number to select the category: \n1-Python \n2-General Knowledge \n3-Sports \n")
        print("------------------------")

        categories = {
            "1": "Python",
            "2": "General Knowledge",
            "3": "Sports"
        }

        if category in categories:
            quiz.load_questions(categories[category])
        else:
            print("Invalid category. Please try again.")
            continue

        quiz.ask_questions()
        quiz.show_results()
        quiz.save_score()
        print("------------------------")

        another = input("Would you like to play again? (yes/no) ")
        if another.lower() != "yes":
            break


if __name__ == "__main__":
    main()
