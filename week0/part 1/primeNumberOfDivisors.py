from sumOfDivisors import divisors
from isPrime import is_prime


def prime_number_of_divisors(n):
    return is_prime(len(divisors(abs(n))))


def main():
    print("should be True: %s" % prime_number_of_divisors(7))
    print("should be False: %s" % prime_number_of_divisors(8))
    print("should be True: %s" % prime_number_of_divisors(9))

if __name__ == '__main__':
    main()
