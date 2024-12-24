NBrs1 =  int(input("Masukkan Baris 1: "))
NBrs2 = int(input("Masukkan Baris 2: "))
NKol1 = int(input("Masukkan Kolom 1: "))
NKol2 = int(input("Masukkan Kolom 2: "))




M1 = [[0 for y in range(NKol1)] for x in range(NBrs1)]
M2 = [[0 for j in range(NKol2)] for i in range(NBrs2)]



for i in range(NBrs1):
    for j in range(NKol1):
        M1[i][j] = int(input(f"Masukkan Elemen M1 ke-({i+1},{j+1}) "))
for k in range(NBrs2):
    for l in range(NKol2):
        M2[k][l] = int(input(f"Masukkan Elemen M1 ke-({k+1},{l+1}) "))

validated = 0
notsame = 0

for o in range(NBrs1):
    for p in range(NKol1):
        if M1[o][p] == M2[o][p]:
            validated +=1
        else:
            notsame += 1

    if validated != 0 and notsame == 0:
        print("Kedua Matriks tersebut sama")
    else:
        print("Kedua Matriks tersebut tidak sama")  

            