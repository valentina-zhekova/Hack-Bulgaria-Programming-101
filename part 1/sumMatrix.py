def sum_matrix(m):
    lst = list(map(lambda x: sum(x), m))
    return sum(lst)


def main():
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    m3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

    print("should be 45: %s" % sum_matrix(m1))
    print("should be 0: %s" % sum_matrix(m2))
    print("should be 55: %s" % sum_matrix(m3))

if __name__ == '__main__':
    main()
