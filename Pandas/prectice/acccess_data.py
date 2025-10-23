import pandas as pd

coffee = pd.read_csv('../warmup-data/coffee.csv')

# Access random data from file
print(coffee.sample(10, random_state=1)) # the random_state is optional , it works like seed

# Access specific cols and rows using .loc[]
print(coffee.loc[0]) # 0 is row
print(coffee.loc[1:5]) # return 0, 1, and 5 row

print(coffee.loc[:,'Day']) # all row and day column
print(coffee.loc[:,['Day','Units Sold']]) # all row and Day & Units Sold columns

# Access specific cols and rows using .loc[]
print(coffee.iloc[:,[0,2]]) # all row and Day & Units Sold columns

# Can use .loc[] for modify perticular values 
coffee.loc[1, "Units Sold"] = 10
print(coffee.head(3))

# Changing value of index for better use
coffee.index = coffee.Day # or coffee["Day"]
print(coffee.index)

# so now the value of coffee.index is monday, tuesday and so on, means 0, 1, 2... (rows) is become monday, tuesday and so on
print(coffee.head(3))


