def nan_expand(n):
    i = 0
    result = ""
    if n == 0:
        return ""
    while i <= n:
        if i < n:
            result += "Not a "
        else:
            result += "NaN"
        i += 1 
    return result

print(nan_expand(3))
print(nan_expand(0))