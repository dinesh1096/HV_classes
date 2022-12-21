
#Break

student1 = int(input("Enter student1 marks: "))
student2 = int(input("Enter student2 marks: "))
student3 = int(input("Enter student3 marks: "))
student4 = int(input("Enter student4 marks: "))
student5 = int(input("Enter student5 marks: "))

num=[student1,student2,student3,student4,student5]

# for i in num:
#     if (i <= 40):
#         break
#     print("stdent marks are: ",i)


for i in num:
    if(i==40):
        continue
    print(i)


# num=[int(input()) for i in range(5)]




