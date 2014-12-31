def nan_interation(string):
    counter = 0
    if string == "":
        return 0
    string = string.replace("Not a ", "*")
    for symbol in string:
        if symbol == "*":
            counter += 1
    string = string.replace("*", "")
    if string != "NaN":
        return False
    else:
        return counter

print(nan_interation("Not a Not a NaN"))
print(nan_interation(""))
print(nan_interation("Show these people"))
