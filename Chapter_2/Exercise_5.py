angka_input = input("Masukkan beberapa angka bulat dipisahkan dengan spasi: ")
daftar_angka = angka_input.split()

print("Angka yang lebih dari nol:")
for angka in daftar_angka:
    angka = int(angka)
    if angka > 0:
        print(angka)