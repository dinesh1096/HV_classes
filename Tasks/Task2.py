#task2
# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen.
# Create a class - Student. Use the method concept, 
# to fetch student name and marks for them


class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def getDetails(self):
        print(f"hi! my name is {self.name}, I received {self.marks}")

    def getDetails1(self):
        print(f"Hi! my name is {self.name}, I received {self.marks} marks.")


stud1=Student("Dinesh",47)
stud2=Student("Ram",96)

stud1.getDetails()
stud2.getDetails1()