#NIM/Nama : 16923151/ Muhamad Hanif Hafizhan
#Tanggal : 2 Oktober 2023
#Deskripsi: Problem 2

# Kamus
# N, pengulangan, suku, N1 , N2 , N3, N4, r, suku ---> (int)


# Algoritma

N = 0

pengulangan = 0
suku = 1


N1 = int(input("Masukkan bilangan pertama: "))
N2 = int(input("Masukkan bilangan kedua: "))
N3 = int(input("Masukkan bilangan ketiga: "))

r = N2//N1
r = N3//N2

if N2//N1 == N3//N2:     # Jika bilangan ketiga pertama adalah bilangan geometri
    N4 = int(input("Masukkan bilangan keempat "))
    bilangan = N1
    while bilangan <= N4:
            bilangan = bilangan * r
            print(bilangan)
            suku += 1
            print(suku)
            if bilangan == N4:
                print("Bilangan ", N4, " merupakan suku ke-", suku," dari barisan geometri")
                break       
    else:
                print("Bilangan ", N4, " bukan merupakan suku dari barisan geometri")
                
        
elif N2/N1 != N3/N2:
    print("Bukan merupakan barisan geometri")



    


        

        

        
    




