import pandas as pd
import numpy as np



file = "aes_data.xlsx"

data = pd.read_excel(file)




# data = data.drop([0,1,2], axis=0)

df = data.drop([0,1,2], axis=0)


data.head()
