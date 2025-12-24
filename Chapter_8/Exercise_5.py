import sys

def main():
    try:
        if len(sys.argv) == 3:
            src = sys.argv[1]
            dst = sys.argv[2]
        else:
            src = input("Masukkan nama input file: ")
            dst = input("Masukkan nama file output: ")
        with open(src, "r") as fin, open(dst, "w") as fout:
            for line in fin:
                fout.write(line)
    except OSError as err:
        print("File error:", err)

if __name__ == "__main__":
    main()