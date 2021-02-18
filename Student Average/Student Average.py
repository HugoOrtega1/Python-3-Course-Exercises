#Hugo Ortega     #Student Average   


StudentName=str(input("Enter student name:"))
StudentID=int(input("Enter Student ID:"))
Assignment1=int(input("Enter Assignment one grade:"))
Assignment2=int(input("Enter Assignment Two grade:"))
Assignment3=int(input("Enter Assignment Three grade:"))

Average = (Assignment1+Assignment2+Assignment3)//3

if Average <= 65:
    print("\n","Studentsname:",StudentName,"\n","StudentsID#:",StudentID,"\n","Students Avergae:",Average,"\n","you have failed")
    
else:
        print("\n","Studentsname:",StudentName,"\n","StudentsID#:",StudentID,"\n","Students Avergae:",Average,"\n","you have passed")


input("Please press enter to close the program")