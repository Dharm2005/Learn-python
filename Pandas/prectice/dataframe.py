import pandas as pd

df = pd.DataFrame([[1,2,3,],[4,5,6],[7,8,9]], columns=["A","B","C"])

print(df) # FULL DATAFRAMS
print(df.head()) # FIRST FIVE ROWS
print(df.head(2)) # FIRST TWO ROWS
print(df.tail(2)) # LAST TWO ROWS

print(df.columns.tolist()) # TO SEE COLUMNS
print(df.index.tolist()) # TO SEE COLUMNS

print(df.info()) # TO SEE INFORMATION
print(df.describe()) # TO SEE MEANINGFULL INFO