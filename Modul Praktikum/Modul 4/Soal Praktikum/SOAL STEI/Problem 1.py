def cekvalid (a,b,c):
    if a + b + c == 1:
        print("Valid!")
        Valid = True
    else:
        print("Tidak Valid!")
        Valid = False
        
    return Valid


def hitung (a,b,c,soal1,soal2,soal3,Valid):
    if Valid == True:
        Nilai = (a*soal1) + (b*soal2) + (c*soal3)
        print(f"Nilai Tugas Praktikum adalah {Nilai} ")
    else:
        print("Tak bisa dihitung! Bobot tidak Valid!")



a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))
soal1 = int(input("Masukkan nilai soal 1: "))
soal2 = int(input("Masukkan nilai soal 2: "))
soal3 = int(input("Masukkan nilai soal 3: "))



Valid = cekvalid(a,b,c)
print(hitung(a,b,c,soal1,soal2,soal3,Valid))

