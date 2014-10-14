def is_increasing(seq):
    lst = sorted(seq)
    return seq == lst and len(lst) == len(set(lst))


def main():
    print("should be True: %s" % is_increasing([1, 2, 3, 4, 5]))
    print("should be True: %s" % is_increasing([1]))
    print("should be False: %s" % is_increasing([5, 6, -10]))
    print("should be False: %s" % is_increasing([1, 1, 1, 1]))

if __name__ == '__main__':
    main()
