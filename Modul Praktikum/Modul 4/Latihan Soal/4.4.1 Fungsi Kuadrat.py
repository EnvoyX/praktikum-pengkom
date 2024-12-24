#Fungsi Kuadrat

def fungsi(x):
    fx = x**2 - 2*x + 5

    return fx




A = int(input("Masukkan A: "))
B = int(input("Masukkan B: "))

for i in range(A,B+1):
    fungsi(i)
    print(f" f({(i)}) = {fungsi(i)}")
 




