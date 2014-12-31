def is_number_balanced(number):
    string = str(number)
    # if len(string) % 2 == 0:
    #     i = 1
    # else:
    i = 1
    # leftsum = 0
    # rightsum = 0
    # for dig in string:
    #     while i < len(string) / 2:
    #         leftsum += int(dig)
    #         i += 1
    #     while i < len(string):
    #         rightsum += int(dig)
    #         i += 1
    # print(leftsum)
    # print(rightsum)
    leftsum = 0
    rightsum = 0
    leftstring = string[0:len(string) // 2]
    rightstring = string[len(string) - len(string) // 2:len(string) + 1]
    for digit in leftstring:
        leftsum += int(digit)
    for digit in rightstring:
        rightsum += int(digit)
    print(leftsum)
    print(rightsum)
    if leftsum == rightsum:
        return True
    else:
        return False





print(is_number_balanced(121))
print(is_number_balanced(12321))
print(is_number_balanced(4518))
print(is_number_balanced(12345))


