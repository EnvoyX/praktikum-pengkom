#Menghitung pinjaman total

awal = int(input("Masukkan pinjaman awal: "))
bunga = int(input("Masukkan bunga: "))
lama = int(input("Masukkan lama waktu pinjam: "))


for i in range(lama):
    start = awal
    hasil_bunga = (awal*(bunga/100))
    awal += (awal*(bunga/100))
    total = awal
    print(f"Pada hari ke {i+1}: {start} X {bunga}% = {hasil_bunga} dengan total {total}")
