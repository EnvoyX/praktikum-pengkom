# Membuat program yang dapat mehitung tagihan listrik berdasarkan kelompok ekonomi

KwH = int(input("Masukkan total kWh: "))
Kelompok = str(input("Masukkan Kelompok Ekonomi: "))

if 0 < KwH <= 250:
    Tagihan = KwH*50
elif 251 <= KwH <= 500:
    Tagihan = KwH*100
elif 501 <= KwH <= 750:
    Tagihan = KwH*150
elif 751 <= KwH <= 1000:
    Tagihan = KwH*200 
else:
    Tagihan = KwH*250

if Kelompok == "rendah":
    if 0 < KwH <= 250:
        print(Tagihan)
    elif 251 <= KwH <= 500:
        Subsidi = (5/100) * Tagihan
        Total = Tagihan - Subsidi
        print(Total)
    elif 501 <= KwH <= 750:
        Subsidi = (5/100) * Tagihan
        Total = Tagihan - Subsidi
        print(Total)
    elif 751 <= KwH <= 1000:
        Subsidi = (5/100) * Tagihan
        Total = Tagihan - Subsidi
        print(Total)
    else:
        Subsidi = (10/100) * Tagihan
        Total = Tagihan - Subsidi
        print(Total)
elif Kelompok == "sedang":
    if 0 < KwH <= 1000 :
        print(Tagihan)
    else:
        Subsidi = (10/100) * Tagihan
        Total = Tagihan - Subsidi
        print(Total)
elif Kelompok == "tinggi":
    print(Tagihan)

