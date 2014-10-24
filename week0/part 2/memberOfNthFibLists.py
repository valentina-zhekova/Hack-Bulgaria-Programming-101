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
