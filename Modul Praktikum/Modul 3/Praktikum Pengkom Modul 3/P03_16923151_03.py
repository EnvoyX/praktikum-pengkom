# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal :  16 Oktober 2023
# Deskripsi: Problem 3

# NIM/Nama  : 16923263/Fitzal Haidar Rahman
# Tanggal   : 16 Oktober 2023
# Deskripsi : FPB dari kelompok bilangan

# Kamus
# N = int
# bil = array of int
# hasil = array of int
# pembagi = array of int
# fpb; minimum; kiri; kanan = int

# Input
N = int(input("Masukkan nilai N: "))
# Deklarasi array
bil = [0 for i in range(N)]
# Input nilai array
for i in range(N):
    bil[i] = int(input(f"Masukkan bilangan ke-{i+1}: "))

# Proses
while N-1 > 0:
    hasil = [0 for i in range(N-1)]                        # Panjang array hasil, diawali dengan N-1

    for i in range(len(hasil)):                            # Membandingkan setiap i dengan nilai setelahnya

        if bil[i] < bil [i+1]:                             # Menentukan nilai minimum untuk membatasi pembagian
            minimum = bil[i]
        else:
            minimum = bil[i+1]

        pembagi = [i+2 for i in range(int(minimum))]       # Array dari 2 sampai nilai minimum dari dua bilangan yang dibandingkan
        kiri = bil[i]; kanan = bil[i+1]                    # Inisialisasi bilangan kiri dan kanan
        fpb = 1                                            # Inisialisasi variabel FPB

        for j in pembagi:                                  # Membagi bilangan dengan angka dalam array pembagi
            divcount = 0                                   # Jumlah pembagian dilakukan
            while kiri % j == 0 and kanan % j == 0:        # Ketika kedua bilangan tidak menghasilkan sisa bagi
                kiri /= j; kanan /= j                      # Maka dilakukan pembagian
                divcount += 1                               
            if divcount != 0:                              # Ketika berhasil dilakukan pembagian
                fpb *= j*divcount                          # FPB = FPB * (pembagi * jumlah pembagian)
                # print(f"FPB {bil[i]} dan {bil[i+1]}: ({fpb})")
        
        hasil[i] = fpb                                     # Replace nilai array hasil dengan hasil FPB untuk output
        bil[i] = fpb                                       # Replace nilai array bil dengan hasil FPB untuk diproses kembali
        
    for i in hasil:                                        # Print array hasil
        print(i,end=" ")
    print()

    N -= 1                                                 # Panjang array hasil -1

# Output
print(f"Nilai FPB berantai adalah {hasil[0]}")