# Program RataBilangan

# Menerima masukan sejumlah bilangan integer sampai pengguna
# memasukkan -999 dan dan menampilkan banyak bilangan, total, dan 
# rata-ratanya

# KAMUS
# X, count, sum : int
# rata : float



# ALGORITMA
sum = 0
count = 0                           # Inisialisasi
X = int(input())                # First-Elmt
while (X != -999):
 count = count + 1                                          # Aksi
 sum = sum + X
 X = int(input())                           # Next-Elmt
    # X = -999
# Terminasi
if (count > 0):
 print("Banyaknya bilangan = " + str(count))
 print("Jumlah total = " + str(sum))
 rata = sum/count
 print("Rata-rata = " + str(rata))
else:
 print ("Tidak ada data yang diolah")