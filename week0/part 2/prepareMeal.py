def prepare_meal(number):
    return "" + spam(spam_condition(number)) + eggs(number)


def spam_condition(number):
    start = 1
    power = 0
    n = 0
    while start <= number:
        if number % start == 0 and start != 1:
            n = power
        start *= 3
        power += 1
    return n


def spam(n):
    if n == 1:
        return "spam"
    elif n == 0:
        return ""
    else:
        return "spam " * (n - 1) + "spam"


def eggs(number):
    if number % 5 == 0 and spam_condition(number) == 0:
        return "eggs"
    elif number % 5 == 0:
        return " and eggs"
    else:
        return ""


def main():
    print("should be \"eggs\": %s" % prepare_meal(5))
    print("should be \"spam\": %s" % prepare_meal(3))
    print("should be \"spam spam spam\": %s" % prepare_meal(27))
    print("should be \"spam and eggs\": %s" % prepare_meal(15))
    print("should be \"spam spam and eggs\": %s" % prepare_meal(45))
    print("should be \"\": %s" % prepare_meal(7))

if __name__ == '__main__':
    main()
