import pandas as pd
import matplotlib .pyplot as plt


df = pd.read_csv("H05.csv")


#Histogram distribusi nilai matematika
df[["nilai_mat"]].plot(kind="hist", bins=[0,20,40,60,80,100], rwidth=0.8)

#Diagaram batang horizontal banyaknya mahas# freq = len(df["fakultas"])
df["fakultas"].value_counts().plot(kind = "barh")

#Diagram Pie banyaknya mahasiswa masing-masing fakultas
df["fakultas"].value_counts().plot(kind = "pie")

#Berdasarkan diagram pie dan batang horizonal, manakah fakultas dengan mahasiswa terbanyak?
#Manakah diagram yang lebih baik dalam menampilkan fakultas dengan mahasiswa terbanyak dan mengapa?

#Fakultas dengan mahasiswa terbanyak, berdasarkan chart pie dan batang, adalah FTI, dan menurut saya lebih mudah dibaca dalam chart bar horizontal dibandingkan dengan pie chart

#Scatter plot dengan nilai kimia sebagai x dan fisika sebagai y
df.plot(kind='scatter', x = "nilai_kim", y = "nilai_fis", color="orange")
