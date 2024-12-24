N = int(input("Masukkan bilangan yang ingin dicek: "))

for i in range(2,N):
    if N % i == 0:
        print(str(N) + " bukan bilangan prima")
    else:
        print(str(N) + " merupakan bilangan prima")