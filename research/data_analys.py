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




'pump_1_amper': pd.concat([df[pump_amper_cols[0]][i[0]:i[1]] for i in segments1],  ignore_index=True),
'pump_2_amper': pd.concat([df[pump_amper_cols[1]][i[0]:i[1]] for i in segments2],  ignore_index=True),
'pump_3_amper': pd.concat([df[pump_amper_cols[2]][i[0]:i[1]] for i in segments3],  ignore_index=True),
'pump_4_amper': pd.concat([df[pump_amper_cols[3]][i[0]:i[1]] for i in segments4],  ignore_index=True),
'pump_5_amper': pd.concat([df[pump_amper_cols[4]][i[0]:i[1]] for i in segments5],  ignore_index=True),
  