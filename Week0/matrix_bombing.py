from copy import deepcopy


def check_pos(m, din1, din2):
    if 0 < din1 < len(m) - 1:
        m[din1-1][din2] -= m[din1][din2]
        m[din1+1][din2] -= m[din1][din2]
    elif din1 == 0:
        m[din1+1][din2] -= m[din1][din2]
    else:
        m[din1-1][din2] -= m[din1][din2]
    if 0 < din2 < len(m[0]) - 1:
        m[din1][din2-1] -= m[din1][din2]
        m[din1][din2+1] -= m[din1][din2]
    elif din2 == 0:
        m[din1][din2+1] -= m[din1][din2]
    else:
        m[din1][din2-1] -= m[din1][din2]
    if din1 > 0 and din2 > 0:
        m[din1-1][din2-1] -= m[din1][din2]
    if din1 < len(m) - 1 and din2 > 0:
        m[din1+1][din2-1] -= m[din1][din2]
    if din1 > 0 and din2 < len(m[0]) - 1:
        m[din1-1][din2+1] -= m[din1][din2]
    if din1 < (len(m)) - 1 and din2 < len(m[0]) - 1:
        m[din1+1][din2+1] -= m[din1][din2]


def matrix_bombing(m):
    default_m = deepcopy(m)

    for din1 in range(len(m)):
        for din2 in range(len(m[0])):
            matrix = deepcopy(default_m)
            check_pos(matrix, din1, din2)
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[0])):
                    if matrix[i][j] < 0:
                        matrix[i][j] = 0
            # for lst in matrix:
            #     print(lst),
            print((din1, din2), sum(sum(matrix, [])))
                # mneeeeeeeeeeeeeeeee

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_bombing(m))


#legacy code
  # m[row-1][col-1] -= m[row][col]
  #               m[row-1][col] -= m[row][col]
  #               m[row-1][col+1] -= m[row][col]
  #               m[row][col-1] -= m[row][col]
  #               m[row][col+1] -= m[row][col]
  #               m[row+1][col-1] -= m[row][col]
  #               m[row+1][col] -= m[row][col]
  #               m[row+1][col+1] -= m[row][col
