def Max2 (A,B):
    #Menghasilkan bilangan terbesar
    #antara A dan B

    #Kamus Lokal
    # maks : int

    # Algoritma
    if (A>B):
        maks = A
    else:
        maks = B

    return maks



def Maks2 (A,B):
    #Menghasilkan bilangan terbesar
    #antara A dan B

    #Kamus Lokal

    # Algoritma
    if (A>B):
        return A
    else:
        return B


A = int(input("A: "))
B = int(input("B: "))



print(f"Versi 1: {Max2(A,B)}")
print(f"Versi 2: {Maks2(A,B)}")





