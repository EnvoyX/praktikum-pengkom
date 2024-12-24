x = int(input("Masukkan nilai X: "))
y = int(input("Masukkan nilai y: "))


if x > 0 and  y > 0:
    print("Koordinat tersebut berada di kuadran 1")
elif x < 0 and  y > 0:
    print("Koordinat tersebut berada di kuadran 2")
elif x < 0 and  y < 0:
    print("Koordinat tersebut berada di kuadran 3")
elif x > 0 and  y < 0:
    print("Koordinat tersebut berada di kuadran 4")
else:
    print("Kuadran tidak bisa dihitung")
