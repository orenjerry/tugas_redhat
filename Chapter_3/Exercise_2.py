numbers = []

while True:
    data = input("Masukkan sebuah angka (atau ketik 'end' untuk keluar): ")
    if data == "end":
        break

    if data.isdigit():
        number = int(data)
        numbers.append(number)
    else:
        print("Yang kamu masukkan bukan angka / desimal. Silahkan masukkan angka atau 'end' untuk keluar.")

print("Isi daftar:", numbers)
print("Jumlah elemen dalam daftar:", sum(numbers))