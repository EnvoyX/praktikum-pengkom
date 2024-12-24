


# TES MODULO dan Penambahan String serta mengubah suatu kalimat string jadi array
# x = 26

# Input = 0

# while (Input != 99):
#     Input = int(input("Masukkan angka dari 1 - 26: "))
    
#     result = Input % x
#     reverse = x % Input
    
#     print(result)
#     print(reverse)

pesan = input(str("Masukkan pesan yang ingin disampaikan: "))

ArrayString = [i for i in pesan]

hasil = "Hasil input nya adalah "

huruf = str(input("Masukkan huruf/kata yang dinginkan: "))

hasil += huruf

for i in range (len(pesan)):
    print(ArrayString[i], end="")
print()


print(hasil)



    

    
    




