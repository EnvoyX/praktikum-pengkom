n = int(input("Masukkan banyak nilai mahasiswa (n): "))


list = [[0 for j in range (n)] for i in range(4)]


for i in range(4):
    for j in range(n):
        list[i][j] = int(input(f"Masukkan nilai praktikum {i+1} pada mahasiswa ke-{j+1} : "))

target = int(input("Masukkan target (x): "))

count = 0
average = 0
total = 0



for y in range(n):
    print(f"Total dalam program ini sekarang adalah (pada iterasi ke {y+1}): {total} ")
    for x in range(4):
        total += list[x][y]
        if x == 3:
            print(f"Total Nilai Mahasiswa ke-{y+1} adalah: {total} ")
            average = total / 4
            print(f"Nilai rata-rata Mahasiswa ke-{y+1} adalah: {average} ")
            if average > target :
                count += 1
                total -= total
            else:
                total -= total

                
print(f"Terdapat {count} mahasiswa yang mendapatkan rata-rata nilai praktikum diatas {target}")
        
        