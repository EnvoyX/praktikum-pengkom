#Selain itu, kita bisa mengakses data berdasar kriteria.
import pandas as pd
df = pd.read_csv("tingkatinflasi20082013.csv")
# mengambil data tahun 2012
print(df.loc[df["Tahun"] == 2012])
# Tahun Cakupan Tingkat_Inflasi
# 12 2012 Kota Bandung 4.02
# 13 2012 Prov. Jawa Barat 3.86
# 14 2012 Nasional 4.30
# mengambil data Kota Bandung sebelum tahun 2012

print(df.loc[(df["Cakupan"] == "Kota Bandung") & (df["Tahun"] < 2012)])
# Tahun Cakupan Tingkat_Inflasi
# 0 2008 Kota Bandung 10.23
# 3 2009 Kota Bandung 2.11
# 6 2010 Kota Bandung 4.53
# 9 2011 Kota Bandung 2.75
# mengambil data dengan tingkat inflasi di atas 10
# atau di bawah 3
print(df.loc[(df["Tingkat_Inflasi"] > 10) | (df["Tingkat_Inflasi"] < 3)])
# Tahun Cakupan Tingkat_Inflasi
# 0 2008 Kota Bandung 10.23
# 1 2008 Prov. Jawa Barat 11.11
# 2 2008 Nasional 11.06
# 3 2009 Kota Bandung 2.11
# 4 2009 Prov. Jawa Barat 2.02
# 5 2009 Nasional 2.78
# 9 2011 Kota Bandung 2.75