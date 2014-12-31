from ifintprime import is_prime


def prime_factorization(number):
    dictionary = {}
    i = 2
    while i <= number:
        if is_prime(i):
            if number % i == 0:
                if i in dictionary:
                    dictionary[i] += 1
                else:
                    dictionary[i] = 1
        i += 1

    return dictionary

print(prime_factorization(10))
print(prime_factorization(356))
print(prime_factorization(1000))
