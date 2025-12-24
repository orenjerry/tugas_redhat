angka_set = set()
duplikat = 0

while True:
    masukan = input("Masukkan angka (atau 'end' untuk selesai): ")
    
    if masukan.lower() == 'end':
        break
    
    if masukan.isdigit():
        angka = int(masukan)
        
        if angka in angka_set:
            duplikat += 1
        else:
            angka_set.add(angka)
    else:
        print("Yang kamu masukkan bukan angka / desimal. Silahkan masukkan angka.")

print(angka_set)
print(f"Angka duplikat: {duplikat}")