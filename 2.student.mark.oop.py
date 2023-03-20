class Students:  
 def __init__(student, id, name, dateofbirth):
    student.id = id
    student.name = name
    student.dateofbirth = dateofbirth
 def studentinfo(student):
   print("student's ",i+1," id:", student.name)
   print("student's ",i+1," name:",  student.name)
   print("student's ",i+1," date of birth:", student.dateofbirth)


print ("Please enter number of student:")
student = int(input())
Studentslist = []
for i in range(student):
    print("Please enter student ", i+1 ," Id:" )
    id = input()

    print("Please enter student ", i+1, " name:" )
    name = input()

    print("Please enter student ", i+1, " date of birth:" )
    Dob = input()
    Studentsinfo = Students(id, name, Dob) 
    Studentslist.append(Studentsinfo)

class Courses:   
  def __init__(course, id, name):
    course.id = id
    course.name = name
  def courseinfo(course):
     print("Course",r+1,"ID:", course.id)
     print("Course",r+1,"Name:", course.name)

print ("Please enter number of course:")
Course = int(input())
courselist = []
for r in range (Course):
   print("Please enter course ", r+1 ," Id:" )
   Cid = input()

   print("Please enter course ", r+1 ," name:" )
   Cname = input()
   ListCourse = Courses(Cid, Cname)
   courselist.append(ListCourse)


class Marks:  
  def __init__(mark, b):
    mark.number = b

  def markinfo(mark):
    print("student",i+1,"mark:",mark.number)

print("Please enter the course's ID you want to choose: ")
Ccourse = input()
Listmark = []
while Ccourse not in Cid:
   print("Invalid")
   Ccourse = input()
for i in range(student):
    print("Input mark for student",i+1," :")
    Mark = int(input())
    lismark = Marks(Mark)
    Listmark.append(lismark )
    if i == student:
     break

for i in range(student):
   Studentslist[i].studentinfo()

for r in range (Course):
   courselist[r].courseinfo()

for i in range(student):
   Listmark[i].markinfo()