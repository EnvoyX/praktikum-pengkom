# Program Jumlah10Angka

# Menerima masukan 10 buah integer dan

# menjumlahkan totalnya

# KAMUS
# N, i, sum : int

# ALGORITMA
N = int(input("Masukkan angka: "))
sum = 0  
sum_negative = 0                   # Inisialisasi
for i in range(1, N + 1):      # Mencacah Maju
    print(i)                       # Aksi
    sum = sum + i             # Aksi

for j in range(N, 0, -2 ):  #Mencacah mundur
    print(j)
    sum_negative = sum_negative + j

print("Jumlah harga ",sum)                # Terminasi
print(sum_negative)       