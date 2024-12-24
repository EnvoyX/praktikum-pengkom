# NIM/Nama: 16923151/Muhammad Hanif Hafizhan
# Tanggal : 24 Oktober 2023
# Deksripsi : Membuat prosedur CetakArray yang menerima masukkan array dan mencetak 

# Kamus
# Total_Bilangan = int
# T = array
# Definisi Prosedur CetakArray
def CreateArray(T):
    # Mencetak index array beserta elemen2 di dalam array
    
    #Kamus
    # X = int
    # Total_Bilangan = int
    # T = Array

    # Algoritma
    for x in range (Total_Bilangan):
        print([x], T[x])
    return


# Algoritma
Total_Bilangan = int(input("Masukkan Total Bilangan N: "))
T = [0 for i in range (Total_Bilangan)] # Mendefinisikan array


for y in range (Total_Bilangan): # Mengisi array
    T[y] = int(input("Masukkan integer untuk didefinisikan dalam Array: "))


if Total_Bilangan == 0:
    print("Array kosong.")
else: #N > 0
    CreateArray(T)
