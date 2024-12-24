# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 29 September 2023
# Deskripsi : Latihan 4 Bab Pengulangan KU1102

#Kamus
# N , (int)

# Algoritma
N = int(input("Anak Ayam Turuanlah: "))

# menggunakan While, tepat digunakan untuk persoalan ini


while N != 1 and N > 0:
    if N > 0:
        N -= 1
        print("Mati satu tinggalah ", N)
else:
    print("Mati satu tinggal induknya")


# menggunakan For, tepat digunakan untuk persoalan ini

ayam = int(input("Anak Ayam Turuanlah: "))


for i in range(ayam,0,-1):
    print("Mati satu tinggalah ", i)
    if i == 1:
        print("Mati satu tinggal induknya")

# menggunakan do-while (jaminan menjalanakan program setidaknya sekali), tepat digunakan untuk persoalan ini

C = int(input("Anak Ayam Turuanlah: "))

while True:

    if C > 0 :
        C -= 1
        print("Mati satu tinggalah ", C)
    if C == 1:
        print("Mati satu tinggal induknya")
        break
