import StudentReader
from AnswerKeyReader import AnswerKeyReader
from PollReader import PollReader
import os
import WriterTest


class main:
    studentListPath = path = 'excel files/CES3063_Fall2020_rptSinifListesi.xls'
    directory = 'excel files'
    pollReader = PollReader()
    poll_list = AnswerKeyReader().readAnswerKey()  # get poll list from answer key

    student_list = StudentReader.read(studentListPath)  # create student list

    readFlag = False
    for filename in os.listdir(directory):
        if 'PollReport' in filename:
            readFlag = True
            pollReader.read_poll(student_list, poll_list,
                                 'excel files/' + filename)  # all students and polls are updated

    for poll in poll_list:
        if readFlag:
            WriterTest.create_statistics(student_list, poll)  # 7-b output
            WriterTest.create_poll_output(student_list, poll)  # 7-a output

    WriterTest.create_attendance_output(student_list)  # 6 output
    WriterTest.create_global_output(student_list, poll_list)  # 8 output
