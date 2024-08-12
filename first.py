import pandas as pd 
dict={"NAME":["Adam","Bob","Catherine","David","Eva"],
      "AGE":[24,25,20,22,23],
      "CITY":["Earth","Heaven","Hell","Unknown","Earth"]}
df=pd.DataFrame(dict)
print("head:")
print(df.head(2))
print("tail:")
print(df.tail(2))
