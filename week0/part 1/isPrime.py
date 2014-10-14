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
    print("should be False: %s" % is_prime(1))
    print("should be True: %s" % is_prime(2))
    print("should be False: %s" % is_prime(8))
    print("should be True: %s" % is_prime(11))
    print("should be False: %s" % is_prime(-10))

if __name__ == '__main__':
    main()
