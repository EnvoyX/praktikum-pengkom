baris = int(input("Masukkan N: "))
kolom = int(input("Masukkan M: "))


peta = [[0 for j in range(kolom)] for i in range(baris)]


for i in range(baris):
    for j in range(kolom):
        peta[i][j] = int(input(f"Masukkan Keadaan Peta pada koordinat ({i+1,j+1}): " ))
        
for k in range(baris):
    for l in range(kolom):
        print(peta[k][l] ,end=" ")
    print()
    
    

# Cek Peta 


marked = [[0 for j in range(kolom)] for i in range(baris)]
scannedEnemy = 0


for i in range(baris):
    for j in range(kolom):
        if (peta[i][j] == 1 and marked[i][j] == 0):
            scannedEnemy += 1
            marked[i][j] = scannedEnemy
            
            # Cek Kanan
            CheckKanan = j + 1
            while(CheckKanan < kolom and peta[i][CheckKanan] == 1):
                marked[i][CheckKanan] = scannedEnemy
                CheckKanan += 1
                
            #Cek Bawah
            CheckBawah = i + 1
            while(CheckBawah < baris and peta[CheckBawah][j] == 1):
                marked[CheckBawah][j] = scannedEnemy
                CheckBawah += 1

# Cek Peta yang terdeteksi Musuh

print("Hasil musuh yang terdeteksi terlihat pada peta yang telah ditandai dibawah ini: ")
for k in range(baris):
    for l in range(kolom):
        print(marked[k][l] ,end=" ")
    print()
                
# Output                
if (scannedEnemy == 0):
    print("Tidak terdapat kapal musuh pada peta")
else:
    print(f"Terdapat {scannedEnemy} kapal musuh pada peta")     
                