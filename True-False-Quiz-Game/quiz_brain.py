from random import randint


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number < 10:
            return True
        else:
            return False

    def next_question(self):
        question_choice = randint(0, len(self.questions_list))
        user_answer = input(f"Question {self.question_number + 1}: {self.questions_list[question_choice].text} (True/False): \n")
        self.check_answer(user_answer, self.questions_list[self.question_number].answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_number + 1}")
        else:
            print(f"False!\nThe correct answer was: {correct_answer}.")
            print(f"Your current score is: {self.score}/{self.question_number + 1}")
