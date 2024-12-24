# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 9 Oktober 2023
# Deskripsi : Problem 3

# Kamus
# duit; duitSisa = integer
# totalStasiun; stasiunTerbanyak; stasiunAwal = integer
# hargaStasiun = array
# Now; Lewat = integer

#Algoritma


# Input
Uang = int(input("Masukkan jumlah uang yang dibawa Tuan Leo: "))
totalStasiun = int(input("Masukkan jumlah stasiun: "))

# Deklarasi variabel
stasiunTerbanyak = 0
hargaStasiun = [0 for i in range(totalStasiun)]   # Deklarasi array

# mendefinisikan nilai array
for i in range(totalStasiun):  
    hargaStasiun[i] = int(input(f"Masukkan harga stasiun ke-{i+1}: ")) #Mendefinisikan Array dengan input
print(hargaStasiun) # mengecek nilai array yang telah didefinisikan

# Proses
for i in range(totalStasiun):
    Sekarang = i                 # Stasiun saat ini yang dilewati
    Lewat = 0               # Jumlah stasiun yang dilewati
    UangSisa = Uang         # Sisa uang Tuan leo
    print("Tuan leo memiliki uang sejumlah ", (UangSisa)) # Uang awal
    print("Tinjau jika stasiun awal ", i+1)  # Tinjau jika memulai dari stasiun i

    # Coba semua kemungkinan pada stasiun i di mana stasiun i sebagai stasiun awal
    while (UangSisa >= hargaStasiun[Sekarang]) and (Lewat < totalStasiun):   # Jika masih memiliki Uang dan belum melewati sejumlah N Total stasiun
        UangSisa -= hargaStasiun[Sekarang]  # Uang akan berkurang terus selagi melewati stasiun
        print("Sekarang pada Stasiun ke-" , Sekarang + 1 ," dengan harga " , hargaStasiun[Sekarang])
        print("Lewat Stasiun ke-", Sekarang + 1, "Sisa uang Tuan Leo: ", UangSisa)
        Sekarang = (Sekarang + 1) % totalStasiun                  # Rute Memutar jika sudah melewati stasiun terakhir maka akan dibagu total stasiun sehingga memulai lagi dari 1
        Lewat += 1                                      # Melewati 1 stasiun
        print("jumlah Stasiun yang dilewati: " , Lewat) 

    # Menggantikan nilai variabel stasiun terbanyak dengan Lewat jika stasiun yang dilewati lebih banyak dari stasiunTerbanyak
    if Lewat > stasiunTerbanyak:
        stasiunTerbanyak = Lewat
        stasiunAwal = i

if stasiunTerbanyak != 0:
    print("Tuan Leo dapat mengunjungi ", stasiunTerbanyak ,  " stasiun dimulai dari stasiun ke-" , stasiunAwal+1)
else:
    print("Tuan Leo kekurangan uang")