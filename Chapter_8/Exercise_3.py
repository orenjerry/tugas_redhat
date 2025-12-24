def main():
    src = input("Enter the name of the input file: ")
    dst = input("Enter the name of the output file: ")

    with open(src, "r") as fin, open(dst, "w") as fout:
        while True:
            line = fin.readline()
            if not line:
                break
            fout.write(line)

if __name__ == "__main__":
    main()