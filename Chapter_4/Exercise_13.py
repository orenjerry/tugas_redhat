def cari_ke(data, objek, urutan):
    hitung = 0
    for i, nilai in enumerate(data):
        if nilai == objek:
            hitung += 1
            if hitung == urutan:
                return i
    raise ValueError


lst = [1, 2, 3, 2, 4, 2]
print(cari_ke(lst, 2, 3))