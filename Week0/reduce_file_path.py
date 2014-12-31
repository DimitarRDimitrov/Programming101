def reduce_file_path(string):
    lst = string.split("/")
    result = "/"
    i = 0
    while i < len(lst):
        if lst[i] == ".":
            result += ""
        elif lst[i] == "..":
            result = result.replace("/" + lst[i-1], "")
        elif lst[i] == "":
            result += ""
        else:
            result = result + "/" + lst[i]
        i += 1
    result = result.replace("//", "/")
    if result == "":
        result = "/"
    return result


# print(reduce_file_path("//home//radorado/code/./hackbulgaria/week0/../"))
# print(reduce_file_path("/"))
# print(reduce_file_path("/srv/../"))
# print(reduce_file_path("/srv/./././././"))
# print(reduce_file_path("/etc//wtf/"))
# print(reduce_file_path("/etc/../etc/../etc/../"))
# print(reduce_file_path("//////////////"))
