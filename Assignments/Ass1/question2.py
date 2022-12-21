# Question 2 - 

# Create a dictionary in Python, with the name “Car”, which has keys and values. Fetch the “brand name” as the key and “color” as the value from the user. Display the complete dictionary in the console and try to save the output in the file also (Using the file handling concept)

Car = {} #Creating Dictionary
Brand = str(input("Enter brand name :")) #Brand name taken from the user(Key)
Color = str(input("Enter color name :")) #Color name taken from the user(Value)
Car={Brand:Color} #{key:value}
x=open("question2.txt","a")  #creating car.txt and appending all user brand name and color name  in that file
print("Car brand name and color name would be",Car,file=x) 
print("Car brand name and color name would be",Car) 
x.close()