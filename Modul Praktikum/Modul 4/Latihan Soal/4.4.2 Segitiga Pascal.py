N = int(input("Masukkan N: "))

M = [[0 for j in range (N)] for i in range(N)]

#Inisialisasi Matriks
for i in range(N):
    for j in range(N):
        M[i][j] = 1
        if i > 0:
            break 
        
for x in range(N):
    for y in range(N):
        M[y][x] = 1
        if x > 0:
            break

#Melihat Hasil Matriks Insialisasi        
for h in range(N):
    for g in range(N):    
        print(M[h][g], end=" ")
    print("")


#Proses dan Algoritma   
#Jika ada yang nol maka akan ditambah dengan bilangan diatas dan kirinya
for c in range(N):
    for v in range(N):
        if M[c][v] == 0:
            M[c][v] = M[c-1][v] + M[c][v-1]
            

#Melihat hasil setelah di proses        
for s in range(N):
    for d in range(N):    
        print(M[s][d], end=" ")
    print("")
