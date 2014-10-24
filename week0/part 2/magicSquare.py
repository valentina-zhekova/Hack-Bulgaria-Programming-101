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
