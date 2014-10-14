def biggest_difference(arr):
    maximum = max(map(abs, arr))
    minimum = min(map(abs, arr))
    return minimum - maximum


def main():
    print("should be -1: %s" % biggest_difference([1, 2]))
    print("should be -4: %s" % biggest_difference([1, 2, 3, 4, 5]))
    print("should be -9: %s" % biggest_difference([-10, -9, -1]))
    print("should be -99: %s" % biggest_difference(range(100)))

if __name__ == '__main__':
    main()
