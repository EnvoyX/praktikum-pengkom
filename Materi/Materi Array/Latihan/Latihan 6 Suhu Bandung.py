#NIM/Nama : 16923151 / Muhamad Hanif Hafizhan
# Tanggal : 17 Oktober 2023
# Deksripsi: Mencari rata-rata, suhu terendah, suhu lebih besar dari 30, suhu lebih rendah dari 15


# Kamus
# N , sum, pertama, total, average, terkecil = int
# Suhu, Tanggal, Tanggal_Baru, = array


# Algoritma

# Memasukan data Suhu di bandung pada bulan september

N = int(input("Masukkan banyak data suhu yang diinginkan: "))

Suhu = [0 for c in range(N)]
Tanggal = [0 for t in range(N)]
sum = 0

# memasukkan data dari range N dengan input user sekaligus mendefinsikan array yang telah dideklarasikan dengan input user
for i in range(N):
        Suhu[i] = int(input(f"Masukkan suhu data ke- {i+1} pada tanggal {i+1} September 2018 : "))

        # Mencari tanggal apa saja yang lebih dari sama dengan 30
        if Suhu[i] >= 30:           
            sum = sum + 1              
            checkpoint = i + 1                       
            Tanggal[sum] = checkpoint

print(f"Hasil Array Suhu setelah input user: {Suhu}") 
print(f"Hasil Array Tanggal yang suhunya >= 30 derajat celcius setelah di cari oleh program: {Tanggal}")



#menghilangkan elemen 0 dari array Tanggal dengan mengecek indexnya Tanggal satu per satu
count = 0   

for i in range(len(Tanggal)):  
    if Tanggal[i] != 0: 
        count += 1                 

Tanggal_Baru = [0 for i in range(count)]             # mendeklrasikan Tanggal_Baru berdasarkan hasil count yang dihasilkan


hitung = 0    # mengulangi proses yang sama namun kali ini kita mendefinisikan array tersebut
for i in range(len(Tanggal)):   
    if Tanggal[i] != 0:                             
        Tanggal_Baru[hitung] = Tanggal[i]    #setiap hasil nilai indeks Tanggal yang tidak nol maka akan didefiisikan ke Tanggal_Baru
        hitung+=1      



# Mencari rata-rata data Suhu di Bandung pada bulan September 2018
total = 0
for x in range(N):
    total = total + Suhu[x]   

average = total/N

# Mencari tanggal pertama yang Suhu nya kurang dari 15 pada bulan September 2018
for l in range(N):
    if Suhu[l] < 15:
        print(f"Tanggal pertama kali di bulan Sept. 2018 di kota Bandung adalah {l+1} September 2018 dengan Suhu {Suhu[l]} Derajat Celcius")
        break
    elif Suhu[l] > 15:
        if l == N-1:
            print("Suhu tidak pernah dibawah 15 derajat Celcius")
# Mencari Suhu Terendah di Bandung bulan pada September 2018

terendah = Suhu[0]
for k in range(N):
    if Suhu[k] < terendah:
        terendah = Suhu[k]
            
print(f"Suhu setelah di urutkan dari kecil ke besar: {Suhu}")

terkecil = Suhu[0]


print(f"Suhu terendah di bulan Sept. 2018 adalah {terendah} Derajat Celcius")
print(f"Rata-rata suhu kota Bandung di bulan Sept. 2018 adalah: {average} Derajat Celcius")
print(f"Tanggal yang lebih dari sama dengan 30 adalah {Tanggal_Baru} September 2018")
