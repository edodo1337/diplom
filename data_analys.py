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

