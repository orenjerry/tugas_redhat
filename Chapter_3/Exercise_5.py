nama_angka = {
    '0': 'nol',
    '1': 'satu',
    '2': 'dua',
    '3': 'tiga',
    '4': 'empat',
    '5': 'lima',
    '6': 'six',
    '7': 'seven',
    '8': 'delapan',
    '9': 'sembilan'
}

angka = input("Masukkan sebuah angka: ")
if angka.isdigit():
    kata  = ' '.join(nama_angka[digit] for digit in angka)
    print(kata)
else:
    print("Yang kamu masukkan bukan angka / desimal")