#Nama/NIM = Muhamad Hanif Hafizhan / 16923151
#Tanggal = 30 OKtober 2023
#Deksripsi = Problem 3


#Kamus
# M , N = int
# Matriks = Array



#Algoritma

M = int(input("Masukkan nilai M: "))
N = int(input("Masukkan nilai N: "))

Matriks =[[0 for y in range(N)] for i in range (M)] 

#Isi Array
for i in range(M):
    for j in range(N):
        Matriks[i][j] = str(input(f"Masukkan elemen matriks ({i+1,+j+1}): "))

#Hasil Array
for a in range(M):
    for b in range(N):
        print(Matriks[a][b], end=" ")
    print("")
    
# Deklarasi variabel
kapalDeb = 0; poinDeb = 0
kapalKil = 0; poinKil = 0

# Kapal Kecil Dan Besar
MarkedDeb = [[0 for j in range(N)] for i in range(M)]
MarkedKil = [[0 for j in range(N)] for i in range(M)]   
    
# Cek Kapal Nona Deb
Kapal_KecilDeb = 0 ; Kapal_KecilKil = 0
Kapal_BesarDeb = 0 ; Kapal_BesarKil = 0

for d in range(M):
    for e in range(N):
        if Matriks[d][e] == 'D' and MarkedDeb[d][e] == 0:
            kapalDeb += 1
            PanjangDeb = 1
            MarkedDeb[d][e] = 'D'
            # Cek Vertikal
            CheckBawah = d + 1
            print(f"PanjangDeb Sekarang adalah (kereset karena memenuhi syarat lagi): {PanjangDeb}")
            while CheckBawah < M and Matriks[CheckBawah][e] == 'D':
                MarkedDeb[CheckBawah][e] = kapalDeb
                CheckBawah += 1
                PanjangDeb += 1
            # Cek Horizontal
            CheckKanan = e + 1
            Deb_panjang_kanan = 0
            while CheckKanan < N and Matriks [d][CheckKanan] == 'D':
                MarkedDeb[d][CheckKanan] = kapalDeb
                CheckKanan += 1
                PanjangDeb += 1

            if PanjangDeb == 2:
                poinDeb += 3
                Kapal_KecilDeb += 1
            elif PanjangDeb == 3:
                poinDeb += 5
                Kapal_BesarDeb += 1
# Cek Kapal Tuan Kil

        if Matriks[d][e] == 'K' and MarkedKil[d][e] == 0:
            kapalKil += 1
            PanjangKil = 1
            MarkedKil[d][e] = 'K'
            print(f"PanjangKil Sekarang adalah (kereset karena memenuhi syarat lagi): {PanjangKil}")
            #Cek Vertikal
            CheckBawahKil = d + 1
            while CheckBawahKil < M and Matriks[CheckBawahKil][e] == 'K':
                MarkedKil[CheckBawahKil][e] = kapalKil
                PanjangKil += 1
                CheckBawahKil += 1
            # Cek Horizontal    
            CheckKananKil = e + 1
            while CheckKananKil < N and Matriks [d][CheckKananKil] == 'K':
                MarkedKil[d][CheckKananKil] = kapalKil
                PanjangKil += 1
                CheckKananKil += 1
                
            if PanjangKil == 2:
                poinKil += 3
                Kapal_KecilKil += 1
            elif PanjangKil == 3:
                poinKil += 5
                Kapal_BesarKil += 1                
                



print(f"PanjangDeb Diluar Loop adalah (Tidak kereset karena tidak memenuhi syarat lagi): {PanjangDeb}")
print(f"PanjangKil Diluar Loop adalah (Tidak kereset karena tidak memenuhi syarat lagi): {PanjangKil}")
print(f"Total Poin Deb: {poinDeb}, Total Poin Kil: {poinKil}")
print(f"Total Kapal Besar Deb: {Kapal_BesarDeb}, Total Kapal Kecil Deb: {Kapal_KecilDeb}")
print(f"Total Kapal Besar Kil: {Kapal_BesarKil}, Total Kapal Kecil Kil: {Kapal_KecilKil}")
print(f"Total Kapal Kil: {kapalKil} , Total Kapal Deb: {kapalDeb}")

if poinDeb > poinKil:
    print("NONA DEB MEMENANGKAN PERMAINAN!")
elif poinDeb < poinKil:
    print("TUAN KIL MEMENAGNKAN PERMAINAN!")
else:
    print("PERMAINAN SERI!")

# peta = ['D','D','D','.','K'], ['K','K','.','D','K'], ['D', '.', '.', 'D','K'], ['D','.', '.', 'D','.']


