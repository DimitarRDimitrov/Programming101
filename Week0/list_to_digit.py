def list_to_digit(digits):
    string = ""
    for digit in digits:
        string += str(digit)
    return int(string)

print(list_to_digit([1, 2, 3]))
