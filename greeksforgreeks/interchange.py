def swap_list(l):
    size=len(l)
    temp=l[0]
    l[0]=l[size-1]
    l[size-1]=temp
    return l

l=[25,35,45,55,65,75]
print(swap_list(l))