def calculate_coins(price):
    new_dict = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
    lst = [100, 50, 20, 10, 5, 2, 1]
    price *= 100
    while price > 0:
        for key in lst:
            while price - key >= 0:
                new_dict[key] += 1
                price -= key

    print(new_dict)

print(calculate_coins(1.00))
print(calculate_coins(0.54))
print(calculate_coins(8.94))
