# python Exercise_7.py [file1] [file2]
import sys

def baca(nama):
    with open(nama, "r") as f:
        return set(line.strip() for line in f)

def main():
    a = baca(sys.argv[1])
    b = baca(sys.argv[2])

    for nama in sorted(a & b):
        print(nama)

if __name__ == "__main__":
    main()