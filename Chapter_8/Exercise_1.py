import sys

def teks_dari_file(nama_file):
    baris = kata = karakter = 0
    with open(nama_file, "r") as f:
        for line in f:
            baris += 1
            kata += len(line.split())
            karakter += len(line)
    return baris, kata, karakter

def main():
    for nama in sys.argv[1:]:
        b, k, c = teks_dari_file(nama)
        print(nama, ":", b, k, c)

if __name__ == "__main__":
    main()