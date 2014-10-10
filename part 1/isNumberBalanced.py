def is_number_balanced(n):
    if n / 10 == 0:
        return True
    else:
        s = 0
        lst = str(n)
        for i in range(int((len(lst) - 1) / 2)):
            d1 = int(lst[i])
            d2 = int(lst[len(lst) - 1 - i])
            s = s + d1 - d2
        if len(lst) % 2 == 0:
            s = s + int(lst[int((len(lst) - 1) / 2)])
            s = s - int(lst[int(len(lst) / 2)])
        if s == 0:
            return True
    return False

# file path --> list ne opashka


print("should be True: %s" % is_number_balanced(9))
print("should be True: %s" % is_number_balanced(11))
print("should be False: %s" % is_number_balanced(13))
print("should be True: %s" % is_number_balanced(121))
print("should be True: %s" % is_number_balanced(4518))
print("should be False: %s" % is_number_balanced(28471))
print("should be True: %s" % is_number_balanced(1238033))
