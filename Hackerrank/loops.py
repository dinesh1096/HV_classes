# The provided code stub reads and integer,n , from STDIN. For all non-negative integers , print .

# Sample Input 0

# 5
# Sample Output 0

# 0
# 1
# 4
# 9
# 16

n=int(input("Enter a number :"))
if(n<=0):
    print("Enter positive number")
else:
    for i in range(0,n):
         print(i*i)