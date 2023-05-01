# Write a Python program that reads the contents of 
# students.csv and creates a list of Student objects, one for each row in the CSV file.
# The program should then do the following:

# Print the name, age, and grade of each student in the 
# list.
# Calculate and print the average grade of all students.
# Find and print the name of the student with the highest grade.
# Sort the list of students by age, and print the sorted list.
#Finally, the program should write a new CSV file called grades.csv 
#that contains only the name and grade of each student, 
#sorted by grade from highest to lowest.


import csv
class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

list_student=[]
sum=0

with open("students.csv","r",newline="") as csvfile:
    data=csv.reader(csvfile,delimiter=",",quotechar="\"")
    next(data)
    
    for row in data:
        student=Student(row[0],int(row[1]),float(row[2]))
        list_student.append(student)
    
    highest_grade=list_student[0]  #Student Object has Highest Grade

    for student in list_student:
        print(f"Name:{student.name} Age:{student.age} Grade:{student.grade}")
        sum=sum+student.grade
        if student.grade>highest_grade.grade:
            highest_grade=student

    average=sum/len(list_student)
    highest_grade_name=highest_grade.name
    
    sorted_list_age=list_student[::]
    sorted_list_grade=list_student[::]
    sorted_list_age.sort(key=lambda k:k.age,reverse=False)
    sorted_list_grade.sort(key=lambda k:k.grade,reverse=True)
    print(f"\nThe Average grade is {average}")
    print(f"\n{highest_grade_name} has the best grade")
    print("\nSorted by Age:\n")
    for student in sorted_list_age:
        
        print(student.name)

    print("\nSorted by Grade:\n")
    for student in sorted_list_grade:
        
        print(student.name)

with open("grades.csv","w",newline="") as grade_file:
    grade_content=csv.writer(grade_file,delimiter=",",quotechar="\"")
    
    for student in sorted_list_grade:
        grade_content.writerow([student.name,student.grade])
