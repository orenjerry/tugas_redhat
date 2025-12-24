def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    return a / b


menu = {
    "1": tambah,
    "2": kurang,
    "3": kali,
    "4": bagi
}

while True:
    print("1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Keluar\n")
    pilihan = input("Pilih: ")
    if pilihan == "5":
        break
    if pilihan not in menu:
        print("Pilihan salah")
        continue

    x = float(input("Angka pertama: "))
    y = float(input("Angka kedua: "))
    print("Hasil:", menu[pilihan](x, y), "\n")