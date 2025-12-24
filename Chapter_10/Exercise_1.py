import re

while True:
    a = input("Masukkan angka (end untuk berhenti): ")
    if a == "end":
        break
    if re.fullmatch("^[+-]?\\d+$", a):
        if a.startswith('-'):
            print("Angka adalah negatif")
        else:
            print("Angka adalah positif")
    else:
        print("Bukan angka")