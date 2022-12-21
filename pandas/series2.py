import pandas as pd
calories ={"day1":450,"day2":460,"day3":470,"day4":480,"day5":490}
check=pd.Series(calories,index=["day1","day5"])
print(check)