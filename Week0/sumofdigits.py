def sum_of_digits(n):
	string = str(n)
	result = sum(int(digit) for digit in str(n) if digit != "-")
	return result
		
print(sum_of_digits(-12345))