N = int(input("Masukkan N: "))
kelipatan = 0
kelipatan_2 = 10
pangkat = 0


while N > kelipatan:
    # kelipatan += 10
    pangkat += 1
    kelipatan = kelipatan_2**pangkat
    if kelipatan > N:
        print(f"Kelipatan ke-{kelipatan}")