import pandas as pd

df = pd.read_csv("D:/H05.csv")

#Nilai matematika, fisika, dan kimia milik Tuan Ric

print(df.loc[df["nama"] == "Tuan Ric"]) 

#Mahasiswa dengan nilai fisika tertinggi
fmax = df["nilai_fis"].idxmax()
print(df[fmax:fmax + 1])

#10 Mahasiswa dengan nilai kimia tertinggi
new = df.sort_values(["nilai_kim"], ascending=[0])
print(new.sort_values(["nilai_kim"], ascending=[0]).head(10))

#Banyaknya nilai matematika di bawah 50
print(len(df.loc[(df["nilai_mat"] < 50)]))

#Banyaknya mahasiswa FMIPA
print(len(df.loc[df["fakultas"] == "FMIPA"]))