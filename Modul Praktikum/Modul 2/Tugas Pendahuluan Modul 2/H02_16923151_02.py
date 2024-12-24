# Nama/NIM : Muhamad Hanif Hafizhan
# Tanggal : 26 September 2023
# Deskripsi : Problem 2, Modul TP 2


#Kamus
# H ,int

#initial

H = int(input("Masukkan nilai H (Tinggi) : "))    # H harus lebih dari 0

number = 1


#Proses  dan Algorimta      
for i in range(1, H + 1):
   if i < H/2 :
    for j in range(i+1):
        print(number, end = " ")
        number = number + 1
    print()
   elif i > H/2 :
        for i in range(H, i-1,-1):
            print(number, end = " " )
            number = number + 1
        print()



# for i in range(1, H + 1):
#     for j in range(i):
#         print(current_number, end=" ")
#         current_number += 1
#     print()















# def generate_special_triangle(H):
#     # Membangun segitiga pertama
#     for i in range(1, H + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

#     # Membangun segitiga kedua sebagai cerminan
#     for i in range(H, 0, -1):
#         for j in range(1, i):
#             print(j, end=" ")
#         print()

# # Contoh dengan tinggi H = 4
# generate_special_triangle(H)
