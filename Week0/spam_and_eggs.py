def prepare_meal(number):
    result = ""
    while number % 3 == 0:
        number /= 3
        if result:
            result += " spam"
        else:
            result = "spam"
    if number % 5 == 0:
        if result != "":
            result += " and eggs"
        else:
            result = "eggs"
    return result
# print(prepare_meal(5))
# print(prepare_meal(3))
# print(prepare_meal(27))
# print(prepare_meal(15))
# print(prepare_meal(45))
# print(prepare_meal(7))
