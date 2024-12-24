# NIM/Nama  : 16923151/Muhamad Hanif Hafizhan
# Tanggal   : 25 Oktober 2023
# Deskripsi : Menghitung jumlah total bakteri setelah K detik, Problem 2

# Kamus
# N = int
# K = int

# Definisi fungsi Replikasi atau Reproduksi Bakteri
def Replikasi(N,K):
    # Menghitung jumlah total bakteri setelah K detik berdasarkan bakteri awal N
    
    # Kamus Lokal
    #total, bakteri, bakteri_Lama, i = int
    
    # Algoritma
    total = N
    bakteri = N
    bakteri_Lama = 0

    for i in range(K):

        bakteri -= bakteri_Lama          # Jumlah bakteri dikurangi dengan bakteri yang sudah tidak menghasilkan bakteri baru lagi 
                                        #dan yang tidak reproduksi lagi tidak mati

        bakteri *= 2                    # Bakteri yang masih bereplikasi menghasilkan 2 bakteri baru
        bakteri_Lama += bakteri//2       # Jumlah bakteri lama bertambah sebanyak bakteri yang bereplikasi
        
        total += bakteri               # Jumlah bakteri ditambah dengan bakteri hasil replikasi
        bakteri = total                
        
        print(f"Terdapat {total} bakteri pada detik ke-{i+1}")
        
    return total
        
# Program Utama / Algoritma Utama
N = int(input("Masukkan jumlah awal bakteri Pengkombacter: "))
K = int(input("Masukkan waktu yang diinginkan: "))

print(f"Nona Deb memiliki {N} bakteri pada detik ke-0. Pada detik ke-{K}, terdapat {Replikasi(N,K)} bakteri Pengkombacter")