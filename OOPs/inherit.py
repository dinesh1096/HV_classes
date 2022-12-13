class person(object):

    def __init__(self,name,id): #parametrized constructor
        self.name=name
        self.id=id

    def display(self):
        print(self.name,self.id)

emp=person("Aditya",474)
emp.display()

class Emp(person):

    def Print(self):
        print("emp class called")

empDetails=Emp("Prabhas",476)
empDetails.display()
empDetails.Print()







