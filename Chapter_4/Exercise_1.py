def input_positif():
    data = input("Masukkan bilangan bulat positif: ")
    if data.isdigit() and int(data) > 0:
        return int(data)
    return 0


nilai = input_positif()
if nilai == 0:
    print("Input tidak valid")
else:
    print("Nilai valid:", nilai)