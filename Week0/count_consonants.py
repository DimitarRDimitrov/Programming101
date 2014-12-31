def count_consonants(string):
    counter = 0
    lowstr = string.lower()
    for char in lowstr:
        if char in "bcdfghjklmnpqrstvwxz":
            counter += 1
    return counter
print(count_consonants("Github is the second best thing that happend to programmers after the keyboard!"))
print(count_consonants("A nice day to code!"))
