#task1
# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen



class Employee():
    company="Aditya College"

    def __init__(self,name,age,salary): #parametrized constructor
        #name age salary are attributes
        self.name=name
        self.age=age
        self.salary=salary

#Creating Object
emp1=Employee("Aditya",21,70000)
emp2=Employee("Dinesh",23,90000)
# emp1.display()

print(f"{emp1.name} and {emp2.name} works in {emp1.__class__.company}") #Formatted string
print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name} and {emp1.name} works in {emp2.__class__.company}")
print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")