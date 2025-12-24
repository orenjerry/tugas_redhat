import re

while True:
    a = input("Masukkan teks `00AA .... DESC` (end untuk berhenti): ")
    if a == "end":
        break
    m = re.fullmatch("^(\\d{2})([A-Z]{2})[\\t ]+(.*)$", a)
    if m:
        print()
        print("Digit        :", m.group(1))
        print("Huruf        :", m.group(2))
        print("Deskripsi    :", m.group(3))
        print()
    else:
        print("Format tidak valid\n")