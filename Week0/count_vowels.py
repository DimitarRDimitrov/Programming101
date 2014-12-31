def count_vowels(string):
    lowstr = string.lower()
    counter = 0
    for char in lowstr:
        if char in "aeiouy":
            counter += 1
    return counter

print(count_vowels("asdfAAA"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
