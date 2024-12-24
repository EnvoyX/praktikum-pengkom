# Program yang dapat membantu Kepala Sekolah untuk meghitung tinggi rata-rata siswa di kelas
JumlahTinggiValid = 0
total = 0
InputTinggi = 0



while InputTinggi != -999:
    InputTinggi = int(input("Masukkan tinggi badan: "))
    if InputTinggi > 100 and InputTinggi < 200 :
        total += InputTinggi
        JumlahTinggiValid += 1
        print(total)
        print(JumlahTinggiValid)


if JumlahTinggiValid != 0 :
    average = total/JumlahTinggiValid
    print("Rata-ratanya adalah: " + str(average))
else:
    print("Tidak ada Data")



