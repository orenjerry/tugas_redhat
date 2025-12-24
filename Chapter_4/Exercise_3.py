def jumlah(*angka):
    total = 0
    for a in angka:
        total += a
    return total


print(jumlah(1, 2, 3, 4))