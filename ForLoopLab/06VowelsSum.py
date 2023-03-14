text = input()

sum_vowels = 0

for i in range(0, len(text)):
    if text[i] == "a":
        sum_vowels += 1
    if text[i] == "e":
        sum_vowels += 2
    if text[i] == "i":
        sum_vowels += 3
    if text[i] == "o":
        sum_vowels += 4
    if text[i] == "u":
        sum_vowels += 5

print(sum_vowels)
