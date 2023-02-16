import json
import random

class Question():
    def __init__(self, text, difficulty, answer, IsCalled=False, UserAnswer=None):
        self.text = text
        self.difficulty = difficulty
        self.answer = answer
        self.IsCalled = IsCalled
        self.UserAnswer = UserAnswer
        self.points = int(self.difficulty) * 10


    def get_points(self):
        """Возвращает int, количество баллов."""

        return self.points

    def is_correct(self, answer):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """

        if self.answer == answer:
            self.UserAnswer = True
        else:
            self.UserAnswer = False


    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        print(f"Вопрос: {self.text}")
        print(f"Сложность {self.difficulty}/5")

    def build_feedback(self):
        if self.UserAnswer == True:
            print(f"Ответ верный, получено {self.points} баллов")
        else:
            print(f"Ответ неверный, верный ответ {self.answer}")



def main():
    correct_answers = 0
    points = 0
    questions = []
    questions_asked = []
    with open("questions.json") as file:
        data = json.loads(file.read())

        questions.append(Question(data[0]["q"], data[0]["d"], data[0]["a"]))
        questions.append(Question(data[1]["q"], data[1]["d"], data[1]["a"]))
        questions.append(Question(data[2]["q"], data[2]["d"], data[2]["a"]))
        questions.append(Question(data[3]["q"], data[3]["d"], data[3]["a"]))
        questions.append(Question(data[4]["q"], data[4]["d"], data[4]["a"]))

    for num in range(len(questions)):
        # Выбираю случайный элемент из списка вопросов, но, поскольку программа не может повториться в вопросах,
        # мне нжно находить случайный индекс и добавлять в список индексов, которые уже были использованы (поэтому random.choice нельзя использовать)
        while True:
            question_index = random.randint(0, (len(questions)-1))
            if question_index not in questions_asked:
                break

        questions_asked.append(question_index)
        question = questions[question_index]


        question.build_question()
        question.is_correct(input())
        question.build_feedback()

    for question in questions:
        if question.UserAnswer == True:
            correct_answers += 1
            points += question.get_points()
    print("Вот и всё!")
    print(f"Отвечено {correct_answers} вопроса из {len(questions)}")
    print(f"Набрано баллов: {points}")


main()