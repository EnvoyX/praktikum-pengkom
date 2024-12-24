# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 23 Oktober 2023
# Deskripsi : Problem 3

def Enemy(Ma,N,M):
    Musuh = 0
    Loop = 0
    for y in range(N):
        for x in range(M):
            if Map[y][x] == 1 :
                Musuh += 1
                y = y + 1
                Loop = Loop + 1
                print(f"Musuh yang terdeteksi: {Musuh}")
        if y >= (N - 1):
            break
        else:
            continue     
            
    if Musuh != 0:
            print(f"Y sekarang adalah: {y}")
            print(f"Terdapat {Musuh} kapal musuh pada peta")
    else:
        print(f'Tidak terdapat kapal musuh pada peta')


N = int(input("N: "))
M = int(input("M: "))


Map = [[0 for x in range (M)] for y in range (N)]

for i in range(N):
    for j in range(M):
            Map[i][j] = int(input(f"Masukkan Keadaan Peta sekarang pada ({i + 1},{j + 1}): ")) # Mengisi ArraY
    
for i in range (N):
    for j in range(M):
        print(str(Map[i][j]) + " " , end= " ") # Melihat hasil Array
    print()

for i in range(len(Map)):
    print(Map[i])
    
Enemy(Map,N,M)

print
