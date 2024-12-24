#Buatlah program yang memeriksa apakah seluruh elemen TI bernilai positif atau tidak




T1 = [0 for i in range(100)]

Pilihan = str(input("Pilihlah pilihan kamu: "))


for x in range(100):
    for y in range(100):
        T1[x][y] = int(input(f"Masukkan elemen2 Array ({x+1},{y+1}): "))



largest = 0
smallest = T1[0][0]

if Pilihan == "0" :
    for l in range(100):
        for s in range(100):
            if largest > T1[l][s]:
                largest = T1[l][s]
                
            if smallest < T1[l][s]:
                smallest = T1[l][s]

            
        

elif Pilihan == "1":
    for l in range(100):
        for s in range(100):
            if largest > T1[l][s]:
                largest = T1[l][s]



elif Pilihan == "2":
    for l in range(100):
        for s in range(100):
            if smallest < T1[l][s]:
                smallest = T1[l][s]

else:
    print("Input tidak valid")
            