#NIM/Nama : 16923151 / Muhamad Hanif Hafizhan
# Tanggal : 16 Oktober 2023
# Deksripsi : Problem 1, membuat program tarik tambang berdasarkan jumlah genap robot, dan menentukan kekuatan masing
#             di sisi kiri dan sisi kanan

# Kamus
# N, sisi_kiri, sisi_kanan; int
# konfigurasi ; array



# Algoritma


N = int(input("Masukkan banyak robot: ")) #N Selalu Genap
konfigurasi = [0 for i in range(N)]

for x in range (0,N):
    konfigurasi[x] = input("Masukkan konfigurasi Robot: ")

# Ngecek isi array konfigurasi setelah didefinisikan sebagai string, dan melihat panjang arraynya
print(konfigurasi)
print(len(konfigurasi))


sisi_kiri = 0
sisi_kanan = 0


for i in range(0,int(len(konfigurasi)/2)):
    sisi_kiri = sisi_kiri + int(konfigurasi[i])

for j in range((int(len(konfigurasi)/2)), int(len(konfigurasi))):
    sisi_kanan = sisi_kanan + int(konfigurasi[j])

print(sisi_kiri)
print(sisi_kanan)


if (sisi_kiri > sisi_kanan):
    print("Sisi Kiri Menang!")

elif (sisi_kanan > sisi_kiri) :
    print("Sisi Kanan Menang!")

else:
    print("Bearkhir seri!")


