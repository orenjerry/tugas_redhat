import json

with open("books.json", "r") as f:
    books = json.load(f)

while True:
    title = input("Masukkan judul buku (end untuk berhenti): ")
    if title.lower() == "end":
        break
    if title in books:
        print(f"{title} Info:")
        for key, value in books[title].items():
            print(f"  {key}: {value}")
    else:
        print("Buku tidak ditemukan")