def enkripsi(pesan,x):
    ArrayPesan = [i for i in pesan]    # untuk bisa menggunakan len dan memasukkan pesan dalam bentuk array
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    hasil = ""
    
    for i in range(len(ArrayPesan)):
        
        if ArrayPesan[i] != " ":
            for j in range(len(alfabet)):
                if ArrayPesan[i] == alfabet[j]:
                    hasil += (alfabet[j-x])
        else:
            hasil += " "
    print(f"Pesan hasil enkripsi adalah: {hasil}")
    return

def dekripsi(pesan,x):
    ArrayPesan = [i for i in pesan]    # untuk bisa menggunakan len dan memasukkan pesan dalam bentuk array
    alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    hasil = ""
    
    for i in range(len(ArrayPesan)):
        if ArrayPesan[i] != " ":
            for j in range(len(alfabet)):
                if ArrayPesan[i] == alfabet[j]:
                    hasil += (alfabet[(j+x) % 26])
        else:
            hasil += " "
    print(f"Pesan hasil enkripsi adalah: {hasil}")
    return 


tipe = str(input("Masukkan tipe pesan: "))
pesan = str(input("Masukkan pesan: "))
x = int(input("Masukkan nilai x: "))




if tipe == "enkripsi":
    enkripsi(pesan,x)

elif tipe == "dekripsi":
    dekripsi(pesan,x)