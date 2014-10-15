def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    elif n == 2:
        return listB
    else:
        count = 2
        while count < n:
            new = listA + listB
            listA = listB
            listB = new
            count += 1
        return listB


def main():
    print("should be [1]: {}".format(nth_fib_lists([1], [2], 1)))
    print("should be [2]: {}".format(nth_fib_lists([1], [2], 2)))
    print("should be [1, 2, 1, 3]: {}".format(
        nth_fib_lists([1, 2], [1, 3], 3)))
    print("should be [1, 2, 3, 1, 2, 3]: {}".format(
        nth_fib_lists([], [1, 2, 3], 4)))
    print("should be []: {}".format(nth_fib_lists([], [], 100)))

if __name__ == '__main__':
    main()
