import pandas as pd
df = pd.read_csv("D:/tingkatinflasi20082013.csv")
# Mendaftar kemunculan tiap tahun pada data
print(df["Tahun"].value_counts())
# 2013 3
# 2012 3
# 2011 3
# 2010 3
# 2009 3
# 2008 3