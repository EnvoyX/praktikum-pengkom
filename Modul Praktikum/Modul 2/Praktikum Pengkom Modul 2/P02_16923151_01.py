#NIM/Nama : 16923151/ Muhamad Hanif Hafizhan
#Tanggal : 2 Oktober 2023
#Deskripsi: Problem 1

#Kamus
#count; N ; tertinggi ; angka_tertinggi; average --> (int)


#Algoritma
val1 = 0
val2 = 0
ratarata = 0.0
while ratarata < 70:
    n = int(input("Masukkan Nilai latihan: "))

    if (n >= val1):
        val2 = val1
        val1 = n

    elif (n >= val2):
        val2 = n

    ratarata = (val1+val2)/2.0

print("Lulus dengan rata-rata: " , ratarata)






