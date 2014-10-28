def sudoku_solved(sudoku):
    return (correct_matrix(sudoku) and check_rows(sudoku)
            and check_columns(sudoku) and check_3x3(sudoku))


def check_rows(matrix):
    m0 = matrix
    m = list(map(lambda x: condition(x), m0))
    if len(set(m)) == 1 and m[0]:
        return True
    return False


def check_columns(matrix):
    flag = True
    s = []
    i = 0
    j = 0
    while i < len(matrix):
        if not flag:
            return False
        while j < len(matrix):
            s.append(matrix[j][i])
            j += 1
        flag = flag and condition(s)
        s = []
        j = 0
        i += 1
    return flag


def check_3x3(matrix):
    m = []
    for row in matrix:
        m += row
    s = []
    flag = True             # to check for wrong 3x3 square
    for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
        if not flag:
            return False
        s = m[i:i + 3] + m[i + 9:i + 12] + m[i + 18:i + 21]
        flag = flag and condition(s)
        s = []
    return flag


def condition(lst):
    l = list(map(lambda x: str(x), sorted(lst)))
    return ''.join(l) == "123456789"


def correct_matrix(matrix):
    m = list(map(lambda x: len(x), matrix))
    return m[0] == len(matrix) and len(set(m)) == 1
