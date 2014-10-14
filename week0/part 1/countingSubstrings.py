def count_substrings(haystack, needle):
    if haystack.count(needle) != 0:
        string = haystack
        count = 0
        while string != "":
            if string[:len(needle)] == needle:
                count += 1
                string = string[len(needle):]
            else:
                string = string[1:]
        return count
    return 0


def main():
    print("should be 2: %s" % count_substrings("This is a test string", "is"))
    print("should be 2: %s" % count_substrings("babababa", "baba"))
    print("should be 4: %s" % count_substrings(
        "Python is an awesome language to program in!", "o"))
    print("should be 0: %s" % count_substrings(
        "We have nothing in common!", "really?"))
    print("should be 2: %s" % count_substrings(
        "This is this and that is this", "this"))

if __name__ == '__main__':
    main()
