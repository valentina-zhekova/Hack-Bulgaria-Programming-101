from containsDigit import contains_digit


def contains_digits(number, digits):
    flag = True
    for index, digit in enumerate(digits):
        flag = flag and contains_digit(number, digits[index])
        if not flag:
            return False
            break
    return True

#groupby(lambda x: "even" if x % 2 else "odd", ....)

print("should be True: %s" % contains_digits(402123, [0, 3, 4]))
print("should be False: %s" % contains_digits(666, [6, 4]))
print("should be False: %s" % contains_digits(123456789, [1, 2, 3, 0]))
print("should be True: %s" % contains_digits(456, []))
