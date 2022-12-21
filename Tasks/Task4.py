# starting number 1st input from user - 2
# last number                     - 40
# 2   40
# find out even numbers and add the even numbers

s=int(input("Enter first number :"))
l=int(input("Enter last number :"))
even = 0
odd=0
for i in range(s,l+1):
 if i % 2 == 0:
   even+= i
else:
    odd+=i

print("Sum of even numbers",even)
print("Sum of odd numbers",odd)

#reverse a number
# palindrome
#armstrong
