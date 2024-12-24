# L = luas segitiga
# a = alas segitiga
# t = tinggi segitiga

t = int(input("Masukkan tinggi segitiga(cm): "))
a = int(input("Masukkan alas segitiga(cm): "))

L = int((1/2 * a * t))

print("Luas segitiga tersebut adalah", L, "cm kuadrat")

if (0 < L <= 25):
    Harga_1 = L * 5000
    print("Maka harga yang didapat adalah: ", "Rp", Harga_1 )
elif (25 < L <= 50):
    Harga_2 = L * 10000
    print("Maka harga yang didapat adalah: ", "Rp", Harga_2)
elif (75 < L <= 100):
    Harga_3 = L * 12500
    print("Maka harga yang didapat adalah: ", "Rp", Harga_3)
else:
    Harga_4 = L * 15000
    print("Maka harga yang didapat adalah: ", "Rp", Harga_4)





