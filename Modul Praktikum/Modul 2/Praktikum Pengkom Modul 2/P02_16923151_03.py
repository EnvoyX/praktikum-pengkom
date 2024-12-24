#NIM/Nama : 16923151/ Muhamad Hanif Hafizhan
#Tanggal : 2 Oktober 2023
#Deskripsi: Problem 3


#Kamus



#Algoritma


# Deklarasi variabel
minuman = int(input("Masukkan Harga Minuman: "))

val = 1
koin = 1

while (val < minuman):
    koin *= 7
    val += koin

while (koin > 0 and val != minuman):
    if val - minuman >= 2*koin:
        val -= 2*koin
    elif val - minuman >= koin:
        val -= koin
    koin /= 7

if (val == minuman):
    print("Transaksi bisa dilakukkan")
else:
    print("Transaksi tidak bisa dilakukkan")