name=input("Enter the name:")
roll=input("Enter the roll number:")
semester=int(input("Enter the sem in which student is studying:"))
if(semester %2 ==0):
    year=semester/2
year=(semester+1)/2
student=[]
student.append(name)
student.append(roll)
student.append(year)
print("---------------------------")

subject=["computer programing","Digital Design","Electrical Circuit","Java","Algorithm","Analog Circuit","Semiconductor","Computer Network","Cloud Computing","Digital Communication","Control Systems","Data Analytics","Real Time Systems","Communication Network"]
subjectId=["CS101","EC101","EC102","CS201","CS202","EC201","EC202","CS352","CS351","EC351","EC380","CS452","CS482","EC452"]

course=dict(zip(subject,subjectId))

course_year={1:["Computer Programing","Digital Design","Electrical Circuit"],2:["Java","Algorithm","Analog Circuit","Semiconductor"],3:["Computer Network","Cloud Computing","Digital Communication","Control Systems"],4:["Data Analytics","Real Time Systems","Communication Network"]}

print("The courses that are offered to your year are following, please choose from them minimum 3:")
print("---------------------------")
print(course_year[year]) 
choose=[]
print("type ,'yes' or 'no' to choose:")
while(1):
    if input()=="yes":
        course1=input("Type course name:")
        choose.append(course1)
    else:
        break;
for i in range(len(choose)):
    student.append(choose[i])
    student.append(course[choose[i]])
print(student)
with open('record.txt', 'a') as filehandle:
    for listitem in student:
        filehandle.write('%s\n' % listitem)


