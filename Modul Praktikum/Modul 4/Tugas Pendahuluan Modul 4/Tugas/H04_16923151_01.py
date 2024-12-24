# NIM/Nama  : 16923263/Muhamad Hanif Hafizhan
# Tanggal   : 25 Oktober 2023
# Deskripsi : Menentukan jumlah maksimum submatriks berukuran 2 x 2 yang memiliki elemen ganjil, Problem 1

# Kamus 
# m,n,i,j = int
# array = Array
# Result = def / fungsi

#Algoritma

def Result(m,n):

    #Kamus Lokal
    #Result = int
    # m, n, k, l = int

    #array = Array / list
    #Algoritma Lokal
    maxResult = 0
    for k in range(m-1):
        for l in range(n-1):
            if  (array[k][l] % 2 != 0) or (array[k][l+1] % 2 != 0) or (array[k+1][l] % 2 != 0) or (array[k+1][l+1] % 2 != 0):
                if (array[k][l]) + (array[k][l+1]) +  (array[k+1][l]) + (array[k+1][l+1]) > maxResult:
                    maxResult = (array[k][l]) + (array[k][l+1]) +  (array[k+1][l]) + (array[k+1][l+1])
    
    if maxResult != 0:
        print(f"Jumlah maksimum submatriks berukuran 2x2 yang memiliki elemen ganjil adalah {maxResult}")
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
Result(m,n)
