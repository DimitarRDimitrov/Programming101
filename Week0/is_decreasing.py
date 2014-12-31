def is_decreasing(seq):
    i = 0
    while i < len(seq) - 1:
        if seq[i] <= seq[i+1]:
            return False
        else:
            i += 1
    return True

print(is_decreasing([5, 4, 3, 2, 1]))
print(is_decreasing([5, 4, 5]))
