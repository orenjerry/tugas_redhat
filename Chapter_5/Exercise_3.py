import sys

def main():
    args = sys.argv[1:]
    args.sort()
    print(args)

if __name__ == "__main__":
    main()