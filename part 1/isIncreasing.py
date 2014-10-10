def is_increasing(seq):
    lst = sorted(seq)
    if seq == lst:
        return True
    return False

# missing check for equals


print("should be True: %s" % is_increasing([1, 2, 3, 4, 5]))
print("should be True: %s" % is_increasing([1]))
print("should be False: %s" % is_increasing([5, 6, -10]))
print("should be False: %s" % is_increasing([1, 1, 1, 1]))
