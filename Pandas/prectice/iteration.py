import pandas as pd

coffee = pd.read_csv("../warmup-data/coffee.csv")

# to iterate using iterrow()

for index,row in coffee.iterrows():
  print(row)
  print(row["Day"]) # specific columns