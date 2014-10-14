from isPrime import is_prime


def prime_factorization(n):
    number = n
    # all primes between 2 and n inclusive
    primes = list(filter(lambda x: is_prime(x), range(2, n + 1)))
    lst = []
    if primes[-1] == n or n == 1:
        lst.append((n, 1))
    else:
        for prime in primes:
            if (prime ** 2 > number and len(lst) == 0) or number == 1:
                break
            elif number % prime == 0:
                power = power_of_prime(number, prime)
                lst.append((prime, power))
                number /= prime ** power
    return lst


def power_of_prime(number, prime):
    power = 0
    while number % prime == 0:
        number /= prime
        power += 1
    return power


def main():
    print("should be [(2, 1), (5, 1)]: %s" % prime_factorization(10))
    print("should be [(2, 1), (7, 1)]: %s" % prime_factorization(14))
    print("should be [(2, 2), (89, 1)]: %s" % prime_factorization(356))
    print("should be [(89, 1)]: %s" % prime_factorization(89))
    print("should be [(2, 3), (5, 3)]: %s" % prime_factorization(1000))

if __name__ == '__main__':
    main()
