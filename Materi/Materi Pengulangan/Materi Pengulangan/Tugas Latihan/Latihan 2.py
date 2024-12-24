N = int(input("Masukkan Banyak Mahasiswa: "))

count = 0
Lulus = 0
Tidak_Lulus = 0
salah_Input = 0


while count < N:
    nilai = input("Masukkan Nilai Matkul KU1102 : ")
    count += 1 

    if nilai == "F" or nilai == "E":
        Tidak_Lulus += 1
    elif nilai == "A" or nilai == "B" or nilai == "C" or nilai == "D":
        Lulus += 1
    else:
        salah_Input += 1
        print("Ada data yang salah", "(", salah_Input , ")")


print("Lulus = ", Lulus)
print("Tidak Lulus = ", Tidak_Lulus)