import numpy as np
import math
import curses

class Students:
    def __init__(self, id, name, dateofbirth):
        self.id = id.decode('utf-8')
        self.name = name.decode('utf-8')
        self.dateofbirth = dateofbirth.decode('utf-8')

    def studentinfo(self):
        return f" Student's id: {self.id}\n Student's name: {self.name}\n Student's date of birth: {self.dateofbirth}"

class Courses:
    def __init__(self, id, name, credit):
        self.id = id.decode('utf-8')
        self.name = name.decode('utf-8')
        self.credit = credit

    def courseinfo(self):
        return f"Course's ID: {self.id} \nCourse's Name: {self.name} \nCourse's credit: {self.credit}"

class Marks:
    def __init__(self, number, student, course):
        self.number = number
        self.student = student
        self.course = course

    def markinfo(self):
        return f"mark: {math.floor(self.number)}"

def main(stdscr):
    stdscr.clear()
    curses.echo()
    stdscr.addstr("\nPlease enter number of student:")
    student = int(stdscr.getstr())
    Studentslist = []
    for i in range(student):
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter student {i+1} Id:")
        id = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter student {i+1} name:")
        name = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter student {i+1} date of birth:")
        Dob = stdscr.getstr()
        Studentsinfo = Students(id, name, Dob)
        Studentslist.append(Studentsinfo)

    stdscr.clear()
    stdscr.addstr("\nPlease enter number of course:")
    Course = int(stdscr.getstr())
    courselist = []
    for r in range(Course):
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter course {r+1} Id:")
        Cid = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter course {r+1} name:")
        Cname = stdscr.getstr()
        stdscr.clear()
        stdscr.addstr(f"\nPlease enter course {r+1} credit:")
        Ccredit = float(stdscr.getstr())
        ListCourse = Courses(Cid, Cname, Ccredit)
        courselist.append(ListCourse)

    Listmark = [[0 for i in range(student)] for r in range(Course)]
    for r in range(Course):
        for i in range(student):
            stdscr.clear()
            stdscr.addstr(f"\nInput mark for student {i+1} in course {r+1}: ")
            Mark = float(stdscr.getstr())
            Listmark[r][i] = Mark

    creditlist = [course.credit for course in courselist]
    creditarray = np.array(creditlist)

    for i in range(student):
        stdscr.addstr('\n')
        stdscr.addstr(f"\n{Studentslist[i].studentinfo()} ")
        stdscr.addstr('\n')
    for r in range (Course):
        stdscr.addstr('\n')
        stdscr.addstr(f'\n{courselist[r].courseinfo()} ')
        stdscr.addstr('\n')
    for r in range(Course):
        for i in range(student):
            stdscr.addstr(f"\nStudent {i+1} in course {r+1} [{Listmark[r][i]}]")

    markarray = np.array(Listmark)
    gpaarray = np.dot(markarray.T, creditarray) / np.sum(creditarray)
    stdscr.addstr('\n')
    sorted_gpa_indices = np.argsort(gpaarray)[::-1]
    for i in sorted_gpa_indices:
        stdscr.addstr(f"\nStudent {i+1} GPA: {gpaarray[i]}")
    stdscr.getkey()

curses.wrapper(main)