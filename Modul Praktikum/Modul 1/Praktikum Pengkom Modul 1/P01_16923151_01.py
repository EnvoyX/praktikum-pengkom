# NIM/NAMA : 16923151/Muhamad Hanif Hafizhan
# Tanggal  : 18 September 2023
# Deskripsi : Problem 1

Kuis_1 = int(input("Masukkan Nilai Kuis 1: "))
Kuis_2 = int(input("Masukkan Nilai Kuis 2: "))
Kuis_3 = int(input("Masukkan Nilai Kuis 3: "))

rata_rata = (Kuis_1 + Kuis_2 + Kuis_3)/3


if (rata_rata >= 80):
    print("Tuan Kil mendapatkan nilai Lulus Memuaskan")
elif (rata_rata >= 70):
    print("Tuan Kil mendapatkan nilai Lulus")
else:
    print("Tuan Kil mendapatkan nilai Tidak Lulus")



