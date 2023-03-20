id = []
name = []
Dateofbirth = []
print ("Please enter number of students:")
student = int(input())
for i in range(student):
    id.append(i)
    print("Please enter student ", i+1 ," Id:" )
    id[i] = input()

    name.append(i)
    print("Please enter student ", i+1, " name:" )
    name[i] = input()

    Dateofbirth.append(i)
    print("Please enter student ", i+1, " Date of birth:" )
    Dateofbirth[i] = input()

CId = []
Cname = []
print("Please enter number of course: ")
course = int(input())
for r in range (course): 
    CId.append(r)
    print("Please enter course ", r+1," Id:") 
    CId[r] = input()

    Cname.append(r)
    print("Please enter coursse", r+1," name: ")
    Cname[r] = input()
    
print("Please enter the course's ID you want to choose: ")
Ccourse = input()
mark = [] 
while Ccourse not in CId:
    print("INvalid")
    Ccourse = input()
for i in range(student):
     mark.append(i)
     print("Please input mark for student", i+1," :")
     mark[i] = int(input())
     if i == student:
         break
     
for i in range(student):
   print("student's ", i+1," ID:", id[i])
   print("student's", i+1,"name:", name[i])
   print("student's", i+1,"date of birth:", Dateofbirth[i])

for r in range(course):
   print("course", r+1," ID:", CId[r])
   print("course", r+1," name:", Cname[r])

for i in range(student):
   print("student's ",i+1,"mark ",":",mark[i])



