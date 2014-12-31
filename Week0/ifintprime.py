def is_prime(n):
    # i = 2
    # if n == 1:
    #     return False
    # elif n == 0:
    #     return False
    # elif n == -1:
    #     return False
    # elif n == 2:
    #     return True
    # elif n == -2:
    #     return True
    # elif n > 0:
    #     while i < n:
    #         if n % i == 0:
    #             i = i + 1
    #             return False
    #         else:
    #             return True
    # else:
    #     while i > n:
    #         if n % i == 0:
    #             i = i - 1
    #             return False
    #         else:
    #             return True
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False

    return True

# print(is_prime(1))
# print(is_prime(11))
# print(is_prime(3))
# print(is_prime(44))
# print(is_prime(-5))
# print(is_prime(-11))
# print(is_prime(-44))
