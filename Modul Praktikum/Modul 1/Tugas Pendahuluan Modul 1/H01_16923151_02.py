# NIM : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 12 September 2023
# Deksripsi : Problem 2, Menentukan apakah garis tersebut garis vertikal, horizontal, atau gradien dengan menggukaan sebuah program


#PROBLEM 2

# memasukkan input x1, x1, y1, y2 dengan menambahkan float diluar kurung supaya mengubah data yang didalam menjadi float

x1 = float(input("Masukkan Nilai x1: "))
y1 = float(input("Masukkan Nilai y1: "))
x2 = float(input("Masukkan Nilai x2: "))
y2 = float(input("Masukkan Nilai y2: "))

if(x1==x2 and y1==y2):                                        # jika x1 dan x2 nya sama beserta y1 dan y2 maka itu bukan merupakan garis
    print("Bukan merupakan garis")
elif (y1==y2):                                                  # jika y1 sama dengan y2 maka garis tersebut adalah horizontal jika kondisi tersebut memenuhi
    print("Garis tersebut merupakan garis horizontal")
elif (x1==x2):                                              # jika x1 sama dengan x2 maka garis tersebut adalah vertikal jika kondis tersebut memenuhi
    print("Garis tersebut merupakan garis vertikal")
else:                                                           #Jika kondisi diatas tidak memenuhi maka fungsi else akan digunakan oleh Pyhthon dan menghasilkan output yang berbeda dari kondisi2 sebelumnya
    gradien = (y2-y1)/(x2-x1)
    print("Garis tersebut memiliki gradien: ", gradien)