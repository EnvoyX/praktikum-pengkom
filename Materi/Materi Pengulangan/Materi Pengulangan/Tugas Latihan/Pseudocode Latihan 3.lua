--{Muhamad Hanif Hafizhan / 16923151}

--{Inisialisasi}

input(angka)  --{first element}
Ganjil << 0 
Genap << 0
count << 0


--{Proses pengulangan while}

while not (angka < 0) do
    if (angka % 2) then
        Genap << Genap + 1
    if (angka % 2 != 0) then
        Ganjil << Ganjil + 1
    count << count + 1
    input(angka)
    {angka < 0}
    
--{Terminasi}

if (angka < 0) and (count > 0) then
    output(Genap)
    output(Ganjil)
else {count = 0}
    output("Tidak ada bilangan positif yang dimasukkan")



