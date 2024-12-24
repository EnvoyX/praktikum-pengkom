# NIM : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 12 September 2023
# Deksripsi : Problem 1, Membuat Fungsi yang dapat memasukkan nilai-nilai ujian dan dapat menentukan apakah lulus atau tidak dengan menggunakan sebuah program

#PROBLEM 1


#Membuat input nilai ujian 1 sampai 4 dengan memberikan int diluar fungsi input supaya mengubah data yang didalam menjadi sebuah tipe data Interger
Nama_Peserta  = str(input("Masukkan Nama peserta ujian: "))
Nilai_Ujian_1 = int(input("Masukkan nilai ujian 1: ")) 
Nilai_Ujian_2 = int(input("Masukkan nilai ujian 2: "))
Nilai_Ujian_3 = int(input("Masukkan nilai ujuan 3: "))
Nilai_Ujian_4 = int(input("Masukkan nilai ujian 4: "))

rata_rata = (Nilai_Ujian_1 + Nilai_Ujian_2 + Nilai_Ujian_3 + Nilai_Ujian_4)/4 # Membuat fungsi rata-rata dengan memasukkan data yang dibuat sebelumnya

#Solusi

if (Nilai_Ujian_1 <= 50 or Nilai_Ujian_2 <= 50 or Nilai_Ujian_3 <= 50 or Nilai_Ujian_4 <= 50 and rata_rata <= 70): # Jika salah satu dari 4 ujian nilainya kurang dari 50 maka dinyatakan tidak lulus ujian, dan 
    print(Nama_Peserta, "dinyatakan tidak lulus kelas Tuan Leo")                                                                  # rata-ratanya harus lebih dari sama dengan 70
else:                                                #Jika semua kondisi yang tertulis tidak memenuhi maka fungsi else akan otomatis menghasilkan output bahwa Tuan Kil lulus kelas Tuan Leo
    print(Nama_Peserta, "dinyatakan lulus kelas Tuan Leo")

#Solusi Alternatif
# if (Nilai_Ujian_1 < 0 or Nilai_Ujian_2 < 0 or Nilai_Ujian_3 < 0 or Nilai_Ujian_4 < 0):
#     print("Data yang diinput salah")
# elif (Nilai_Ujian_1 >100 or Nilai_Ujian_2 >100 or Nilai_Ujian_3 > 100 or Nilai_Ujian_4 > 100) :
#     print("Data yang diinput salah")
# elif (Nilai_Ujian_1 <= 50 or Nilai_Ujian_2 <= 50 or Nilai_Ujian_3 <= 50 or Nilai_Ujian_4 <= 50 or rata_rata < 70):
#     print(Nama_Peserta , "dinyatakan tidak lulus ujian kelas Tuan Leo")
# else:
#     print("Congratulations!!" , Nama_Peserta , "dinyatakan lulus ujian kelas Tuan Leo")


