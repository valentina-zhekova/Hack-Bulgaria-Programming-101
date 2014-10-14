from containsDigit import contains_digit


def contains_digits(number, digits):
    lst = list(filter(lambda x: contains_digit(number, x), digits))
    return len(lst) == len(digits)


def main():
    print("should be True: %s" % contains_digits(402123, [0, 3, 4]))
    print("should be False: %s" % contains_digits(666, [6, 4]))
    print("should be False: %s" % contains_digits(123456789, [1, 2, 3, 0]))
    print("should be True: %s" % contains_digits(456, []))

if __name__ == '__main__':
    main()
