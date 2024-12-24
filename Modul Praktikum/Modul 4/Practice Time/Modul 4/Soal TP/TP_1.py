





m = int(input("Masukkan Nilai M: "))
n = int(input("Masukkan Nilai N: "))


matriks = [[0 for j in range(n)] for i in range(m)]

for i in range (m):
    for j in range(n):
        matriks[i][j] = int(input(f"Masukkan nilai-nilai matariks pada elemen di koordinat ({i+1},{j+1}): "))
        

for i in range(m):
    for j in range(n):
        print(str(matriks[i][j]) ,end=" ")
    print()
    
    


# Cek Submatriks yang memiliki elemen ganjil

TotalMakismal = 0
for k in range(m-1):
    for l in range(n-1):
        if(matriks[k][l]) % 2 != 0 or matriks[k][l+1] % 2 != 0 or matriks [k+1][l] % 2 != 0 or matriks[k][l] % 2 != 0:
            if ((matriks[k][l]) + (matriks[k][l+1]) + (matriks[k+1][l]) + (matriks[k+1][l+1]) > TotalMakismal):
                TotalMakismal = ((matriks[k][l]) + (matriks[k][l+1]) + (matriks[k+1][l]) + (matriks[k+1][l+1]))

if TotalMakismal != 0:
    print(f"Jumlah Maksimum dari submatriks 2x2 yang memiliki elemen ganjil adalah {TotalMakismal}")
else:
    print("Tidak ada submatriks yang memenuhi syarat")
                
            

