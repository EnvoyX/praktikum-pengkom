#membuat program deret 


X = float(input("Nilai X: ")) #asumsikan -1 < x < 1
n = int(input("Nilai n: ")) #Asumsikan N > 0


hasil = 0
for d in range(0,n+1):
    hasil += X**d
    print(hasil)

print("hasilnya adalah: " + str(hasil))