def positive(*nilai, num):
    hitung = 0
    for n in nilai:
        if n > num:
            hitung += 1
    return hitung


res = positive(5, -10, 10, -20, 30, num=0)
print(res)