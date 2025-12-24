# python Exercise_6.py [dir] [max_size]
import sys
import os
import time

def main():
    folder = sys.argv[1]
    batas = int(sys.argv[2])
    for nama in os.listdir(folder):
        path = os.path.join(folder, nama)
        if os.path.isfile(path):
            ukuran = os.path.getsize(path)
            if ukuran > batas:
                mod = time.ctime(os.path.getmtime(path))
                print(nama, ukuran, mod)

if __name__ == "__main__":
    main()