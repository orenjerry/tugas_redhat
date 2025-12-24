def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    while True:
        try:
            nilai = input("Masukkan index (end untuk keluar): ")
            if nilai == "end":
                break
            index = int(nilai)
            print("Nilai:", data[index])
        except ValueError:
            print("Input bukan angka")
        except IndexError:
            print("Index di luar jangkauan")

if __name__ == "__main__":
    main()