N = int(input("Masukkan N: "))

bilangan = [0 for i in range(N)]

for m in range(N):
    bilangan[m] = int(input("Masukan elemen matriks N: "))
print(bilangan)

terbalik = [0 for y in range(N)]

itung = N
for n in range(N):
    itung -= 1
    terbalik[itung] = bilangan[n] 

print(terbalik)




