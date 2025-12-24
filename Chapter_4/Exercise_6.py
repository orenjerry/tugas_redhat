def cari_positif(data):
    hasil = []
    for x in data:
        if x > 0:
            hasil.append(x)
    return hasil

print(cari_positif([-5, 10, -3, 7, 0, 2]))