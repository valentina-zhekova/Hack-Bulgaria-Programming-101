from functools import reduce


def sort_fractions(fractions):
    denominators = list(map(lambda x: x[1], fractions))
    common_denominator = reduce(lambda x, y: x * y, denominators)
    result = list(map(lambda x: (x[0] * (common_denominator // x[1]),
                  x[0], x[1]), fractions))
    result = sorted(result, key=lambda tup: tup[0])
    result = list(map(lambda x: (x[1], x[2]), result))
    return result
