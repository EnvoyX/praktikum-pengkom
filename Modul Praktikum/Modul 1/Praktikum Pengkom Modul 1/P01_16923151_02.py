# NIM/NAMA : 16923151/Muhamad Hanif Hafizhan
# Tanggal : 18 September 2023
# Deskiripsi : Problem 2


Bilangan = int(input("Masukkan sebuah bilangan 4 digit: "))

B1 = Bilangan // 1000
B2 = Bilangan % 1000 // 100
B3 = Bilangan % 100 // 10
B4 = Bilangan % 10 // 1


print(B1)
print(B2)
print(B3)
print(B4)

if ((B4 > B3 > B2 > B1) or (B1> B2 > B3 > B4)) and abs((int(str(B1) + str(B2))) - int(str(B3) + str(B4))) >= 30:
    print("Bilangan Gamma")
elif (B4 > B3 > B2 > B1) or (B1> B2 > B3 > B4):
    print("Bilangan Alfa")
elif(abs(int(str(B1) + str(B2))) - int(str(B3) + str(B4)) >=30 ):
    print("Bilangan Beta")
else:
    print("Bilangan Delta")



    
#Alternative Solution
# if (B4 > B3 > B2 > B1):

#     if ((int(str(B3) + str(B4)) - int(str(B1) + str(B2)))>= 30):
#         print("Bilangan tersebut adalah bilangan Gamma")
#     else:
#         print("Bilangan tersebut merupakan bilangan Alfa")

# elif (B1 > B2 > B3 > B4):

#     if ((int(str(B1) + str(B2)) - int(str(B3) + str(B4)))>= 30):
#         print("Bilangan tersebut adalah bilangan Gamma")
#     else:
#         print("Bilangan tersebut merupakan bilangan Alfa")

# elif ((int(str(B3) + str(B4)) - int(str(B1) + str(B2)))>= 30) or ((int(str(B1) + str(B2)) - int(str(B3) + str(B4)))>= 30):
#     print("Bilangan tersebut merupakan bilangan Beta")

# else:
#     print("Bilangan tersebut merupakan bilangan Delta")