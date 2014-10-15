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
    print("33333333333333333333")
    m = []
    for row in matrix:
        m += row
    s = []
    i = 0  # index
    flag = True  # to check for wrong 3x3 square
    while i < len(m):
        if not flag:
            return False
        print("for i = %s" % i)
        print(m[i:i + 3])
        print(m[i + 9:i + 12])
        print(m[i + 18:i + 21])
        s = m[i:i + 3] + m[i + 9:i + 12] + m[i + 18:i + 21]
        flag = flag and condition(s)
        i += 27
        s = []
    return flag


def condition(lst):
    l = list(map(lambda x: str(x), sorted(lst)))
    return ''.join(l) == "123456789"


def correct_matrix(matrix):
    m = list(map(lambda x: len(x), matrix))
    return m[0] == len(matrix) and len(set(m)) == 1


def main():
    print("should be True: %s" % sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4, 8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5, 2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))
    print("should be False: %s" % sudoku_solved([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))

if __name__ == '__main__':
    main()
