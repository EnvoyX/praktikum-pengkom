# Membuat program yang dapat menentukan kelas berat badan


berat_badan = int(input("Masukkan berat badan untuk ditentukkan kelasnya: "))

if berat_badan < 45:
    print("Tidak memenuhui kualifikasi")
elif berat_badan < 50: 
    print("Kelas A")
elif berat_badan < 55: 
    print("Kelas B")
elif berat_badan < 60: 
    print("Kelas C")
elif berat_badan < 65: 
    print("Kelas D")
elif berat_badan < 70: 
    print("Kelas E")
else:
    print("Kelas F")
    