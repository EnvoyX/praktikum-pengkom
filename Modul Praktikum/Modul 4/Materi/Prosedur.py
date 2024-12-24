#Prosedur sebenarnya sama seperti fungsi, namun tidak ada kembalian. Sebagai contoh, berikut
#adalah program untuk menuliskan menu


def tulis_menu (pil1 , pil2 , pil3):
    print("Menu:")
    print("1. " + str(pil1))
    print("2. " + str(pil2))
    print("3. " + str(pil3))
    print("Masukkan pilihan: ")



tulis_menu ("Burger", "Ayam Geprek", "Mie Instan")
pilihan_makanan = int(input())
tulis_menu ("Jus Alpukat", "Thai Tea", "Teh Tarik")
pilihan_minuman = int(input())
tulis_menu ("Kentang", "Krupuk", "Abon")
pilihan_tambahan = int(input())