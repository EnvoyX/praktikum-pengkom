import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
# Mengambil data dengan inflasi maksimum
imax = df["Tingkat_Inflasi"].idxmax()
print(df[imax:imax + 1])
# Tahun Cakupan Tingkat_Inflasi
# 1 2008 Prov. Jawa Barat 11.1

# Mengambil data dengan inflasi minimum
imin = df["Tingkat_Inflasi"].idxmin()
print(df[imin:imin + 1])
# Tahun Cakupan Tingkat_Inflasi
# 4 2009 Prov. Jawa Barat 2.02