def sum_of_divisors(n):
    num = abs(n)
    if n == 0:
        return "infinity?"
    elif is_prime_demo(num):
        return num + 1
    else:
        return sum(divisors(num))


def is_prime_demo(n):
    for i in range(2, n):
        if i ** 2 > n:
            if n % i == 0:
                return False
            else:
                return True
        elif n % i == 0:
            return False


def divisors(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst


def main():
    print("should be 15: %s" % sum_of_divisors(8))
    print("should be 8: %s" % sum_of_divisors(7))
    print("should be 1: %s" % sum_of_divisors(1))
    print("should be 2340: %s" % sum_of_divisors(1000))

if __name__ == '__main__':
    main()
