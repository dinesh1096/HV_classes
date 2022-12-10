class Car: #Creating Class 
    attr1 = "Audi";
    attr2 = "Benz";

    def names(self): #Creating Function
        print("The car name is ",self.attr1)
        print("The car name is ",self.attr2)

MyCar = Car() #Creating Object - MyCar is object and Car is class
print(MyCar.attr1)
MyCar.names()