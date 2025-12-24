def main():
    total = 0

    while True:
        try:
            nilai = input("Masukkan bilangan bulat: ")
            total += int(nilai)

        except ValueError:
            print("Bukan bilangan bulat, diabaikan")

        except KeyboardInterrupt:
            print()
            print("Program dihentikan oleh user (Ctrl+C)")
            print("Total:", total)
            break

        except EOFError:
            print()
            print("End of file terdeteksi")
            print("Total:", total)
            break

if __name__ == "__main__":
    main()