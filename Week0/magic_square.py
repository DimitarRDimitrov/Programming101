def magic_square(matrix):
    i = 0
    target_sum = 0
    temp_sum = 0
    while i < len(matrix):
        target_sum += matrix[i][0]
        i += 1
    sum_cols = []
    row = 0
    col = 0
    for rows in range(0, len(matrix) - 1):
        while col < len(matrix[0]):
            temp_sum += matrix[rows][col]
            col += 1
        if temp_sum == target_sum:
            temp_sum = 0
            col = 0
        else:
            return False

    for cols in range(0, len(matrix[0]) - 1):
        while row < len(matrix):
            temp_sum += matrix[row][cols]
            row += 1
        print(temp_sum)
        if temp_sum == target_sum:
            temp_sum = 0
            row = 0
        else:
            return False
    for main_diag in range(0, len(matrix)):
        while i <
    




print(magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
