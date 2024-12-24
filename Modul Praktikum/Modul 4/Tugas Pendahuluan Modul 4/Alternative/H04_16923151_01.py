# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 23 Oktober 2023
# Deskripsi : Problem 1


# Cara Wisa
#Kamus
#n ,m, i, j = int
# array = Array / list


#Algoritma


def MaxOddNumberResultInSubmatrix(m,n):

    #Kamus
    #MaxSumOddNumberinSubMatrixResult = int
    # m, n, k, l = int

    #array = Array / list
    #Algoritma
    MaxSumOddNumberinSubMatrixResult = 0
    for k in range(m-1):
        for l in range(n-1):
            if  (array[k][l] % 2 != 0) or (array[k][l+1] % 2 != 0) or (array[k+1][l] % 2 != 0) or (array[k+1][l+1] % 2 != 0):
                if (array[k][l]) + (array[k][l+1]) +  (array[k+1][l]) + (array[k+1][l+1]) > MaxSumOddNumberinSubMatrixResult:
                    MaxSumOddNumberinSubMatrixResult = (array[k][l]) + (array[k][l+1]) +  (array[k+1][l]) + (array[k+1][l+1])
    
    if MaxSumOddNumberinSubMatrixResult != 0:
        print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {MaxSumOddNumberinSubMatrixResult}")
    else:
        print(f"Tidak ada submatriks 2x2 yang memenuhi syarat")
    

m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan nilai n: "))

array = [[0 for j in range(n)]  for i in range(m)]  #Deklrasi Array

for i in range(m):
    for j in range(n):
            array[i][j] = int(input(f"Masukkan elemen matriks ({i+1},{j+1}): "))    # Mengisi Array
    
for i in range (m):
    for j in range(n):
            print(str(array[i][j]) + " " , end= " ") # Melihat hasil Array
    print()


for i in range(len(array)):
    print(array[i])

    #Jumlah maksimum dari submatriks 2x2 yang memiliki elemen ganjil 
MaxOddNumberResultInSubmatrix(m,n)


# NIM/Nama  : 16923263/Muhamad Hanif Hafizhan
# Tanggal   : 25 Oktober 2023
# Deskripsi : Menentukan jumlah maksimum submatriks berukuran 2 x 2 yang memiliki elemen ganjil

# Input
B = int(input("Masukkan nilai M: "))    # Input panjang baris
K = int(input("Masukkan nilai N: "))    # Input panjang kolom

# Deklarasi array
matriks = [[0 for j in range(K)] for i in range(B)]
submatriks = [[0 for j in range(2)] for i in range(2)]

# Input elemen matriks
for i in range(B):
    print()
    for j in range(K):
        matriks[i][j] = int(input(f"Masukkan elemen matriks baris {B+1} kolom {K+1}: "))
print()

# Print matriks
for i in range(B):
    print("[", end=" ")
    for j in range(K):
        print(matriks[i][j], end=" ")
    print("]")
print()

# Inisialisasi variabel
jumlahPertama = False

# Mencari seluruh kemungkinan submatriks 2x2
for x in range(B-1):
    for y in range (K-1):
        
        # Inisialisasi variabel
        jumlah = 0; ganjil = False
        submatriks = [[matriks[x][y], matriks[x][y+1]], [matriks[x+1][y], matriks[x+1][y+1]]]
        
        # Mengecek apakah terdapat elemen ganjil di dalam submatriks 2x2
        for i in range(2):
            for j in range(2):
                if submatriks[i][j] % 2 != 0:
                    ganjil = True

        # Menghitung jumlah sumbatriks 2x2 jika memiliki elemen ganjil
        if ganjil:   
            for i in range(2):
                for j in range(2):
                    jumlah += submatriks[i][j]
            
            # Menentukan jumlah maksimum dari submatriks 2x2
            if not jumlahPertama:        
                jumlahMax = jumlah
                jumlahPertama = True
            else:
                if jumlah > jumlahMax:
                    jumlahMax = jumlah

# Output
if jumlahPertama:
    print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {jumlahMax}")
else:
    print("Tidak ada submatriks 2x2 yang memenuhi syarat")