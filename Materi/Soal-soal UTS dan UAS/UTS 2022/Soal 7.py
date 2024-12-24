N = int(input("Masukkan Nilai N: "))

D1 = [0 for i in range(N)]
D2 = [0 for j in range(N)]

for x in range(N):
    D1[x] = int(input(f"Masukkan elemen D1 yang ke-{x+1}: "))

for y in range(N):
    D2[y] = int(input(f"Masukkan elemen D2 yang ke-{y+1}: "))

print(D1)
print(D2)

TP = 0
TN = 0
FP = 0
FN = 0

for i in range(N):
    if D1[i] == D2[i] == 1:
        TP += 1
    if D1[i] == D2[i] == -1:
        TN += 1
    if D1[i] == -1 and D2[i] == 1:
        FP += 1
    if D1[i] == 1 and D2[i] == -1:
        FN += 1
    
akurasi = (TP + TN)/(TP + TN + FP + FN)


print(f"Akurasinya adalah {akurasi}")

