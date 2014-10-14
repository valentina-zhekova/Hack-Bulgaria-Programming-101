def count_consonants(str):
    check = "bcdfghjklmnpqrstvwxz"
    count = list(map(lambda x: str.count(x) + str.count(x.upper()), check))
    return sum(count)


def main():
    print("should be 4: %s" % count_consonants("Python"))
    print("should be 11: %s" % count_consonants("Theistareykjarbunga"))
    print("should be 7: %s" % count_consonants("grrrrgh!"))
    print("should be 44: %s" % count_consonants(
          "Github is the second best thing that happend to programmers, " +
          "after the keyboard!"))
    print("should be 6: %s" % count_consonants("A nice day to code!"))

if __name__ == '__main__':
    main()
