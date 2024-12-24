# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 23 Oktober 2023
# Deskripsi : Problem 2


#Fungsi Jumlah Bakteri
# def count_bakteri(x,y):
#     bakteribaru = 0
#     bakteritotal = 0
#     for i in range(y+1):
#         bakteribaru = x*(2**i)
#         bakteritotal += bakteribaru
#     return bakteritotal
# #input
# N = int(input('Masukkan N: '))
# K = int(input('Masukkan K: '))

# #Gunakan rumus jumlah bakteri
# bakteritotal = count_bakteri(N,K)
# print(f'Terdapat {bakteritotal} Bakteri Pengkombacter.')

# # NIM/Nama  : 16923151/Muhamad Hanif Hafizhan
# # Tanggal   : 25 Oktober 2023
# # Deskripsi : Menghitung jumlah total bakteri setelah K detik

# # Kamus
# # N = int
# # K = int

# # Definisi fungsi Replikasi
# def Replikasi(N,K):
#     # Menghitung jumlah total bakteri setelah K detik berdasarkan bakteri awal N
    
#     # Kamus Lokal
#     jumlah = N
#     bakteri = N
#     bakteriLama = 0
    
#     # Aggoritma
#     for i in range(K):
        
#         bakteri -= bakteriLama          # Jumlah bakteri dikurangi dengan bakteri yang sudah tidak menghasilkan bakteri baru lagi
        
#         bakteri *= 2                    # Bakteri yang masih bereplikasi menghasilkan 2 bakteri baru
#         bakteriLama += bakteri//2       # Jumlah bakteri lama bertambah sebanyak bakteri yang bereplikasi
        
#         jumlah += bakteri               # Jumlah bakteri ditambah dengan bakteri hasil replikasi
#         bakteri = jumlah                
        
#         # print(f"Terdapat {jumlah} bakteri pada detik ke {i+1}")
        
#     return jumlah
        
# # Program Utama
# N = int(input("Masukkan jumlah awal bakteri: "))
# K = int(input("Masukkan waktu: "))

# print(f"Nona Deb memiliki {N} bakteri pada detik ke-0. Pada detik ke-{K}, terdapat {Replikasi(N,K)} bakteri")



# Fungsi untuk menghitung bakteri
def hitung_bakteri(N, K):

    jumlah = N
    
    # Algoritma
    for i in range(K):
        jumlah *= 2  # Setiap detik, jumlah bakteri menjadi dua kali lipat
        jumlah += N  # Jumlah bakteri baru yang ditambahkan setiap detik
        print(f"Sekarang jumlah bakterinya ke-{jumlah} di waktu {K} detik")
    return jumlah

# Algoritma program utama
N = int(input("Masukkan jumlah bakteri awal (N): "))
K = int(input("Masukkan jumlah detik (K): "))
total_bakteri = hitung_bakteri(N, K)
print(f"Terdapat {total_bakteri} bakteri Pengkombacter setelah {K} detik:")