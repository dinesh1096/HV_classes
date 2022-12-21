l=[]
user_input=int(input("Enter the number of series :"))
for i in range(1,user_input+1):
    entries=int(input("enter the number :"))
    l.append(entries)

l.sort()
print(l)
print("The second largest number is :",l[-2])
