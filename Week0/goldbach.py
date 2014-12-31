from ifintprime import is_prime


def goldbach(n):
    my_list = []
    i = 1
    while i < n // 2 + 1:
        if is_prime(i) and is_prime(n - i):
            my_list.append((i, n - i))
        i += 1

    return my_list

print(goldbach(100))
print(goldbach(10))
