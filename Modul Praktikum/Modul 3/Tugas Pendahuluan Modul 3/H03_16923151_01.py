# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 9 Oktober 2023
# Deskripsi : Problem 1

# Kamus

# N, M, ; (int)
# perwakilan, kehadiran, ; (array)


# Algoritma
N = int(input("Masukkan nilai N: "))
M = int(input("Masukkan nilai M: "))


perwakilan = [0 for i in range(N)]   
kehadiran = [0 for j in range(M)]

for i in range(N):
    perwakilan[i] = i + 1    #Mendeklrasikan Array perwakilan dari i + 1

print("Data perwakilan: ", perwakilan)   # Melihat hasil array perwakilan setelah didefinisikan

for j in range(M):
    kehadiran[j] = int(input('Masukkan nilai ke-' + str(j+1) + str(": "))) # Mendefinisikan semua index di dalam array kehadiran

print("Data kehadiran: ", kehadiran) # Melihat hasil array kehadiran setelah didefinisikan 

print("Perwakilan yang tidak datang adalah:") 


# for x in perwakilan:  # untuk setiap nilai di perwakilan
#     if x not in kehadiran:     # jika ada nilai x yang tidak ada di kehadiran maka nilai x yang tidak ada akan muncul
#         print(x , end =" ")




for x in range(M):
    for y in range(N):
        if perwakilan[y] == kehadiran[x]:
            perwakilan[y] = 0


print("Perwakilan yang tidak hadir adalah ", perwakilan)

count = 0

for o in range(N):
    if perwakilan[o] != 0:
        count += 1

Tidak_Hadir = [0 for j in range(count)]

idx = 0
for c in range(N):
    if perwakilan[c] != 0:
        idx +=1
        Tidak_Hadir[idx-1] = perwakilan[c] 
print(Tidak_Hadir)







