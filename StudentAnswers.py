class StudentAnswers:
    def __init__(self, poll):
        self.__poll = poll  # poll object
        self.__questionAndAnswers = {}  # dictionary of questions and answers

    def add_question_and_answers(self, question, answer):
        self.__questionAndAnswers[question] = answer

    def set_question_and_answers(self, dict):
        self.__questionAndAnswers = dict

    def get_answer(self, question):
        return self.__questionAndAnswers[question.get_text()]

    def get_poll(self):
        return self.__poll

    def get_questions_and_answers(self):
        return self.__questionAndAnswers
