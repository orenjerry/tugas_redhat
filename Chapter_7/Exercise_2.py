def main():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    while True:
        try:
            nilai = input("Masukkan index (end untuk keluar): ")
            if nilai == "end":
                break

            index = int(nilai)

            if index < 0:
                raise IndexError("Index negatif tidak diperbolehkan")

            print("Nilai:", data[index])

        except ValueError:
            print("Input bukan angka")
        except IndexError as ie:
            print("Error index:", ie)


if __name__ == "__main__":
    main()