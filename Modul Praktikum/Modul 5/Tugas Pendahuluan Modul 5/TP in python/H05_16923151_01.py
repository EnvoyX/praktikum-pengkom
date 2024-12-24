import pandas as pd

#Mencari Banyaknya Data
data = pd.read_csv("D:/H05.csv")
print(len(data))

# Mencari 10 data pertama
print(data[:10])

# Mencari Data ke-50 sampai 60
print(data[49:60])

#Banyaknya mahasiswa tiap fakultas
print(data["fakultas"].value_counts())

#Nilai Korelasi antara nilai fisika dan kimia
data["nilai_fis"].corr(data["nilai_kim"])

#Berdasarkan nilai korelasi antara nilai fisika dan kimia, 
#bahwa nilai korelasinya sekitar 0.79 yaitu mendekati nilai 1,
#maka kedua nilai pelajaran relatif berbanding lurus.