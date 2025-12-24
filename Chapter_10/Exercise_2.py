import re

while True:
    a = input("Masukkan angka desimal (end untuk berhenti): ")
    if a == "end":
        break
    if re.fullmatch("^[+-]?\\d+\\.\\d+$", a):
        if a.startswith('-'):
            print("Angka desimal adalah negatif")
        else:
            print("Angka desimal adalah positif")
    else:
        print("Bukan angka")