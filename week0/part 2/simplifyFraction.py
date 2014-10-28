def simplify_fraction(fraction):
    divisors_nominator = divisors(fraction[0])
    divisors_denominator = divisors(fraction[1])
    common_divisors = list(filter(lambda x: divisors_nominator.count(x) != 0,
                           divisors_denominator))
    d = max(common_divisors)
    return (int(fraction[0] / d), int(fraction[1] / d))


def divisors(number):
    lst = []
    for div in range(1, number + 1):
        if number % div == 0:
            lst.append(div)
    return lst
