# NIM/Nama  : 16923151/Muhamad Hanif Hafizhan
# Tanggal   : 30 Oktober 2023
# Deskripsi : Enkripsi dan Dekripsi pesan

# Kamus
# tipe, pesanInput, hasil = str
# x = int

# Kamus Lokal
# alfabet; pesan = list of str
# kata = str

# Algoritma
def encdec(tipe, pesanInput, x):
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pesan = [i for i in pesanInput]
    kata = ""
    
    # Proses enkripsi
    if tipe == "enkripsi":
        for i in range(len(pesan)):
            if pesan[i] != " ":
                for j in range(len(alfabet)):
                    if pesan[i] == alfabet[j]:
                        kata += alfabet[j-x]
            else:
                kata += " "
    
    # Proses dekripsi
    if tipe == "dekripsi":
        for i in range(len(pesan)):
            if pesan[i] != " ":
                for j in range(len(alfabet)):
                    if pesan[i] == alfabet[j]:
                        kata += alfabet[(j+x) % 26] # Loop jika out of range
            else:
                kata += " "
    
    return kata
    
# Input
tipe = input("Masukkan tipe pesan: ")
pesanInput = input("Masukkan pesan: ")
x = int(input("Masukkan nilai x: "))

# Output
hasil = encdec(tipe, pesanInput, x)
print(hasil)




# Test
# tipe = "dekripsi"
# pesanInput = "dsja svs lmsf cad"
# x = 8