class Employee:
    def __init__(self):
        print('employee created')

    def __del__(self):
        print('Destructor called Employee deleted')

emp= Employee()
del emp 