def simplify_fractions(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    for i in range(2, nominator):
        if nominator % i == 0 and denominator % i == 0:
                nominator //= i
                denominator //= i
    return (nominator, denominator)

print(simplify_fractions((63, 462)))
