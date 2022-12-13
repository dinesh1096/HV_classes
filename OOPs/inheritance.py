class person(object):

    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(person):

    def isEmployee(self):
        return True

Emp=person("Dinesh")
print(Emp.getName(),Emp.isEmployee())

Emp1=Employee("Dinesh")
print(Emp1.getName(),Emp1.isEmployee())