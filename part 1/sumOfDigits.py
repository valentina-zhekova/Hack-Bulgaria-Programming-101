def sum_of_digits(n):
    num = abs(n)
    s = 0
    while num != 0:
        s += num % 10
        num = num // 10
    return s

"""
def main():
    print(asd(5))

if __name__ == '__main__':
    main()
"""

print("should be 43: %s" % sum_of_digits(1325132435356))
print("should be 6: %s" % sum_of_digits(123))
print("should be 6: %s" % sum_of_digits(6))
print("should be 1: %s" % sum_of_digits(-10))
