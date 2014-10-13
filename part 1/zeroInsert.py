from listToNumber import list_to_number
from numberToList import number_to_list


def zero_insert(n):
    lst = number_to_list(n)
    i = 0
    end = len(lst) - 1
    while i < end:
        if lst[i] == lst[i + 1] or (int(lst[i]) + int(lst[i + 1])) % 10 == 0:
            lst.insert(i + 1, '0')
            end += 1
        i += 1
    return list_to_number(lst)


def main():
    print("should be 10160457: %s" % zero_insert(116457))
    print("should be 505050505050505: %s" % zero_insert(55555555))
    print("should be 6040406: %s" % zero_insert(6446))

if __name__ == '__main__':
    main()
