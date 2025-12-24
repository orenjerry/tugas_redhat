angka_keberuntungan = input("Masukkan angka keberuntungan Anda: ")

if angka_keberuntungan.isdigit():
    angka = int(angka_keberuntungan)
    print(f"Angka keberuntungan Anda adalah: {angka}")
    print(f"Jumlah digit: {len(angka_keberuntungan)}")
else:
    print("Yang kamu masukkan bukan angka / adalah desimal")
