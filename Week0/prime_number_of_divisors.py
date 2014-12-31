def prime_number_of_divisors(n):
    counter = 0
    number = 1
    while number <= n:
        if n % number == 0:
            counter += 1
            number += 1
        else:
            number += 1
    for a in range(2, counter):
        if counter % a == 0:
            return False
        else:
            return True
print(prime_number_of_divisors(8))
print(prime_number_of_divisors(9))
