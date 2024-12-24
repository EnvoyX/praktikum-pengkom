# NIM/Nama : Muhamad Hanif Hafizhan
# Tanggal : 23 Oktober 2023
# Deskripsi : Problem 3, Mencari kapal musuh dalam suatu map matriks



#Kamus
# Baris, Kolom, Row, Column, i = int
# Map = Array
# Enemy = def / fungsi


#Algoritma

def Enemy(Map,Baris,Kolom):
    #Kamus Lokal
    #Scanned, TempBaris, TempKolom = int
    #Opponent = Array

    #Algoritma Lokal

    #Proses
    #Mencari Musuh

    Opponent = [[0 for Column in range(Kolom)] for Row in range(Baris)]
    Scanned = 0
    for Row in range(Baris):
        for Column in range(Kolom):
            #Jika terdapat ada angka 1 pada peta dan dalam peta Opponent belum ditandai alias nol(0)
            if (Map[Row][Column] == 1 and Opponent[Row][Column] == 0):
                Scanned += 1
                Opponent[Row][Column] = Scanned
                
                # Cek apakah kananya ada angka 1 lagi, jika iya maka akan terhitung sebagai 1 kapal yang sama
                CekKanan = Column + 1
                while(CekKanan < Kolom and Map[Row][CekKanan] == 1) :
                    Opponent[Row][CekKanan] = Scanned
                    CekKanan += 1

                # Cek apakah Disebelah bawahnya ada angka 1 lagi, jika ya maka terhitung sebagai 1 kapal yang sama
                CekBawah = Row + 1
                while(CekBawah < Baris and Map[CekBawah][Column] == 1):
                    Opponent[CekBawah][Column] = Scanned
                    CekBawah += 1

                
                
    # Output                
    if (Scanned == 0):
        print("Tidak terdapat kapal musuh pada peta")
    else:
        print(f"Terdapat {Scanned} kapal musuh pada peta")

    
    return Scanned


#Menginput Baris dan Kolom
Baris = int(input("N (Sebagai Baris): "))   
Kolom = int(input("M (Sebagai Kolom): "))


Map = [[0 for y in range (Kolom)] for x in range (Baris)] # Definsikan Array

#Mengisi Array
for Row in range(Baris):
    for Column in range(Kolom):
            Map[Row][Column] = int(input(f"Masukkan Keadaan Peta sekarang pada ({Row + 1},{Column + 1}): ")) 

#Melihat hasil array   
for Row in range (Baris):
    for Column in range(Kolom):
        print((Map[Row][Column]), end=" ") 
    print()
    
Enemy(Map,Baris,Kolom)



# Alternative Solution













# def Enemy(Map,N,M):
#     Musuh = 0
#     for y in range(N):
#         for x in range(M):
#             #Check secara Horizontal
#             if Map[y][x] == 1 :
#                 Musuh += 1
#                 y = y + 1
#                 print(f"Musuh yang terdeteksi: {Musuh}")
#         if y >= (N - 1):
#             break
#         else:
#             continue     
            
#     if Musuh != 0:
#             print(f"Y sekarang adalah: {y}")
#             print(f"Terdapat {Musuh} kapal musuh pada peta")
#     else:
#         print(f'Tidak terdapat kapal musuh pada peta')
