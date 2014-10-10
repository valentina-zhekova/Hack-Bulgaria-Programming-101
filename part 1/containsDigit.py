def contains_digit(number, digit):
    count = str(number).count(str(digit))
    if count != 0:
        return True
    return False


print("should be False: %s" % contains_digit(123, 4))
print("should be True: %s" % contains_digit(42, 2))
print("should be True: %s" % contains_digit(1000, 0))
print("should be False: %s" % contains_digit(12346789, 5))
