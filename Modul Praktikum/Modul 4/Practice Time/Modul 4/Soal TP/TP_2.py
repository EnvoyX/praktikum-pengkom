def Replication(N,K):
    
    total = N
    new = 0
    old = 0
    for i in range(K):
        
        new = total * 2
        total = new + N
            
            
            
        print(f"Total Sekarang adalah {total}")
    return total
    
    
    # for i in range(K):
        
    #     total = total*2
    #     print(f"Total Bakteri Baru {total}")
    #     total = total + N
    #     print(f"Ditambah {N}")
        
        
    # print(f"Total Sekarang adalah {total}")
    # return total


N = int(input("Masukkan N: "))
K = int(input("Masukkan K: "))

print(f"Nona Deb memiliki {N} bakteri pada detik ke-0. Pada detik ke-{K}, terdapat {Replication(N,K)} bakteri Pengkombacter")
