# NIM/Nama : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 18 September 2023
# Deskripsi : Problem Set 3



# INPUT

Method = str(input("Metode pengiriman barang: "))
Quantity = int(input("Masukkan banyak barang: "))
Weight = int(input("Masukkan total berat barang (dalam kg): "))

Starting_Price =  15000            #Harga_awal

#Proses

if Weight <= 10:
    HBE = 0
else:
    HBE = 2000 * (Weight - 10)         # Harga ketika ada berat lebih

if Method == "Reguler":
    if (Quantity > 4):
     Q_Sum = 5000 * Quantity
     Sum = Starting_Price + Q_Sum + HBE 
     Disc_Reguler = Sum * 0.10
     Total = Starting_Price + Q_Sum + HBE - Disc_Reguler
     print(Total)
    else:
        Q_Sum = 5000 * Quantity
        Sum = Starting_Price + Q_Sum + HBE
        print(Sum)
        
if Method == "Kilat":
    if(Quantity >= 2):
        Q_Sum = 9000 * Quantity
        Sum = Starting_Price + Q_Sum + HBE
        Disc_Kilat = Sum * 0.15 
        Total = Starting_Price + Q_Sum + HBE - Disc_Kilat
        print(Total)
    else:
        print("Pengiriman tidak dapat dilakukkan")

