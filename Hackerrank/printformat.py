# The included code stub will read an integer, , from STDIN.

# Without using any string methods, try to print the following:


# Note that "" represents the consecutive values in between.Sample Input 0

# 3
# Sample Output 0

# 123

# n=int(input("Enter a number :"))
# if(n<=0):
#     print("Enter positive number")
# else:
#     for i in range(1,n+1):
#         print(i,end=" ")

n=int(input("Enter a number :"))
for i in range(1,n+1,3): 
    print(i)
