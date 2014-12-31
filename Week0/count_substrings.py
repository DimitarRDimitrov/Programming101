def count_substrings(haystack, needle):
    count = 0
    truecount = 0
    i = 0
    j = 0
    while i < len(haystack):
        # print(i, j)
        # print(count, len(needle))
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            # print("%s == %s" % (haystack[i], needle[j]))
            count += 1
            if count == len(needle):
                truecount += 1
                count = 0
                j = 0
        else:
            i += 1
            j = 0

    return truecount

print(count_substrings("what are you?", "a"))
print(count_substrings("babababa", "baba"))
print(count_substrings("Python is an awesome language to program in!", "o"))
print(count_substrings("This is this and that is this", "this"))
