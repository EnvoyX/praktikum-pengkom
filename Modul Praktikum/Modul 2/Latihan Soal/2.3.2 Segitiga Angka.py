N = int(input("Masukkan N: "))

for i in range(1,N+1):
    for j in range(i):
        print(j+1, end=" ")
    print()