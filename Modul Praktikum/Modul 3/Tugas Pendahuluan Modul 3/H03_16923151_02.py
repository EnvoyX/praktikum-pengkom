# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 9 Oktober 2023
# Deskripsi : Problem 2

#Kamus
#Total, N ; int
# NumbersArray ; array


#Algoritma

#Membuat Array
Total = int(input("Masukkan banyak data: "))
N = int(input("Masukkan nilai N: "))

Array = [0 for x in range(Total)]   # Deklarasi Array

for x in range(Total):
    Array[x] = int(input("Masukkan data ke- " + str(x+1) + str(": ")))    #Mendefinisikan Array dengan input user

print("Hasil Arraynya adalah: " , Array)  # Melihat hasil Array


#Proses
for x in range(Total):  #menghitung index dengan range Total dalam x
    print("Index x Array di ", str(x) , "adalah ", Array[x])
    for y in range(x+1,Total): # menghitung y dengan index yang 1 lebih maju dari x
        print("Index y Array di ", str(y) , "adalah ", Array[y])
        if Array[x] >= Array [y]:   # jika nilai array [x] lebih besar dari nilai array [y]
            placeholder = Array[x]      #menaruh nilai array[x] di placeholder untuk ditukar
            Array[x] = Array[y]          #Menggantikan nilai index pada array [x] dengan nilai array [y], untuk mengurutkan yang bernilai besar ke kanan
            Array[y] = placeholder          # menggantikan nilai index pada nilai array [y] dengan nilai array [x]
            print("Placeholder sekarang " , placeholder )   #Nilai yang ditukar setelah kondisi if diatas memenuhi
            print("Array Sekarang: ", Array)              # Memperlihatkan isi nilai array setelah di tukar
print("Nilai terbesar ke-" + str(N) , " adalah", Array[Total-N])











