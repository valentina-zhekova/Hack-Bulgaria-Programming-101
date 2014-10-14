def is_an_bn(word):
    if len(word) == 0:
        return True
    elif word.count("a") == 0:
        return False
    else:
        n = word.count("a")
        fixed_word = "a" * n + "b" * n
        return word == fixed_word


def main():
    print("should be True: %s" % is_an_bn(""))
    print("should be False: %s" % is_an_bn("rado"))
    print("should be False: %s" % is_an_bn("aaabb"))
    print("should be True: %s" % is_an_bn("aaabbb"))
    print("should be False: %s" % is_an_bn("aabbaabb"))
    print("should be False: %s" % is_an_bn("bbbaaa"))
    print("should be True: %s" % is_an_bn("aaaaabbbbb"))

if __name__ == '__main__':
    main()
