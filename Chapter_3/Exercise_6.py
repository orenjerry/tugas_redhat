teks = input("Masukkan kata-kata: ")

kata_kata = teks.split()

frekuensi = {}

for kata in kata_kata:
    if kata in frekuensi:
        frekuensi[kata] += 1
    else:
        frekuensi[kata] = 1

print("\nUrut berdasarkan kata:")
for kata in sorted(frekuensi):
    print(f"{kata:15} {frekuensi[kata]}")

def ambil_jumlah(kunci):
    return frekuensi[kunci]

print("\nUrut berdasarkan jumlah:")
daftar_kunci = list(frekuensi.keys())
daftar_kunci.sort()
daftar_kunci.sort(key=ambil_jumlah, reverse=True)

for kata in daftar_kunci:
    print(f"{kata:15} {frekuensi[kata]}")