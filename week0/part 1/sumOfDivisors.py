def sum_of_divisors(n):
    num = abs(n)
    if n == 0:
        return "infinity?"
    else:
        return sum(divisors(num))


def divisors(n):
    lst = list(filter(lambda x: n % x == 0, range(1, n + 1)))
    return lst


def main():
    print("should be 15: %s" % sum_of_divisors(8))
    print("should be 8: %s" % sum_of_divisors(7))
    print("should be 1: %s" % sum_of_divisors(1))
    print("should be 2340: %s" % sum_of_divisors(1000))

if __name__ == '__main__':
    main()
