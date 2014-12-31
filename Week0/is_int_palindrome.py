def is_int_palindrome(n):
    last = len(str(n)) - 1
    string = str(n)
    for count in range(0, int(last/2) + 1):
        if string[count] == string[last - count]:
            return True
        else:
            return False
print(is_int_palindrome(141))
print(is_int_palindrome(123))
