
# Kamus
# N , sum, pertama, total, average, terkecil = int
# Suhu, Tanggal, Tanggal_Baru, = array


# Algoritma



N = int(input("Masukkan banyak data suhu yang diinginkan: "))

Suhu = [0 for c in range(N)]
Tanggal = [0 for t in range(N)]
sum = 0
pertama = 0

for i in range(N):
        Suhu[i] = int(input(f"Masukkan suhu data ke- {i+1} pada tanggal {i+1} September 2018 : "))

        if Suhu[i] >= 30:           
            sum = sum + 1              
            checkpoint = i + 1                       
            Tanggal[sum] = checkpoint

print(f"Hasil Array Suhu setelah input user: {Suhu}") 
print(f"Hasil Array Tanggal yang suhunya >= 30 derajat celcius setelah di cari oleh program: {Tanggal}")



count = 0   

for i in range(len(Tanggal)):  
    if Tanggal[i] != 0: 
        count += 1                 

Tanggal_Baru = [0 for i in range(count)]            


hitung = 0    
for i in range(len(Tanggal)):   
    if Tanggal[i] != 0:                             
        Tanggal_Baru[hitung] = Tanggal[i]   
        hitung+=1      



total = 0
for x in range(N):
    total = total + Suhu[x]   

average = total/N

for l in range(N):
    if Suhu[l] < 15:
        print(f"Tanggal pertama kali di bulan Sept. 2018 di kota Bandung adalah {l+1} September 2018 dengan Suhu {Suhu[l]} Derajat Celcius")
        break
    elif Suhu[l] > 15:
        if l == N-1:
            print("Suhu tidak pernah dibawah 15 derajat Celcius")

for z in range(N):
    for j in range(z+1,N):
        if Suhu[z] > Suhu[j]:    
            placeholder = Suhu[z]
            Suhu[z] = Suhu[j]
            Suhu[j] = placeholder
            
print(f"Suhu setelah di urutkan dari kecil ke besar: {Suhu}")

terkecil = Suhu[0]


print(f"Suhu terendah di bulan Sept. 2018 adalah {terkecil} Derajat Celcius")
print(f"Rata-rata suhu kota Bandung di bulan Sept. 2018 adalah: {average} Derajat Celcius")
print(f"Tanggal yang lebih dari sama dengan 30 adalah {Tanggal_Baru} September 2018")
