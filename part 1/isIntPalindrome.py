def is_int_palindrome(n):
    if abs(n) / 10 == 0:
        return True
    string = str(n)
    i = 0
    while i <= (len(string) - 1) / 2:
        if string[i] != string[len(string) - i - 1]:
            return False
        i += 1
    return True

# a[::2] --> prez st1pka 2

print("should be True: %s" % is_int_palindrome(1))
print("should be False: %s" % is_int_palindrome(42))
print("should be True: %s" % is_int_palindrome(100001))
print("should be True: %s" % is_int_palindrome(999))
print("should be False: %s" % is_int_palindrome(123))
