from math import ceil
from nthFibLists import nth_fib_lists


def member_of_nth_fib_lists(listA, listB, needle):
    fib_list = nth_fib_lists(listA, listB, calculate_n(listA, listB, needle))
    compare = fib_list[:len(needle)]
    return compare == needle


def calculate_n(listA, listB, needle):
    m = max(len(listA), len(listB))
    m = ceil(len(needle) / 2)
    f1 = 1
    f2 = 1
    next = 1
    n = 2
    while next < m:
        next = f1 + f2
        f1 = f2
        f2 = next
        n += 1
    if n == 2:
        return 3
    return n


def main():
    print("should be False: {}".format(
        member_of_nth_fib_lists([1, 2], [3, 4], [5, 6])))
    print("should be True: {}".format(member_of_nth_fib_lists(
        [1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4])))
    print("should be True: {}".format(
        member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2])))
    print("should be False: {}".format(
        member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7])))

if __name__ == '__main__':
    main()
