# python Exercise_8.py [file]
import sys

def main():
    hitung = {}
    for nama_file in sys.argv[1:]:
        with open(nama_file, "r") as f:
            for line in f:
                nama = line.strip()
                hitung[nama] = hitung.get(nama, 0) + 1
    for nama in sorted(hitung):
        print("{:<10} {}".format(nama, hitung[nama]))

if __name__ == "__main__":
    main()