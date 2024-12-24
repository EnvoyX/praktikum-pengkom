import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
# Mengambil nilai minimum dan maximum tiap kolom
minimum = df.min()
maximum = df.max()
# Menuliskan range tingkat inflasi
print(maximum["Tingkat_Inflasi"]) # 11.11
print(minimum["Tingkat_Inflasi"]) # 2.02