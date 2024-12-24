N = int(input("Masukkan bilangan yang ingin dicek: "))

prime = True

for i in range(2,N):
    if N % i == 0:
        prime = False

if prime:
    print(f"{N} merupakan bilangan prima")
else:
    print(f"{N} bukan bilangan prima")