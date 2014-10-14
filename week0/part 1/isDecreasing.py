from isIncreasing import is_increasing


def is_decreasing(seq):
    return is_increasing(list(reversed(seq)))


def main():
    print("should be True: %s" % is_decreasing([5, 4, 3, 2, 1]))
    print("should be False: %s" % is_decreasing([1, 2, 3]))
    print("should be True: %s" % is_decreasing([100, 50, 20]))
    print("should be False: %s" % is_decreasing([1, 1, 1, 1]))

if __name__ == '__main__':
    main()
