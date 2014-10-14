def sevens_in_a_row(arr, n):
    lst = list(map(lambda x: str(x), arr))
    string = ''.join(lst)
    if string.count('7') < n:
        return False
    else:
        return string.count('7' * n) != 0


def main():
    print("should be True: %s" %
          sevens_in_a_row([10, 8, 7, 6, 7, 7, 7, 20, -7], 3))
    print("should be False: %s" % sevens_in_a_row([1, 7, 1, 7, 7], 4))
    print("should be True: %s" %
          sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))
    print("should be True: %s" % sevens_in_a_row([7, 2, 1, 6, 2], 1))

if __name__ == '__main__':
    main()
