while True:
    try:
        angka = int(input("Masukkan angka: "))
    except ValueError:
        print("Input harus berupa angka! Coba lagi.")
        continue

    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap.")
    else:
        print(f"{angka} adalah bilangan ganjil.")

    ulangi = input("Mau cek angka lagi? (y/n): ")
    if ulangi.strip().lower() != "y":
        break
