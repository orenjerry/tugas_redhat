x = input("Masukkan kalimat: ")

karakter_pertama = x[0]
karakter_terakhir = x[-1]

jml_pertama = x.count(karakter_pertama)
jml_terakhir = x.count(karakter_terakhir)

print(f"Karakter pertama: '{karakter_pertama}' muncul {jml_pertama} kali")
print(f"Karakter terakhir: '{karakter_terakhir}' muncul {jml_terakhir} kali")