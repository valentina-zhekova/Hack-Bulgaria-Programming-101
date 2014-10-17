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
    if n == 0:
        return ""
    return "spam " * (n - 1) + "spam"


def eggs(number):
    if number % 5 == 0 and spam_condition(number) == 0:
        return "eggs"
    elif number % 5 == 0:
        return " and eggs"
    else:
        return ""
