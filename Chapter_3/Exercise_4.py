kata_unik = set()

while True:
    kalimat = input("Masukkan kalimat (atau ketik 'selesai' untuk keluar): ")
    if kalimat.lower() == 'selesai':
        break
    kata_unik.update(kalimat.split())

print("Kata-kata unik:", sorted(kata_unik))
print("Jumlah kata unik:", len(kata_unik))