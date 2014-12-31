def count_words(arr):
    mydict = {}
    for word in arr:
        if word in mydict:
            mydict[word] += 1
        else:
            mydict[word] = 1
    return mydict

# print(count_words(["apple", "banana", "apple", "pie"]))
# print(count_words(["python", "python", "python", "ruby"]))
