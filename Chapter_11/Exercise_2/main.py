import json
import re

freq = {}

with open("cyclone", "r") as f:
    text = f.read().lower()
    words = re.findall(r"\b\w+\b", text)

for w in words:
    freq[w] = freq.get(w, 0) + 1

with open("cyclone_freq.json", "w") as out:
    json.dump(freq, out, indent="\t")

most_word = max(freq, key=freq.get)
print(f"'{most_word}' occurred {freq[most_word]} times")