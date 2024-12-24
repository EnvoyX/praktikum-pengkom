--16923151 / Muhamad Hanif Hafizhan
--Latihan 5 Pseudocode

--{Insialisasi}


input(a)
input(b)
input(delta)


count << 0
luas_daerah << 0

x2 << a
x_max << b

--{Proses pengulangan while}

while (x2 < x_max) and (a >= 1) and (b > 0) and (delta > 0) do
    count << count + 1
    output("Data ke--", count)

    --{mencari data sumbu x}
    x2 << x2 + delta
    x1 << x2 - delta

    --{mencari data sumbu y}
    y1 << x1*3 + x1 + 1
    y2 << x2*3 + x2 + 1
    
    --{menghitung luas trapeisum}
    tinggi_trapesium << x2 - x1
    luas_trapesium_interval << (y1 + y2) / 2 *(tinggi_trapesium)
    luas_daerah << luas_daerah + luas_trapesium_interval    

    --{Pengecekan data}
    output("Data ditambahi delta: ", x2)
    output("Data dikurangi delta: " , x1)
    output("Tinggi trapesium adalah: " ,tinggi_trapesium)
    output("Luas Trapesium", "Ke---", count , "adalah: " , luas_trapesium_interval, " Satuan Luas")

    if (x2 == x_max) or (x2 > x_max) then
    output("Luas Daerah di bawah kurva adalah: " , luas_daerah, " Satuan Luas")
    break

else: 
output("Data tidak bisa dihitung")