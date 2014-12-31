def number_to_list(n):
    lst = []
    string = str(n)
    for char in string:
        lst.append(char)
    return lst

print(number_to_list(1231231))