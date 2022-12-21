def Rec_fact(n):
    if(n==0):
        return 1
    
    return n*Rec_fact(n-1)

n=int(input("Enter a number :"))
print(Rec_fact(n))