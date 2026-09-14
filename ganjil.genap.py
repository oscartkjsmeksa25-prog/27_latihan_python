def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")


while True:
    angka = int(input("Masukkan sebuah angka: "))

    cek_ganjil_genap(angka)

    pilihan = input("Apakah ingin lanjut y/n: ").lower()

    if pilihan == 'n':
        print("Program selesai. Terima kasih.")
        break
