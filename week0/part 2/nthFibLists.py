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
