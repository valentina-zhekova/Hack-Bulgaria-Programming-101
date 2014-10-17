def groupby(func, seq):
    dictionary = {}
    for item in seq:
        if not func(item) in dictionary:
            dictionary[func(item)] = [item]
        else:
            dictionary[func(item)].append(item)
    return dictionary
