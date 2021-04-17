ict = 0
python = 1
javascript = 2


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
        self.name = input("Enter The Name")
        self.ictm = float(input("Enter The ICT Marks:"))
        ict_grade = identify_grade(self.ictm)
        self.pythonm = float(input("Enter The PYTHON Marks:"))
        python_grade = identify_grade(self.pythonm)
        self.javascriptm = float(input("Enter The JAVASCRIPT Marks:"))
        javascript_grade = identify_grade(self.javascriptm)
        self.total = self.ictm + self.pythonm + self.javascriptm
        self.average = self.total/3
        grade = []
        grade.extend(range(ict, javascript))
        grade[ict] = identify_grade(self.ictm)
        grade[python] = identify_grade(self.pythonm)
        grade[javascript] = identify_grade(self.javascriptm)

        self.acount = grade.index("A")
        self.bcount = grade.index("B")
        self.ccount = grade.index("C")
        self.scount = grade.index("S")
        self.wcount = grade.index("W")


total_students = 2
student = []
student.extend(range(0, total_students))
n = 0
while total_students > 0:
    student[n] = Student()
    print(student[n].name, " ", student[n].ictm, " ",
          student[n].pythonm, " ", student[n].javascriptm, " ", student[n].acount, " ", student[n].bcount, " ", student[n].ccount, " ", " ")
    n = n+1
    total_students = total_students-1

for x in student:
    print(x.name, " ", x.ictm, " ", x.pythonm, " ", x.javascriptm)


def highest(j):
    if j == 0:
        max_marks = 0
        for y in student:
            if y.ictm > max_marks:
                max_marks = y.ictm
                max_student = y.name
    elif j == 1:
        max_marks = 0
        for y in student:
            if y.ictm > max_marks:
                max_marks = y.pythonm
                max_student = y.name
    elif j == 2:
        max_marks = 0
        for y in student:
            if y.ictm > max_marks:
                max_marks = y.javascriptm
                max_student = y.name

    return max_student, max_marks


ictmaxstudent, ictmaxmarks = highest(0)
print("THE HIGHEST MARKS ON ICT IS ", ictmaxmarks, "GET BY", ictmaxstudent)

pythonmaxstudent, pythonmaxmarks = highest(1)
print("THE HIGHEST MARKS ON PYTHON IS ",
      pythonmaxmarks, "GET BY", pythonmaxstudent)

javascriptmaxstudent, javascriptmaxmarks = highest(2)
print("THE HIGHEST MARKS ON JAVASCRIPT IS ",
      javascriptmaxmarks, "GET BY", javascriptmaxstudent)
