n=int(input("Enter the Factorial number :"))
fact=1   #global variable
if (n<0):
    print("negative numbers are not accepted")
elif(n==0):
    print("factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(f"the factorial of ",n,"is",fact)