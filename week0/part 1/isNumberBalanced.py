def is_number_balanced(n):
    string = str(abs(n))
    if len(string) == 1:
        return True
    else:
        first_half = list(map(lambda x: int(x), string[:len(string) // 2]))
        second_half = list(map(lambda x: int(x), string[-(len(string) // 2):]))
        return sum(first_half) == sum(second_half)


def main():
    print("should be True: %s" % is_number_balanced(9))
    print("should be True: %s" % is_number_balanced(11))
    print("should be False: %s" % is_number_balanced(13))
    print("should be True: %s" % is_number_balanced(121))
    print("should be True: %s" % is_number_balanced(4518))
    print("should be False: %s" % is_number_balanced(28471))
    print("should be True: %s" % is_number_balanced(1238033))

if __name__ == '__main__':
    main()
