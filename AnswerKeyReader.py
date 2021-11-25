import csv
import re

import pandas
import numpy as np
import Poll
import Question


class AnswerKeyReader:
    def readAnswerKey(self):
        pollList = []
        i = 0
        with open("excel files/Answer Key.csv", newline='') as csvfile:
            c = csv.reader(csvfile, delimiter=',', quotechar='"')
            isFirst = True
            for row in c:
                if row[1] == '':
                    isFirst = True
                if isFirst:
                    list = row[0].split("_")  # split poll name to get date
                    poll = Poll.Poll(row[0], list[1], [])  # create poll object
                    pollList.append(poll)  # add created poll to pollList
                    isFirst = False
                else:
                    while True:
                        try:
                            a = re.sub("[^0-9a-zA-Z]+", '', row[i].lower())
                            b = re.sub("[^0-9a-zA-Z]+", '', row[i + 1].lower())
                            question = Question.Question(a, b)  # create question object
                            poll.add_question(question)  # add question to poll object
                            i += 2
                        except IndexError:
                            break
        return pollList
