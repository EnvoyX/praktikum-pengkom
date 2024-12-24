# Program CountPosGenap
# Menghitung banyaknya bilangan positif dan genap dari sebuah array of integer
# KAMUS
# N : int
# T : array [0..N-1] of int – array of integer dengan indeks dari 0 s.d. N-1
# Tuliskan di bawah ini variabel lain yang diperlukan

# ALGORITMA
# Mendeklarasikan array dan mengisi array
N = int(input())
T = [0 for i in range(N)]

for g in range(N):
    T[g] = int(input("Masukkan elemen ke Array: "))

PositifGenap = 0
for p in range(N):
    if T[p] > 0 and T[p] % 2 == 0 :
        PositifGenap += 1

print(PositifGenap)

... # diasumsikan program untuk mengisi array T dengan sejumlah integer sudah ada,
# tidak diminta dibuat
# Tuliskan di bawah ini: program untuk menghitung ada berapa banyak bilangan integer yang
# positif dan genap dalam array T dan menampilkan hasilnya ke layar