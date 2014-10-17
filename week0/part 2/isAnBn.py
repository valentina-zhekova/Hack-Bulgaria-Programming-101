def is_an_bn(word):
    if len(word) == 0:
        return True
    elif word.count("a") == 0:
        return False
    else:
        n = word.count("a")
        fixed_word = "a" * n + "b" * n
        return word == fixed_word
