angka1 = int(input("Masukkan bilangan bulat pertama: "))
angka2 = int(input("Masukkan bilangan bulat kedua: "))

if angka1 > angka2:
    print(f"Angka yang lebih besar adalah: {angka1}")
elif angka2 > angka1:
    print(f"Angka yang lebih besar adalah: {angka2}")
else:
    print("Kedua angka sama")