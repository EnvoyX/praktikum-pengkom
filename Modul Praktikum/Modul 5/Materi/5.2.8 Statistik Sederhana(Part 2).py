
#Kita dapat juga mengambil statistik satu per satu:

import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
df.mean()
# Tahun 2010.500000
# Tingkat_Inflasi 5.818889
df["Tingkat_Inflasi"].mean() # 5.818888888888889
df["Tingkat_Inflasi"].std() # 3.1486727154915681