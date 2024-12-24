import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
# Mengurutkan data berdasar tingkat inflasi , ascending
print(df.sort_values(["Tingkat_Inflasi"], ascending=[1]))
# Mengurutkan data berdasar tahun ascending ,
# lalu tingkat inflasi descending
print(df.sort_values(["Tahun", "Tingkat_Inflasi"], ascending=[1, 0]))