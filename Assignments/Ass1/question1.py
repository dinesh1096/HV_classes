#Question 1 - 

# Take five inputs from the user. Make sure those inputs are positive numbers (write the code for the same) and then add those numbers. Once the total is displayed in the console.
# Optional - Try to save that number in the file as well (Using the file handling concept.)


x=open("question1_data","a")
input1=int(input("Enter First number:"))
input2=int(input("Enter Second number:"))
input3=int(input("Enter Third number:"))
input4=int(input("Enter Fourth number:"))
input5=int(input("Enter fifth number:"))
print("The Numbers are:",input1,input2,input3,input4,input5)
print("The Numbers are:",input1,input2,input3,input4,input5,file=x)
if (input1<=0) or (input2<=0) or (input3<=0) or (input4<=0) or (input5<=0):
    print("Enter positive numbers only")
    print("Enter positive numbers only",file=x)
else:
    total=input1+input2+input3+input4+input5
    print("Adding all  values would be:",total)
    print("Adding all  values would be:",total,file=x)
    x.close()


