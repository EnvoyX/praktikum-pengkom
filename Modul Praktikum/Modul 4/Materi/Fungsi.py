# Apa itu fungsi? Fungsi adalah suatu bagian dari program yang mampu mengerjakan tugas atau
# operasi tertentu di luar program utama. Fungsi akan mengembalikan nilai sesuai algoritma yang
# diberikan.


def kuadrat(x):
    x_kuadrat = x * x
    return x_kuadrat



n = int(input("Angka: "))

hasil = kuadrat(n)

print(hasil)

# Perhatikan pada contoh di atas, variabel di program utama bernama n. Namun di fungsi, variabel
# berubah nama menjadi x. Meskipun x berubah, nilai n di program utama tidak akan berubah.




# Sebuah fungsi juga dapat menerima lebih dari satu parameter. Selain itu, fungsi juga dapat
# melakukan hal-hal layaknya program biasa, namun tidak dapat mengubah variabel di program
# utama. Sebagai contoh, berikut adalah fungsi yang menghitung nilai a


def pangkat(a, b):
# asumsi b >= 0
    c = 1
    for i in range(b):
       c *= a
    return c


a = int(input("Angka A: "))
b = int(input("Angka B: "))

print(pangkat(a,b))