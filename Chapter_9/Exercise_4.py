lst = {}
with open('exc4.txt', "r") as f:
    f.readline()
    for line in f:
        owner, tipe, harga = line.split()
        if owner not in lst:
            lst[owner] = {}
        
        if tipe not in lst[owner]:
            lst[owner][tipe] = harga
        else:
            lst[owner][tipe] += harga

print(lst)