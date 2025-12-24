def irisan(a, b):
    hasil = []
    for x in a:
        if x in b and x not in hasil:
            hasil.append(x)
    return hasil

print(irisan([1, 2, 3, 4], [3, 4, 5, 6]))