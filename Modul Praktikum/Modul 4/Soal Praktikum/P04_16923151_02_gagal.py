#Nama/NIM = Muhamad Hanif Hafizhan / 16923151
#Tanggal = 30 OKtober 2023
#Deksripsi = Problem 2

#Kamus
#Tipe, Pesan = str
# x = int

# Algoritma



def enkripsi(Pesan,x):
    #Kamus Lokal

    #Algoritma Lokal
    alfabet = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    kata =''
    PesanArray = [i for i in Pesan]

    for i in range(len(PesanArray)):
        if PesanArray[i] != " ":
            for j in range(len(alfabet)):
                if PesanArray[i] == alfabet[j]:
                    kata += alfabet[j-x]
        else:
            kata += " "

        
    print(f"Pesan hasil enkripsi adalah: {kata}")
    


def dekripsi(Pesan,x):
    # Kamus Lokal

    #Algoritma Lokal
    alfabet = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    kata =''
    PesanArray = [i for i in Pesan]

    for i in range(len(PesanArray)):
        if PesanArray[i] != " ":
            for j in range(len(alfabet)):
                if PesanArray[i] == alfabet[j]:
                        kata += (alfabet[(j+x) % 26])
        else:
            kata += " "

    print(f"Pesan hasil deskripsi adalah: {kata} ")




Tipe = str(input("Masukkan tipe pesan: "))
Pesan = str(input("Masukkan pesan: "))
x = int(input("Masukkan nilai x: "))



if Tipe == "enkripsi":
    enkripsi(Pesan,x)

elif Tipe == "dekripsi":
    dekripsi(Pesan,x)



