def is_int_palindrome(n):
    string = str(abs(n))
    if len(string) == 1:
        return True
    else:
        first_half = string[:len(string) // 2]
        second_half = string[-(len(string) // 2):]
        return second_half == first_half[::-1]


def main():
    print("should be True: %s" % is_int_palindrome(1))
    print("should be False: %s" % is_int_palindrome(42))
    print("should be True: %s" % is_int_palindrome(100001))
    print("should be True: %s" % is_int_palindrome(999))
    print("should be False: %s" % is_int_palindrome(123))

if __name__ == '__main__':
    main()
