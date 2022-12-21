import pandas as pd
a=[1,2,3]
myVar=pd.Series(a,index=["x","y","z"])
print(myVar)


a1=[76,74,83]
y=pd.Series(a1, index=["Dinesh","Dinu","deepak"])
print(y)

studentname=[input("Enter students name :")for _ in range(5)]
marks=[input("Enter students marks :")for _ in range(5)]
z=pd.Series(marks,index=[studentname])
print(z)