def count_substrings(haystack, needle):
    count = 0
    string = haystack
    i = 0
    while i <= len(haystack):
        print(i)
        print(string[i:i + 1])
        if len(string) - i < len(needle):
            return count
        if string[i:i + len(needle)] == needle:
            count += 1
            i += len(needle) - 1
        else:
            i += 1
    return count


print("should be 2: %s" % count_substrings("This is a test string", "is"))
print("should be 2: %s" % count_substrings("babababa", "baba"))
print("should be 4: %s" % count_substrings(
    "Python is an awesome language to program in!", "o"))
print("should be 0: %s" % count_substrings(
    "We have nothing in common!", "really?"))
print("should be 2: %s" % count_substrings(
    "This is this and that is this", "this"))
