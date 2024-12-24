M = int(input("Masukkan nilai m: "))

Papan = [[0 for y in range(M)] for x in range(M)]
for i in range(M):
    for j in range(M):
        Papan[i][j] = str(input(f"Masukkan elemen matriks pada ({i+1},{j+1}): "))
        

print("Hasil Papan Catur")
for c in range(M):
    for h in range(M):
        print(Papan[c][h], end=" ")
    print(" ")

count = 0  
for b in range(M):
    for z in range(M):
        if Papan[b][z] == "K":
            if (0 <= b-2 <= M-1) and (0 <= z+1 <= M-1):   
                if Papan[b-2][z+1] == "R": 
                    count += 1
            if (0 <= b-2 <= M-1) and (0 <= z-1 <= M-1):
                if Papan[b-2][z-1] == "R": 
                    count += 1
            #Gerak Arah Bawah
            if (0 <= b+2 <= M-1) and (0 <= z+1 <= M-1):
                if Papan[b+2][z+1] == "R": 
                    count += 1
            if (0 <= b+2 <= M-1) and (0 <= z-1 <= M-1):
                if Papan[b+2][z-1] == "R": 
                    count += 1
            #Gerak Arah Kanan
            if (0 <= b+1 <= M-1) and (0 <= z+2 <= M-1):
                if Papan[b+1][z+2] == "R": 
                    count += 1
            if (0 <= b-1 <= M-1) and (0 <= z+2 <= M-1):
                if Papan[b-1][z+2] == "R": 
                    count += 1
            #Gerak Arah Kiri
            if (0 <= b+1 <= M-1) and (0 <= z-2 <= M-1):
                if Papan[b+1][z-2] == "R": 
                    count += 1
            if (0 <= b-1 <= M-1) and (0 <= z-2 <= M-1):
                if Papan[b-1][z-2] == "R": 
                    count += 1
                    
        if (count > 0) and (b == M-1 and z == M-1) :
            print("Raja tidak aman dari serangan kuda")
        elif (count == 0) and (b == M-1 and z == M-1):
            print("Raja aman dari serangan kuda")


            
