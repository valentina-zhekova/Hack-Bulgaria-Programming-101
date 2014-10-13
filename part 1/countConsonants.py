def count_consonants(str):
    count = 0
    check = "bcdfghjklmnpqrstvwxz"
    for char in str:
        if check.count(char) != 0 or check.upper().count(char) != 0:
            count += 1
    return count


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
