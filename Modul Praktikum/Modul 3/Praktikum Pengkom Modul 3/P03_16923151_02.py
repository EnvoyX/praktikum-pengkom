# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal :  16 Oktober 2023
# Deskripsi: Problem 2


# Kamus
# PanjangPapan ; Deb ; Sal ; Angka = int
# Papan ; = array

# Algoritma


PanjangPapan = int(input("Panjang Papan: "))
Deb = int(input("Dadu Nona Deb: "))
Sal = int(input("Dadu Nona Sal: "))

Papan  = [0 for i in range (PanjangPapan)]
for x in range(0,PanjangPapan):
    Papan[x] = x + 1

print(Papan) # Melihat hasil petak 1-N
# Dengan Asumsi input/masukan angka dan dadu dalam permainan selalu bernilai benar

