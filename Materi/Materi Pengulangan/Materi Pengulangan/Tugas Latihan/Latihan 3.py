# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 29 September 2023
# Deskripsi : Latihan 3 Bab Pengulangan KU1102


#Kamus
# Genap, Ganjil,Count, angka; (int)

# Algoritma

angka = int(input("Masukkan bilangan bulat: "))
Genap = 0
Ganjil = 0
count = 0

while not angka < 0 :
   if angka%2 :
      Genap = Genap + 1
   if angka%2 != 0 :
      Ganjil = Ganjil + 1
   count += 1
   angka = int(input("Masukkan bilangan bulat: "))

if angka < 0 and count > 0 :
   print("Genap = ", Genap)
   print("Ganjil = ", Ganjil)
else:
   print("Tidak ada bilangan positif yang dimasukkan")


