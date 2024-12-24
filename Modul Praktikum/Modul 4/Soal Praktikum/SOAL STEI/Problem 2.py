M = int(input("Masukkan nilai m: "))
N = int(input("Masukkan nilai n: "))


Matriks = [[0 for j in range(N)] for i in range(M)]
New = [[0 for j in range(N)] for i in range(M)]


for i in range(M):
    for j in range(N):
        Matriks[i][j] = int(input(f"Masukkan elemen matriks pada ({i+1},{j+1}): "))
        
        
for x in range(M):
    for y in range(N):
        # Cek atas
        if (0 <= x-1 <= M-1):
            Atas = Matriks[x-1][y]
        #Cek Bawah
        if (0 <= x+1 <= M-1):
            Bawah = Matriks[x+1][y]
        #Cek Kanan
        if (0 <= y+1 <= N-1):
            Kanan = Matriks[x][y+1]
        #Cek Kiri 
        if (0 <= y-1 <= N-1):
            Kiri = Matriks[x][y-1]
        # Cek atas
        if not(0 <= x-1 <= M-1):
            Atas = 0
        #Cek Bawah
        if not(0 <= x+1 <= M-1):
            Bawah = 0
        #Cek Kanan
        if not(0 <= y+1 <= N-1):
            Kanan = 0
        #Cek Kiri 
        if not(0 <= y-1 <= N-1):
            Kiri = 0   
        #Assign Matriks baru dengan penjumlahan matriks sekitar
        New[x][y] = Atas + Bawah + Kiri + Kanan
        
        
        
print("Matriks Baru:")
for n in range(M):
    for e in range(N):
        print(New[n][e], end=" ")
    print()