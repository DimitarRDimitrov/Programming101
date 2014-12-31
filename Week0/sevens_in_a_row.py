def sevens_in_a_row(arr, n):
    counter = 0
    for digit in arr:
        if digit == 7:
            counter += 1
            if counter == n:
                return True
                break
        elif digit != 7:
            counter = 0
    if counter != n:
        return False

print(sevens_in_a_row([10, 8, 7, 6, 7, 7, 7], 3))
print(sevens_in_a_row([1, 7, 1, 7], 2))
