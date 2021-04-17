print("                   Python Zero To Hero Course Project 02                  ")
print(" ")
print("-------------------MARKS SHEDULE PROJECT USING PYTHON-----------------------")

ict = 0
python = 1
javascript = 2
m = set()


def identify_grade(marks):
    if marks >= 0 and marks <= 100:
        if marks >= 75:
            grade = "A"
        elif marks >= 65:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 35:
            grade = "S"
        else:
            grade = "W"
        return grade
    else:
        return "Error"


class Student:
    def __init__(self):
        self.name = input("Enter The Name : ")
        self.ictm = float(input("Enter The ICT Marks :"))
        self.pythonm = float(input("Enter The PYTHON Marks :"))
        self.javascriptm = float(input("Enter The JAVASCRIPT Marks :"))
        self.total = self.ictm + self.pythonm + self.javascriptm
        self.average = self.total/3
        m.add(self.ictm)
        m.add(self.pythonm)
        m.add(self.javascriptm)

        grade = []
        grade.extend(range(0, 3))
        grade[ict] = identify_grade(self.ictm)
        grade[python] = identify_grade(self.pythonm)
        grade[javascript] = identify_grade(self.javascriptm)
        self.acount = 0
        self.bcount = 0
        self.ccount = 0
        self.scount = 0
        self.wcount = 0
        if "A" in grade:
            self.acount = grade.count("A")
        if "B" in grade:
            self.bcount = grade.count("B")
        if "C" in grade:
            self.ccount = grade.count("C")
        if "S" in grade:
            self.scount = grade.count("S")
        if "W" in grade:
            self.wcount = grade.count("W")


print(" ")
total_students = int(input("Enter The Students Count : "))
student = []
student.extend(range(0, total_students))
n = 0
while total_students > 0:
    print(" ")
    student[n] = Student()
    print(student[n].name, " ", student[n].ictm, " ",
          student[n].pythonm, " ", student[n].javascriptm, " ", student[n].total, " ", student[n].average, " ", student[n].acount, " ", student[n].bcount, " ", student[n].ccount, " ", student[n].scount, " ", student[n].wcount)
    print("--------------------------------",
          student[n].name, "COMPLETED", "-----------------------------------")
    n = n+1
    total_students = total_students-1
print(" ")
print("---------------------------------COMPLETED------------------------------------------")

print("NAME  ", " ICT", " PYTHON", " JAVASCRIPT",
      " TOTAL", " AVERAGE", "A", "B", "C", "S", "W")
for x in student:
    print(x.name, " ", x.ictm, " ", x.pythonm, " ", x.javascriptm, " ", x.total, " ", x.average, " ",
          x.acount, " ", x.bcount, " ", x.ccount, " ", x.scount, " ", x.wcount)
print(" ")


def highest(j):
    if j == 0:
        max_marks = 0
        for y in student:
            if y.ictm > max_marks:
                max_marks = y.ictm
                max_student = y.name
            elif y.ictm == max_marks:
                max_marks = y.ictm
                max_student = max_student+"," + y.name
    elif j == 1:
        max_marks = 0
        for y in student:
            if y.pythonm > max_marks:
                max_marks = y.pythonm
                max_student = y.name
            elif y.pythonm == max_marks:
                max_marks = y.ictm
                max_student = max_student+"," + y.name
    elif j == 2:
        max_marks = 0
        for y in student:
            if y.javascriptm > max_marks:
                max_marks = y.javascriptm
                max_student = y.name
            elif y.javascriptm == max_marks:
                max_marks = y.ictm
                max_student = max_student+"," + y.name

    return max_student, max_marks


print(" ")
print("HIGHSEST MARKS ON THE SUBJECTS")
ictmaxstudent, ictmaxmarks = highest(0)
print("ICT :- ", ictmaxmarks, "GET BY", ictmaxstudent)

pythonmaxstudent, pythonmaxmarks = highest(1)
print("PYTHON :- ",
      pythonmaxmarks, "GET BY", pythonmaxstudent)

javascriptmaxstudent, javascriptmaxmarks = highest(2)
print("JAVASCRIPT :- ",
      javascriptmaxmarks, "GET BY", javascriptmaxstudent)

print(" ")
print(m)
