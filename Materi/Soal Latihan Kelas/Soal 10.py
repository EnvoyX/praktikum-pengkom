NBrs =  int(input("Masukkan Baris : "))
NKol = int(input("Masukkan Kolom : "))




M = [[0 for y in range(NKol)] for x in range(NBrs)]


#
for i in range(NBrs):
    for j in range(NKol):
        M[i][j] = int(input(f"Masukkan Elemen M ke-({i+1},{j+1}) "))
        
for k in range(NBrs):
    for l in range(NKol):
        print(M[k][l], end=" ")
    print("")


for o in range(NBrs):
    for p in range(o,NKol):
        if NBrs == NKol:
            if (M[o][p])!= 0 and p < NKol :
                print(f" O sekarang: {o}") ; print(f" P adalah: {p} ")
                print(f"Elemen yang tidak nol adalah {M[o][p]}")
                if (o and p) == NBrs-1 :
                    print("Merupakan Matriks segitiga atas")
            elif M[o][p] == 0 :
                print("Bukan matriks segitga atas karena isi tidak tepat")                
        else:
            print("Bukan Matriks segitiga atas karena NBrs != Nkol")