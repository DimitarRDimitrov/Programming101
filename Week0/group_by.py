def group_by(func, values):
    my_dict = {}
    for value in values:
        if func(value) in my_dict:
            my_dict[func(value)].append(value)
        else:
            my_dict[func(value)] = [value]
    return my_dict

# print(group_by(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6, 7]))
