first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

hari_dalam_seminggu = [first[i] + second[i] for i in range(len(first))]

print(hari_dalam_seminggu)