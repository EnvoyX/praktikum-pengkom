# Nama/NIM : Muhamad Hanif Hafizhan/16923151
# Tanggal : 26 September 2023
# Deksripsi : TP Modul 2 Problem 1

#Kamus
# N , int
# k , int
# i, int


#initial
N = int(input("Masukkan bilangan N: "))
k = int(input("Masukkan nilai k: "))
x = k
i = int(1)


#Proses  dan Algorimta
while (x < N):
    print(x)
    x = x * k
    i += 1 
if(x == N):
    print(N, " merupakan perpangkatan ", k, " dengan ", k, "^", i)
else:
    print(N , " bukan merupakan perpangkatan ", k)

