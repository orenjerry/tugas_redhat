angka_awal = int(input("Masukkan angka awal: "))
angka_akhir = int(input("Masukkan angka akhir: "))
langkah = int(input("Masukkan langkah: "))

for angka in range(angka_awal, angka_akhir + 1, langkah):
    print(angka)