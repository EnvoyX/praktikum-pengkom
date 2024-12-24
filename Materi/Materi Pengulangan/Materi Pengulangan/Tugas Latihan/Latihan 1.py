N = int(input("Masukkan Bilangan Interger positif: "))

if N >= 5:
    i = 1
    while (N > 5*i):
        i  = i + 1
    print(" Bilangan Kelipatan 5 antara 1 s.d " + str(N) + " Adalah ")


    for i in range (1, i):
     print(5*i , ", " , end="")

    sum = 0
    for j in range (1, i):
        sum = sum + 5*i
    print("Jumlah totalnya adalah: ", sum)
else:
   print(" Bilangan bukan merupakan Kelipatan 5 antara 1 s.d " , N )




   

