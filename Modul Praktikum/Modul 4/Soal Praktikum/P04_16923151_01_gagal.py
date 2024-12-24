#Nama/NIM = Muhamad Hanif Hafizhan / 16923151
#Tanggal = 30 OKtober 2023
#Deksripsi = Problem 1


# Kamus
# N , target ,average1, average2, average3, average4, total1, total2, total3, total4 i, j , x , y ,b , c = int
# list = Array/Matriks

#Algoritma

N = int(input(f"Masukkan nilai banyak mahasiswa (n): "))


# Mendefinisikan Matriks
list = [[0 for j in range(N)] for i in range(4)] 

#Medefinisikan elemen matriks
for i in range(4):
    for j in range(N):
        list[i][j] = int(input(f"Masukkan nilai praktikum pada elemen ({i+1},{j+1}) : "))


# Melihat hasil matriks nilai praktikum
for b in range(4):
    for c in range(N):
        print(list[b][c], end=" ")
    print("")


#mencari Target
target = int(input("Masukkan target(x): "))
count = 0


#Baris pertama
total1 = 0
for y in range(N):
        total1 += list[0][y]
        average1 = total1 / N 
        if y >= (N-1) :
            print(average1)
            if average1 > target:
                count += 1


#Baris kedua
total2 = 0
for y in range(N):
        total2 += list[1][y]
        average2 = total2 / N 
        if y >= (N-1) :
            print(average2)
            if average2 > target:
                count += 1


#Baris ketiga
total3 = 0
for y in range(N):
        total3 += list[2][y]
        average3 = total3 / N  
        if y >= (N-1) :
            print(average3)
            if average3 > target:
                count += 1


#Baris keempat
total4 = 0
for y in range(N):
        total4 += list[3][y]
        average4 = total4 / N
        if y >= (N-1) :
            print(average4)
            if average4 > target:
                count += 1



print(f"Terdapat {count} mahasiswa yang mendapatkan rata-rata nilai praktikum diatas {target}")




