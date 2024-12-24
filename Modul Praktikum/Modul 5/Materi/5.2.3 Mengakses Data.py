import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
# mengambil data ke-5
print(df.loc[4])
# Tahun 2009
# Cakupan Prov. Jawa Barat
# Tingkat_Inflasi 2.02
# Name: 4, dtype: object

# mengambil data ke-5 hingga 7
print(df[4:7])
# Tahun Cakupan Tingkat_Inflasi
# 4 2009 Prov. Jawa Barat 2.02
# 5 2009 Nasional 2.78
# 6 2010 Kota Bandung 4.53

# mengambil data ke -17 hingga akhir
print(df[16:])
# Tahun Cakupan Tingkat_Inflasi
# 16 2013 Prov. Jawa Barat 9.15
# 17 2013 Nasional 8.38

# mengambil 5 data pertama
print(df[:5])
# Tahun Cakupan Tingkat_Inflasi
# 0 2008 Kota Bandung 10.23
# 1 2008 Prov. Jawa Barat 11.11
# 2 2008 Nasional 11.06
# 3 2009 Kota Bandung 2.11
# 4 2009 Prov. Jawa Barat 2.02

# melihat panjang data
print(len(df))
# 18

# mengambil kolom "Cakupan" dari data ke-2
print(df.loc[1, "Cakupan"])
# ’Prov. Jawa Barat’




