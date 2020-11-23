import pandas as pd

file = "aes_data.xlsx"

# data = pd.read_excel(file)

# print(data.head())

from iapws import IAPWS97, IAPWS95

sat_steam = IAPWS97(P=1, x=1)
sat_liquid = IAPWS97(T=300, x=0)  # saturated liquid with known T
steam = IAPWS97(P=0.1, T=300)  # steam with known P and T

water1 = IAPWS97(P=1, T=380)
water2 = IAPWS95(P=1, T=380)

print(water1.rho, water1.phase)
print(water2.rho, water2.phase)


df["10LAB13CP002_XQ01"] = df.loc[df["10LAB13CP002_XQ01"]>8, "10LAB13CP002_XQ01"].apply(lambda x: x-x//1)




for col in df.columns.values[1:]:
    df[col] = df[col].apply(lambda x: 0 if x<0 else x)


pump_columns = ["10LAB11CF001_XQ01","10LAB12CF001_XQ01","10LAB13CF001_XQ01","10LAB14CF001_XQ01","10LAB15CF001_XQ01"]

for col in pump_columns:
    df[col] = df[col].apply(lambda x: x if x<510 else 0)    
