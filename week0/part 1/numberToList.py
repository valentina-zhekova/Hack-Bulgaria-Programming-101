def number_to_list(n):
    return list(map(lambda x: int(x), str(n)))


def main():
    print("should be [1, 2, 3]: %s" % number_to_list(123))
    print("should be [9, 9, 9, 9, 9]: %s" % number_to_list(99999))
    print("should be [1, 2, 3, 0, 2, 3]: %s" % number_to_list(123023))

if __name__ == '__main__':
    main()
