# NIM : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 12 September 2023
# Deksripsi : Problem 3, Membuat fungsi yang dapat menentukkan harga berdasarkan Baris Kursi dan Posisi Kursi yang dipilih


#PROBLEM 3

# Baris_Kursi dan Posisi_Kursi dengan memasukkan input dan diubah dengan int untuk Baris Kursi dan str untuk Posisi Kursi

Baris_Kursi = int(input("Masukkan Nomor Kursi: "))   
Posisi_Kursi = str(input("Masukkan Posisi Kursi: "))

#Solusi

if (1<= Baris_Kursi <= 20 or 51<= Baris_Kursi <=60):     #Menentukan apakah input yang dimasukkan diantara 1-20 atau 51-60 (Hotseat), karena hanya memilih satu kursi
    if(Posisi_Kursi == "A" or Posisi_Kursi== "F"):        # Jika iya, maka Posisi Hotseat mana kah yang dipilih?
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1600000") # Jika A / F maka harga nya 160OK
    elif(Posisi_Kursi == "B" or Posisi_Kursi == "E"):
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1550000") # Jika B / E maka harga nya 1550K
    elif(Posisi_Kursi == "C" or Posisi_Kursi == "D"):
        print("Tuan Kil memilih kursi Hot Seat dengan harga 1500000") # Jika C / D maka harga nya 1500K

if (21 <= Baris_Kursi <= 50 or 61 <= Baris_Kursi <= 100): # Menentukan apakah input yang dimasukkan diantara 21-50 atau 61-100 karena hanya memilih satu kursi diantara lain
    if(Posisi_Kursi == "A" or Posisi_Kursi == "F"): #Jika iya, maka Posisi Reguler mana kah yang dipilih?
        print("Tuan Kil memilih kursi regular dengan harga 1000000")  # Jika A / F maka harga nya 1000K
    elif(Posisi_Kursi == "B" or Posisi_Kursi == "E"):
        print("Tuan Kil memilih kursi reguler dengan harga 950000") # Jika B / E maka harga nya 950K
    elif(Posisi_Kursi == "C" or Posisi_Kursi == "D"):
        print("Tuan Kil memilih kursi Regular dengan harga 900000 ")  # Jika C / D maka harga nya 900K