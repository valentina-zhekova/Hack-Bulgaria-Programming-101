def list_to_number(digits):
    number = ''.join(str(num) for num in digits)
    number = int(number)
    return number


def main():
    print("should be 123: %s" % list_to_number([1, 2, 3]))
    print("should be 99999: %s" % list_to_number([9, 9, 9, 9, 9]))
    print("should be 123023: %s" % list_to_number([1, 2, 3, 0, 2, 3]))

if __name__ == '__main__':
    main()
