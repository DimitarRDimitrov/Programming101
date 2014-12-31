def sum_matrix(m):
    result = 0
    for lst in m:
        for digit in lst:
            result += digit

    return result

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
