from contains_digit import contains_digit


def contains_digits(number, digits):
    for dig in digits:
        if not contains_digit(str(number), dig):
            return False
    return True


print(contains_digits(123123, [1, 2]))
print(contains_digits(123333, [1, 4]))

 # strnumber = str(number)
    # counter =  1
    # for dig in digits:
    #     for num in strnumber:
    #         if num == str(dig):
