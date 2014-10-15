def goldbach(n):
    if n > 2 and n % 2 == 0:
        primes = list(filter(lambda x: is_prime(x), range(2, n // 2 + 1)))
        result = []
        for prime in primes:
            if is_prime(n - prime):
                result.append((prime, n - prime))
        return result
    return []


def is_prime(n):
    num = abs(n)
    if num == 0 or num == 1:
        return False
    divide_by = 2
    while divide_by ** 2 <= num:
        if num % divide_by == 0:
            return False
        divide_by += 1
    return True


def main():
    print("should be [(2, 2)]: %s" % goldbach(4))
    print("should be [(3, 3)]: %s" % goldbach(6))
    print("should be [(3, 5)]: %s" % goldbach(8))
    print("should be [(3, 7), (5, 5)]: %s" % goldbach(10))
    print("[(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]: %s"
          % goldbach(100))

if __name__ == '__main__':
    main()
