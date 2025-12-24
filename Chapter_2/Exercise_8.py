num1 = int(input("Masukkan bilangan bulat pertama: "))
num2 = int(input("Masukkan bilangan bulat kedua: "))

if num1 > num2:
    num1, num2 = num2, num1

total = 0

for i in range(num1, num2 + 1):
    total += i

print(f"Jumlah bilangan dari {num1} hingga {num2} adalah: {total}")
