def hitung(*angka):
    total = 0
    for a in angka:
        total += a
    rata = total / len(angka)
    return total, rata

hasil = hitung(10, 20, 30)
print(hasil)