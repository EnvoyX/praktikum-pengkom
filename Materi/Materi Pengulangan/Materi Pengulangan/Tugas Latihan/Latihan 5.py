# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 29 September 2023
# Deskripsi : Latihan 5 Bab Pengulangan KU1102

#Kamus
# a ,b, delta, count, luas_daerah, xmax, x2; (int)




# Algoritma


a = int(input("Masukkan nilai a: ")) # a >= 0
b = int(input("Masukkan nilai b: ")) # b > 0
# a < b


delta = float(input("Masukkan nilai delta: ")) # delta > 0  # delta ====> interval

# x = a sampai x = b dengan interval delta
count = 0
luas_daerah = 0

x2 = a
x_max = b
# f(X) = y
while x2 < x_max and a >= 1 and b > 0 and delta > 0:
        count += 1
        print("Data ke----",count)

        #  mencari data sumbu x
        x2 = x2 + delta
        x1 = x2 - delta

        # mencari data sumbu y
        y1 = x1*3 + x1 + 1
        y2 = x2* 3 + x2 + 1


        #Menghitung luas trapesium
        tinggi_trapesium = x2 - x1
        luas_trapesium_interval = (y1 + y2)/2*(tinggi_trapesium)
        luas_daerah = luas_daerah + luas_trapesium_interval


        #Pengecekan data
        print("Data ditambahi delta: ", x2)
        print("Data dikurangi delta: " , x1)
        print("Tinggi trapesium adalah: " ,tinggi_trapesium)
        print("Luas Trapesium", "Ke---", count , "adalah: " , luas_trapesium_interval, " Satuan Luas")
        
        if x2 == x_max or x2 > x_max:
            print("Luas Daerah di bawah kurva adalah: " , luas_daerah, " Satuan Luas")
            break

else:
    print("Data tidak bisa dihitung")


        
        
