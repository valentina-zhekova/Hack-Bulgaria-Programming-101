def contains_digit(number, digit):
    return str(number).count(str(digit)) != 0


def main():
    print("should be False: %s" % contains_digit(123, 4))
    print("should be True: %s" % contains_digit(42, 2))
    print("should be True: %s" % contains_digit(1000, 0))
    print("should be False: %s" % contains_digit(12346789, 5))

if __name__ == '__main__':
    main()
