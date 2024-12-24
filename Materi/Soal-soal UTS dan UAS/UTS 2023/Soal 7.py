N = int(input("Masukkan N: "))
X = int(input("Masukkan X: "))
Y = int(input("Masukkan Y: "))


Daftar = [0 for i in range(N)]

for j in range(N):
    Daftar[j] = int(input("Masukkan identitas pemilik kupon: "))

for p in range(N):
    if (X-Y) < Daftar[p] < (X+Y):
        print(f"Nomor {p+1} - Identitas: {Daftar[p]}  ")
    

