def tambah_semua(nilai, data):
    for k in data:
        data[k] += nilai
    return data

d = {"a": 1, "b": 2, "c": 3}
print(tambah_semua(5, d))