class Poll:
    def __init__(self, name, date, questions):
        self.__name = name
        self.__date = date
        self.__questions = questions

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def get_questions(self):
        return self.__questions

    def set_questions(self, questions):
        self.__questions = questions

    def add_question(self, question):
        self.__questions.append(question)
