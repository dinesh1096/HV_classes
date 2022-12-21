result=[]
scorelist=[]
for _ in range(int(input("enter number :"))):
        name = input("enter a name :")
        score = float(input("enter marks :"))
        result+=[[name,score]]
        scorelist+=[score]
b=sorted(list(set(scorelist)))[1]

for a,c in sorted(result):
    if(c!=b):
        print("second lowest person",a)