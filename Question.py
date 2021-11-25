class Question:
    def __init__(self, text, trueChoice):
        self.__text = text
        self.__trueChoice = trueChoice

    def get_text(self):
        return self.__text

    def get_trueChoice(self):
        return self.__trueChoice

    def set_trueChoice(self, choice):
        self.__trueChoice = choice
