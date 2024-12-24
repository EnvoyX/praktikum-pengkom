
def Max2 (A,B,C):
    #Menghasilkan bilangan terbesar
    #antara A dan B plus C

    #Kamus Lokal
    # maks : int

    # Algoritma
    if (A>=B and A>=C ):
        maks = A
    elif  (B>=A and B>=C ):
        maks = B
    else:
        maks = C

    return maks



def Maks2 (A,B,C):
    #Menghasilkan bilangan terbesar
    #antara A dan B plus C

    #Kamus Lokal

    # Algoritma
    if (A>=B and A>=C ):
        return A
    elif  (B>=A and B>=C ):
        return B
    else:
        return C


A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))



print(f"Versi 1: {Max2(A,B,C)}")
print(f"Versi 2: {Maks2(A,B,C)}")





