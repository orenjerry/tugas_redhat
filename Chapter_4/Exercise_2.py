def teks_terpanjang(kumpulan_teks):
    return max(len(s) for s in kumpulan_teks)


data = ["apel", "pisang", "semangka", "jeruk"]
lebar = teks_terpanjang(data)

for item in data:
    print(f"{item:>{lebar}}")