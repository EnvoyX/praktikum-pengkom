# Soal 5

X = int(input('X: '))
a = int(input('a: '))
b = int(input('b: '))

temp = 0
keluaran = 0

print("Keterangan: ")
while temp < b:
    temp = temp + X
    if a < temp < b:
        keluaran = keluaran + 1
        print(temp, end=" ")

print(f"keluaran = {keluaran}")
X = int(input("X adalah: "))
a = int(input("a adalah: "))
b = int(input("b adalah: "))

count = 0
temp = 0

print("Keluaran: ")
while temp < b:
    temp = temp + 2
    if a < temp < b:
        count = count + 1
        print(temp, end=" ")

print(f"Keluaran = {keluaran} ")




