import pandas as pd
# pandas akan membaca file
# tingkatinflasi20082013.csv
# yang ada di folder yang sama dengan
# tempat kode python ini disimpan
df1 = pd.read_csv("D:/tingkatinflasi20082013.csv")
print(df1)

# pandas akan membaca file data.xlsx
# yang ada di D:/, lalu meload data
# yang ada di sheet bernama "Sheet 1"
df2 = pd.read_excel("D:/data.xlsx", sheet_name="Sheet 1")
print(df2)

# pandas akan menulis data ke file
# data_out.csv yang ada di folder sama
# dengan file python ini
df1.to_csv("D:/data_out.csv")

# pandas akan menulis data ke
# D:/data_out.xlsx di sheet bernama
# "Sheet 1" dan "Sheet 2"
writer = pd.ExcelWriter("data_out.xlsx")
df2.to_excel(writer , "Sheet1")
df2.to_excel(writer , "Sheet2")
writer.save()