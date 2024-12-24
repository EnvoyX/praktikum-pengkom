def Max2 (A,B):
    #Menghasilkan bilangan terbesar
    #antara A dan B

    #Kamus Lokal
    # maks : int

    # Algoritma
    if (A>B):
        maks = A
        percent = float(maks/10)
    else:
        maks = B
        percent = float(maks/10)

    return percent



def Maks2 (A,B):
    #Menghasilkan bilangan terbesar
    #antara A dan B

    #Kamus Lokal

    # Algoritma
    if (A>B):
        return A/10
    else:
        return B/10
    

def Persen (A,B):
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
        


A = int(input("A: "))
B = int(input("B: "))



print(f"Versi 1: {Max2(A,B)}")
print(f"Versi 2: {Maks2(A,B)}")

hasil = 0.1 * Persen(A,B)
print ("10 persen dari bilangan terbesar = " + str(hasil))





