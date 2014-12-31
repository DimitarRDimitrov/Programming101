from copy import copy


def is_an_bn(word):
    a_counter = 0
    b_counter = 0
    i = 0
    cword = copy(word)
    for char in word:
        if char == "a":
            a_counter += 1
        elif char == "b":
            b_counter += 1
    if a_counter == b_counter:
        while i < len(word) + 1:
            cword = cword.replace("a"*i + "b"*i, "")
            if cword == "":
                return True
            else:
                i += 1
                cword = word
        return False
    else:
        return False

print(is_an_bn("aabbaabbaabb"))
print(is_an_bn(""))
print(is_an_bn("aaabb"))
print(is_an_bn("bbbaaa"))
print(is_an_bn("aaaaaaabbbbbbb"))
print(is_an_bn("aabbsomething"))
