def ChangeNumber(mylist):
    mylist.append([1,2,3,4,5])
    print("values inside the funcytion",mylist)
    return

mylist=[40,50,60,70]
print("values outside the function :",mylist)
ChangeNumber(mylist)
