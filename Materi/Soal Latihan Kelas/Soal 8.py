def BacaArray(Array1, Array2):
    for i in range(100):
        Array1[i] = int(input(f"Masukkan elemen array di ({i+1}"))
    for j in range(100):
        Array2[j] = int(input(f"Masukkan elemen array di ({j+1}"))

    validated = 0
    notsama = 0

    for x in range(100):
        if Array1[x] == Array2[x]:
            validated += 1
        else:
            notsama += 1    
    if validated != 0 and notsama == 0:
        print("Kedua Array tersebut sama")
    else:
        print("Kedua Array tersebut tidak sama")        

            



Array1 = [0 for i in range(100)]

Array2 = [0 for j in range(100)]



BacaArray(Array1,Array2)