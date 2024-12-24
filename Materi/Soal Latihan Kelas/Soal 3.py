TC = int(input("Masukkan Nilai Celcius: "))
Kode = str(input("Masukkan kode konversi: "))



if Kode == "F":
    rumus = (9/5) * (TC) + 32
    print(f"Hasilnya adalah {rumus}")
elif Kode == "R":
    rumus = (4/5) * (TC) 
    print(f"Hasilnya adalah {rumus}")    
elif Kode == "K":
    rumus = (TC) + 273
    print(f"Hasilnya adalah {rumus}")