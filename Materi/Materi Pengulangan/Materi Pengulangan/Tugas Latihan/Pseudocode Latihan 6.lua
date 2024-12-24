--NIM/Nama : 16923151/Muhamad Hanif Hafizhan
-- Deskripsi : Latihan 6 Bab Pengulangan KU1102

--input(N)

--{Inisialisasi}
count << 0
hari << 0
Suhu_Total << 0
terbesar << None
terkecil << None

--{Proses while}
while hari <= N do
        if not hari == N then
            --{Mengamati data hari keberapa yang dimasuki}
            hari << hari + 1
            output("Hari ke-", hari)

            --{Memasukan input data suhu serta algoritma untuk penjumlahan suhu dan untuk break loop}
            Data_Suhu = input("Masukkan data suhu udara di Kota Bandung: ")
            Suhu_Total << Suhu_Total + Data_Suhu
            count << count + 1
            
            --{Algoritma mencari data terbesar dan terkecil}      

        --{Meng-assign Data_Suhu ke dua variabel (terkecil dan terbesar)}

            if terbesar is None then
                terbesar = Data_Suhu
            if terkecil is None then
                terkecil = Data_Suhu

            if Data_Suhu > terbesar then
                terbesar = Data_Suhu
            if Data_Suhu < terkecil then
                terkecil = Data_Suhu

                
            if count == N then
                    output("Suhu Tertinggi bulan ini: ", terbesar ,   "derajat celcius")
                    output("Suhu Terendah bulan ini: ", terkecil ,   "derajat celcius")

                    average << Suhu_Total / hari
                    print("Suhu rata-rata bulan ini: ", average,   "derajat celcius")


            
        










