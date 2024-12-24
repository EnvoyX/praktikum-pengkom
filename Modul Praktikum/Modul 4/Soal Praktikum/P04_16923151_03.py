# NIM/Nama  : 16923151/Muhamad Hanif Hafizhan
# Tanggal   : 30 Oktober 2023
# Deskripsi : Menghitung kapal pada peta dengan poin yang berbeda untuk setiap panjang kapal

# Kamus
# M; N = int
# kapalDeb; poinDeb = int
# kapalKil; poinKil = int
# panjang = int
# peta = list of str
# markDeb; markKil = list of int

# Input
M = int(input("Mauskkan nilai M: "))
N = int(input("Mauskkan nilai N: "))

# Deklarasi array
peta = [[0 for j in range(N)] for i in range(M)]
markDeb = [[0 for j in range(N)] for i in range(M)]
markKil = [[0 for j in range(N)] for i in range(M)]

# Mengisi array peta
for i in range(M):
    peta[i] = [i for i in input()]
    
# Deklarasi variabel
kapalDeb = 0; poinDeb = 0
kapalKil = 0; poinKil = 0

# Proses
for i in range(M):
    for j in range(N):
        # Menghitung kapal Nona Deb
        if peta[i][j] == "D" and markDeb[i][j] == 0:
            kapalDeb += 1
            panjang = 1
            markDeb[i][j] = kapalDeb
            # Menghitung panjang vertikal
            y = i+1
            while y<M and peta[y][j] == "D":
                markDeb[y][j] = kapalDeb
                y += 1
                panjang += 1
            # Menghitung panjang horizontal
            x = j+1
            while x<N and peta[i][x] == "D":
                markDeb[i][x] = kapalDeb
                x += 1
                panjang += 1
            # Menghitung poin
            if panjang == 2:
                poinDeb += 3
            elif panjang == 3:
                poinDeb += 5
                
        # Menghitung kapal Tuan Kil
        if peta[i][j] == "K" and markKil[i][j] == 0:
            kapalKil += 1
            panjang = 1
            markKil[i][j] = kapalKil
            # Menghitung panjang vertikal
            y = i+1
            while y<M and peta[y][j] == "K":
                markKil[y][j] = kapalKil
                y += 1
                panjang += 1
            # Menghitung panjang horizontal    
            x = j+1
            while x<N and peta[i][x] == "K":
                markKil[i][x] = kapalKil
                x += 1
                panjang += 1
            # Menghitung poin
            if panjang == 2:
                poinKil += 3
            elif panjang == 3:
                poinKil += 5
                
# Ouput
if poinDeb > poinKil: 
    print("Nona Deb Memenangkan permainan")
elif poinKil > poinDeb:
    print("Tuan Kil Memenangkan permainan")
else:
    print("Permainan Seri")



# Test
# M = 4
# N = 5
# peta = [['D', 'D', 'D', '.', 'K'], ['K', 'K', '.', 'D', 'K'], ['D', '.', '.', 'D', 'K'], ['D', '.', '.', 'D', '.']]