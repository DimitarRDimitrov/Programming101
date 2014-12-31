def sum_of_divisors(n):
	total = 0
	i = 1
	while i <= n:
		if n % i == 0:
			total += i
			i = i + 1
		else:
			i = i + 1
	return total

print(sum_of_divisors(8))
print(sum_of_divisors(1000))
print(sum_of_divisors(1))