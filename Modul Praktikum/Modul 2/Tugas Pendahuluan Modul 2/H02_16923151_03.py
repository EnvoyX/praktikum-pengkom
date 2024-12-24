#  NIM/Nama : 16923151/Muhamad Hanif Hafizhan
#  Tanggal : 26 
#  Deksripsi : Problem 3, Modul TP 2

#Kamus
# A, int
# B, int
# N, int
# value = 1, int
# value_2 = 1 , int

#initial
A = int(input("Masukkan bilangan A: "))
B = int(input("Masukkan bilangan B: "))
N = int(input("Masukkan bilangan N: "))


#Proses  dan Algorimta
value = 1
while value < N:
        if value < N: 
            print(value)
            value *= A

        if value < N:
            print(value)
            value *= B
print(value)
       
if value == N:
     print("Bilangan ", N ," dapat dicapai.")

elif value != N:
     value_2 = 1
     while value_2 < N:

        if value_2 < N: 
            print(value_2)
            value_2 *= B

        if value_2 < N:
            print(value_2)
            value_2 *= A


        if value_2 == N:
            print(value_2, "| Bilangan ", N ," dapat dicapai.")


if value != N and value_2 != N:
     print("Bilangan ", N ," tidak dapat dicapai.")


# My Solution Without Print and Solidified

F = int(input("Masukkan bilangan F: "))
X = int(input("Masukkan bilangan X: "))
M = int(input("Masukkan bilangan M: "))

value = 1
while value < M:
        if value < M: 
            value *= F
        if value < M:
            value *= X
       
if value == M:
     print("Bilangan ", M ," dapat dicapai.")

elif value != M:
     value_2 = 1
     while value_2 < M:
        if value_2 < M: 
            value_2 *= X
        if value_2 < M:
            value_2 *= F
        if value_2 == M:
            print(value_2, "| Bilangan ", M ," dapat dicapai.")
if value != M and value_2 != M:
     print("Bilangan ", M ," tidak dapat dicapai.")



# Alternative Solution


        
G = int(input("Masukkan bilangan G: "))
J = int(input("Masukkan bilangan J: "))
N = int(input("Masukkan bilangan N: "))

#Proses

x = 1; y = 1 # inisialisasi

while x < N or y < N:
     if x < y:
        x *= G
        x *= J
     else:
        y *= G
        y *= J

 # Terminasi

if (x % N == 0) or (y % N == 0):
    print(f"Bilangan {N} dapat dicapai. ")
else:
     print (f"Bilangan {N} tidak dapat dicapai. ")

    

