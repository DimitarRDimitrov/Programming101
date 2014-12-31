def biggest_diference(array):
    bigdiff = 0
    for digit in array:
        for minus in range(0, len(array)):
            if (digit - array[minus]) < bigdiff:
                bigdiff = digit - array[minus]
    return bigdiff
print(biggest_diference([1, 2, 3, 4, 5]))
print(biggest_diference(range(100)))

