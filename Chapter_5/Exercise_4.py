import sys

def angka_valid(teks):
    if teks.startswith("-"):
        teks = teks[1:]
    bagian = teks.split(".")
    if len(bagian) > 2:
        return False
    for b in bagian:
        if not b.isdigit():
            return False
    return True

def main():
    args = sys.argv[1:]
    for val in args:
        if not angka_valid(val):
            print("Yang kamu masukkan bukan angka.")
            return
    total = 0
    for val in args:
        total += float(val)
    rata = total / len(args)
    print("Jumlah:", total)
    print("Rata-rata:", rata)

if __name__ == "__main__":
    main()