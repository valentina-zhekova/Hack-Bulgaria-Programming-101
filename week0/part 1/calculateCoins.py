from math import ceil


def calculate_coins(sum):
    value = ceil(sum * 100)
    coins = [100, 50, 20, 10, 5, 2, 1]
    coins_dictionary = {}
    for coin in coins:
        coins_dictionary[coin] = value // coin
        value -= (coin * coins_dictionary[coin])
    return coins_dictionary


def main():
    print("should be {1: 1, 2: 1, 100: 0, 5: 0, 10: 0, 50: 1, 20: 0}: %s" %
          calculate_coins(0.53))
    print("should be {1: 0, 2: 2, 100: 8, 5: 0, 10: 0, 50: 1, 20: 2}: %s" %
          calculate_coins(8.94))

if __name__ == '__main__':
    main()
