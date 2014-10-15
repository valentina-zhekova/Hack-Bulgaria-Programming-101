from functools import reduce


def sort_fractions(fractions):
    denominators = list(map(lambda x: x[1], fractions))
    common_denominator = reduce(lambda x, y: x * y, denominators)
    result = list(map(lambda x: (x[0] * (common_denominator // x[1]),
                  x[0], x[1]), fractions))
    result = sorted(result, key=lambda tup: tup[0])
    result = list(map(lambda x: (x[1], x[2]), result))
    return result


def main():
    print("should be [(1, 2), (2, 3)]: {}".format(
          sort_fractions([(2, 3), (1, 2)])))
    print("should be [(1, 3), (1, 2), (2, 3)]: {}".format(
          sort_fractions([(2, 3), (1, 2), (1, 3)])))
    print("[(22, 78), (15, 32), (5, 6), (7, 8), (9, 6), (22, 7)]: {}".format(
        sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)])))

if __name__ == '__main__':
    main()
