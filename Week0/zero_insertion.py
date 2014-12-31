def zero_insertion(number):
    string = str(number)
    result = ""
    i = 0
    while i < len(string) - 1:
        if string[i] == string[i+1]:
            result += string[i] + "0"
        elif (int(string[i]) + int(string[i+1])) % 10 == 0:
            result += string[i] + "0"
        else:
            result += string[i]
        i += 1
    return result

print(zero_insertion(5564123))
