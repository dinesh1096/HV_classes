entries=int(input(""))
n1,n2=0,1
count=0
if entries <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif entries == 1:
   print("Fibonacci sequence upto",entries,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < entries:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1