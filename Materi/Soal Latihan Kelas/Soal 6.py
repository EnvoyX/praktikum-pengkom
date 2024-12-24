#Buatlah program yang memeriksa apakah seluruh elemen TI bernilai positif atau tidak




T1 = [0 for i in range(100)]


positif  = True
positive = 0
negative = 0

for x in range(100):
    for y in range(100):
        T1[x][y] = int(input(f"Masukkan elemen2 Array ({x+1},{y+1}): "))


for i in range(100):
    for j in range(100):
        if T1[i][j] > 0:
            positif = True
            positive +=1
        else:
            negative += 1

if positif > 0 and negative == 0:
    print("Semua elemen array positif")
else:
    print("Tidak semua elemen array positif")



            