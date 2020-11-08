import pandas as pd
file = "aes_data.xlsx"

data = pd.read_excel(file)

print(data.head())

