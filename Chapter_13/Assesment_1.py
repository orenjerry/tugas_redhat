def bottle_word(n):
    return "bottle" if n == 1 else "bottles"

for i in range(99, 0, -1):
    next_count = i - 1

    print(f"{i} {bottle_word(i)} of water on the wall!")
    print(f"{i} {bottle_word(i)} of water!")
    print("Take one down")
    print("And pass it around")

    if next_count > 0:
        print(f"{next_count} {bottle_word(next_count)} of water on the wall!\n")
    else:
        print("No more bottles of water on the wall!\n")