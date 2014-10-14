def count_vowels(str):
    count = 0
    for char in str:
        if "aeiouyAEIOUY".count(char) != 0:
            count += 1
    return count


def main():
    print("should be 2: %s" % count_vowels("Python"))
    print("should be 8: %s" % count_vowels("Theistareykjarbunga"))
    print("should be 0: %s" % count_vowels("grrrrgh!"))
    print("should be 22: %s" % count_vowels(
        "Github is the second best thing that happend to programmers, " +
        "after the keyboard!"))
    print("should be 8: %s" % count_vowels("A nice day to code!"))

if __name__ == '__main__':
    main()
