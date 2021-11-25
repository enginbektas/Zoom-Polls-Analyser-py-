import StudentAnswers


class Student:
    def __init__(self, name, attendance):
        self.__name = name
        self.__attendance = attendance
        self.__answeredPolls = []  # list of StudentAnswers
        self.__totalAttendance = 0

    def myFunc(self):
        print("Hello my name is " + self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def increment_attendance(self):
        self.__attendance += 1

    def get_attendance(self):
        return self.__attendance

    def add_answered_poll(self, poll):
        sa = StudentAnswers.StudentAnswers(poll)
        self.__answeredPolls.append(sa)

    def get_answered_polls(self):
        return self.__answeredPolls

    def increment_total_attendance(self):
        self.__totalAttendance += 1

    def get_totalAttendance(self):
        return self.__totalAttendance
