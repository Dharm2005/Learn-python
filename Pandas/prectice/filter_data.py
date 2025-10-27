import pandas as pd

bios = pd.read_csv("../data/bios.csv")

# SYNTEX FILTERING

print(bios) # there are 145500 rows & 10 cols

print(bios.loc[bios["height_cm"] > 220, ["name","height_cm"]]) # using loc

print(bios[bios["height_cm"] > 220]["name"]) # without using loc , can only get columns

# multiple condition

print(bios.loc[(bios["height_cm"] > 220) & (bios["weight_kg"] > 135), ["name","height_cm","weight_kg"]]) # use format like () & ()


# STRING METHOD TO FILTER DATA

# .contains()
print(bios[bios['name'].str.contains("patel",case=False)])

# .isin()
print(bios[bios["born_country"].isin(["UAS","FRA"])])

# .startwith()
print(bios[bios["name"].str.startswith("Dharm")])

# .query function

print(bios.query("born_country == 'IND' and born_city == 'Ahmedabad'"))