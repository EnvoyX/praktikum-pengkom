baris = int(input("Baris: "))
kolom = int(input("Kolom: "))



A = [[0 for j in range(kolom)] for i in range(baris)]


for i in range(baris):
    for j in range(kolom):
        A[i][j] = int(input(f"Masukkan elemen di ({i+1},{j+1}): "))


for i in range(baris):
    for j in range(kolom):
        print(A[i][j], end=" ")
    print("")



# Berikut contoh program untuk membaca matriks A berukuran n×m, membaca matriks B berukuran m × l, dan menuliskan hasil perkalian matriks A kali B berukuran n × l.



n = int(input())
m = int(input())
l = int(input())
A = [[0 for j in range(m)] for i in range(n)]
B = [[0 for j in range(l)] for i in range(m)]
C = [[0 for j in range(l)] for i in range(n)]
for i in range(n):
    for j in range(m):
        A[i][j] = int(input("masukkan elemen A baris " + str(i + 1) + " kolom " + str(j + 1) + ": "))
                                                                                
for i in range(m):
    for j in range(l):
        B[i][j] = int(input("masukkan elemen B baris " + str(i + 1) + " kolom " + str(j + 1) + ": "))
for i in range(n):
    for j in range(l):
        C[i][j] = 0
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
        print(C[i][j], end=" ")
    print("")