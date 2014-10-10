def sort_fractions(fractions):
    # tuples are immutable
    #common_denominator = reduce(lambda x, y: x[1] * y[1], fractions)
    print(common_denominator)
    return fractions


def main():
    print("should be [(1, 2), (2, 3)]]: {}".format(
          sort_fractions([(2, 3), (1, 2)])))
    print("should be [(1, 3), (1, 2), (2, 3)]: {}".format(
          sort_fractions([(2, 3), (1, 2), (1, 3)])))
    print("should be [(5, 6),(22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]: {}".
          format(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6),
                (15, 32)])))

if __name__ == '__main__':
    main()
