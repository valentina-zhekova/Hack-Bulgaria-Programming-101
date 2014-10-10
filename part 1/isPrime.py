from sumOfDivisors import is_prime_demo


def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        return is_prime_demo(abs(n))


print("should be False: %s" % is_prime(1))
print("should be True: %s" % is_prime(2))
print("should be False: %s" % is_prime(8))
print("should be True: %s" % is_prime(11))
print("should be False: %s" % is_prime(-10))
