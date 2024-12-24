# Program yang dapat mendata Berat Badan Siswa dan mencari Berat Badan terbesar  
# Serta dapat mencari data yang lebih dari X(input dari user)

Siswa = 50

N = int(input("Masukkan berapa banyak siswa: "))

Data = [0 for x in range (N)]

for i in range(N):
    Data[i] = int(input("Masukkan data berat badan siswa ke-" + str(i+1)+ str(": ") ))

#Mencari data terbesar
Terbesar = Data[0]
for y in range(N):
    if Data[y] > Terbesar:
        Terbesar = Data[y]

Find = int(input("Masukkan berat badan yang ingin di sort: "))
Count = 0
Daftar = [0 for a in range(N)]

for b in range(N):
    if Data[b] > Find:
        Count += 1
        Daftar[b] = Data[b]

check = 0
for o in range(N):
    if Daftar[o] != 0 :
        check += 1

Daftar_Sortir = [0 for m in range(check)]

temp = 0
for l in range(N):
    if Daftar[l] != 0 :
        temp += 1
        Daftar_Sortir[temp-1] =  Daftar[l]

print("Berat badan terbesar adalah: " + str(Terbesar))
print("Daftar berat badan lebih dari " + str(Find) + " " + str(" = ") + str(Daftar_Sortir) )



