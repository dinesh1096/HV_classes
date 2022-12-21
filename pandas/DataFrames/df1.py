
#dataframe is a multidirectional array
import pandas as pd
entries ={
    "Temperature":[99,100,120,140,150],
    "Days":["mon","tue","wed","thu","fri"]
}
df=pd.DataFrame(entries)
# print(df)
print(df.loc[0])