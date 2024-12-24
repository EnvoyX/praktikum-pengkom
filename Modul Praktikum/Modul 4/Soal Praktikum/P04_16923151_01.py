# NIM/Nama  : 16923263/Fitzal Haidar Rahman
# Tanggal   : 30 Oktober 2023
# Deskripsi : Menentukan rata-rata nilai praktikum

# Kamus
# N; count; jumlah = int
# nilai = list of float
# x = float

# Input
N = int(input("Masukkan nilai banyak mahasiswa: "))
nilai = [[float(input(f"Masukkan nilai praktikum {i+1} mahasiswa {j+1}: ")) for j in range(N)] for i in range(4)]
x = float(input("Masukkan target (x): "))
# Inisialisasi jumlah
count = 0

# Proses
for j in range(N):
    jumlah = 0
    for i in range(4):
        jumlah += nilai[i][j]
    rata = jumlah/4
    print(f"Rata-rata mahasiswa {j+1} = {rata}")
    if rata > x:
        count += 1
        
# Output
print(f"Terdapat {count} mahasiswa yang mendapatkan rata-rata nilai praktikum di atas {x}")




# Test
# N = 5
# nilai = [[100,100,100,100,0],[80,100,100,100,100],[0,40,100,0,100],[0,80,100,0,100]]
# x = 70