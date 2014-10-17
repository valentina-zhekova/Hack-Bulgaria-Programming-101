from functools import reduce
import copy


def magic_square(matrix):
    if correct_matrix(matrix):
        m1 = check_rows(matrix)
        m2 = check_columns(matrix)
        m3 = check_diagonals(matrix)
        return (type(m1) == int and type(m2) == int and type(m3) == int
                and m1 == m2 and m1 == m3)
    return False


def check_rows(matrix):
    m = list(map(lambda x: sum(x), matrix))
    if len(set(m)) == 1:
        return m[0]
    return False


def check_columns(matrix):
    m0 = copy.deepcopy(matrix)
    sum_by_columns = reduce(lambda x, y: sum_list(x, y), m0)
    if len(set(sum_by_columns)) == 1:
        return sum_by_columns[0]
    return False


def check_diagonals(matrix):
    index = 0
    main_diagonal = 0
    diagonal = 0
    while index < len(matrix):
        main_diagonal += matrix[index][index]
        diagonal += matrix[index][len(matrix) - 1 - index]
        index += 1
    if main_diagonal == diagonal:
        return main_diagonal
    return False


def sum_list(l1, l2):
    # lenghts are equal because this is a help function
    for i in range(len(l1)):
        l1[i] = l1[i] + l2[i]
    return l1


def correct_matrix(matrix):
    m = list(map(lambda x: len(x), matrix))
    return m[0] == len(matrix) and len(set(m)) == 1


def main():
    print("should be False: %s" % magic_square(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print("should be True: %s" % magic_square(
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
    print("should be True: %s" % magic_square(
        [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
    print("should be True: %s" % magic_square(
        [[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print("should be False: %s" % magic_square(
        [[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
    main()
