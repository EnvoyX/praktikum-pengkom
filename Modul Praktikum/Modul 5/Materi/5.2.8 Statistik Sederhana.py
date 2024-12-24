import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
df.describe()
#               Tahun           Tingkat_Inflasi
# count         18.000000       18.000000
# mean          2010.500000      5.818889
# std           1.757338          3.148673
# min           2008.000000       2.020000
# 25%           2009.000000       3.272500
# 50%           2010.500000       4.415000
# 75%           2012.000000       8.277500
# max           2013.000000       11.110000