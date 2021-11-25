import re

import xlrd
from Student import Student


def read(path):
    studentList = []
    excel_workbook = xlrd.open_workbook(path)
    excel_worksheet = excel_workbook.sheet_by_index(0)
    i = 0
    j = 0
    while True:
        try:
            if len(excel_worksheet.cell_value(i, 2)) == 9:
                result = excel_worksheet.cell_value(i, 4).lower()
                result = re.sub("ı", "i", result)
                result = re.sub("ü", "u", result)
                result = re.sub("ö", "o", result)
                result = re.sub("ç", "c", result)
                result = re.sub("ş", "s", result)
                result = re.sub("ğ", "g", result)

                result2 = excel_worksheet.cell_value(i, 7).lower()
                result2 = re.sub("ı", "i", result2)
                result2 = re.sub("ü", "u", result2)
                result2 = re.sub("ö", "o", result2)
                result2 = re.sub("ç", "c", result2)
                result2 = re.sub("ş", "s", result2)
                result2 = re.sub("ğ", "g", result2)
                std = Student(result + " " + result2,
                              0)
                studentList.append(std)
                j += 1
            i += 1
        except IndexError:
            break
    return studentList
