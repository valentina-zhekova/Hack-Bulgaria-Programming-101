# how to print on one line? -> print("...", end='') doesn't work
from sumMatrix import sum_matrix


def matrix_bombing_plan(m):
    # we accept that the matrix is a correct NxM matrix
    rows = len(m)
    columns = len(m[0])
    matrix_dictionary = {}
    i = 0
    j = 0
    # initiallize the dictionary
    while i < rows and j < columns:
        matrix_dictionary[(i, j)] = dictionary_values(i, j, m)
        if j == columns - 1:
            j = 0
            i += 1
        else:
            j += 1
    return matrix_dictionary


# return a list of the values of the neighbours
def neighbours(i, j, m):
    lst = []
    rows = len(m)
    columns = len(m[0])
    # all possible neighbours
    lst.append((i - 1, j - 1))
    lst.append((i - 1, j))
    lst.append((i - 1, j + 1))
    lst.append((i, j - 1))
    lst.append((i, j + 1))
    lst.append((i + 1, j - 1))
    lst.append((i + 1, j))
    lst.append((i + 1, j + 1))
    # all real ones like index tuples
    lst = list(filter(lambda x: x[0] >= 0 and x[0] < rows and x[1] >= 0
                      and x[1] < columns, lst))
    # take their value
    lst = list(map(lambda x: m[x[0]][x[1]], lst))
    return lst


def dictionary_values(i, j, m):
    return sum_matrix(m) - sum(map(lambda x: min(x, m[i][j]),
                               neighbours(i, j, m)))


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix_bombing_plan(m))

if __name__ == '__main__':
    main()
