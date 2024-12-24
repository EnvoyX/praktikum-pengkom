# Program JumlahAngka

# Menghitung 1+2+3+...+N Asumsi N > 0

# KAMUS


# N : int
# i, sum : int


# ALGORITMA


sum = 0    # intial

for i in range (1,11):
    N = float(input("Masukkan bilangan yang ingin dihitung: "))
    sum = sum + N

print(sum)