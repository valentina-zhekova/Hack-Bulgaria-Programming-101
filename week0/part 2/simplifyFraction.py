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


def main():
    print("should be (1,3): {}".format(simplify_fraction((3, 9))))
    print("should be (1,7): {}".format(simplify_fraction((1, 7))))
    print("should be (2,5): {}".format(simplify_fraction((4, 10))))
    print("should be (3,22):  {}".format(simplify_fraction((63, 462))))

if __name__ == '__main__':
    main()
