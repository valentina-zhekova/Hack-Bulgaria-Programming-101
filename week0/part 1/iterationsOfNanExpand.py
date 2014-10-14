from nanExpand import nan_expand


def iterations_of_nan_expand(expanded):
    times = expanded.split().count('a')
    if expanded == nan_expand(times):
        return times
    else:
        return False


def main():
    print("should be 0: %s" % iterations_of_nan_expand(""))
    print("should be 1: %s" % iterations_of_nan_expand("Not a NaN"))
    print("should be 10: %s" % iterations_of_nan_expand("Not a " * 10 + "NaN"))
    print("should be False: %s" % iterations_of_nan_expand(
        "Show these people!"))

if __name__ == '__main__':
    main()
