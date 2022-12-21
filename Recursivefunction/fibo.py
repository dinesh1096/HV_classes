def Rec_fib(n):
    if(n<=1):
        return n
    else:
        return(Rec_fib(n-1) + Rec_fib(n-2))

entries = int(input("Enter a number :"))
if(entries<=0):
    print("invalid entry")
else:
    print("Fibnocci series :")
    for i in range(entries):
        print(Rec_fib(i))