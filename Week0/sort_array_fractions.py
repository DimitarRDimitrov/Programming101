def sort_array_fractions(fractions):
    my_list = []
    for fraction in fractions:
        my_list.append((fraction, fraction[0] / fraction[1]))
    newlist = sorted(my_list, key=lambda x: x[1])  #stolen from the internet
    result = []
    for tup in newlist:
        result.append(tup[0])
    return result

print(sort_array_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
print(sort_array_fractions([(1, 2), (2, 3), (1, 4)]))
