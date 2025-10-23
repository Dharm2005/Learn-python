import pandas as pd

# load files

coffee = pd.read_csv('../warmup-data/coffee.csv')
result = pd.read_parquet('../data/results.parquet')
olympics = pd.read_excel('../data/olympics-data.xlsx')

# reading different files

print(coffee.head()) # csv file
print(result.head()) # parquet file
print(olympics.head()) # excel file

