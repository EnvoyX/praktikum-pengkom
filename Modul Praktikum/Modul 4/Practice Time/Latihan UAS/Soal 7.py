n = int(input("Masukkan nilai n: "))


matriks = [[0 for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        matriks[i][j] = int(input(f"Masukkan isi elemen-elemen matriks ({i+1},{j+1}): "))
        
        
for i in range(n):
    for j in range(n):
        print(matriks[i][j], end=" ")
    print()


                        

        
    
                        
                        
                
                
            
                
                