m = int(input("Masukkan nilai M: "))
n = int(input("Masukkan nilai N: "))


peta = [[0 for j in range (n)] for i in range (m)]

for i in range(m):
    for j in range(n):
        peta[i][j] = str(input(f"Masukkan keadaan peta ({i+1},{j+1}): "))     
        
# Deklarasi variabel
kapalDeb = 0; poinDeb = 0
kapalKil = 0; poinKil = 0

scannedDeb = [[0 for j in range (n)] for i in range (m)]
scannedKil = [[0 for j in range (n)] for i in range (m)]

        
        
for i in range(m):
    for j in range(n):
        # Deb
        if peta[i][j] == 'D' and scannedDeb[i][j] == 0:
            kapalDeb += 1
            PanjangDeb = 1
            scannedDeb[i][j] = 'D'
            
            # Cek Horizontal
            CekHorizontalDeb = j + 1
            while(CekHorizontalDeb < n and scannedDeb[i][CekHorizontalDeb] == 0):
                scannedDeb[i][CekHorizontalDeb] = 'D'
                PanjangDeb += 1
                CekHorizontalDeb += 1
            # Cek Vertikal
            CekVertikalDeb = i + 1
            while(CekVertikalDeb < m and scannedDeb[CekVertikalDeb][j] == 0):
                scannedDeb[CekVertikalDeb][j] = 'D'
                PanjangDeb += 1
                CekVertikalDeb += 1
            
        if PanjangDeb == 3:
            poinDeb += 5
        elif PanjangDeb == 2:
            poinDeb += 3
        
        # Kil
        if peta[i][j] == 'K' and scannedKil[i][j] == 0:
            kapalKil += 1
            PanjangKil = 1
            scannedKil[i][j] = 'K'
            
            # Cek Horizontal
            CekHorizontalKil = j + 1
            while(CekHorizontalKil < n and scannedKil[i][CekHorizontalKil] == 0):
                scannedKil[i][CekHorizontalKil] = 'K'
                PanjangKil += 1
                CekHorizontalKil += 1
            # Cek Vertikal
            CekVertikalKil = i + 1
            while(CekVertikalKil < m and scannedKil[CekVertikalKil][j] == 0):
                scannedKil[CekVertikalKil][j] = 'K'
                PanjangKil += 1
                CekVertikalKil += 1
            
        if PanjangKil == 3:
            poinKil += 5
        elif PanjangKil == 2:
            poinKil += 3
            
        
        