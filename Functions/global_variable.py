total=0       #global variable 
def Sum(para1,para2):
    total=para1+para2     #toatal -> local variable
    print("The total is :",total)
    return total

Sum(10,20)
print("The new total is :",total)
