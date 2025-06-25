import pandas as pd

df = pd.read_csv("../csv/employees.csv")

names = [f"{row['first_name']} {row['last_name']}" for index, row in df.iterrows()]
print("All names:", names)


names_with_e = [name for name in names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)