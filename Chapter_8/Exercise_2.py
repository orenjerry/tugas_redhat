import sys

def main():
    args = sys.argv[1:]
    isTotal = False
    if args and args[0] == "-t":
        isTotal = True
        args = args[1:]
    tb = tk = tc = 0
    for nama in args:
        with open(nama, "r") as f:
            for line in f:
                tb += 1
                tk += len(line.split())
                tc += len(line)
        if not isTotal:
            print(nama, ":", tb, tk, tc)
            tb = tk = tc = 0
    if isTotal:
        print("TOTAL:", tb, tk, tc)

if __name__ == "__main__":
    main()